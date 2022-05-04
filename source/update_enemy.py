###########################################################
#  update_enemyクラス                                     #
###########################################################
# Appクラスのupdate関数から呼び出される関数群                #
# 主に敵の更新を行うメソッド                                #
# 敵の移動更新、敵のクリッピング                             #
# 敵弾の移動更新,敵弾のクリッピング                          #
# 当たり判定は別のクラス(update_collision)で行う             #
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_obj import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update_ship import * #自機関連の更新関数モジュールの読み込み、「自機のダメージ追加」で使用します
class update_enemy:
    def __init__(self):
        None

    #####################################敵関連の処理関数######################################
    #イベントリストによる敵の発生システム
    def append_event_system(self):
        if self.stage_count == self.event_list[self.event_index][0]:#ステージカウントとリストのカウント値が同じならリスト内容を実行する
            if   self.event_list[self.event_index][1] == EVENT_ENEMY:             #イベント「敵出現」の場合
                if   self.event_list[self.event_index][2] == CIR_COIN:      #サーコイン発生！
                    for number in range(self.event_list[self.event_index][5]):
                        #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                        new_enemy = Enemy()
                        new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0, -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1*self.enemy_speed_mag,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT02,PT02,  PT01,PT01,PT03)
                        self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    func.record_enemy_formation(self,self.event_list[self.event_index][5]) 
                elif self.event_list[self.event_index][2] == TWIN_ARROW:    #追尾戦闘機ツインアロー出現
                    new_enemy = Enemy()
                    new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5 - (self.enemy_speed_mag // 2),0,  0,    HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)                
                elif self.event_list[self.event_index][2] == SAISEE_RO:     #回転戦闘機サイシーロ出現(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1*self.enemy_speed_mag,0,  0,  HP01 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,     0,0,0,0,    E_NO_POW,ID00 ,0,0,0,              0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)    
                elif self.event_list[self.event_index][2] == GREEN_LANCER:   #グリーンランサー 3way弾を出してくる緑の戦闘機(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(GREEN_LANCER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.1*self.enemy_speed_mag,0,  0,  HP05 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.01,0,     0,0,0,0,    E_MISSILE_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == RAY_BLASTER:    #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
                    new_enemy = Enemy()
                    new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    -2,(func.s_rndint(self,0,1)-0.5),       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,  0,  HP02 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,80 + func.s_rndint(self,0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == VOLDAR:        #ボルダー 硬めの弾バラマキ重爆撃機
                    new_enemy = Enemy()
                    new_enemy.update(VOLDAR,ID00,     ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07*self.enemy_speed_mag,1,  0,  HP59 * self.enemy_hp_mag,   0,0,  E_SIZE_HI_MIDDLE53,  0,0,0,     0,0,0,0,     E_SHOT_POW,ID00    ,1,0.007,0.6,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT10)
                    self.enemy.append(new_enemy)
                
            elif self.event_list[self.event_index][1] == EVENT_FAST_FORWARD_NUM:  #イベント「早回し編隊パラメーター設定」の場合
                self.fast_forward_destruction_num   = self.event_list[self.event_index][2] #早回しの条件を満たすのに必要な「敵編隊殲滅必要数」を変数に代入する
                self.fast_forward_destruction_count = self.event_list[self.event_index][3] #敵編隊を早回しで破壊した時にどれだけ出現時間が速くなるのか？そのカウントを変数に代入する         
            elif self.event_list[self.event_index][1] == EVENT_ADD_APPEAR_ENEMY:  #イベント「敵出現（早回しによる敵追加出現）」の場合
                if self.add_appear_flag == FLAG_ON: #「早回し敵発生フラグ」が立っているのならば
                    #サーコイン発生！
                    if self.event_list[self.event_index][2] == CIR_COIN:
                        for number in range(self.event_list[self.event_index][5]):
                            #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                            new_enemy = Enemy()
                            new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                            self.enemy.append(new_enemy) 
                            
                        #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                        func.record_enemy_formation(self,self.event_list[self.event_index][5]) 
                
                self.fast_forward_destruction_num = 0       #「敵編隊殲滅必要数」を初期化
                self.fast_forward_destruction_count = 0     #「早回しで破壊した時にどれだけ出現時間が速くなるカウント」を初期化
                self.fast_forward_num += 1          #累計早回し発生数をインクリメント
                self.add_appear_flag = FLAG_OFF     #早回し関連のパラメーター数値、フラグは全てリセットします
            elif self.event_list[self.event_index][1] == EVENT_SCROLL:            #イベント「スクロール」の場合
                #スクロールスタート
                if   self.event_list[self.event_index][2] == SCROLL_START:
                    self.side_scroll_speed         = 1 #スクロールスピードを通常の1にする
                    self.side_scroll_speed_set_value = 1 #設定目標値も1にする
                    self.side_scroll_speed_variation = 0 #変化量は0
                #スクロールストップ！
                elif self.event_list[self.event_index][2] == SCROLL_STOP:
                    self.side_scroll_speed         = 0 #スクロールスピードを0にする
                    self.side_scroll_speed_set_value = 0 #設定目標値も0にする
                    self.side_scroll_speed_variation = 0 #変化量も0
                #スクロールスピードチェンジ
                elif self.event_list[self.event_index][2] == SCROLL_SPEED_CHANGE:
                    self.side_scroll_speed_set_value = self.event_list[self.event_index][3] #横スクロールスピードの設定値を代入
                    self.side_scroll_speed_variation = self.event_list[self.event_index][4] #横スクロールスピードの変化量を代入
                #縦スクロールスピードチェンジ
                elif self.event_list[self.event_index][2] == SCROLL_SPEED_CHANGE_VERTICAL:
                    self.vertical_scroll_speed_set_value = self.event_list[self.event_index][3] #縦スクロールスピードの設定値を代入
                    self.vertical_scroll_speed_variation = self.event_list[self.event_index][4] #縦スクロールスピードの変化量を代入
                #スクロール関連のパラメーターの設定
                elif self.event_list[self.event_index][2] == SCROLL_NUM_SET:
                    self.side_scroll_speed_set_value    = self.event_list[self.event_index][3] #横スクロールスピードの設定値を代入
                    self.side_scroll_speed_variation    = self.event_list[self.event_index][4] #横スクロールスピードの変化量を代入
                    self.vertical_scroll_speed_set_value = self.event_list[self.event_index][5] #縦スクロールスピードの設定値を代入
                    self.vertical_scroll_speed_variation = self.event_list[self.event_index][6] #縦スクロールスピードの変化量を代入
                
            elif self.event_list[self.event_index][1] == EVENT_DISPLAY_STAR:                 #イベントが「EVENT_DISPLAY_STAR」の場合
                self.star_scroll_flag = self.event_list[self.event_index][2] #星スクロールのon/offのフラグを代入する
            elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_CLS_COLOR:          #イベントが「EVENT_CHANGE_BG_CLS_COLOR」の場合
                self.bg_cls_color = self.event_list[self.event_index][2]    #BGをCLS(クリアスクリーン)するときの色を代入する
            elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_TRANSPARENT_COLOR:  #イベントが「EVENT_CHANGE_BG_TRANSPARENT_COLOR」の場合
                self.bg_transparent_color = self.event_list[self.event_index][2]    #BGを敷き詰める時の透明色を指定する
            elif self.event_list[self.event_index][1] == EVENT_CLOUD:                        #イベントが「背景雲の表示設定」の場合
                #雲のパラメータを設定します
                if   self.event_list[self.event_index][2] == CLOUD_NUM_SET:
                    self.cloud_append_interval  = self.event_list[self.event_index][3]    #雲を追加する間隔を設定
                    self.cloud_quantity        = self.event_list[self.event_index][4]    #雲の量を設定
                    self.cloud_how_flow        = self.event_list[self.event_index][5]    #雲の流れ方を設定
                    self.cloud_flow_speed      = self.event_list[self.event_index][6]    #雲の流れるスピードを設定
                #雲の表示を開始する
                elif self.event_list[self.event_index][2] == CLOUD_START:
                    self.display_cloud_flag = DISP_ON  #雲の表示フラグをonにします
                #雲の表示を停止する
                elif self.event_list[self.event_index][2] == CLOUD_STOP:
                    self.display_cloud_flag = DISP_OFF #雲の表示フラグをoffにします
                
            elif self.event_list[self.event_index][1] == EVENT_RASTER_SCROLL:     #イベントが「ラスタースクロールの制御」の場合
                search_id = self.event_list[self.event_index][3] #ラスタスクロールのidを変数に代入
                #IDごとにラスタスクロールの表示をon/offする
                if self.event_list[self.event_index][2] == RASTER_SCROLL_ON:     #ラスタスクロールon
                    func.disp_control_raster_scroll(self,search_id,RASTER_SCROLL_ON) #idを元にラスタスクロールの表示フラグを変更する関数の呼び出し
                elif self.event_list[self.event_index][2] == RASTER_SCROLL_OFF:   #ラスタスクロールoff
                    func.disp_control_raster_scroll(self,search_id,RASTER_SCROLL_OFF)#idを元にラスタスクロールの表示フラグを変更する関数の呼び出し
                
            elif self.event_list[self.event_index][1] == EVENT_BG_SCREEN_ON_OFF:  #イベントが「BGスクリーンオンオフ」の場合
                if   self.event_list[self.event_index][2] == BG_FRONT: #[2]で指定された数値をもとにして、各disp_flagへ、[3]に入っているDISP_OFF(0)またはDISP_ON(1)の数値を代入する
                    self.disp_flag_bg_front  = self.event_list[self.event_index][3]
                elif self.event_list[self.event_index][2] == BG_MIDDLE:
                    self.disp_flag_bg_middle = self.event_list[self.event_index][3]
                elif self.event_list[self.event_index][2] == BG_BACK:
                    self.disp_flag_bg_back   = self.event_list[self.event_index][3]
                
            elif self.event_list[self.event_index][1] == EVENT_ENTRY_SPARK_ON_OFF:#イベントが「大気圏突入の火花エフェクト表示のオンオフ」の場合
                self.atmospheric_entry_spark_flag = self.event_list[self.event_index][2] #火花エフェクトのon/offのフラグを代入する
            elif self.event_list[self.event_index][1] == EVENT_WARNING:           #イベントが「WARNING表示」の場合
                self.warning_dialog_flag = 1                                    #WARNING警告表示フラグをonにする
                self.warning_dialog_display_time = self.event_list[self.event_index][2] #警告表示時間を代入(単位は1フレーム)
                self.warning_dialog_logo_time    = self.event_list[self.event_index][3] #グラフイックロゴ表示にかける時間を代入(単位は1フレーム)
                self.warning_dialog_text_time    = self.event_list[self.event_index][4] #テキスト表示にかける時間を代入(単位は1フレーム)
                
                #pyxel.playm(0)#警告音発生！緊急地震速報Ver・・・・怖い・・・
                pyxel.playm(2)#警告音発生！
            elif self.event_list[self.event_index][1] == EVENT_BOSS:              #イベントの内容が「BOSS」の場合
                self.boss_battle_damaged_flag  = FLAG_OFF #ボス戦でダメージを受けたかどうかのフラグをオフにします(ステージスタートした時にオフ、ボス出現時にオフ、ダメージ受けたらオン)
                self.game_status = SCENE_BOSS_APPEAR      #ゲームのステータスを「BOSS_APPEAR」ボス出現！にします
                func.born_boss(self)                      #各面のボスを生み出す関数を呼び出します
                self.boss_battle_time = 0                 #ボスとの戦闘時間を0で初期化！ボスとの戦闘スタート！
            self.event_index += 1 #イベントインデックス値を1増やして次のイベントの実行に移ります

    #マップスクロールによる敵の発生
    def append_map_scroll(self):
        if self.no_enemy_mode == 1: #敵が出ないモードがonだったら・・・
            return              #何もせずに帰ります・・・・・
        
        #今表示したマップに（「敵出現」情報）のキャラチップが含まれていたら敵を発生させる
        for i in range(self.bg_height // 8):     #BGの縦キャラチップ数だけy軸下方向に調べていく 通常スクロールなら15回 縦2画面スクロールステージなら30回ループする
            func.get_bg_chip(self,WINDOW_W,i*8,0)#画面右端のマップチップのＢＧナンバーをゲットする(iの値・・・8で割ってまた8を掛けるのはスマートじゃないかも・・・)
            if self.bg_chip == BG_HOUDA_UNDER:       #マップチップが地上固定砲台ホウダのとき
                item_number = 0 #アイテムナンバー初期化
                func.get_bg_chip(self,WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                if self.bg_chip == SHOT_POW_BG_NUM:      #ショットマップチップだったらショットアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SHOT_POW    #ショットアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                elif self.bg_chip == MISSILE_POW_BG_NUM: #ミサイルマップチップだったらミサイルアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_MISSILE_POW #ミサイルアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                elif self.bg_chip == SHIELD_POW_BG_NUM:  #シールドマップチップだったらシールドアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SHIELD_POW  #シールドアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                func.get_bg_chip(self,WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                new_enemy = Enemy()
                new_enemy.update(3,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,    0, HP01 * self.enemy_hp_mag,   0,0,E_SIZE_NORMAL,0,0,0,     0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む                    
                
            elif self.bg_chip == BG_HOUDA_UPPER:     #マップチップが天井固定砲台ホウダのとき
                item_number = 0 #アイテムナンバー初期化
                func.get_bg_chip(self,WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                if self.bg_chip == SHOT_POW_BG_NUM:      #ショットマップチップだったらショットアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SHOT_POW    #ショットアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                elif self.bg_chip == MISSILE_POW_BG_NUM: #ミサイルマップチップだったらミサイルアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_MISSILE_POW #ミサイルアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                elif self.bg_chip == SHIELD_POW_BG_NUM:  #シールドマップチップだったらシールドアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SHIELD_POW  #シールドアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                
                func.get_bg_chip(self,WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                new_enemy = Enemy()
                new_enemy.update(4,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,  0,  HP01 * self.enemy_hp_mag,    0,0,E_SIZE_NORMAL,0,0,0,    0,0,0,0,    item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら(「敵出現」情報)のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_HOPPER_CHAN2:    #マップチップがはねるホッパーちゃん２のとき
                new_enemy = Enemy()
                new_enemy.update(5,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,    0.4,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    0.2*self.enemy_speed_mag,0,  -1,    HP01 * self.enemy_hp_mag,   0,0,   E_SIZE_NORMAL,(i * 8),-20,1,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_SAISEE_RO:       #マップチップがサイシーロの時(サインカーブを描く敵）
                new_enemy = Enemy()
                new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    1*self.enemy_speed_mag,0,   0,   HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,   0.5,0.05,0,    0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_KURANBURU_UNDER: #マップチップが地上スクランブルハッチのとき
                new_enemy = Enemy()
                new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32,  (func.s_rndint(self,0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_KURANBURU_UPPER: #マップチップが天井スクランブルハッチのとき
                new_enemy = Enemy()
                new_enemy.update(11,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32_Y_REV,  (func.s_rndint(self,0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_TEMI:            #マップチップが赤いアイテムキャリアーテミーのとき
                item_number = 0 #アイテムナンバー初期化
                func.get_bg_chip(self,WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                if self.bg_chip == CLAW_POW_BG_NUM: #クローマップチップだったらクローアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_CLAW_POW    #クローアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == TAIL_SHOT_BG_NUM: #テイルショットマップチップだったらテイルショットアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_TAIL_SHOT_POW  #テイルショットアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == PENETRATE_ROCKET_BG_NUM: #ペネトレートロケットマップチップだったらペネトレートロケットアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_PENETRATE_ROCKET_POW  #ペネトレートロケットアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == SEARCH_LASER_BG_NUM: #サーチレーザーマップチップだったらサーチレーザーアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SEARCH_LASER_POW #サーチレーザーアイテムアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == HOMING_MISSILE_BG_NUM: #ホーミングミサイルマップチップだったらホーミングミサイルアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_HOMING_MISSILE_POW  #ホーミングミサイルアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == SHOCK_BUMPER_BG_NUM: #ショックバンパーマップチップだったらショックバンパーアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_SHOCK_BUMPER_POW #ショックバンパーアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                    
                elif self.bg_chip == TRIANGLE_POW_BG_NUM: #トライアングルアイテムマップチップだったらトライアイングルアイテム情報を付加せよの命令のマップチップなので
                    item_number = E_TRIANGLE_POW #トライアングルアイテム
                    func.delete_map_chip(self,self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                
                func.get_bg_chip(self,WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                new_enemy = Enemy()
                new_enemy.update(14,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -0.44,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_8,   0,0,   0,    HP10,   0,0,   E_SIZE_NORMAL,  0,0,0,   0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む 
                
            elif self.bg_chip == BG_RAY_BLASTER:     #マップチップがレイブラスターのとき(直進して画面前方のどこかで停止→レーザービーム射出→急いで後退)
                new_enemy = Enemy()
                new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,i * 8,0,0,      0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -2,(func.s_rndint(self,0,1)-0.5),     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.98,0,    0,    HP01 * self.enemy_hp_mag,  0,0,    E_SIZE_NORMAL,   80 + func.s_rndint(self,0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_MUU_ROBO:        #マップチップがムーロボのとき(地面を左右に動きながらチョット進んできて弾を撃つ移動砲台,何故か宇宙なのに重力の影響を受けて下に落ちたりもします)
                new_enemy = Enemy()
                new_enemy.update(MUU_ROBO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,       0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.8*self.enemy_speed_mag,0,    -1,    HP01 * self.enemy_hp_mag,  70,80,    E_SIZE_NORMAL,   70,80,0,     0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_ROLL_BLITZ:      #マップチップがロールブリッツのとき(画面内のあらかじめ決められた場所へスプライン曲線で移動)
                new_enemy = Enemy()
                new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,      E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む

    #アペンドイベントリクエスト(イベント追加依頼）による敵の発生
    def append_event_request(self):
        event_append_request_count = len(self.event_append_request)
        for i in reversed (range(event_append_request_count)):
            if self.stage_count == self.event_append_request[i].timer:
                if self.event_append_request[i].event_type == EVENT_ENEMY: #イベントの内容が敵出現の場合
                    #サーコインの追加発生！
                    if self.event_append_request[i].enemy_type == CIR_COIN:
                        for e in range(self.event_append_request[i].number):
                            #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                            new_enemy = Enemy()
                            new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (e * 12),self.event_append_request[i].posy,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0,     0,0,0,0,        E_NO_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                            self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    func.record_enemy_formation(self,self.event_append_request[i].number)
                    del self.event_append_request[i] #敵を追加発生リクエストをリストから消去します

    #敵の更新（移動とか弾の発射とか他の敵を生み出すとか、そういう処理）
    def enemy(self):
        enemy_count = len(self.enemy)
        for i in range (enemy_count):
            if   self.enemy[i].enemy_type ==  1:#敵タイプ1の更新   サーコイン 直進して斜め後退→勢いよく後退していく10機編隊
                if self.enemy[i].enemy_flag1 == 0:
                #敵１を前進させる
                    self.enemy[i].posx = self.enemy[i].posx - self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                    if self.enemy[i].posx < 20:#敵の座標が20以下なら後退処理を始める
                        self.enemy[i].enemy_flag1 = 1 #flag1 後退フラグON
                        if self.enemy[i].posy > (WINDOW_H / 2):#画面の上半分に居るのか下半分に居るのか判別
                            self.enemy[i].vy = -1#画面上半分に居たのならVYに-1を入れて下方向に移動（初期設定ではVYには１が入っているので上方向に移動することに成る）
                    
                else:
                    if self.enemy[i].enemy_count1 > 0:#enemy_count1には斜め方向に移動する回数が入っている
                        self.enemy[i].enemy_count1 -= 1#斜め移動する回数を１減らす
                        self.enemy[i].posx += 0.5#0.5の増分で斜め右方向に逃げていく
                        self.enemy[i].posy += self.enemy[i].vy
                    else:#斜め後退処理が終わったら高速で右方向に逃げていく
                        self.enemy[i].posx = self.enemy[i].posx + 2#2ドットの増分で右方向に逃げていく
                        if self.enemy[i].posx > WINDOW_W -8 and (func.s_rndint(self,0,self.run_away_bullet_probability) == 0):
                            self.ex = self.enemy[i].posx
                            self.ey = self.enemy[i].posy
                            func.enemy_aim_bullet(self,self.ex,self.ey,0,0,0,0,1)#後退時に自機狙いの弾を射出して去っていく
                
            elif self.enemy[i].enemy_type ==  2:#敵タイプ2の更新   サイシーロ サインカーブを描く3機編隊
                #敵２をサインカーブを描きながら移動させる 
                self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅
                
            elif self.enemy[i].enemy_type ==  3:#敵タイプ3の更新  固定砲台ホウダ（地面に張り付く１連射タイプ）
                #敵３を背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (func.s_rndint(self,0,(self.run_away_bullet_probability) * 50) == 0):
                    self.ex = self.enemy[i].posx
                    self.ey = self.enemy[i].posy
                    func.enemy_aim_bullet(self,self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                
            elif self.enemy[i].enemy_type ==  4:#敵タイプ4の更新   固定砲台ホウダ（天井に張り付く１連射タイプ）
                #敵４を背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (func.s_rndint(self,0,(self.run_away_bullet_probability) * 50) == 0):
                    self.ex = self.enemy[i].posx
                    self.ey = self.enemy[i].posy
                    func.enemy_aim_bullet(self,self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                
            elif self.enemy[i].enemy_type ==  5:#敵タイプ5の更新   ホッパーチャンmk2
                #敵５を背景スクロールに合わせて左へ移動させる
                #
                #enemy_count1をy_prevとして使用してます
                #enemy_count2をFとして使用してます
                #enemy_count3を地面に接触した時弾を出すため滞在するタイマーカウンターとして使用します
                #マリオのジャンプアルゴリズム参考
                #
                #初期変数定義
                #y_prev = pos.y
                #F = -1 ジャンプの瞬間だけ-10 空中の状態は1
                #
                #メイン処理 
                #y_temp = pos.y
                #pos.y += (pos.y -posy_prev) + F
                #pos.y_prev = y_temp
                if self.enemy[i].enemy_count2 < -20:
                    self.enemy[i].enemy_count2 = -20
                
                self.enemy[i].enemy_count3 -= 1
                
                if self.enemy[i].enemy_count3 <= 0:
                    self.enemy[i].vx = 1.2
                    self.enemy[i].enemy_count3 = 0
                else:
                    self.enemy[i].vx = 0.5
                
                #x座標をVX（増加数）とdirection(-1なら左方向 1なら右方向)によって更新する
                self.enemy[i].posx += self.enemy[i].vx * self.enemy[i].direction
                
                if self.enemy[i].enemy_count3 <= 0:
                    self.y_tmp = self.enemy[i].posy#y_temp = y
                    self.enemy[i].posy += (self.enemy[i].posy - self.enemy[i].enemy_count1) + (self.enemy[i].enemy_count2 * self.enemy[i].move_speed) #y += ((y -y_prev) + F) * move_speed (ココが重要！)
                    self.enemy[i].enemy_count1 = self.y_tmp#y_prev = y_tmp
                    self.enemy[i].enemy_count2 = 1#F = 1
                    
                    self.x = self.enemy[i].posx + 4
                    self.y = self.enemy[i].posy + 8
                    func.check_bg_collision(self,self.x,self.y,0,0)#ホッパー君の足元が障害物かどうかチェック
                
                if self.collision_flag == 0:#足元に障害物が無かった時の処理→そのままで行く
                    
                    self.enemy_bound_collision_flag = 0#デバッグ用のバウンドフラグをＯＦＦにする
                    
                else:                    
                    self.x = self.enemy[i].posx + 4
                    self.y = self.enemy[i].posy - 8
                    func.check_bg_collision(self,self.x,self.y,0,0)#ホッパー君の頭の上が障害物なのか（足元と頭上、障害物に挟まっているのか？）チェック
                    if self.collision_flag == 0:
                        #ホッパー君の足元は障害物、ホッパー君は障害物に今っていなかったので再ジャンプできるゾ！
                        self.enemy[i].enemy_count2 = -20#  F=-10   Fに-10を入れて再度ジャンプさせる
                        self.enemy_bound_collision_flag = 1#デバッグ用のバウンドフラグをＯＮにする
                        
                        self.enemy[i].enemy_count3 = 20#地面に留まる踏ん張りカウントを１０に設定
                        self.enemy[i].posy -= 1#なんだかわかんないけど地面にめり込んでいくので強制的にＹ軸を上方向に移動させてやる（－１補正を入れる）
                        if func.s_rndint(self,0,self.run_away_bullet_probability) == 0:
                            self.ex = self.enemy[i].posx
                            self.ey = self.enemy[i].posy
                            func.enemy_aim_bullet_rank(self,self.ex,self.ey,0,0,0,0,1)#自機狙いの弾発射！
                        else:
                            #ホッパー君の足元は障害物＆ホッパー君も壁に挟まっていた（ガーン！）だからそのまま壁に衝突したことは無しとするッ！
                            self.enemy_bound_collision_flag = 0#デバッグ用のバウンドフラグをＯＦＦにする
                            self.enemy[i].enemy_count2 = -1#ジャンプ力は初期値に戻してやる
                            self.enemy[i].enemy_count1 = self.enemy[i].posy #y_prev = posy
                            self.enemy[i].enemy_count3 = 1
                
                pyxel.blt(135,WINDOW_H - 8, 0, 0,80, 8,8, 0)
                if self.enemy[i].posx < 0:
                    self.enemy[i].direction = 1#もしx座標が0まで画面の左端に進んだら跳ね返りdirectionフラグを(+1右方向増加）にして右に反転後退していく
                
            elif self.enemy[i].enemy_type ==  6:#敵タイプ6の更新   謎の回転飛翔体Ｍ５４
                #敵6を回転させる 
                
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー(timer) enemy_count_2は速度(speed)
                self.enemy[i].posx += self.enemy[i].enemy_count1 * math.cos(self.enemy[i].enemy_count3)
                self.enemy[i].posy += self.enemy[i].enemy_count1 * -math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅(intensity)
                self.enemy[i].posx -= 0.05
                
            elif self.enemy[i].enemy_type ==  7:#敵タイプ7の更新   真！(SIN)ツインアロー追尾戦闘機(サインカーブを描きつつ追尾してくる)
                #敵７を自機に追尾させる
                #目標までの距離を求める dに距離が入る
                self.d = math.sqrt((self.my_x - self.enemy[i].posx) * (self.my_x - self.enemy[i].posx) + (self.my_y - self.enemy[i].posy) * (self.my_y - self.enemy[i].posy))
                #弾の速度 vx,vyを求める
                #速さが一定値move_speedになるようにする
                #目標までの距離dが0の時は速度を左方向にする
                if self.d == 0:
                    self.vx = 0
                    self.vy = self.enemy[i].move_speed
                else:
                    #敵と自機との距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                    self.vx = ((self.my_x - self.enemy[i].posx) / (self.d * self.enemy[i].move_speed))
                    self.vy = ((self.my_y - self.enemy[i].posy) / (self.d * self.enemy[i].move_speed))
                
                #敵の座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる
                self.enemy[i].posx += self.vx
                self.enemy[i].posy += self.vy
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー(timer) enemy_count_2は速度(speed)
                self.enemy[i].posx += self.enemy[i].enemy_count1 * math.cos(self.enemy[i].enemy_count3)
                self.enemy[i].posy += self.enemy[i].enemy_count1 * -math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅(intensity)
                self.enemy[i].posx -= 0.05
                
            elif self.enemy[i].enemy_type ==  8:#敵タイプ8の更新   ツインアロー追尾戦闘機
                #敵８を自機に追尾させる
                vx0 = self.enemy[i].vx
                vy0 = self.enemy[i].vy #敵の速度(vx,vy)を(vx0,vy0)に退避する
                #目標までの距離を求める dに距離が入る
                self.d = math.sqrt((self.my_x - self.enemy[i].posx) * (self.my_x - self.enemy[i].posx) + (self.my_y - self.enemy[i].posy) * (self.my_y - self.enemy[i].posy))
                
                #敵の速度 vx,vyを求める
                #速さが一定値move_speedになるようにする
                #目標までの距離dが0の時は速度を左方向にする
                #enemy_count3をtheta(Θ)旋回できる角度の上限として使用します
                #自機方向の速度ベクトル(vx1,vy1)を求める
                if self.d == 0:#目標（自機）までの距離は0だった？（重なっていた？）
                    vx1= 0
                    vy1 = self.enemy[i].move_speed #目標までの距離dが0の時は速度を左方向にする
                else:
                    #敵と自機との距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                    
                    vx1 = ((self.my_x - self.enemy[i].posx) / (self.d * self.enemy[i].move_speed))
                    vy1 = ((self.my_y - self.enemy[i].posy) / (self.d * self.enemy[i].move_speed))
                
                #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                #math.piはπ（円周率3.141592......)
                #ううううぅ・・・難しい・・・・数学赤点の私には難しい・・・・
                self.rad = 3.14 / 180 * self.enemy[i].enemy_count3#rad = 角度degree（theta）をラジアンradianに変換
                
                vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                #自機方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                    #自機方向が旋回可能範囲内の場合の処理
                    #自機方向に曲がるようにする
                    self.enemy[i].vx = vx1
                    self.enemy[i].vy = vy1
                else:
                    #自機が旋回可能範囲を超えている場合（ハンドルをいっぱいまで切っても自機に追いつけないよ～）ハンドル一杯まで切る！
                    #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                    vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                    vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                    #敵から自機への相対ベクトル(px,py)を求める
                    px = self.my_x - self.enemy[i].posx
                    py = self.my_y - self.enemy[i].posy
                    #右回りか左回りを決める
                    #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                    #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                    if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                        #右回り（面舵方向）の場合
                        self.enemy[i].vx = vx2
                        self.enemy[i].vy = vy2
                    else:
                        #左回り（取り舵方向）の場合
                        self.enemy[i].vx = vx3
                        self.enemy[i].vy = vy3
                #敵の座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる(座標更新！)
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
                
            elif self.enemy[i].enemy_type ==  9:#敵タイプ9の更新   ロルボード 自機のＹ軸を合わせた後突進してくる敵
                if self.enemy[i].enemy_flag2 == 0:#自機撃墜フラグ（自機と完全に重なったフラグ）はまだ建ってない？？
                    if self.enemy[i].enemy_flag1 == 0:#自機の位置をサーチしてどちらの方向に進むかのフラグはまだ建ってない？
                        if self.my_y > self.enemy[i].posy:
                            self.enemy[i].vy = 0.5
                        else:
                            self.enemy[i].vy = -0.5
                        #自機索敵フラグenemy_flag1をonにする
                        self.enemy[i].enemy_flag1 = 1
                
                if self.enemy[i].posy == self.my_y:#自機と敵機のY座標は同じになったかな？？？？
                    if self.my_x > self.enemy[i].posx:#自機のｘ座標を見て右方向か左方向か進む方向に増分(vx)を加減算してやる
                        self.enemy[i].vx = 1
                        self.enemy[i].vy = 0
                    else:
                        self.enemy[i].vx = -1
                        self.enemy[i].vy = 0
                
                if self.my_x == self.enemy[i].posx and self.my_y == self.enemy[i].posy:
                    self.enemy[i].enemy_flag2 = 1#自機と敵機の座標が完全に重なっていたら自機撃墜フラグをＯＮにする
                
                if self.enemy[i].posx < 5:#x座標が左端なら弾を射出
                            self.ex = self.enemy[i].posx
                            self.ey = self.enemy[i].posy
                            func.enemy_aim_bullet_rank(self,self.ex,self.ey,0,0,0,0,1)#後退時に自機狙いの弾を射出して去っていく
                #vx,vyで敵の座標posx,posy更新！移動！！
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
                
            elif self.enemy[i].enemy_type == 10:#敵タイプ10の更新  クランブルアンダー スクランブルハッチ（地面タイプ）
                #enemy_flag1を状態遷移フラグとして使用します
                #    0=待機中（射出開始カウンタを減らしていく）
                #    1～20ハッチ開放アニメーション中
                #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                #    23以上ハッチ閉鎖アニメーション中
                #    23以上は敵を出し切ったので何もしない
                #enemy_flag2を敵射出間隔制御用の変数として使用します
                #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                  （最初に何機だすか数字を入れておいてね）
                #enemy_count3を敵を射出する間隔用カウンタとして使用します（射出間隔用カウンタ）（定数です変化はしません）
                if self.enemy[i].enemy_flag1 == 0:#ハッチから敵を出し切ってないかどうかチェック
                    self.enemy[i].enemy_count1 -= 1#射出開始カウンタを１減らす
                    if self.enemy[i].enemy_count1 == 0:
                        self.enemy[i].enemy_flag1 = 1#射出開始カウンタが0になったら遷移状態を「ハッチ開放開始」にする
                
                if 1 <= self.enemy[i].enemy_flag1 <= 20:#flag1が1～20の間はハッチ開放アニメーションをするのでflag1を1増やしていく(flag1はアニメーション様にオフセットとして使う)
                    self.enemy[i].enemy_flag1 += 1
                
                if self.enemy[i].enemy_flag1 == 21:#敵機発進待機中？
                    self.enemy[i].enemy_flag2 -= 1#射出間隔カウント(変数)を1減らす
                    if self.enemy[i].enemy_flag2 <= 0:#射出間隔カウンターがゼロ以下になったら敵機射出
                        self.enemy[i].enemy_flag1 = 22#遷移状態を「22敵機発射」にする
                
                if self.enemy[i].enemy_flag1 == 22:#敵機発射？
                    if len(self.enemy) < 400:
                        new_enemy = Enemy()#敵９を1機生み出す
                        new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy - 2,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   1.2,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,0,      0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)#リストにアペンド追加！
                    
                    self.enemy[i].enemy_count2  -= 1#敵射出数を1減らす
                    if self.enemy[i].enemy_count2 == 0:#射出する敵の数はもうゼロになったかな？
                        self.enemy[i].enemy_flag1 = 23#敵を全部出し切ったのなら遷移状態を「23ハッチ閉鎖中」にする
                    else:
                        self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count3#射出間隔カウンターを設定した初期に戻す
                        self.enemy[i].enemy_flag1 = 21#遷移状態を「21敵機発進待機中」にする
                
                if 23 <= self.enemy[i].enemy_flag1 <= 46:#flag1が23以上の間はハッチ閉鎖アニメーションするのでflag1を1増やしていく(flag1はアニメーション様にオフセット値として使う４６まで引っ張る)
                    self.enemy[i].enemy_flag1 += 1
                    self.enemy[i].status = ENEMY_STATUS_DEFENSE #敵９を出し切った後は防御モードにする
                #背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）         
                
            elif self.enemy[i].enemy_type == 11:#敵タイプ11の更新  クランブルアッパー スクランブルハッチ（天井タイプ）
                #enemy_flag1を状態遷移フラグとして使用します
                #    0=待機中（射出開始カウンタを減らしていく）
                #    1～20ハッチ開放アニメーション中
                #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                #    23以上ハッチ閉鎖アニメーション中
                #    23以上は敵を出し切ったので何もしない
                #enemy_flag2を敵射出間隔制御用の変数として使用します
                #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                  （最初に何機だすか数字を入れておいてね）
                #enemy_count3を敵を射出する間隔用カウンタとして使用します（射出間隔用カウンタ）（定数です変化はしません）
                if self.enemy[i].enemy_flag1 == 0:#ハッチから敵を出し切ってないかどうかチェック
                    self.enemy[i].enemy_count1 -= 1#射出開始カウンタを１減らす
                    if self.enemy[i].enemy_count1 == 0:
                        self.enemy[i].enemy_flag1 = 1#射出開始カウンタが0になったら遷移状態を「ハッチ開放開始」にする
                
                if 1 <= self.enemy[i].enemy_flag1 <= 20:#flag1が1～20の間はハッチ開放アニメーションをするのでflag1を1増やしていく(flag1はアニメーション様にオフセットとして使う)
                    self.enemy[i].enemy_flag1 += 1
                
                if self.enemy[i].enemy_flag1 == 21:#敵機発進待機中？
                    self.enemy[i].enemy_flag2 -= 1#射出間隔カウント(変数)を1減らす
                    if self.enemy[i].enemy_flag2 <= 0:#射出間隔カウンターがゼロ以下になったら敵機射出
                        self.enemy[i].enemy_flag1 = 22#遷移状態を「22敵機発射」にする
                
                if self.enemy[i].enemy_flag1 == 22:#敵機発射？
                    if len(self.enemy) < 400:
                        new_enemy = Enemy()#敵９を1機生み出す
                        new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy + 10,0,0,       0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   1.2,0,    0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,0,     0,0,0,0,        E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)#リストにアペンド追加！
                    
                    self.enemy[i].enemy_count2  -= 1#敵射出数を1減らす
                    if self.enemy[i].enemy_count2 == 0:#射出する敵の数はもうゼロになったかな？
                        self.enemy[i].enemy_flag1 = 23#敵を全部出し切ったのなら遷移状態を「23ハッチ閉鎖中」にする
                    else:
                        self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count3#射出間隔カウンターを設定した初期に戻す
                        self.enemy[i].enemy_flag1 = 21#遷移状態を「21敵機発進待機中」にする
                
                if 23 <= self.enemy[i].enemy_flag1 <= 46:#flag1が23以上の間はハッチ閉鎖アニメーションするのでflag1を1増やしていく(flag1はアニメーション様にオフセット値として使う４６まで引っ張る)
                    self.enemy[i].enemy_flag1 += 1
                    self.enemy[i].status = ENEMY_STATUS_DEFENSE #敵９を出し切った後は防御モードにする
                #背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5 #基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）
                
            elif self.enemy[i].enemy_type == 12:#敵タイプ12の更新  レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退
                #enemy_flag1を状態遷移フラグとして使用します
                #  0=前進中
                #  1=レーザービーム発射スタート
                #  2～28=レーザービーム発射中(アニメーションパターン用の補正数値として使用します)
                #  28～56=後退アニメーションしつつ後退中
                #  57以上  ただの後退
                #enemy_count1を敵が前進してくる限界のＸ座標として設定してます
                
                if self.enemy[i].enemy_flag1 == 0:
                    #遷移状態が「前進中」なら敵１２を前進させる
                    self.enemy[i].vx = self.enemy[i].vx * self.enemy[i].move_speed#VXをmove_speed分掛けて少しづつ小さくしていく（減速させる）
                    self.enemy[i].posx += self.enemy[i].vx#x座標を更新
                    self.enemy[i].vy = self.enemy[i].vy * self.enemy[i].move_speed#VYをmove_speed分掛けて少しづつ小さくしていく（減速させる）
                    self.enemy[i].posy += self.enemy[i].vy#Y座標を更新
                    if self.enemy[i].posx < self.enemy[i].enemy_count1:#敵の座標が前進限界以下なら後退処理を始める
                        self.enemy[i].enemy_flag1 = 1#敵のＸ座標が前進限界以下なら 遷移状態を「レーザービーム発射中にする」
                elif self.enemy[i].enemy_flag1 == 1:
                    #遷移状態が「レーザービーム発射スタート」ならレーザー発射関数を呼び出し
                    func.enemy_laser(self,self.enemy[i].posx,self.enemy[i].posy,30,2 * self.enemy_bullet_speed_mag)#レーザーの長さ30 スピード2*ランクによる倍率
                    self.enemy[i].enemy_flag1 = 2#遷移状態を「レーザービーム発射中」にする
                    
                elif 2 <= self.enemy[i].enemy_flag1 <= 28:
                    self.enemy[i].enemy_flag1 += 1#遷移状態が「レーザービーム発射中」ならフラグを1増やしていく（その場にとどまるので座標の更新は無し）
                    
                elif 28 <= self.enemy[i].enemy_flag1 <= 46:#遷移状態が「後退中」なら高速で右方向に逃げていく
                    self.enemy[i].enemy_flag1 += 1#アニメーションしたいのでflag1だけは増やしていく
                    self.enemy[i].posx = self.enemy[i].posx + 1#2ドットの増分で右方向に逃げていく
                else:
                    self.enemy[i].posx = self.enemy[i].posx + 2#2ドットの増分で右方向に逃げていく                 
                
            elif self.enemy[i].enemy_type == 13:#敵タイプ13の更新  グリーンランサー ゆらゆら浮遊する3way弾を発射する硬い敵(倒すとショットパワーアップアイテム)
                #サインカーブを描きながら移動させる 
                self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅
                
                self.enemy[i].enemy_flag1 += 1 #flag1を利用してカウント90ごとに弾を発射させる
                if self.enemy[i].enemy_flag1 == 90:
                    func.enemy_forward_3way_bullet(self,self.enemy[i].posx,self.enemy[i].posy) #前方3way弾発射
                    self.enemy[i].enemy_flag1 = 0
                
            elif self.enemy[i].enemy_type == 14:#敵タイプ14の更新  テミー ゆっくり直進してくる赤いアイテムキャリアー
                #vx,vyで敵の座標posx,posy更新！移動！！
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
                
            elif self.enemy[i].enemy_type == 15:#敵タイプ15の更新  ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
                #敵１５を背景スクロールに合わせて移動させる（地上キャラなので不自然が無いように・・・）
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (func.s_rndint(self,0,(self.run_away_bullet_probability) * 50) == 0):
                            self.ex = self.enemy[i].posx
                            self.ey = self.enemy[i].posy
                            func.enemy_aim_bullet(self,self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                
                #directionは -1=左方向に移動 1=右方向に移動
                #enemy_count1は左に動く原本カウント enemy_flag1はその変数として使用します
                #enemy_count2は右に動く原本カウント enemy_flag2はその変数として使用します
                if self.enemy[i].vy == 0: #地面を移動中の場合は(vy=0の時は横方向だけの移動)
                    if self.enemy[i].direction == -1: #左に移動
                        func.check_bg_collision(self,self.enemy[i].posx - 8,self.enemy[i].posy,0,0) #左側が障害物かどうかチェックする
                        if self.enemy[i].enemy_flag1 <= 0 or self.collision_flag == 1:#左移動のカウンタが0以下、又は左に障害物があったら
                            self.enemy[i].direction = 1                #方向転換して右移動にする
                            self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count2 #右移動するカウントを原本からコピーしてやる
                            self.enemy[i].vx = 0             #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                        else:
                            self.enemy[i].enemy_flag1 -= 1 #左移動のカウンタを1減らします
                            self.enemy[i].vx = -1             #x軸の移動ベクトルは左方向です
                    elif self.enemy[i].direction == 1: #右に移動
                        func.check_bg_collision(self,self.enemy[i].posx + 8,self.enemy[i].posy,0,0) #右側が障害物かどうかチェックする
                        if self.enemy[i].enemy_flag2 <= 0 or self.collision_flag == 1:#右移動のカウンタが0以下、又は右に障害物があったら
                            self.enemy[i].direction = -1               #方向転換して左移動にする
                            self.enemy[i].enemy_flag1 = self.enemy[i].enemy_count1 #左移動するカウントを原本からコピーしてやる
                            self.enemy[i].vx = 0             #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                        else:
                            self.enemy[i].enemy_flag2 -= 1 #右移動のカウンタを1減らします
                            self.enemy[i].vx = 1             #x軸の移動ベクトルは右方向です
                
                func.check_bg_collision(self,self.enemy[i].posx + 4,self.enemy[i].posy + 8,0,0) #足元が障害物かどうかチェックする
                if self.collision_flag == 0:#もし足元に障害物が無かった時は
                    self.enemy[i].vy = 0.5  #y軸の移動ベクトルを1にして下方向(落下方向)にする
                    self.enemy[i].vx = self.enemy[i].vx * 0.8 #x軸方向の移動ベクトルもだんだんと小さくしていく
                else:
                    self.enemy[i].vy = 0  #障害物があった時はy軸のベクトルを0にする
                
                self.enemy[i].posx += self.enemy[i].vx * self.enemy[i].move_speed #移動ベクトル分加減算して移動！
                self.enemy[i].posy += self.enemy[i].vy * self.enemy[i].move_speed
                
            elif self.enemy[i].enemy_type == 16:#敵タイプ16の更新  クランパリオン 2機一体で挟みこみ攻撃をしてくる
                #enemy_flag1は自機とx座標が一致して挟みこむ行動を開始するかのフラグ 0=off 1=on
                if self.enemy[i].enemy_flag1 == 0 and -3 <= self.enemy[i].posx - self.my_x <= 3: #もしflag1がたっていない&自機と敵のx座標の差が+-3以内だったら
                    self.enemy[i].enemy_flag1 = 1  #挟みこみ開始フラグをonにする
                    self.enemy[i].vx = 0 #x軸はもう動かないようx方向の速度ベクトルvxを0にする
                    self.enemy[i].move_speed = 1.02 #移動スピードを加速気味にする
                    if self.enemy[i].posy < self.my_y: #自機より敵が上に居たのならば
                        self.enemy[i].vy = 0.92 #速度ベクトルのy軸を下方向にする
                    else:
                        self.enemy[i].vy = -0.92 #そうでないのなら逆に速度ベクトルのy軸を上方向にする
                self.enemy[i].vx = self.enemy[i].vx * self.enemy[i].move_speed #速度ベクトルをだんだん大きくさせていく（挟み込み時）
                self.enemy[i].vy = self.enemy[i].vy * self.enemy[i].move_speed
                self.enemy[i].posx += self.enemy[i].vx #移動ベクトル分加減算して移動！
                self.enemy[i].posy += self.enemy[i].vy
                
            elif self.enemy[i].enemy_type == 17:#敵タイプ17の更新  ロールブリッツ ベジェ曲線で定点まで移動して離脱する敵
                if self.enemy[i].status == ENEMY_STATUS_MOVE_COORDINATE_INIT: #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                    enemy_type = self.enemy[i].enemy_type
                    func.enemy_get_bezier_curve_coordinate(self,enemy_type,i) #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                    self.enemy[i].status = ENEMY_STATUS_MOVE_BEZIER_CURVE #状態遷移を「ベジェ曲線で移動」に設定
                    
                elif self.enemy[i].status == ENEMY_STATUS_MOVE_BEZIER_CURVE: #「ベジェ曲線で移動」
                    t =  self.enemy[i].obj_time / self.enemy[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        self.enemy[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする
                        self.enemy[i].move_index += 1 #目的座標のリストのインデックスを1進める
                    
                    if self.enemy_move_data17[self.enemy[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                        self.enemy[i].move_index = 0 #リストインデックス値を0にしてリセットする
                        
                        enemy_type = self.enemy[i].enemy_type
                        func.enemy_get_bezier_curve_coordinate(self,enemy_type,i) #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                        t = self.enemy[i].obj_time / self.enemy[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                    
                    if self.enemy[i].posx < 90: #x座標が90より小さい時は
                        #自機狙いの弾を撃つ
                        ex,ey = self.enemy[i].posx,self.enemy[i].posy
                        div_type,div_count,div_num,stop_count = 0,0,0,0
                        accel = 1
                        func.enemy_aim_bullet_rank(self,ex,ey,div_type,div_count,div_num,stop_count,accel)
                    
                    #ベジェ曲線で移動させる方法の説明はボスキャラの所と同じなのでそれを参考にしてくださいな
                    p1x = (1-t) * self.enemy[i].ax + t * self.enemy[i].qx
                    p1y = (1-t) * self.enemy[i].ay + t * self.enemy[i].dy
                    p2x = (1-t) * self.enemy[i].qx + t * self.enemy[i].dx
                    p2y = (1-t) * self.enemy[i].qy + t * self.enemy[i].dy   
                    px = (1-t) * p1x + t * p2x
                    py = (1-t) * p1y + t * p2y
                    self.enemy[i].posx = px + self.enemy[i].offset_x #(px,py)にオフセット値を加減算したものを(posx,posy)にします（こうするとあらかじめ決められたルートからずれた位置も通らせることができるのです）
                    self.enemy[i].posy = py + self.enemy[i].offset_y
                    
                    self.enemy[i].move_speed = self.enemy[i].move_speed * self.enemy[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします
                    
                    if self.enemy[i].move_speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                        self.enemy[i].move_speed = 0.2
                    self.enemy[i].obj_time += self.enemy[i].move_speed * self.enemy[i].move_speed_offset #タイムフレーム番号を(スピード*スピードオフセット)分加算していく
                
            elif self.enemy[i].enemy_type == 18:#敵タイプ18の更新  ボルダー 硬めの弾バラマキ重爆撃機 大きいサイズ
                #敵18をサインカーブを描きながら移動させる 
                self.enemy[i].posx += self.enemy[i].move_speed  #X座標をmove_speed分加減算する
                self.enemy[i].timer += self.enemy[i].speed     #タイマーをスピード分増やしていく
                self.enemy[i].posy += self.enemy[i].intensity * math.sin(self.enemy[i].timer)#振れ幅と時間を使ってサインカーブのy軸の値を求める
                
                self.enemy[i].enemy_flag1 += 1 #flag1(弾発射間隔カウント)を利用してカウント190ごとに弾を発射させる
                if self.enemy[i].enemy_flag1 == 190:
                    if func.to_my_ship_distance(self,self.enemy[i].posx,self.enemy[i].posy) < 100: #自機との距離が100より小さかったら
                        self.enemy[i].status = ENEMY_STATUS_BERSERK #ステータス「怒り」にする
                        #自機狙い4way発射*3連
                        for num in range(3):
                            theta = 30
                            n = 4
                            division_type = 0
                            division_count = 0
                            division_num = 0
                            stop_count = 5 * num
                            if self.my_x < self.enemy[i].posx + 4*8: #自機とのx座標の位置を見て前と後ろのどちらの銃口から発射するのか判定する
                                func.enemy_aim_bullet_nway(self,self.enemy[i].posx     ,self.enemy[i].posy + 8 ,theta,n,division_type,division_count,division_num,stop_count) #後ろから発射  
                            else:
                                func.enemy_aim_bullet_nway(self,self.enemy[i].posx + 4*8,self.enemy[i].posy + 10,theta,n,division_type,division_count,division_num,stop_count) #前から発射
                        
                        self.enemy[i].enemy_flag1 = 20   #カウンター値を多めにしてリセット
                    else:#そうでなかったら
                        self.enemy[i].status = ENEMY_STATUS_NORMAL #ステータスを「通常」にする
                        func.enemy_forward_3way_bullet(self,self.enemy[i].posx,self.enemy[i].posy) #前方3way弾発射
                        self.enemy[i].enemy_flag1 = 0 #カウンターリセット
                
                self.enemy[i].intensity = self.enemy[i].intensity * 0.9997#振れ幅を徐々に小さくしていく
                
                if self.enemy[i].posx < 0 and self.enemy[i].enemy_flag2 == 0: #座標がマイナス＆flag2(反転離脱フラグ)が立っていないのなら
                    self.enemy[i].enemy_flag2 = 1 #flag2(反転離脱フラグ)を立てる
                    self.enemy[i].move_speed = self.enemy[i].move_speed * -1 #移動方向を反転させる
                    
                    #反転開始時は分裂弾を発射
                    new_enemy_shot = Enemy_shot()
                    division_type        = ENEMY_SHOT_DIVISION_3WAY   #自機狙いの3way
                    division_count       = 80 #分裂するまでのカウント数
                    division_count_origin = 80 #分裂するまでのカウント数(元数値)
                    division_num        = 0    #分裂する回数
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, self.enemy[i].posx + 4*8,self.enemy[i].posy + 10,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, 1,0,     0.95,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)            
                
                if self.enemy[i].enemy_flag2 == 1: #反転離脱中の時は
                    self.enemy[i].move_speed += 0.002 #加速して離脱していく

    #画面外に出た敵を消去する
    def clip(self):
        enemy_count = len(self.enemy)
        for i in reversed(range (enemy_count)):
            if -30 < self.enemy[i].posx and self.enemy[i].posx < WINDOW_W + 200:#敵のx座標は-30~160+200以内？
                if -50 < self.enemy[i].posy and self.enemy[i].posy < self.bg_height + 50:#敵のY座標は-50~マップ全体の縦幅+50以内？
                    continue
                else:
                    if self.enemy[i].formation_id != 0: #編隊機の場合は・・・・・
                        func.check_enemy_formation_exists(self,self.enemy[i].formation_id) #画面上の編隊総数を減らす関数をよびだす
                    del self.enemy[i]#敵が画面外に存在するときはインスタンスを破棄する(敵消滅)
            else:
                if self.enemy[i].formation_id != 0: #編隊機の場合は・・・・・
                        func.check_enemy_formation_exists(self,self.enemy[i].formation_id) #画面上の編隊総数を減らす関数をよびだす
                del self.enemy[i]

    #################################敵弾関連の処理関数##################################################
    #敵の弾の更新&自機と敵弾の衝突判定
    def shot(self):
        enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
        for i in reversed(range (enemy_shot_count)):
            #敵の弾の位置を更新する！
            #サインカーブ弾の場合
            if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SIN:
                self.enemy_shot[i].posx += self.enemy_shot[i].vx      #敵の弾のx座標をvx分加減算して更新
                self.enemy_shot[i].timer += self.enemy_shot[i].speed
                self.enemy_shot[i].posy += self.enemy_shot[i].intensity * math.sin(self.enemy_shot[i].timer + 3.14 / 4)
            #コサインカーブ弾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_COS:
                self.enemy_shot[i].posx += self.enemy_shot[i].vx       #敵の弾のx座標をvx分加減算して更新
                self.enemy_shot[i].timer += self.enemy_shot[i].speed
                self.enemy_shot[i].posy += self.enemy_shot[i].intensity * math.cos(self.enemy_shot[i].timer + 3.14/2 + 3.14/4)
            #誘導弾orホーミングレーザーの場合
            elif    self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_BULLET\
                or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER:
                #誘導弾orホーミングレーザーを自機に追尾させる
                vx0 = self.enemy_shot[i].vx
                vy0 = self.enemy_shot[i].vy #誘導弾の速度ベクトル(vx,vy)を(vx0,vy0)に退避しておきます
                
                #自機までの距離を求めdに距離として代入します
                d = math.sqrt((self.my_x - self.enemy_shot[i].posx) * (self.my_x - self.enemy_shot[i].posx) + (self.my_y - self.enemy_shot[i].posy) * (self.my_y - self.enemy_shot[i].posy))
                
                #誘導弾orホーミングレーザーの速度 vx,vyを求める
                #速さはenemy_shot_speedで一定になるようにしています
                #目標までの距離dが0の時は速度ベクトルを左方向にします
                #turn_theta(Θシータ)は旋回できる角度の上限です
                
                #count1をホーミング性能が落ちていくカウンタの変数として使用します(1フレームごとに加算されていきます)
                #count2に入っている数値とenemy_shot_count1が同じ数値になった時に旋回できる角度の上限を1減らします
                
                #自機方向の速度ベクトル(vx1,vy1)を求める
                if d == 0:#自機までの距離は0だった？（重なっていた？）
                    vx1= 0
                    vy1 = self.enemy_shot[i].speed #自機までの距離dが0の時は速度を左方向にする
                else:
                    #誘導弾orホーミングレーザーと自機との距離dとx,y座標との差からvx,vyの増分を計算する
                    
                    vx1 = ((self.my_x - self.enemy_shot[i].posx) / (d * self.enemy_shot[i].speed))
                    vy1 = ((self.my_y - self.enemy_shot[i].posy) / (d * self.enemy_shot[i].speed))
                
                #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                #math.piはπ（円周率3.141592......)
                self.rad = 3.14 / 180 * self.enemy_shot[i].turn_theta #rad = 角度degree（theta）をラジアンradianに変換
                
                vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                
                #自機方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                    #自機方向が旋回可能範囲内の場合の処理
                    #自機方向に曲がるようにする
                    self.enemy_shot[i].vx = vx1
                    self.enemy_shot[i].vy = vy1
                else:
                    #自機が旋回可能範囲を超えている場合（ハンドルをいっぱいまで切っても自機に追いつけないよ～）ハンドル一杯まで切る！
                    #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                    vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                    vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0
                    
                    #誘導弾orホーミングレーザーから自機への相対ベクトル(px,py)を求める
                    px = self.my_x - self.enemy_shot[i].posx
                    py = self.my_y - self.enemy_shot[i].posy
                    
                    #右回りか左回りを決める
                    #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                    #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                    #
                    if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                        #右回り（面舵方向）の場合
                        self.enemy_shot[i].vx = vx2
                        self.enemy_shot[i].vy = vy2
                    else:
                        #左回り（取り舵方向）の場合
                        self.enemy_shot[i].vx = vx3
                        self.enemy_shot[i].vy = vy3
                
                #誘導弾orホーミングレーザーの座標(posx,posy)に速度ベクトル(vx,vy)を加減算して移動させる(座標を更新！)
                self.enemy_shot[i].posx += self.enemy_shot[i].vx
                self.enemy_shot[i].posy += self.enemy_shot[i].vy
                #誘導性能を落していく処理
                self.enemy_shot[i].count1 +=1 #誘導性能を落として行くカウンタ数をインクリメント
                if self.enemy_shot[i].count1 >= self.enemy_shot[i].count2: #カウント上限(count2)を超えたのなら・・・
                    self.enemy_shot[i].turn_theta -= 1 #旋回上限角度を1度減らす
                    if self.enemy_shot[i].turn_theta < 0:
                        self.enemy_shot[i].turn_theta = 0 #turn_thetaはマイナスにならないようにする
                    self.enemy_shot[i].count1 = 0 #誘導性能を落として行くカウンタ数を初期化
                
                if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER: #ホーミングレーザーの場合は
                    #ホーミングレーザーの尻尾部分を育成する
                    if (pyxel.frame_count % 3) == 0:
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_HOMING_LASER_TAIL,ID00,self.enemy_shot[i].posx,self.enemy_shot[i].posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,  0,0, 0,0,   0,  1,1, 0,0,  0,0,0, 0, 60,0,PRIORITY_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
                
            #ホーミングレーザーの尻尾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER_TAIL:
                self.enemy_shot[i].disappearance_count -= 1 #消滅カウンターを1減少させる
                if self.enemy_shot[i].disappearance_count <= 0:#消滅カウンターが0以下になったのなら
                    del self.enemy_shot[i]    #インスタンスを消滅させる 古い尻尾から消えていく・・・
                    continue                #これ以下の処理はせずにループを続けていく
                
            #サーチレーザーの場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER:
                if self.enemy_shot[i].search_flag == 0: #サーチフラグがまだだっていないのなら自機とのx座標の比較を以下行っていく
                    if -2 <= self.my_x - self.enemy_shot[i].posx <= 2: #自機のx座標とサーチレーザーのx座標の差が+-2以内なら
                        self.enemy_shot[i].search_flag = 1 #サーチ完了フラグを立てる
                        self.enemy_shot[i].vx = 0 #サーチ完了したのでx軸方向の移動は今後させないようにvx=0にする
                        if self.my_y >= self.enemy_shot[i].posy:#サーチレーザーのy軸移動方向を決めていく
                            self.enemy_shot[i].vy = 1 #自機がサーチレーザーより下方向にあるのでvy=1にして下方向に曲がらせる
                        else:
                            self.enemy_shot[i].vy = -1 #自機がサーチレーザーより上方向にあるのでvy=-1にして上方向に曲がらせる
                
                self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                #サーチレーザーの尻尾部分を育成する
                if (pyxel.frame_count % 4) == 0:
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_SEARCH_LASER_TAIL,ID00,self.enemy_shot[i].posx,self.enemy_shot[i].posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,  0,0, 0,self.enemy_shot[i].vy, 0,  1,1, 0,0,  0,0,0, 0, 60,0,PRIORITY_FRONT,0,self.enemy_shot[i].search_flag,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0) #search_flagとvyはdraw時に使用するのでそのままコピーします
                    self.enemy_shot.append(new_enemy_shot)
                
            #サーチレーザーの尻尾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER_TAIL:
                self.enemy_shot[i].disappearance_count -= 1 #消滅カウンターを1減少させる
                if self.enemy_shot[i].disappearance_count <= 0:#消滅カウンターが0以下になったのなら
                    del self.enemy_shot[i]    #インスタンスを消滅させる 古い尻尾から消えていく・・・
                    continue                #これ以下の処理はせずにループを続けていく
                
            #回転弾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_BULLET:
                self.enemy_shot[i].rotation_omega += self.enemy_shot[i].rotation_omega_incremental #rotation_omega_incrementalの分だけ角度を増加させていく(回転していく)
                self.enemy_shot[i].rotation_omega = self.enemy_shot[i].rotation_omega % 360 #角度は３６０で割った余りとする(0~359)
                
                self.enemy_shot[i].cx += self.enemy_shot[i].vx #回転の中心を速度ベクトルvx,vyを加算して位置を更新する
                self.enemy_shot[i].cy += self.enemy_shot[i].vy
                
                #現在の半径radiusを目標となる半径radius_maxに近づけていく
                if not -1 <= self.enemy_shot[i].radius_max - self.enemy_shot[i].radius <= 1: #radiusとradius_maxの差が+-1以内でない時は・・・
                    if self.enemy_shot[i].radius >= self.enemy_shot[i].radius_max:
                        self.enemy_shot[i].radius -= self.enemy_shot[i].radius_incremental
                    else:
                        self.enemy_shot[i].radius += self.enemy_shot[i].radius_incremental
                
                #中心cx,cy半径radius回転角度rotation_omegaから現在の敵弾の座標(posx.posy)を求める
                self.enemy_shot[i].posx = self.enemy_shot[i].cx+ self.enemy_shot[i].radius * math.cos(math.radians(self.enemy_shot[i].rotation_omega))
                self.enemy_shot[i].posy = self.enemy_shot[i].cy+ self.enemy_shot[i].radius * math.sin(math.radians(self.enemy_shot[i].rotation_omega))
                
            #落下弾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_DROP_BULLET:
                #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる x軸の速度ベクトルは変化させない
                self.enemy_shot[i].vy += self.enemy_shot[i].accel #y軸の速度ベクトルに加速度を足し合わせて加速もしくは減速させる
                self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
            #アップレーザー,ダウンレーザーの場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_UP_LASER or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_DOWN_LASER:
                if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                    self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                    self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                    self.enemy_shot[i].width += self.enemy_shot[i].expansion #毎フレームごとexpansion分だけ横幅を拡大させていく
                    if self.enemy_shot[i].width >= self.enemy_shot[i].width_max: #widthはwidth_maxを超えないようにします
                        self.enemy_shot[i].width = self.enemy_shot[i].width_max #幅は最大値とする
                        self.enemy_shot[i].vx = 0                         #最大幅まで広くなったのでもう横方向の移動は無し
                    
                else:
                    self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
                
            #ベクトルレーザーの場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_VECTOR_LASER:
                if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                    self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                    self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                    self.enemy_shot[i].height += self.enemy_shot[i].expansion #毎フレームごとexpansion分だけ縦幅を拡大させていく
                    if self.enemy_shot[i].height >= self.enemy_shot[i].height_max: #heightはheight_maxを超えないようにします
                        self.enemy_shot[i].height = self.enemy_shot[i].height_max #幅は最大値とする
                        self.enemy_shot[i].vy = 0                         #最大幅まで広くなったのでもう縦方向の移動は無し
                    
                else:
                    self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
                
            #その他の敵弾の場合
            else: 
                if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                    self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                    self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                    if   self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_3WAY: #3way分裂弾を生み出す
                        self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                        if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                            ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                            theta = 20 #発射角度は20度
                            n = 3 #3way弾
                            if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                div_type = 0 #分裂無しタイプにする
                            else:
                                self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                div_type = ENEMY_SHOT_DIVISION_3WAY #3way弾
                            
                            div_num = self.enemy_shot[i].division_num
                            div_count = self.enemy_shot[i].division_count_origin
                            stop_count = 0
                            func.enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い3way分裂弾育成
                            del self.enemy_shot[i] #元の弾のインスタンスは消去する
                            continue #ループはそのまま続けるのでcontinue
                        
                    elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_5WAY: #5way分裂弾を生み出す
                        self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                        if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                            ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                            theta = 40 #発射角度は40度
                            n = 5 #3way弾
                            if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                div_type = 0 #分裂無しタイプにする
                            else:
                                self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                div_type = ENEMY_SHOT_DIVISION_5WAY #5way弾
                            
                            div_num = self.enemy_shot[i].division_num
                            div_count = self.enemy_shot[i].division_count_origin
                            stop_count = 0
                            func.enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い5way分裂弾育成
                            del self.enemy_shot[i] #元の弾のインスタンスは消去する
                            continue #ループはそのまま続けるのでcontinue
                        
                    elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_7WAY: #7way分裂弾を生み出す
                        self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                        if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                            ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                            theta = 100 #発射角度は100度
                            n = 7 #7way弾
                            if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                div_type = 0 #分裂無しタイプにする
                            else:
                                self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                div_type = ENEMY_SHOT_DIVISION_7WAY #7way弾
                            
                            div_num = self.enemy_shot[i].division_num
                            div_count = self.enemy_shot[i].division_count_origin
                            stop_count = 0
                            func.enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い7way分裂弾育成
                            del self.enemy_shot[i] #元の弾のインスタンスは消去する
                            continue #ループはそのまま続けるのでcontinue
                        
                    elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_9WAY: #9way分裂弾を生み出す
                        self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                        if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                            ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                            theta = 160 #発射角度は160度
                            n = 9 #9way弾
                            if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                div_type = 0 #分裂無しタイプにする
                            else:
                                self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                div_type = ENEMY_SHOT_DIVISION_9WAY #9way弾
                            
                            div_num = self.enemy_shot[i].division_num
                            div_count = self.enemy_shot[i].division_count_origin
                            stop_count = 0
                            func.enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い9way分裂弾育成
                            del self.enemy_shot[i] #元の弾のインスタンスは消去する
                            continue #ループはそのまま続けるのでcontinue
                    
                else:
                    self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
            
            #敵のレーザー兵器がＬ’ｓシールドシステムに当たっているか判別###################################
            if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_LASER and self.ls_shield_hp > 0:#敵のショットがレーザーの時かつシールドエナジーが残っているときのみ処理する
                if   0 <= self.enemy_shot[i].posx - (self.my_x + 8) <= 4 and 0 <= self.enemy_shot[i].posy - (self.my_y - 12) < 26:#シールドと敵レーザーが接触したのなら
                    self.ls_shield_hp -= 1#シールドエナジーを1減らす
                    del self.enemy_shot[i]
                    continue
            
            #敵の弾が自機に当たっているか判別###########################################################
            if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
                continue                #衝突判定はせずループだけ続ける(continue)・・・無敵っていいよね・・・うん、うん.....
            
            if self.enemy_shot[i].collision_type == ESHOT_COL_MIN88: #最小の正方形8x8ドットでの当たり判定の場合
                #敵の弾と自機の位置の2点間の距離を求める
                self.dx = (self.enemy_shot[i].posx + 4) - (self.my_x + 4)
                self.dy = (self.enemy_shot[i].posy + 4) - (self.my_y + 4)
                self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
                if self.distance < 3:
                    update_ship.damage(self,1) #敵弾と自機の位置の距離が3以下なら衝突したと判定し自機のシールド値を１減らす
                
            elif self.enemy_shot[i].collision_type == ESHOT_COL_BOX: #長方形での当たり判定の場合
                if      0 <= (self.my_x+4) - (self.enemy_shot[i].posx+4) <= self.enemy_shot[i].width\
                    and 0 <= (self.my_y+4) - (self.enemy_shot[i].posy+4) <= self.enemy_shot[i].height:
                    update_ship.damage(self,1) #自機が敵弾の長方形の当たり判定の中に居たのなら衝突したと判定し自機のシールド値を１減らす

    #敵の弾のはみだしチェック（はみ出していたら消去する）
    def clip_shot(self):
        enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
        for i in reversed(range (enemy_shot_count)):
            if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_BULLET or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_LASER:
                #回転系の弾の座標はcx,cyを基準としてはみだし判定する(結構大きくはみ出しても消えない感じで判定します)
                if  (-40 < self.enemy_shot[i].cx < WINDOW_W + 40 ) and ( -40 < self.enemy_shot[i].cy < self.bg_height + 40 ):
                    continue
                else:
                    del self.enemy_shot[i]
            else:#それ以外の弾の座標はposx,posyを基準としてはみだし判定する
                if  (-8 < self.enemy_shot[i].posx < WINDOW_W + 8) and ( -8 < self.enemy_shot[i].posy < self.bg_height + 8 ):
                    continue
                else:
                    del self.enemy_shot[i]            

