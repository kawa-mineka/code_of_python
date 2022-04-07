###########################################################
#  update_bossクラス                                      #      
###########################################################
# Appクラスのupdate関数から呼び出される関数群                #
# 主にボスの更新を行うメソッド                               #
# ボスの移動更新、ボスのクリッピング                         #
# 当たり判定は別のクラス(update_collision)で行う             #
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_obj import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)

class update_boss:
    def __init__(self):
        None

    ####################################ボス関連の処理関数########################################
    #ボスの更新
    def boss(self):
        boss_count = len(self.boss)
        for i in reversed (range(boss_count)):
            if   self.boss[i].boss_type == BOSS_FATTY_VALGUARD: #ボスタイプ1の更新 ファッティ・バルガード ###########################
                if   self.boss[i].status == BOSS_STATUS_MOVE_COORDINATE_INIT:  #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                    func.boss_get_bezier_curve_coordinate(self,i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                    self.boss[i].status = BOSS_STATUS_MOVE_BEZIER_CURVE #状態遷移を「ベジェ曲線で移動」に設定
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_BEZIER_CURVE:    #「ベジェ曲線で移動」
                    t = self.boss[i].obj_time / self.boss[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        self.boss[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする                    
                        self.boss[i].move_index += 1 #目的座標のリストのインデックスを1進める
                        if self.boss_move_data1[self.boss[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                            self.boss[i].move_index = 0 #リストインデックス値を0にしてリセットする
                        func.boss_get_bezier_curve_coordinate(self,i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                        t = self.boss[i].obj_time / self.boss[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                    
                    #          A(移動元)--D(移動先)
                    #            \    点P /     
                    #(AとQの内分点)P1\     /P2(QとDの内分点)    
                    #              \   /
                    #               Q(制御点)
                    #
                    #内分の公式からP1の座標は((1-t)ax+t*qx,(1-t)ay+t*qy)
                    #           P2の座標は((1-t)qx+t*dx,(1-t)qy+t*dy)
                    #したがってPの座標も内分の公式から求められる
                    #P1の座標を(p1x,p1y),P2の座標を(p2x,p2y)とすると点Pの座標は
                    #        ((1-t)p1x+t*p2x,(1-t)p1y+t*p2y)となり
                    #先に求めたP1,P2を代入してやると
                    #        ((1-t)(1-t)ax+t*qx+t*(1-t)qx+t*dx,(1-t)(1-t)ay+t*qy+t*(1-t)qy+t*dy)となる
                    p1x = (1-t) * self.boss[i].ax + t * self.boss[i].qx
                    p1y = (1-t) * self.boss[i].ay + t * self.boss[i].dy
                    p2x = (1-t) * self.boss[i].qx + t * self.boss[i].dx
                    p2y = (1-t) * self.boss[i].qy + t * self.boss[i].dy
                    
                    px = (1-t) * p1x + t * p2x
                    py = (1-t) * p1y + t * p2y
                    
                    self.boss[i].posx = px 
                    self.boss[i].posy = py
                    
                    self.boss[i].speed = self.boss[i].speed * self.boss[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします
                    if self.boss[i].speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                        self.boss[i].speed = 0.2
                    self.boss[i].obj_time += self.boss[i].speed #タイムフレーム番号をスピード分加算していく
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                    self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                    if self.boss[i].degree >= 360:
                        self.boss[i].degree = 0
                    
                    #(x**2+y**2)**2=2a**2(x**2-y**2) (ベルヌーイのレムニスケート曲線)を使用
                    #極座標を(r,θ）とする
                    #
                    #x**2 + y**2 = r**2
                    #x = r*cos(θ)
                    #y = r*cos(θ)より
                    #(r**2)**2 = 2(r**2(cos(θ)**2) - r**2(sin(θ)**2)
                    #(r**2)**2 = 2r**2(cos(θ)**2 - sin(θ)**2)
                    #
                    #cos(θ)**2 + sin(θ)**2 = 1 尚且つ・・・
                    #cos(θ)**2 - sin(θ)**2 = cos(2θ) となるので・・・
                    #
                    #(r**2)**2 = 2r**2(cos(2θ))
                    #r**2 = 2a2cos(2θ)
                    #となるはず・・・・多分
                    #
                    #
                    #x = sqrt(2)*cos(degree) / (sin(degree)**2+1)
                    #y = sqrt(2)*cos(degree)*sin(degree) / (sin(degree)**2+1)
                    #
                    #？？？「ベルヌーイだよ、レムニスケートは別名ヤコブ・ベルヌーイのレムニスケートとも呼ばれてるよ」
                    #
                    #横スクロールシューティングで縦に倒した状態のレムニスケート曲線を描きたいのでx座標とy座標を入れ替えて使用します
                    self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 50
                    self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 30 + 80
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:      #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:           #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:    #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:         #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + func.s_rndint(self,0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + func.s_rndint(self,0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:        #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機のオートムーブモードをonにして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                               #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if   self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY:         #画面上部を左から右に弧を描いて移動中
                    if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら60フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                    
                    if (pyxel.frame_count % 100) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら100フレーム毎に
                        ex = self.boss[i].posx + 16
                        ey = self.boss[i].posy
                        length = 2
                        speed =  1
                        func.enemy_red_laser(self,ex,ey,length,speed) #レッドレーザービーム発射！
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_RIGHT_GREEN_LASER:    #背後で下から上に移動中
                    if (pyxel.frame_count % 30) == 0: #30フレーム毎に
                        ex = self.boss[i].posx + 48
                        ey = self.boss[i].posy + 27
                        length = 4
                        speed = -3 #画面左端にボスが居るので右方向にレーザー発射（マイナスのスピードだと反転され右方向に射出される）
                        func.enemy_green_laser(self,ex,ey,length,speed) #グリーンレーザービーム発射！
                    
                    if (pyxel.frame_count % 30) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら30フレーム毎に
                        ex = self.boss[i].posx + 16
                        ey = self.boss[i].posy
                        length = 2
                        speed =  1
                        func.enemy_red_laser(self,ex,ey,length,speed) #レッドレーザービーム発射！
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_AIM_BULLET:#前方で上から下に移動中
                    if (pyxel.frame_count % int(40 * self.enemy_bullet_interval / 100)) == 0: #40フレーム毎に
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                        
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_aim_bullet(self,ex,ey,0,0,0,0,1)        #狙い撃ち弾発射
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_HOMING:    #下部を右から左に弧を描いて移動中
                    if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #60フレーム毎に5way砲台が健在なら
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                    if self.boss[i].posx < 10:
                        if (pyxel.frame_count % 20) == 0: #20フレーム毎に
                            if len(self.enemy) < 400:
                                new_enemy = Enemy()#敵8ツインアローを1機生み出す
                                new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.boss[i].posx + 48,self.boss[i].posy + 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   1,-1,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,1,       0,0,0,0,        E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                self.enemy.append(new_enemy)#リストにアペンド追加！
                
            elif self.boss[i].boss_type == BOSS_BREEZARDIA:    #ボスタイプ0の更新 ブリザーディア ##################################
                #flag1  = 主砲が発射中なのかのフラグ
                #direction = 前進か更新かの方向フラグ(1=前進 0=後進)
                #count1 = 主砲が何発撃ったのか？のカウント用
                #count2 = ボスを破壊した時に真っ二つになる演出全体のフレーム数
                #count3 = 主砲の待ち時間用カウンタ
                #offset_x = x軸のオフセット値
                #weapon2を前部グリーンレーザー砲とします
                if   self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                    if self.boss[i].direction == 0: #x軸の移動方向が後進だったのなら
                        self.boss[i].offset_x -= 0.05 #x軸のオフセット値を減らす
                    else:
                        self.boss[i].offset_x += 0.3 #前進だったのでx軸のオフセット値を増やす
                    
                    self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                    if self.boss[i].degree >= 360:
                        self.boss[i].degree = 0
                    self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 40 + 60
                    self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 80/2 + 20 + self.boss[i].offset_x
                    
                    if self.boss[i].posx > WINDOW_W - 40: #x座標が画面右端を超えたのなら
                        self.boss[i].direction = 0         #方向を後退(0)にする
                    elif self.boss[i].posx < -60:        #x座標が画面左端を超えたのなら
                        self.boss[i].direction = 1         #方向を前進(1)にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:      #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:           #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:    #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:         #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + func.s_rndint(self,0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + func.s_rndint(self,0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします 
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:        #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag             = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time     = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機の移動モードをを「AUTO」にして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                                 #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY: #画面上部を左から右に弧を描いて移動中
                    if (pyxel.frame_count % 120) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら120フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_3way_bullet(self,ex,ey) #前方3way発射！
                    
                    if (pyxel.frame_count % 180) == 0 and self.boss[i].parts4_flag == 1: #上部グリーンカッターが健在なら180フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -1,0,      1.05,    1,1,    0,0,  0,0,0,            0,   0,0,PRIORITY_BOSS_BACK,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
                    
                    if self.boss[i].weapon1_status == WEAPON_READY and self.boss[i].parts3_flag == 1: #上部主砲が健在で主砲待機中ならば・・
                        if self.boss[i].weapon1_cool_down_time > 0:
                            self.boss[i].weapon1_cool_down_time -= 1 #主砲の休憩時間カウンタを1減らして行く
                        
                        if self.my_x > self.boss[i].posx + 48 and self.my_y < self.boss[i].posy + 4 and self.boss[i].weapon1_cool_down_time == 0: #自機主砲の右上に居るかどうか判別し・・・更に主砲の休憩時間が0以下になったのなら
                            self.boss[i].weapon1_status = WEAPON_FIRE #主砲発射中フラグを建てる
                    
                    if self.boss[i].weapon1_status == WEAPON_FIRE and pyxel.frame_count % self.boss[i].weapon1_interval == 0: #主砲発射中フラグが建っており尚且つweapon1_interval(4フレームごとに)・・
                        posx = self.boss[i].posx + 48
                        posy = self.boss[i].posy + 4
                        func.enemy_aim_bullet_nway(self,posx,posy,20,3, 0,0,0,0) #自機狙い3way発射！
                        
                        self.boss[i].weapon1_rapid_num += 1 #主砲が発射した弾数を1増やす
                        if self.boss[i].weapon1_rapid_num >= 3 + self.enemy_bullet_append: #(3+ランクに応じた追加数)ぶん発射したのならば・・
                            self.boss[i].weapon1_rapid_num = 0    #主砲が発射した弾数をリセット
                            self.boss[i].weapon1_cool_down_time = 600  #主砲の待ち時間用カウンタを設定してやる
                            self.boss[i].weapon1_status  = WEAPON_READY    #主砲発射中フラグを降ろす
                    
                    if self.boss[i].posx <= -30: #x座標がマイナスの時(左画面外)時,は右方向にグリーンレーザーを出す
                        if pyxel.frame_count % self.boss[i].weapon2_interval == 0:
                            ex = self.boss[i].posx + 8*13 +4
                            ey = self.boss[i].posy + 8*4 -3
                            length = 2
                            speed = -2
                            func.enemy_green_laser(self,ex,ey,length,speed)

