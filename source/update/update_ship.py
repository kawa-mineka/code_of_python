###########################################################
#  update_shipクラス                                      #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主に自機関連の更新を行うメソッド                          #
#  自機の移動、自機の座標の履歴記録,自機のクリッピング         #
#  自機ショット関連の更新、自機ミサイル関連の更新              #
#   クロー関連の更新                                        #
# 当たり判定は別のクラス(update_collision)で行う             #
# 2022 04/05からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func  import * #汎用性のある関数群のモジュールの読み込み

from update.update_obj    import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update.update_sound  import * #SE再生で使用

class update_ship:
    def __init__(self):
        None

    #!自機の移動関連#################################################################################################################
    #自機の移動          キーボードとゲームパッド、または移動座標先を指定しての「自動移動モード」による自機の移動処理を行う関数です
    def ship(self):
        """
        自機の移動
        """
        self.my_rolling_flag = 0  #自機ローリングフラグ(旋回フラグ)を0に初期化する
        self.my_moved_flag = 0    #自機が動いたかどうかのフラグを0に初期化する
        
        if self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST: #ゲームステータスが「ステージクリア後、自機がブースト加速して右に過ぎ去っていく」なら
            self.my_x += self.my_vx
            self.my_vx += 0.025                #速度0.01で加速していく
            self.my_boost_injection_count += 1 #ステージクリア後のブースト噴射用のカウンターを1増やしていく
            self.my_moved_flag = 1             #トレースクローも動かしたいので自機移動フラグOnにする
            
        elif self.replay_status != REPLAY_PLAY and self.move_mode == MOVE_MANUAL: #リプレイステータスが(再生中)では無い & 移動モードが(MANUAL)の時は
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            
            # 左入力があったのなら  x座標を  1*my_speedの数値だけ減らす
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT):
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = -1
                self.pad_data_l += PAD_LEFT
            
            # 右入力があったのなら  x座標を  1*my_speedの数値だけ増やす
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT):
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = 1
                self.pad_data_l += PAD_RIGHT
            
            # 上入力があったのなら  y座標を  1*my_speedの数値だけ減らす
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
                self.my_rolling_flag = 2
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = -1
                self.pad_data_l += PAD_UP
            
            # 下入力があったのなら  y座標を  1*my_speedの数値だけ増やす
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
                self.my_rolling_flag = 1
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = 1
                self.pad_data_l += PAD_DOWN
            
            self.my_x += self.my_vx * self.my_speed #自機の移動量(vx,vy)と自機の速度(speed)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy * self.my_speed
            
        elif self.replay_status == REPLAY_PLAY and self.move_mode == MOVE_MANUAL: #リプレイステータスが「PLAY」で移動モードが「MANUAL」のときは
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            #self.replay_frame_index    インデックス値のリストの内容はパッド入力データのHigh Byte
            #self.replay_frame_index + 1インデックス値のリストの内容はパッド入力データのLow Byte となります
            #リプレイデータを調べて左入力だったのなら  x座標を  my_speedの数値だけ減らす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000100 == 0b00000100:  #LowByte
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = -1
            
            #リプレイデータを調べて右入力があったのなら x座標を  my_speedの数値だけ増やす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00001000 == 0b00001000:  #LowByte
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = 1
            
            #リプレイデータを調べて上入力があったのなら y座標を  my_speedの数値だけ減らす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000001 == 0b00000001:  #LowByte
                self.my_rolling_flag = 2
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = -1
            
            #リプレイデータを調べて下入力があったのなら y座標を  my_speedの数値だけ増やす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000010 == 0b00000010:  #LowByte
                self.my_rolling_flag = 1
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = 1
            
            self.my_x += self.my_vx * self.my_speed #自機の移動量(vx,vy)と自機の速度(speed)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy * self.my_speed
            
        elif self.move_mode == MOVE_AUTO and self.move_mode_auto_complete == 0: #移動モード「AUTO」&まだ移動完了フラグが建っていなかったら・・・
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            
            if self.my_x > self.move_mode_auto_x:
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vx = -0.5                     #左に自動移動
            else:
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vx = 0.5                      #右に自動移動
            
            if self.my_y > self.move_mode_auto_y:
                self.my_rolling_flag = 2
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vy = -0.5                     #上に自動移動
            else:
                self.my_rolling_flag = 1
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vy = 0.5                      #下に自動移動
            
            self.my_x += self.my_vx #自機の移動量(vx,vy)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy
            
            if -1 <= self.my_x - self.move_mode_auto_x <= 1 and -1 <= self.my_y - self.move_mode_auto_y <= 1: #自機座標(x,y)と移動目的先の座標の差が誤差+-1以内ならば
                self.move_mode_auto_complete = 1    #自動移動完了フラグをonにする
                if self.game_status == Scene.STAGE_CLEAR_MOVE_MY_SHIP: #ゲームステータスが「ステージクリア後の自機自動移動」だったら
                    self.move_mode = MOVE_MANUAL    #自動移動モードを解除し手動移動モードに移行します
                    self.game_status = Scene.STAGE_CLEAR_MY_SHIP_BOOST   #ゲームステータスを「ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン」にする
                    self.my_vx = -1.3 #ブースト開始の初期スピードは左へ1ドット毎フレーム（ちょっと左に戻ってから加速し、右へ飛んでいく）
                    self.my_boost_injection_count = 1 #ステージクリア後のブースト噴射用のカウンターの数値を初期化
                    self.my_moved_flag = 1          #トレースクローも動かしたいので自機移動フラグOnにする
                    pyxel.playm(3)  #ブーストサウンド？再生

    #自機の座標を過去履歴リストに書き込んでいく関数（トレースクローの座標として使用します）
    def record_coordinate(self):
        """
        自機の座標を過去履歴リストに書き込んでいく関数（トレースクローの座標として使用します）
        """
        if self.my_moved_flag == 1:#自機が移動したフラグがonならＸＹ座標を過去履歴リストに書き込み一番古い物を削除する
            new_traceclaw = Trace_coordinates()#new_traceclawにTrace_coordinatesクラスの型を登録
            new_traceclaw.update(self.my_x,self.my_y)#クラス登録された（クラス設計された？）new_traceclawに自機のＸＹ座標データを入れてインスタンスを作成する
            self.claw_coordinates.append(new_traceclaw)#1フレームごとに自機のXY座標の入ったインスタンスをclaw_coordinatesリストに追加していく(append)
            
            del self.claw_coordinates[0]#一番古いXY座標データをdelする(一番古いXY座標のインデックス値は0)
            
            #自機が移動したフラグがonならリバースクロー用のショット方向ベクトルも書き込む
            self.reverse_claw_svx = -(self.my_vx)#リバースクロー用のショット方向ベクトルは自機移動ベクトルを反転したものとなります
            self.reverse_claw_svy = -(self.my_vy)

    #自機をはみ出さないようにする
    def clip(self):
        """
        自機をはみ出さないようにする
        """
        if    self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status == Scene.STAGE_CLEAR_FADE_OUT: #ステータスが「ブースト加速して去る」「ステージクリアフェードアウト」なら
            if self.my_x < 0:
                self.my_x = 0
            if self.my_x >= WINDOW_W + 80:
                self.my_x = WINDOW_W + 80
            return  #x軸はある程度まではみ出してok
        else:
            if self.my_x < 0:
                self.my_x = 0
            if self.my_x >= WINDOW_W - MOVE_LIMIT:
                self.my_x = WINDOW_W - MOVE_LIMIT - 1
        
        
        if self.my_y < 0:
            self.my_y = 0
        
        if self.stage_number == STAGE_VOLCANIC_BELT:
            if self.my_y >= WINDOW_H + self.bg_height - SHIP_H * 17  -5:
                self.my_y  = WINDOW_H + self.bg_height - SHIP_H * 17 -5 - 1
        else:
            if self.my_y >= WINDOW_H - SHIP_H:
                self.my_y  = WINDOW_H - SHIP_H - 1

    #!自機弾の移動関連###############################################################################################################
    #自機弾の更新
    def shot(self):
        """
        自機弾の更新
        """
        shot_count = len(self.shots)#弾の数を数える
        for i in reversed(range (shot_count)):
            #弾の位置を更新！
            if 0 <= self.shots[i].shot_type <= 3:#ショットタイプがバルカンショットの場合
                self.shots[i].posx += self.shots[i].vx * self.shot_speed_magnification #弾のX座標をVX*speed_magnification(倍率)分加減算して更新
                self.shots[i].posy += self.shots[i].vy                           #弾のY座標をVY分加減算して更新
                
            elif 4 <= self.shots[i].shot_type <= 6:#ショットタイプがレーザーの場合
                self.shots[i].posx += self.shots[i].vx#弾のX座標をVX分加減算して更新
                self.shots[i].offset_y = self.shots[i].offset_y * self.shots[i].vy#Ｙ軸オフセット値 vyの倍率ごと乗算して行って上下にずらしていく
                self.shots[i].posy = self.my_y + self.shots[i].offset_y#自機のｙ座標+Ｙ軸オフセット値をレーザーのＹ座標としてコピーする（ワインダー処理）
                self.shots[i].shot_hp = 1#レーザーなのでHPは減らず強制的にＨＰ＝１にする（ゾンビ化～みたいな）
                
            elif 7 <= self.shots[i].shot_type <= 10:#ショットタイプがウェーブカッターの場合
                self.shots[i].posx += self.shots[i].vx * self.shot_speed_magnification #弾のX座標をVX*speed_magnification(倍率)分加減算して更新
                self.shots[i].posy += self.shots[i].vy                           #弾のY座標をVY分加減算して更新
                self.shots[i].shot_hp = 1#ウェーブカッターはHPは減らず強制的にＨＰ＝１にする（ゾンビ化～みたいな）
            
            if self.shots[i].shot_hp == 0:
                del self.shots[i]#自機弾のHPがゼロだったらインスタンスを破棄する（弾消滅） 

    #自機弾のはみだしチェック（はみ出て画面外に出てしまったら消去する)
    def clip_shot(self):
        """
        自機弾のはみだしチェック（はみ出て画面外に出てしまったら消去する)
        """
        shot_count = len(self.shots)#弾の数を数える
        for i in reversed(range (shot_count)):
            if (-16 < self.shots[i].posx < WINDOW_W + 16 ) and (-16 <self.shots[i].posy < self.bg_height + 16):
                continue
            else:
                del self.shots[i]

    #!自機ミサイルの移動関連###############################################################################################################
    #自機ミサイルの更新（背景障害物との当たり判定も行っています）
    def missile(self):
        """
        自機ミサイルの更新（ついでに背景障害物との当たり判定も行っています）
        """
        missile_count = len(self.missile)#ミサイルの総数を数える
        for i in reversed(range (missile_count)):
            if 0 <= self.missile[i].missile_type <= 3:#通常ミサイルの処理
                self.missile[i].vy = self.missile[i].y_reverse * 0.7#ミサイルの落下スピードを標準の0.7にしておく（ｙ軸反転を掛けて反転もさせる）
                #ミサイルの真下（もしくは真上）が地形かどうか？チェック
                update_bg.check_bg_collision(self,self.missile[i].posx,(((self.missile[i].posy ) // 8) * 8) + self.missile[i].y_reverse + 8,  0,0)#これで上手くいった・・なんでや・・どうしてや？
                
                if self.collision_flag == 1:#障害物に当たった時の処理
                    self.missile[i].missile_flag1 = 1#もしミサイルの真下(y_reverseが-1なら真上）が障害物ならmissile_flag1を１にして
                    self.missile[i].vy = 0#縦方向の移動量vyを0にして横方向だけに進むようにする
                    if  2 <= self.missile[i].missile_type <= 3:
                        self.missile[i].vx = -1
                
                #ミサイルの進行先が地形かどうか？チェック
                update_bg.check_bg_collision(self,self.missile[i].posx + (self.missile[i].x_reverse * 8),self.missile[i].posy + 4,0,0)
                
                if self.missile[i].missile_hp == 0:
                    del self.missile[i]#ミサイルのＨＰが0だったらインスタンスを破棄する(ミサイル消滅)
                elif self.collision_flag == 1:
                    update_obj.append_particle(self,PARTICLE_MISSILE_DEBRIS,PRIORITY_FRONT,self.missile[i].posx + (self.missile[i].missile_type // 2) * 2 - 8,self.missile[i].posy,0,0, 7,0,0)
                    #(self.missile[i].missile_type // 2) * 2 - 8の計算結果は
                    #ミサイルタイプが0右下ミサイルの場合は 0 // 2 * 2 - 8で -8
                    #ミサイルタイプが1右上ミサイルの場合は 1 // 2 * 2 - 8で -8
                    #ミサイルタイプが2左下ミサイルの場合は 2 // 2 * 2 - 8で +8
                    #ミサイルタイプが3左上ミサイルの場合は 3 // 2 * 2 - 8で +8となる よって補正値は右向きのミサイルの場合は-8 左向きのミサイルは+8となる
                    #
                    #う～ん、後方のミサイルは別にx+8の補正を入れなくても良いかもしれない・・・
                    #スクロールスピードの関係でミサイルデブリを表示した瞬間にスクロールして表示位置ずれるし
                    del self.missile[i]#ミサイルの右側が障害物だったらインスタンスを破棄する（ミサイル消滅）
                else:
                    #進行先が地形ではなく尚且つミサイルのＨＰがまだ残っていたのなら、ミサイルの位置を更新！
                    if self.missile[i].vy == 0: #地面に設置して横方向動くときだけ倍率補正値を掛け合わせたvxとする
                        self.missile[i].posx += self.missile[i].vx * self.missile_speed_magnification #ミサイルのX座標を(VX*倍率補正)分加減算して更新
                    else:   
                        self.missile[i].posx += self.missile[i].vx #上下に落ちていくときはミサイルのX座標をVXだけ加減算して更新
                    
                    self.missile[i].posy += self.missile[i].vy                             #ミサイルのY座標をVY分加減算して更新
                
            elif    self.missile[i].missile_type == 4:#テイルショットの処理        
                #テイルショットの位置が地形かどうか？チェック
                update_bg.check_bg_collision(self,self.missile[i].posx,self.missile[i].posy,0,0)
                if self.collision_flag == 1 or self.missile[i].missile_hp == 0:
                    del self.missile[i]#テイルショットの位置が障害物かもしくはテイルショットのＨＰが0だったらインスタンスを破棄する（テイルショット消滅） 
                else:
                    #進行先が地形ではなく尚且つテイルショットのＨＰがまだ残っていたのなら位置を更新！
                    self.missile[i].posx += self.missile[i].vx#テイルショットのX座標をVX分加減算して更新
                    self.missile[i].posy += self.missile[i].vy#テイルショットのY座標をVY分加減算して更新                 
            elif    self.missile[i].missile_type == 5:#ペネトレートロケットの処理
                #進行先が地形ではなく尚且つペネトレートロケットのＨＰがまだ残っていたのなら位置を更新！
                self.missile[i].vx += 0.02 #vxをだんだんと増加させていく
                self.missile[i].posx += self.missile[i].vx #ペネトレートロケットのx座標をvxと足し合わせて更新
                
                self.missile[i].vy += 0.01 #vyをだんだんと増加させていく
                self.missile[i].posy += self.missile[i].vy * self.missile[i].y_reverse #ペネトレートロケットのx,y座標をvx,vyと足し合わせて更新(y_reverseが-1ならy軸の補正が逆となる)           
            elif    self.missile[i].missile_type == 6:#サーチレーザーの処理        
                #サーチレーザーの位置が地形かどうか？チェック
                update_bg.check_bg_collision(self,self.missile[i].posx,self.missile[i].posy,0,0)
                if self.collision_flag == 1 or self.missile[i].missile_hp == 0:
                    del self.missile[i]#サーチレーザーの位置が障害物かもしくはサーチレーザーのＨＰが0だったらインスタンスを破棄する（サーチレーザー消滅） 
                else:
                    self.missile[i].posx += self.missile[i].vx          #サーチレーザーのX座標をVX分加減算して更新
                    
                    if self.missile[i].missile_flag1 == 0:#状態遷移が(敵索敵中=0)なら
                        if self.missile[i].posx > self.my_x + 16:#サーチレーザーは自機より前方16ドット進んでから索敵を始める
                            #索敵用関数の呼び出し(missile_flag2*16のぶんだけｘ方向の先で敵とのＸ座標を比較する)
                            func.search_laser_enemy_cordinate(self,self.missile[i].posx + self.missile[i].missile_flag2 * 8,self.missile[i].posy)
                            if self.search_laser_flag == 1:#敵機索敵ＯＫ！のフラグが立っていたのなら
                                self.missile[i].missile_flag1 = 1 #状態遷移を(屈折中=1)にする                  
                                self.missile[i].y_reverse = self.search_laser_y_direction #Y軸加算用の反転フラグ(-1=上方向 1=下方向)もそのまま代入
                        
                    elif self.missile[i].missile_flag1 == 1:#状態遷移が（屈折中=1)なら
                        self.missile[i].vx = 0 #x軸（横）に移動はさせないようvxに0を強制代入
                        self.missile[i].missile_flag1 = 2 #状態遷移を（縦に進行中=2)にする
                        
                        self.missile[i].width  = 8   #レーザーは縦長になるので当たり判定は16x16に変化する(本当は8x16何だけど甘めに16x16にしちゃう)
                        self.missile[i].height = 16
                        
                    elif self.missile[i].missile_flag1 == 2:#状態遷移が（縦に進行中=2)なら
                        self.missile[i].vx = 0 #x軸（横）に移動はさせないようvxに0を強制代入
                        #self.missile[i].posx += self.missile[i].vx          #サーチレーザーのX座標をVX分加減算して更新
                        self.missile[i].posy += self.missile[i].y_reverse * 2#サーチレーザーのY座標をy_reverse分加減算して更新
                
            elif    self.missile[i].missile_type == 7:#ホーミングミサイルの処理        
                if self.missile[i].missile_hp == 0:
                    del self.missile[i]#ホーミングミサイルのＨＰが0だったらインスタンスを破棄する（ホーミングミサイル消滅） 
                else:
                    func.search_homing_missile_enemy_cordinate(self,self.missile[i].posx,self.missile[i].posy)#ホーミングミサイルのposx.posyを元に一番近距離の敵の座標を見つけ出す
                    if self.search_homing_missile_flag == 1:#もし狙い撃つ敵を見つけたのなら
                        self.missile[i].tx = self.search_homing_missile_tx #ターゲットとなる敵の座標をミサイルリストのTargetX,TargetYに代入する
                        self.missile[i].ty = self.search_homing_missile_ty
                        
                    #ホーミングミサイルを目標位置まで追尾させる
                    vx0 = self.missile[i].vx
                    vy0 = self.missile[i].vy #ホーミングミサイルの速度(vx,vy)を(vx0,vy0)に退避する
                    
                    #目標までの距離を求める dに距離が入る
                    #狙うターゲットとなる座標(tx,ty)
                    self.d = math.sqrt((self.missile[i].tx - self.missile[i].posx) * (self.missile[i].tx - self.missile[i].posx) + (self.missile[i].ty - self.missile[i].posy) * (self.missile[i].ty - self.missile[i].posy))
                    
                    #ホーミングミサイルの速度 vx,vyを求める
                    #速さが一定値speedになるようにする
                    #目標までの距離dが0の時は速度を左方向にする
                    #theta(Θ)は旋回できる角度の上限
                    #ターゲット方向の速度ベクトル(vx1,vy1)を求める
                    if self.d == 0:#目標（ターゲット）までの距離は0だった？（重なっていた？）
                        vx1= 0
                        vy1 = self.missile[i].speed #目標までの距離dが0の時は速度を左方向にする
                    else:
                        #ホーミングミサイルとターゲットとの距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                    
                     vx1 = ((self.missile[i].tx - self.missile[i].posx) / (self.d * self.missile[i].speed))
                     vy1 = ((self.missile[i].ty - self.missile[i].posy) / (self.d * self.missile[i].speed))
                    #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                    #math.piはπ（円周率3.141592......)
                    #ううううぅ・・・難しい・・・・数学赤点の私には難しい・・・・
                    self.rad = 3.14 / 180 * self.missile[i].theta #rad = 角度degree（theta）をラジアンradianに変換
                    
                    self.missile[i].theta += 0.2 #旋回できる角度を増やしていく
                    if self.missile[i].theta > 360:
                        self.missile[i].theta = 360 #旋回可能角度は360度を超えないようにする
                    
                    vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                    vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                    
                    #ターゲット方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                    if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                        #ターゲット方向が旋回可能範囲内の場合の処理
                        #ターゲット方向に曲がるようにする
                        self.missile[i].vx = vx1
                        self.missile[i].vy = vy1
                    else:
                        #ターゲットが旋回可能範囲を超えている場合（ハンドルをいっぱいまで切ってもターゲットに追いつけないよ～）ハンドル一杯まで切る！
                        #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                        vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                        vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                        
                        #ホーミングミサイルからターゲットへの相対ベクトル(px,py)を求める
                        px = self.missile[i].tx - self.missile[i].posx
                        py = self.missile[i].ty - self.missile[i].posy
                        
                        #右回りか左回りを決める
                        #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                        #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                        if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                            #右回り（面舵方向）の場合
                            self.missile[i].vx = vx2
                            self.missile[i].vy = vy2
                        else:
                            #左回り（取り舵方向）の場合
                            self.missile[i].vx = vx3
                            self.missile[i].vy = vy3
                    
                    #ホーミングミサイルの座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる(座標更新！)
                    self.missile[i].posx += self.missile[i].vx#ホーミングミサイルのX座標をVX分加減算して更新
                    self.missile[i].posy += self.missile[i].vy#ホーミングミサイルのY座標をVY分加減算して更新

    #自機ミサイルのはみだしチェック（はみ出て画面外に出てしまったら消去する）
    def clip_missile(self):
        """
        自機ミサイルのはみだしチェック（はみ出て画面外に出てしまったら消去する）
        """
        missile_count = len(self.missile)#ミサイルリストの総数を数える
        for i in reversed(range (missile_count)):
            if (-24 < self.missile[i].posx < WINDOW_W + 18 ) and (-18 <self.missile[i].posy < self.bg_height + 18):
                continue
            else:
                del self.missile[i]

    #!自機クローの移動関連###############################################################################################################
    #クローの更新
    def claw(self):
        """
        クローの更新
        """
        if   self.claw_type == ROLLING_CLAW: #ローリングクローの時のみ実行
            #ひとつ前を回るクローとの回転角度の差の計算処理
            if self.claw_number   == 4:#クロー4機の時の処理
                self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                self.claw[1].angle_difference = self.claw[2].degree - self.claw[1].degree
                self.claw[2].angle_difference = self.claw[3].degree - self.claw[2].degree
                self.claw[3].angle_difference = self.claw[0].degree - self.claw[3].degree
            elif self.claw_number == 3:#クロー3機の時の処理
                self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                self.claw[1].angle_difference = self.claw[2].degree - self.claw[1].degree
                self.claw[2].angle_difference = self.claw[0].degree - self.claw[2].degree
            elif self.claw_number == 2:#クロー2機の時の処理
                self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                self.claw[1].angle_difference = self.claw[0].degree - self.claw[1].degree
                #クローが1機と0機の時は角度計算しないのです
            
            #クローの回転処理
            claw_count = len(self.claw)#クローの数を数える
            for i in range(claw_count):
                if self.claw[i].status == 0:#ステータスが(0)の場合は回転開始の初期位置まで動いていく（自機の真上）
                    #self.claw[i].offset_x += self.claw[i].roll_vx
                    #self.claw[i].offset_y += self.claw[i].roll_vy#現在のオフセット座標値をroll_vx,roll_vyの分だけ加減算させていく
                    #
                    #self.claw[i].posx = self.my_x + self.claw[i].offset_x
                    #self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていって回転開始位置まで移動させてやる
                    #if  self.claw[i].offset_x == self.claw[i].offset_roll_x and self.claw[i].offset_y == self.claw[i].offset_roll_y:
                    #      self.claw[i].status = 1#回転開始初期位置のオフセット値まで行ったのならステータスを回転開始(1)にする
                    if self.claw[i].offset_x < self.claw[i].offset_roll_x:#offset_xとyをoffset_fix_xとyに+1ドット単位で増減させて同じ値に近づけていく
                        self.claw[i].offset_x += 1
                    elif self.claw[i].offset_x > self.claw[i].offset_roll_x:
                        self.claw[i].offset_x -= 1
                    
                    if self.claw[i].offset_y < self.claw[i].offset_roll_y:
                        self.claw[i].offset_y += 1
                    elif self.claw[i].offset_y > self.claw[i].offset_roll_y:
                        self.claw[i].offset_y -= 1
                    
                    self.claw[i].posx = self.my_x + self.claw[i].offset_x
                    self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていって回転開始位置まで移動させてやる
                    if  int(self.claw[i].offset_x) == int(self.claw[i].offset_roll_x) and int(self.claw[i].offset_y) == int(self.claw[i].offset_roll_y):
                        self.claw[i].status = 1#ローリングクロー回転開始初期位置のオフセット値まで行ったのならステータスを回転開始！！(1)にする 比較するときはint()を使って切り捨てた整数値で比較する
                    
                elif  self.claw[i].status == 1:#ステータスが(1)の場合は回転開始！
                    if self.claw[i].angle_difference == self.claw_difference:
                        self.claw[i].degree -= self.claw[i].speed#クローの個数に応じた回転間隔
                    elif self.claw[i].angle_difference > self.claw_difference:
                        self.claw[i].degree -= self.claw[i].speed - 1
                    else:
                        self.claw[i].degree -= self.claw[i].speed + 1
                    
                    self.claw[i].degree = self.claw[i].degree % 360#角度は３６０で割った余りとする(0~359)
                    #極座標(r,θ)から直交座標(x,y)への変換は
                    #     x = r cos θ
                    #     y = r sin θ
                    self.claw[i].offset_x = self.claw[i].radius *   math.cos(math.radians(self.claw[i].degree))
                    self.claw[i].offset_y = self.claw[i].radius *  -math.sin(math.radians(self.claw[i].degree))
                    
                    #クローの座標を自機の座標を中心としオフセット値を足した物とする
                    #線形補間値0.2で線形補間してやる（ピッタリ自機に付いてくる）
                    self.claw[i].posx = self.claw[i].posx + 0.2 * ((self.my_x + self.claw[i].offset_x) - self.claw[i].posx)
                    self.claw[i].posy = self.claw[i].posy + 0.2 * ((self.my_y + self.claw[i].offset_y) - self.claw[i].posy)
            
        elif self.claw_type == TRACE_CLAW:   #トレースクローの時のみ実行
            for i in range(self.claw_number):#iの値は0からクローの数まで増えてイクです  ハイ！
                self.claw[i].status = 1#トレースクローは出現と同時に移動開始のステータスにする
                self.claw[i].posx = self.claw_coordinates[self.trace_claw_index + (TRACE_CLAW_BUFFER_SIZE - self.trace_claw_distance) - self.trace_claw_distance * i].posx#クローの座標をオフセット値のＸＹ座標とする
                self.claw[i].posy = self.claw_coordinates[self.trace_claw_index + (TRACE_CLAW_BUFFER_SIZE - self.trace_claw_distance) - self.trace_claw_distance * i].posy
            
        elif self.claw_type == FIX_CLAW:     #フィックスクローの時のみ実行
            claw_count = len(self.claw)#クローの数を数える
            for i in range(claw_count):
                if self.claw[i].status == 0:#ステータスが(0)の場合はフイックスクローの初期位置まで動いていく（自機の上か下）
                    if self.claw[i].offset_x < self.claw[i].offset_fix_x:#offset_xとyをoffset_fix_xとyに0.5単位で増減させて同じ値に近づけていく
                        self.claw[i].offset_x += 0.5
                    elif self.claw[i].offset_x > self.claw[i].offset_fix_x:
                        self.claw[i].offset_x -= 0.5
                    
                    if self.claw[i].offset_y < self.claw[i].offset_fix_y:
                        self.claw[i].offset_y += 0.5
                    elif self.claw[i].offset_y > self.claw[i].offset_fix_y:
                        self.claw[i].offset_y -= 0.5
                    
                    self.claw[i].posx = self.my_x + self.claw[i].offset_x
                    self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていってクロ―固定位置まで移動させてやる
                    
                    if  -0.5 <= self.claw[i].offset_x - self.claw[i].offset_fix_x <= 0.5 and -0.5 <= self.claw[i].offset_y - self.claw[i].offset_fix_y <= 0.5:
                        self.claw[i].status = 1#クロー固定位置のオフセット値付近(+-0.5)まで行ったのならステータスをクロー固定完了！！(1)にする
                    
                elif self.claw[i].status == 1:#ステータスが(1)の場合はフイックスクローの固定は完了したので弾を発射とかしちゃう
                    if i <=1:
                        #クローの座標を自機の座標を中心としオフセット値を足した物とする
                        #クローナンバー0と1（内側のクロー）は線形補間値0.2で線形補間してやる（ピッタリ自機に付いてくる）
                        self.claw[i].posx = self.claw[i].posx + 0.2 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                        self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + (self.claw[i].offset_y * self.fix_claw_magnification) - self.claw[i].posy)
                    else:
                        #クローの座標を自機の座標を中心としオフセット値を足した物とする
                        #クローナンバー2と3（外側のクロー）は線形補間値0.1で線形補間してやる（ちょっと遅れて自機に引っ付いてくる）
                        self.claw[i].posx = self.claw[i].posx + 0.1 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                        self.claw[i].posy = self.claw[i].posy + 0.1 * (self.my_y + (self.claw[i].offset_y * self.fix_claw_magnification) - self.claw[i].posy)
            
        elif self.claw_type == REVERSE_CLAW: #リバースクローの時のみ実行
            claw_count = len(self.claw)#クローの数を数える
            for i in range(claw_count):
                if self.claw[i].status == 0:#ステータスが(0)の場合はリバースクローの初期位置まで動いていく（自機の上か下）
                    if self.claw[i].offset_x < self.claw[i].offset_reverse_x:#offset_xとyをoffset_reverse_xとyに0.5単位で増減させて同じ値に近づけていく
                        self.claw[i].offset_x += 0.5
                    elif self.claw[i].offset_x > self.claw[i].offset_reverse_x:
                        self.claw[i].offset_x -= 0.5
                    
                    if self.claw[i].offset_y < self.claw[i].offset_reverse_y:
                        self.claw[i].offset_y += 0.5
                    elif self.claw[i].offset_y > self.claw[i].offset_reverse_y:
                        self.claw[i].offset_y -= 0.5
                    
                    self.claw[i].posx = self.my_x + self.claw[i].offset_x
                    self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていってクロ―固定位置まで移動させてやる
                    
                    if  -0.5 <= self.claw[i].offset_x - self.claw[i].offset_reverse_x <= 0.5 and -0.5 <= self.claw[i].offset_y - self.claw[i].offset_reverse_y <= 0.5:
                        self.claw[i].status = 1#リバースクローの開始のオフセット値付近(+-0.5)まで行ったのならステータスをクロー固定完了！！(1)にする
                    
                elif self.claw[i].status == 1:#ステータスが(1)の場合はリバースクローの固定は完了したので弾を発射とかしちゃう
                    if i == 1 or i == 2:
                        #クローの座標を自機の座標を中心としオフセット値を足した物とする
                        #クローナンバー1と2（上下のクロー）は線形補間値0.3で線形補間してやる（ピッタリ自機に付いてくる）
                        self.claw[i].posx = self.claw[i].posx + 0.3 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                        self.claw[i].posy = self.claw[i].posy + 0.3 * (self.my_y + self.claw[i].offset_y - self.claw[i].posy)
                    else:
                        #クローの座標を自機の座標を中心としオフセット値を足した物とする
                        #クローナンバー0と3（後部についてくるクロー）は線形補間値0.2で線形補間してやる（ちょっと遅れて自機に引っ付いてくる）
                        self.claw[i].posx = self.claw[i].posx + 0.2 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                        if self.claw_number == 4:#クローが4機の場合は定着させるＹ座標をそれぞれ変化させる
                            self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + self.claw[i].offset_y + ((i * 3) - 4) - self.claw[i].posy)
                            #クローナンバーi=0の時は(i*3)-4=0*3-4=-4で Y軸の補正値が-4になる
                            #クローナンバーi=3の時は(i*3)-4=3*3-4=+5で Y軸の補正値が+5になる
                        else:#クローが１～３機のときは固定位置は変化させない
                            self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + self.claw[i].offset_y - self.claw[i].posy)

    #クローショットの更新
    def claw_shot(self):
        """
        クローショットの更新
        """
        claw_shot_count = len(self.claw_shot)#クローの弾の数を数える
        for i in reversed(range (claw_shot_count)):
            #クローの弾の位置を更新！
            self.claw_shot[i].posx += self.claw_shot[i].vx * self.claw_shot_speed #弾のX座標をVX*claw_shot_speed分加減算して更新
            self.claw_shot[i].posy += self.claw_shot[i].vy * self.claw_shot_speed #弾のY座標をVY*claw_shot_speed分加減算して更新
            
            if self.claw_shot[i].shot_hp != 0:
                if (-16 < self.claw_shot[i].posx < WINDOW_W + 16 ) and (-16 <self.claw_shot[i].posy < self.bg_height + 16):
                    continue
                else:
                    del self.claw_shot[i]#クローショットが画面外まで飛んで行ってはみ出ていたのならインスタンス破棄（クローショット消滅）
            else:
                del self.claw_shot[i]#クローショットのHPがゼロだったらインスタンスを破棄する（クローショット消滅）

    #クローの追加
    def append_claw(self):
        """
        クローの追加
        """
        if   len(self.claw) == NO_CLAW:#1機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 1
            self.claw_difference = 360 / self.claw_number
            new_claw.update(ID00,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  -1,0,      0,0,  0,-12,  -2,-12,    -2,-12,   -12,-1,  0,0,    90,0,2,12,    self.claw_difference,0,   0,1,   0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == ONE_CLAW:#2機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 2
            self.claw_difference = 360 / self.claw_number
            new_claw.update(ID01,   self.claw_type,0,    posx,posy,  0,-1,   -1,1,  0,-1,       0,0, 0,-12,    -2,12,  -2,12,   -3,-9, 0,0,       90,0,2,12,    self.claw_difference,0,   0,1,   0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == TWO_CLAW:#3機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 3
            self.claw_difference = 360 / self.claw_number
            new_claw.update(ID02,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  0,1,       0,0,  0,-12,    -6,-24, -6,-24,  -3,8,   0,0,      90,0,2,12,    self.claw_difference,0,   0,1,    0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == THREE_CLAW:#4機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 4
            self.claw_difference = 360 / self.claw_number
            new_claw.update(ID03,   self.claw_type,0,    posx,posy,  0,-1,    -1,1,   -1,0,       0,0, 0,-12,    -6,24,  -6,24,  -12,-1,     0,0,       90,0,2,12,   self.claw_difference,0,    0,1,      0)
            self.claw.append(new_claw)
            return

    #クローが弾を発射!!!!!!
    def fire_claw_shot(self):
        """
        クローが弾を発射!!!!!!
        """
        if (pyxel.frame_count % 16) == 0: #16フレーム毎だったら クローショットを育成する
            if len(self.claw_shot) < CLAW_RAPID_FIRE_NUMBER * (self.claw_number):#クローショットの要素数がクローの数x２以下なら弾を発射する
                #ここからクローが弾を発射する実処理
                claw_count = len(self.claw)#クローの数を数える
                for i in range(claw_count):
                        if self.claw[i].status != 0:#ステータスが0の時は初期回転位置や初期固定位置に移動中なので弾は発射しない
                            new_claw_shot = Claw_shot()
                            if self.claw_type == REVERSE_CLAW:#クロータイプがリバースクローの時はクローショットの方向をreverse_claw_svx,reverse_claw_svyにして8方向弾にする
                                new_claw_shot.update(0,self.claw[i].posx,self.claw[i].posy,    self.reverse_claw_svx,self.reverse_claw_svy,   8,8,   0,0,  1,1)
                                self.claw_shot.append(new_claw_shot)
                            else:#リバースクロー以外のクローは全て前方に弾を撃つ
                                new_claw_shot.update(0,self.claw[i].posx,self.claw[i].posy,    3,0,   8,8,   0,0,  1,1)
                                self.claw_shot.append(new_claw_shot)

    #フイックスクローの間隔を変化させる
    def change_fix_claw_interval(self):
        """
        フイックスクローの間隔を変化させる
        """
        if (pyxel.frame_count % 8) == 0:
            self.fix_claw_magnification += 0.1      #ボタンが押されたら0.1刻みで増加させる
            if self.fix_claw_magnification >= 2:
                self.fix_claw_magnification = 0.4   #2以上になったら0.4にする

    #クロースタイルの変更
    def change_claw_style(self):
        """
        クロースタイルの変更
        """
        self.claw_type += 1#クローの種類を変化させる
        if self.claw_type > REVERSE_CLAW: #もしtype3のリバースタイプを超えてしまったら0のローリングタイプにする
            self.claw_type = ROLLING_CLAW
        
        claw_count = len(self.claw)
        for i in reversed(range(claw_count)):
            self.claw[i].status = 0#全てのクローのステータスを0=回転開始や固定開始の初期位置まで動いていくにする

    #!スピードチェンジ関連#################################################################################################################
    #自機のスピードチェンジ!!!!
    def change_ship_speed(self):
        """
        自機のスピードチェンジ!!!!
        """
        if self.my_speed == 1:
            self.my_speed = 1.5
        elif self.my_speed == 1.5:
            self.my_speed = 1.75
        else:
            self.my_speed = 1

    #!武器発射関連#########################################################################################################################
    #ショットを発射する!!!!!
    def fire_shot(self):
        """
        ショットを発射する!!!!!
        """
        if self.shot_level == SHOT_LV7_WAVE_CUTTER_LV1:#ウェーブカッターLv1発射
            if len(self.shots) < self.shot_rapid_of_fire:
            #if self.shot_type_count(self.shot_level) < 3: 
                if (pyxel.frame_count % 8) == 0:
                    update_sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)#チャンネル2でサウンドナンバー5=SE_WAVE_CUTTERを鳴らす
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -4,      3,0,  8,16,  0,   2,1)
                    
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV8_WAVE_CUTTER_LV2:#ウェーブカッターLv2発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 8) == 0:
                    update_sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)#チャンネル2でサウンドナンバー5=SE_WAVE_CUTTERを鳴らす
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -8,      3,0,  8,24,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV9_WAVE_CUTTER_LV3:#ウェーブカッターLv3発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 8) == 0:
                    update_sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)#チャンネル2でサウンドナンバー5=SE_WAVE_CUTTERを鳴らす
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,      3,0,  8,32,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV10_WAVE_CUTTER_LV4:#ウェーブカッターLv4発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 6) == 0:
                    update_sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol) #チャンネル2でサウンドナンバー5=SE_WAVE_CUTTERを鳴らす
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,      4,0,  8,32,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV4_LASER:      #レーザー発射
            if len(self.shots) < 20:
                if (pyxel.frame_count % 2) == 0:
                    update_sound.se(self,2,SE_LASER,self.master_se_vol)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y,         3,1,  8,8,  0,   0.3,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV5_TWIN_LASER: #ツインレーザー発射
            if len(self.shots) < 40:
                if (pyxel.frame_count % 2) == 0:
                    update_sound.se(self,2,SE_LASER,self.master_se_vol)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y - 3,     3,1,  8,8,  -3,  0.3,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y + 3,     3,1,  8,8,    3, 0.3,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV6_3WAY_LASER: #３ＷＡＹレーザー発射
            if len(self.shots) < 80:
                if (pyxel.frame_count % 2) == 0:
                    update_sound.se(self,2,SE_LASER,self.master_se_vol)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 1,self.my_y  -1,    1,-1.08,   8,8,   -1,  0.2,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y,       3,1,      8,8,    0,  0.3,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 1,    2, 1.07,   8,8,    1,  0.2,1)
                    self.shots.append(new_shot)
        
        func.count_missile_type(self,5,5,5,5) #ミサイルタイプ5(ペネトレートロケット）がいくつ存在するのか調べる
        if self.type_check_quantity == 0 and self.select_sub_weapon_id == PENETRATE_ROCKET:#もしペネトレートロケットが全く存在しないのなら発射する！！！
            new_missile = Missile()
            new_missile.update(5,self.my_x + 4,self.my_y,   -0.8,-0.7,   6,    1   ,0,0,   0,1,   8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
            
            new_missile = Missile()
            new_missile.update(5,self.my_x + 4,self.my_y,   -0.8,-0.7,   6,    1   ,0,0,   0,-1,  8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
            
            new_missile = Missile()
            new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,1,    8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
            
            new_missile = Missile()
            new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,-1,    8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
        
        func.count_missile_type(self,4,4,4,4) #ミサイルタイプ4(テイルショット）がいくつ存在するのか調べる    
        if self.type_check_quantity < self.sub_weapon_tail_shot_level_data_list[self.sub_weapon_list[TAIL_SHOT]-1][1] and self.select_sub_weapon_id == TAIL_SHOT and (pyxel.frame_count % 6) == 0:#もしテイルショットが全く存在しないのなら発射する！！！
            level = self.sub_weapon_list[TAIL_SHOT] #現在のテイルショットのレベルを取得する
            #テイルショットのレベルデータリストから現時点のレベルに応じたデータを取得する
            speed = self.sub_weapon_tail_shot_level_data_list[level - 1][2] #スピード
            power = self.sub_weapon_tail_shot_level_data_list[level - 1][3] #攻撃力
            n_way = self.sub_weapon_tail_shot_level_data_list[level - 1][4] #n_way数
            if n_way == 1 or n_way == 3: #真後ろにテイルショット発射
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#真後ろに射出されるテイルショット育成
                if n_way == 3: #3wayの場合は更に斜め後ろ方向にテイルショット発射
                    new_missile = Missile()
                    new_missile.update(4,self.my_x - 4,self.my_y - 2,   -2*speed,-0.5,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                    self.missile.append(new_missile)#斜め後ろ(上)のテイルショット育成
                    
                    new_missile = Missile()
                    new_missile.update(4,self.my_x - 4,self.my_y + 2,   -2*speed, 0.5,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                    self.missile.append(new_missile)#斜め後ろ(下)のテイルショット育成
                
            elif n_way == 2: #ツインテイルショット発射
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y - 2,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#ツインテイルショット(上)育成
                
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y + 2,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#ツインテイルショット(下)育成
        
        func.count_missile_type(self,6,6,6,6) #ミサイルタイプ6(サーチレーザー）がいくつ存在するのか調べる
        if self.type_check_quantity <= 1 and self.select_sub_weapon_id == SEARCH_LASER and pyxel.frame_count % 32 == 0: #サーチレーザーが全く存在しないのなら発射する！！！
            new_missile = Missile()
            new_missile.update(6,self.my_x + 14,self.my_y,   2,0,   1,1,   0,1,   0,0,   16,8,  0,0,  0,0) #サーチレーザー(flag2=1なのでちょっとｘ軸前方向に対して索敵する)
            self.missile.append(new_missile)#サーチレーザー育成
            
            new_missile = Missile()
            new_missile.update(6,self.my_x    ,self.my_y,   2,0,   1,1,   0,0,   0,0,   16,8,  0,0,  0,0) #サーチレーザー
            self.missile.append(new_missile)#サーチレーザー育成
        
        func.count_missile_type(self,7,7,7,7) #ミサイルタイプ7(ホーミングミサイル）がいくつ存在するのか調べる
        if self.type_check_quantity <= self.sub_weapon_homing_missile_level_data_list[self.sub_weapon_list[HOMING_MISSILE]-1][1] - 4 and self.select_sub_weapon_id == HOMING_MISSILE and pyxel.frame_count % 8 == 0: #ホーミングミサイルの個数が1以下なら発射する！！！
            level = self.sub_weapon_list[HOMING_MISSILE] #現在のホーミングミサイルのレベルを取得する
            #ホーミングミサイルのレベルデータリストから現時点のレベルに応じたデータを取得する
            speed = self.sub_weapon_homing_missile_level_data_list[level - 1][2] #スピード
            power = self.sub_weapon_homing_missile_level_data_list[level - 1][3] #攻撃力
            new_missile = Missile()
            new_missile.update(7,self.my_x - 4,self.my_y,   -2*speed,1*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            new_missile = Missile()
            new_missile.update(7,self.my_x - 4,self.my_y,   -2*speed,-1*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            
            new_missile = Missile()
            new_missile.update(7,self.my_x + 4,self.my_y + 2,   0*speed,2*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            new_missile = Missile()
            new_missile.update(7,self.my_x + 4,self.my_y - 2,   0*speed,-2*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
        
        if len(self.shots) < (self.shot_rapid_of_fire + (self.shot_level) * 2):#バルカンショットの発射
            if (pyxel.frame_count % 6) == 0:    
                if self.shot_level == SHOT_LV0_VULCAN_SHOT:#初期ショット バルカンショット1連装
                    update_sound.se(self,2,SE_VULCAN_SHOT,self.master_se_vol)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 4,self.my_y    ,4,0,  8,8,    0, 1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV1_TWIN_VULCAN_SHOT:#ツインバルカンショット 2連装
                    update_sound.se(self,2,SE_VULCAN_SHOT,self.master_se_vol)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,4,0,  8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,4,0,  8,8,     0,  1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV2_3WAY_VULCAN_SHOT:#３ＷＡＹバルカンショット
                    update_sound.se(self,2,SE_VULCAN_SHOT,self.master_se_vol)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2  ,5,-0.3,  8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y     ,5,0,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2  ,5,0.3,   8,8,    0,  1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV3_5WAY_VULCAN_SHOT:#５ＷＡＹバルカンショット
                    update_sound.se(self,2,SE_VULCAN_SHOT,self.master_se_vol)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,    5,-1,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 1,    5,-0.3,   8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y,       5,0,     8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 1,    5,0.3,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,    5,1,     8,8,    0,  1,1)
                    self.shots.append(new_shot)

    #ミサイルを発射する!!!!!
    def fire_missile(self):
        """
        ミサイルを発射する!!!!!
        """
        if (pyxel.frame_count % 10) == 0:
            func.count_missile_type(self,0,1,2,3)#ミサイルタイプ0,1,2,3の合計数を数える
            if self.type_check_quantity < (self.missile_level + 1) * self.missile_rapid_of_fire:  #初期段階では２発以上は出せないようにする
                if self.missile_level == MISSILE_LV0_NORMAL_MISSILE:
                    update_sound.se(self,2,SE_MISSILE,self.master_se_vol)
                    new_missile = Missile()
                    new_missile.update(0,self.my_x + 4,self.my_y,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8  ,0,0,   0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                elif self.missile_level == MISSILE_LV1_TWIN_MISSILE:
                    update_sound.se(self,2,SE_MISSILE,self.master_se_vol)
                    new_missile = Missile()
                    new_missile.update(0,self.my_x + 2,self.my_y +2,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8,  0,0,   0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(1,self.my_x + 2,self.my_y -2,   0.7,0.7,   3,    1   ,0,0    ,1,-1,  8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                elif self.missile_level == MISSILE_LV2_MULTI_MISSILE:
                    update_sound.se(self,2,SE_MISSILE,self.master_se_vol)
                    new_missile = Missile()
                    new_missile.update(0,self.my_x +2,self.my_y +2,   0.7,0.7,    3,    1   ,0,0,    1,1,   8,8,  0,0,  0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(1,self.my_x +2,self.my_y -2,   0.7,0.7,    3,    1   ,0,0    ,1,-1,   8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(2,self.my_x -2,self.my_y +2,   -0.7,0.7,   3,    1   ,0,0,    -1,1,    8,8,  0,0,   0,0) #後方左下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(3,self.my_x -2,self.my_y -2,   -0.7,0.7,   3,    1   ,0,0    ,-1,-1,   8,8,  0,0,   0,0) #後方左上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成

    #!武装選択関連##########################################################################################################################
    #サブウェポンを切り替える!!!!!
    def change_sub_weapon(self):
        """
        サブウェポンを切り替える!!!!!
        """
        for __i in range(5):#5回繰り返す
            self.select_sub_weapon_id += 1#サブウェポンIDを増やして切り替えていく
            if self.select_sub_weapon_id >= 5:#idナンバーが5以上になったら
                self.select_sub_weapon_id = 0#強制的にidナンバーを0にする
            
            if self.sub_weapon_list[self.select_sub_weapon_id] != 0:#サブウェポンを変更してそれが所持しているものならば
                break#ブレイクしてループを抜け出す そうでないのならばサブウェポンは5種類あるので,最大5回ループして所持しているものを見つけ出すまで繰り返す

    #!ダメージ処理関連#######################################################################################################################
    #自機が被弾しダメージを受け、シールドパワー減少、ダメージ音再生、ダメージを受けた後の無敵時間の設定
    def damage(self,damage):
        """
        自機が被弾しダメージを受け、シールドパワー減少、ダメージ音再生、ダメージを受けた後の無敵時間の設定
        
        damage=ダメージ値
        """
        self.my_shield -= damage                 #シールドパワーをdamage分減少させる
        self.damaged_flag              = FLAG_ON #自機がダメージを受けたかどうかのフラグをONにします(スコアスターの連続取得時の倍率上昇で使用するフラグです)
        self.stage_battle_damaged_flag = FLAG_ON #1ステージ用のダメージを受けたかどうかのフラグをONにします(ステージスタートした時にオフ、ダメージ受けたらオン)
        self.boss_battle_damaged_flag  = FLAG_ON #ボス戦用のダメージを受けたかどうかのフラグをONにします   (ステージスタートした時にオフ、ボス出現時にオフ、ダメージ受けたらオン)
        
        self.score_star_magnification = 1 #スコアスター取得点数の倍率は初期値の1倍に戻っちゃいます・・・・残念・・・
        if self.my_shield < 0:
            self.my_shield = 0 #シールドパワーがマイナスまで行ってしまったら0に修正する
        
        update_sound.se(self,0,SE_SHIP_DAMAGE,self.master_se_vol) #自機ダメージ音再生
        self.invincible_counter += self.invincible_time        #ダメージ後の無敵時間を加算する
        
        self.rank_down_count += 1 #ランクダウン用カウンタを１増やす
        if self.rank_down_count == self.rank_down_need_damage: #カウンタがランクダウンに必要であるダメージ分まで増えたのなら
            func.rank_down(self)  #1ランクダウンさせる関数の呼び出し
            self.rank_down_count = 0 #カウンターをリセット

    #自機のシールドパワーがまだあるのかチェックする
    def check_shield(self):
        """
        自機のシールドパワーがまだあるのかチェックする
        """
        if self.my_shield <= 0:
            self.game_status = Scene.EXPLOSION #シールドパワーが0以下になってしまったのでステータスを爆発中にする
            #自機の座標に爆発を生成する
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_MY_SHIP,PRIORITY_MORE_FRONT,self.my_x - 4 ,self.my_y-2,0,0,64,RETURN_BULLET_NONE,0,  1,1)
            self.explosions.append(new_explosion)
            
            #爆発音再生
            update_sound.se(self,2,SE_SHIP_BROKEN,self.master_se_vol)
