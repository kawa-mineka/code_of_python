###########################################################
#  update_btnクラス                                       #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にキー入力(パッドの入力)の更新を行うメソッド             #
#  ショットボタンが押されたか？ミサイルボタンが押されたか？    #
#  クローショットボタンが押されたか？などのチェック            #
#                                                         #
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

from update_obj    import *   #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update_ship   import *   #自機関連更新関数モジュール読み込み
# from update_window import *   #ポーズウィンドウ作成時に使用するのでインポート

class update_btn:
    #キーボードの上かカーソルとジョイパッドの上方向ボタンが押されたかどうかを調べる(キーリピート付き)                  KEY UP PAD UP
    #帰り値は上ボタンが押された時=True 上ボタンは押されていなかった時=Falseを返します
    def keypad_up(self):
        if pyxel.btnp(pyxel.KEY_UP,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_UP,10,self.keypad_repeat_num): #上ボタンが押されているかチェック
            update_btn.reduce_repeat_time_count(self)
            # print (self.cursor_repeat_time_count)
            return(True)
            
        else:
            if    pyxel.btnr(pyxel.KEY_UP) == True\
            or  pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_UP) == True\
            or  pyxel.btnr(pyxel.GAMEPAD2_BUTTON_DPAD_UP) == True:   #上ボタンが離された時は
                self.cursor_repeat_time_count = 10                   #カーソルリピートタイムカウントを初期状態に戻す
                # print("REPEAT RESET!")
                # print (self.cursor_repeat_time_count)
                return(False)
            else:
                return(False)

    #キーボードの下かカーソルとジョイパッドの下方向ボタンが押されたかどうかを調べる(キーリピート付き)                  KEY DOWN PAD DOWN
    #帰り値は下ボタンが押された時=True 下ボタンは押されていなかった時=Falseを返します
    def keypad_down(self):
        if pyxel.btnp(pyxel.KEY_DOWN,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN,10,self.keypad_repeat_num): #下ボタンが押されているかチェック
            update_btn.reduce_repeat_time_count(self)
            # print (self.cursor_repeat_time_count)
            return(True)
        else:
            if    pyxel.btnr(pyxel.KEY_DOWN) == True\
            or  pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) == True\
            or  pyxel.btnr(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN) == True:   #下ボタンが離された時は
                self.cursor_repeat_time_count = 10                     #カーソルリピートタイムカウントを初期状態に戻す
                # print("REPEAT RESET!")
                # print (self.cursor_repeat_time_count)
                return(False)
            else:
                return(False)

    #キーボードの左かカーソルとジョイパッドの左方向ボタンが押されたかどうかを調べる(キーリピート付き)                  KEY LEFT PAD LEFT
    #帰り値は左ボタンが押された時=True 左ボタンは押されていなかった時=Falseを返します
    def keypad_left(self):
        if pyxel.btnp(pyxel.KEY_LEFT,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT,10,self.keypad_repeat_num): #左ボタンが押されているかチェック
            update_btn.reduce_repeat_time_count(self)
            # print (self.cursor_repeat_time_count)
            return(True)
            
        else:
            if    pyxel.btnr(pyxel.KEY_LEFT) == True\
            or  pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) == True\
            or  pyxel.btnr(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT) == True: #左ボタンが離された時は
                self.cursor_repeat_time_count = 10                   #カーソルリピートタイムカウントを初期状態に戻す
                # print("REPEAT RESET!")
                # print (self.cursor_repeat_time_count)
                return(False)
            else:
                return(False)

    #キーボードの右かカーソルとジョイパッドの右方向ボタンが押されたかどうかを調べる(キーリピート付き)                  KEY RIGHT PAD RIGHT
    #帰り値は右ボタンが押された時=True 右ボタンは押されていなかった時=Falseを返します
    def keypad_right(self):
        if pyxel.btnp(pyxel.KEY_RIGHT,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT,10,self.keypad_repeat_num) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT,10,self.keypad_repeat_num): #右ボタンが押されているかチェック
            update_btn.reduce_repeat_time_count(self)
            # print (self.cursor_repeat_time_count)
            return(True)
            
        else:
            if    pyxel.btnr(pyxel.KEY_RIGHT) == True\
            or  pyxel.btnr(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) == True\
            or  pyxel.btnr(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT) == True: #右ボタンが離された時は
                self.cursor_repeat_time_count = 10                   #カーソルリピートタイムカウントを初期状態に戻す
                # print("REPEAT RESET!")
                # print (self.cursor_repeat_time_count)
                return(False)
            else:
                return(False)

    #カーソルリピートタイムカウントを減少させていく関数
    def reduce_repeat_time_count(self):
        if   7 <= self.cursor_repeat_time_count <= 9:
            self.keypad_repeat_num = 4
        elif 2 <= self.cursor_repeat_time_count <= 6:
            self.keypad_repeat_num = 3
        else:
            self.keypad_repeat_num = 2
        
        self.cursor_repeat_time_count -= 1
        
        if self.cursor_repeat_time_count <= 0:    #リピートタイムは0より小さくはしないように補正します
                self.cursor_repeat_time_count = 0

    #スペースキーかゲームパッドのショットボタンが押されたかどうか？もしくはリプレイモードでショット発射したのか調べる  KEY SPACE GAMEPAD-SHOT GAMEPAD-SHOT&SUB_WEAPON
    def shot_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1 ] & 0b00010000 == 0b00010000: #LowByte リプレイデータを調べてPAD Aが押された記録だったのなら...
                update_ship.fire_shot(self) #ショット発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or func.push_pad_btn(self,ACT_SHOT_AND_SUB_WEAPON) or func.push_pad_btn(self,ACT_SHOT): #パッドのショット発射ボタン又はスペースキーが押されたか？
                self.pad_data_l += PAD_A #コントロールパッド入力記録にAボタンを押した情報ビットを立てて記録する
                update_ship.fire_shot(self) #ショット発射関数呼び出し！

    #スペースキーかゲームバットのミサイルボタンが押さたかどうか？もしくはリプレイモードでミサイル発射したのか調べる    KEY SPACE GAMEPAD-MISSILE
    def missile_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00100000 == 0b00100000: #LowByte リプレイデータを調べてPAD Bが押された記録だったのなら...
                update_ship.fire_missile(self) #ミサイル発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or func.push_pad_btn(self,ACT_MISSILE): #パッドのミサイル発射ボタン又はスペースキーが押されたか？
                self.pad_data_l += PAD_B #コントロールパッド入力記録にBボタンを押した情報ビットを立てて記録する
                update_ship.fire_missile(self) #ミサイル発射関数呼び出し！

    #サブウェポン切り替えボタンが押された＆サブウェポンを一つでも所維持しているのか？チェックする                      GAMEPAD-SUB_WEAPON_CHANGE
    def change_sub_weapon_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b10000000 == 0b10000000: #LowByte リプレイデータを調べてPAD Yが押された記録だったのなら...
                update_ship.change_sub_weapon(self) #サブウェポン切り替え関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if func.push_pad_btnp(self,ACT_SUB_WEAPON_CHANGE) and self.select_sub_weapon_id != -1:#サブウェポン切り替えボタンが押された＆サブウェポンを一つでも所維持しているのか？
                self.pad_data_l += PAD_Y #コントロールパッド入力記録にYボタンを押した情報ビットを立てて記録する
                update_ship.change_sub_weapon(self) #サブウェポン切り替え関数呼び出し！

    #クローが弾を発射するのか調べる関数                                                                               KEY SPACE GAMEPAD-SHOT GAEPAD-SHOT&SUB_WEAPON
    def claw_shot_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00010000 == 0b00010000: #LowByte リプレイデータを調べてPAD Aが押された記録だったのなら...
                update_ship.fire_claw_shot(self) #クローショット発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or func.push_pad_btn(self,ACT_SHOT_AND_SUB_WEAPON) or func.push_pad_btn(self,ACT_SHOT):  #パッドのショット発射ボタン又はスペースキーが押されたか？
                update_ship.fire_claw_shot(self) #クローショット発射関数呼び出し！

    #クローを消滅させるボタンが押されたかどうかを調べる関数                                                           KEY W
    def delete_claw_btn(self):
        if pyxel.btnp(pyxel.KEY_W):   #wキーが押されたら自機クローを消滅させる
            claw_count = len(self.claw)
            for i in reversed(range(claw_count)):
                if claw_count != 0:  #クローの数が0以外なら
                    del self.claw[i] #クローのインスタンスを破棄する(クロー消滅)
            
            self.claw_number = 0     #クローの数を0機にする

    #フイックスクローの間隔変化ボタンが押されたかチェックする                                                        KEY N  GAMEPAD RIGHT_SHOULDER
    def change_fix_claw_interval_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00001000 == 0b00001000: #HighByte リプレイデータを調べてPAD_RIGHT_Sが押された記録だったのなら...
                update_ship.change_fix_claw_interval(self) #フイックスクローの間隔変化関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_N) or func.push_pad_btn(self,ACT_CHANGE_CLAW_INTERVAL):#NキーかCHANGE_CLAW_INTERVALが押されたらフックスクローの間隔を変化させる
                self.pad_data_h += PAD_RIGHT_S #パッド入力データのRIGHT_SHOULDERボタンの情報ビットを立てる
                update_ship.change_fix_claw_interval(self) #フイックスクローの間隔変化関数呼び出し！

    #クロースタイル変更ボタンが押されたかチェックする                                                                 KEY M  GAMEPAD LEFT_SHOULDER
    def change_claw_style_btn(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00000100 == 0b00000100: #HighByte リプレイデータを調べてPAD_LEFT_Sが押された記録だったのなら...
                update_ship.change_claw_style(self) #クロースタイル変更関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btnp(pyxel.KEY_M) or func.push_pad_btnp(self,ACT_CHANGE_CLAW_STYLE):#MキーかCHANGE_CLAW_STYLEが押されたらクローの種類を変更する
                self.pad_data_h += PAD_LEFT_S #パッド入力データのLEFT_SHOULDERボタンの情報ビットを立てる
                update_ship.change_claw_style(self) #クロースタイル変更関数呼び出し！

    #キーボードの1が推されたらショット経験値を増やしていく                                                           KEY 1
    def powerup_shot(self):
        if pyxel.btnp(pyxel.KEY_1):
            self.shot_exp += 1  #ショット経験値を１増やして武器をアップグレードさせていく
            func.level_up_my_shot(self) #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
            if self.shot_level > 10:
                self.shot_level = 0

    #キーボードの2が推されたらミサイル経験値を増やしていく                                                           KEY 2
    def powerup_missile(self):
        if pyxel.btnp(pyxel.KEY_2):
            self.missile_exp += 1#ミサイル経験値を１増やしてミサイルをアップグレードさせていく
            func.level_up_my_missile(self) #自機ミサイルの経験値を調べ可能な場合はレベルアップさせる関数を呼び出す
            if self.missile_level > 2:
                self.missile_level = 0

    #キーボードの3かゲームパッドの「BACK」ボタン(スピードチェンジ)が押されたか？チェックする                          KEY 3      GAMEPAD BACK
    def change_speed(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00000001 == 0b00000001: #HighByte リプレイデータを調べてPAD SELECTが押された記録だったのなら...
                update_ship.change_ship_speed(self) #スピードチェンジ関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btnp(pyxel.KEY_3) or func.push_pad_btnp(self,BTN_BACK):
                self.pad_data_h += PAD_SELECT #パッド入力データのSELECTボタンの情報ビットを立てる(GUIDE)
                update_ship.change_ship_speed(self) #スピードチェンジ関数呼び出し！

    #ポーズボタンが押されたか調べる 「START」ボタン                                                                  KEY TAB    GAMEPAD START
    def pause_btn(self):
        # if pyxel.btnp(pyxel.KEY_TAB) == True or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START) == True:
        if pyxel.btnp(pyxel.KEY_TAB) == True or func.push_pad_btnp(self,ACT_PAUSE) == True:
            if    self.game_status == SCENE_PLAY\
                or self.game_status == SCENE_BOSS_APPEAR\
                or self.game_status == SCENE_BOSS_BATTLE\
                or self.game_status == SCENE_BOSS_EXPLOSION:#ステータスが「PLAY」もしくは「BOSS関連」のときにポーズボタンが押されたときは・・
                
                self.record_games_status = self.game_status #ステータスを一時記憶しておく
                self.game_status = SCENE_PAUSE              #ステータスを「PAUSE」にする
                if func.search_window_id(self,WINDOW_ID_PAUSE_MENU) == -1: #ポーズメニューウィンドウが存在しないのなら・・
                    # update_window.create(self,WINDOW_ID_PAUSE_MENU,30,70)          #ポーズメニューウィンドウウィンドウの作製 なんかどうもimportの循環エラー出るのでここで直接ポーズメニューウィンドウを育成しちゃう 後日どうしたら良いのか考えよう・・・多分忘れてると思うけど
                    func.create_master_flag_list(self) #まず先にフラグ＆データ関連のマスターリスト作成関数を呼び出す
                    new_window = Window()
                    new_window.update(\
                    WINDOW_ID_PAUSE_MENU,\
                    WINDOW_ID_SUB_NORMAL_MENU,\
                    WINDOW_TYPE_NORMAL,\
                    WINDOW_FRAME_NORMAL,\
                    WINDOW_BG_BLUE_BACK,\
                    WINDOW_PRIORITY_NORMAL,\
                    DIR_RIGHT_DOWN,\
                    DIR_LEFT_UP,\
                    WINDOW_OPEN,\
                    0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
                    WINDOW_BETWEEN_LINE_7,\
                    ["BACK TO GAMES",   CLICK_SOUND_ON ,DISP_CENTER,0,0, 7,MES_RED_FLASH],\
                    
                    [[ "RETURN TITLE",  CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH],\
                    [  "RESTART STAGE", CLICK_SOUND_ON ,DISP_CENTER,0,0, 7,MES_NO_FLASH],\
                    [  "EXIT GAME",     CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH],\
                    [  " ",             CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
                    
                    NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
                    30,70,30,70,   0,0,  92,29,   2,2, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
                    BUTTON_DISP_OFF,0,0,0,\
                    BUTTON_DISP_OFF,0,0,0,\
                    
                    CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
                    DISP_OFF,\
                    
                    NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
                    NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
                    NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
                    NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
                    NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
                    NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
                    NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
                    
                    self.master_flag_list,\
                    NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
                    NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
                    
                    COMMENT_FLAG_OFF,0,0,0,0,\
                    NO_COMMENT_DISP_FLAG,\
                    NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
                    NO_ITEM_ID,\
                    )
                    self.window.append(new_window)                  #ウィンドウを育成する
                    
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「BACK TO GAMES」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は3項目なので 4-1=3を代入,メニューの階層は一番低いMENU_LAYER0にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,46,73,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,4-1,0,MENU_LAYER0)
                    self.active_window_id = WINDOW_ID_PAUSE_MENU    #このウィンドウIDを最前列でアクティブなものとする
                    self.select_cursor_flag = 1            #セレクトカーソル移動フラグを建てる
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
                self.cursor_button_data = BTN_NONE          #押されたボタンIDを初期化
                self.cursor_decision_item_y = UNSELECTED
                
            elif self.game_status == SCENE_PAUSE:          #ポーズ状態でポーズボタンが押されたときは・・・
                self.game_status = self.record_games_status #一時記憶しておいたゲームステータスを元に戻してあげます
                self.star_scroll_speed = 1                  #星のスクロールスピードを倍率1に戻す
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                if func.search_window_id(self,WINDOW_ID_PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = func.search_window_id(self,WINDOW_ID_PAUSE_MENU)
                    self.window[i].vy = -0.3            #WINDOW_ID_PAUSE_MENUウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.select_cursor_flag = 0         #セレクトカーソル移動フラグを降ろす
                    
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                
            else:
                self.cursor_button_data = BTN_NONE          #押されたボタンIDを初期化
                self.cursor_decision_item_y = UNSELECTED
                return
