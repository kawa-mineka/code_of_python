###########################################################
#  update_eventクラス                                     #
###########################################################
# Appクラスのupdate関数から呼び出される関数群                #
# 主にイベントリストでの敵の発生やボスの発生を行うメソッド     #
# BGマップスクロール時にBGチップデータを調べて               #
# 敵の砲台とかも出現させる処理を行う                         #
# 2022 05/07からファイル分割してモジュールとして運用開始      #
###########################################################

from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_boss import * #ボスを出現させる時に使用します

class update_event:
    def __init__(self):
        None

    #イベントリストを解析してその内容を実行し,敵の発生や背景オブジェクトの発生、スクロール方向スピードなどの調整を行う (まぁこのメソッドで敵が出現する訳です)
    def list_execution(self):
        """
        イベントリストを解析してその内容を実行し,敵の発生や背景オブジェクトの発生、スクロール方向スピードなどの調整を行う (まぁこのメソッドで敵が出現する訳です)
        """
        if self.stage_count == self.event_list[self.event_index][0]:#ステージカウントとリストのカウント値が同じならリスト内容を実行する
            if   self.event_list[self.event_index][1] == EVENT_ENEMY:             #イベント「敵出現」の場合
                if   self.event_list[self.event_index][2] == EnemyName.CIR_COIN:      #サーコイン発生！
                    for number in range(self.event_list[self.event_index][5]):
                        #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                        new_enemy = Enemy()
                        new_enemy.update(EnemyName.CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0, -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1*self.enemy_speed_mag,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT02,PT02,  PT01,PT01,PT03)
                        self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    func.record_enemy_formation(self,self.event_list[self.event_index][5]) 
                elif self.event_list[self.event_index][2] == EnemyName.TWIN_ARROW:    #追尾戦闘機ツインアロー出現
                    new_enemy = Enemy()
                    new_enemy.update(EnemyName.TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5 - (self.enemy_speed_mag // 2),0,  0,    HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)                
                elif self.event_list[self.event_index][2] == EnemyName.SAISEE_RO:     #回転戦闘機サイシーロ出現(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(EnemyName.SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1*self.enemy_speed_mag,0,  0,  HP01 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,     0,0,0,0,    E_NO_POW,ID00 ,0,0,0,              0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)    
                elif self.event_list[self.event_index][2] == EnemyName.GREEN_LANCER:   #グリーンランサー 3way弾を出してくる緑の戦闘機(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(EnemyName.GREEN_LANCER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.1*self.enemy_speed_mag,0,  0,  HP05 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.01,0,     0,0,0,0,    E_MISSILE_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == EnemyName.RAY_BLASTER:    #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
                    new_enemy = Enemy()
                    new_enemy.update(EnemyName.RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    -2,(func.s_rndint(self,0,1)-0.5),       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,  0,  HP02 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,80 + func.s_rndint(self,0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == EnemyName.VOLDAR:        #ボルダー 硬めの弾バラマキ重爆撃機
                    new_enemy = Enemy()
                    new_enemy.update(EnemyName.VOLDAR,ID00,     ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07*self.enemy_speed_mag,1,  0,  HP59 * self.enemy_hp_mag,   0,0,  E_SIZE_HI_MIDDLE53,  0,0,0,     0,0,0,0,     E_SHOT_POW,ID00    ,1,0.007,0.6,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT10)
                    self.enemy.append(new_enemy)
                
            elif self.event_list[self.event_index][1] == EVENT_FAST_FORWARD_NUM:  #イベント「早回し編隊パラメーター設定」の場合
                self.fast_forward_destruction_num   = self.event_list[self.event_index][2] #早回しの条件を満たすのに必要な「敵編隊殲滅必要数」を変数に代入する
                self.fast_forward_destruction_count = self.event_list[self.event_index][3] #敵編隊を早回しで破壊した時にどれだけ出現時間が速くなるのか？そのカウントを変数に代入する         
            elif self.event_list[self.event_index][1] == EVENT_ADD_APPEAR_ENEMY:  #イベント「敵出現（早回しによる敵追加出現）」の場合
                if self.add_appear_flag == FLAG_ON: #「早回し敵発生フラグ」が立っているのならば
                    #サーコイン発生！
                    if self.event_list[self.event_index][2] == EnemyName.CIR_COIN:
                        for number in range(self.event_list[self.event_index][5]):
                            #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                            new_enemy = Enemy()
                            new_enemy.update(EnemyName.CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                self.game_status = Scene.BOSS_APPEAR      #ゲームのステータスを「BOSS_APPEAR」ボス出現！にします
                update_boss.born_boss(self)                      #各面のボスを生み出す関数を呼び出します
                self.boss_battle_time = 0                 #ボスとの戦闘時間を0で初期化！ボスとの戦闘スタート！
            self.event_index += 1 #イベントインデックス値を1増やして次のイベントの実行に移ります

    #マップスクロールによる敵の発生を行う
    def enemy_born_map_scroll(self):
        """
        マップスクロールによる敵の発生を行う
        """
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
                new_enemy.update(EnemyName.HOUDA_UNDER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,    0, HP01 * self.enemy_hp_mag,   0,0,E_SIZE_NORMAL,0,0,0,     0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                new_enemy.update(EnemyName.HOUDA_UPPER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,  0,  HP01 * self.enemy_hp_mag,    0,0,E_SIZE_NORMAL,0,0,0,    0,0,0,0,    item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら(「敵出現」情報)のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_HOPPER_CHAN2:    #マップチップがはねるホッパーちゃん２のとき
                new_enemy = Enemy()
                new_enemy.update(EnemyName.HOPPER_CHAN2,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,    0.4,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    0.2*self.enemy_speed_mag,0,  -1,    HP01 * self.enemy_hp_mag,   0,0,   E_SIZE_NORMAL,(i * 8),-20,1,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_SAISEE_RO:       #マップチップがサイシーロの時(サインカーブを描く敵）
                new_enemy = Enemy()
                new_enemy.update(EnemyName.SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    1*self.enemy_speed_mag,0,   0,   HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,   0.5,0.05,0,    0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_KURANBURU_UNDER: #マップチップが地上スクランブルハッチのとき
                new_enemy = Enemy()
                new_enemy.update(EnemyName.KURANBURU_UNDER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32,  (func.s_rndint(self,0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_KURANBURU_UPPER: #マップチップが天井スクランブルハッチのとき
                new_enemy = Enemy()
                new_enemy.update(EnemyName.KURANBURU_UPPER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32_Y_REV,  (func.s_rndint(self,0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
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
                new_enemy.update(EnemyName.TEMI,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -0.44,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_8,   0,0,   0,    HP10,   0,0,   E_SIZE_NORMAL,  0,0,0,   0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む 
                
            elif self.bg_chip == BG_RAY_BLASTER:     #マップチップがレイブラスターのとき(直進して画面前方のどこかで停止→レーザービーム射出→急いで後退)
                new_enemy = Enemy()
                new_enemy.update(EnemyName.RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,i * 8,0,0,      0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -2,(func.s_rndint(self,0,1)-0.5),     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.98,0,    0,    HP01 * self.enemy_hp_mag,  0,0,    E_SIZE_NORMAL,   80 + func.s_rndint(self,0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_MUU_ROBO:        #マップチップがムーロボのとき(地面を左右に動きながらチョット進んできて弾を撃つ移動砲台,何故か宇宙なのに重力の影響を受けて下に落ちたりもします)
                new_enemy = Enemy()
                new_enemy.update(EnemyName.MUU_ROBO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,       0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.8*self.enemy_speed_mag,0,    -1,    HP01 * self.enemy_hp_mag,  70,80,    E_SIZE_NORMAL,   70,80,0,     0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == BG_ROLL_BLITZ:      #マップチップがロールブリッツのとき(画面内のあらかじめ決められた場所へスプライン曲線で移動)
                new_enemy = Enemy()
                new_enemy.update(EnemyName.ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,      E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                func.delete_map_chip(self,self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む

    #アペンドイベントリクエスト(イベント追加依頼）による敵の発生
    def append_request(self):
        """
        アペンドイベントリクエスト(イベント追加依頼）による敵の発生
        """
        event_append_request_count = len(self.event_append_request)
        for i in reversed (range(event_append_request_count)):
            if self.stage_count == self.event_append_request[i].timer:
                if self.event_append_request[i].event_type == EVENT_ENEMY: #イベントの内容が敵出現の場合
                    #サーコインの追加発生！
                    if self.event_append_request[i].enemy_type == EnemyName.CIR_COIN:
                        for e in range(self.event_append_request[i].number):
                            #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                            new_enemy = Enemy()
                            new_enemy.update(EnemyName.CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (e * 12),self.event_append_request[i].posy,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0,     0,0,0,0,        E_NO_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                            self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    func.record_enemy_formation(self,self.event_append_request[i].number)
                    del self.event_append_request[i] #敵を追加発生リクエストをリストから消去します
