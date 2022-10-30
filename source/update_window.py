###########################################################
#  update_windowクラス                                    #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にウィンドウの更新を行う関数(メソッド？）ですよ～♪        #
#  あとウィンドウシステムで使用するセレクトカーソルとかも      #
# 2022 04/05からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const     import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func      import * #汎用性のある関数群のモジュールの読み込み
from update_se import * #CONFIGでSEボリュームを変化させたときSEを鳴らすために使用します

class update_window:
    def __init__(self):
        None

    #ウィンドウの更新
    def window(self):
        window_count = len(self.window)
        for i in range(window_count):
            if   self.window[i].window_status == WINDOW_OPEN:     #ステータスが「オープン」の時は・・・・・・・・・・・・
                if self.window[i].width < self.window[i].open_width:#widthをopen_widthの数値になるまで増加させていく
                    self.window[i].width += int(self.window[i].change_x * self.window[i].open_speed)
                
                if self.window[i].height < self.window[i].open_height:#heightをopen_heightの数値になるまで増加させていく
                    self.window[i].height += int(self.window[i].change_y * self.window[i].open_speed)
                
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].open_width  - self.window[i].width  <= 2 and\
                    -2 <= self.window[i].open_height - self.window[i].height <= 2:#もしwidthとheightの値がopenした時の数値と+-2以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウは完全に開ききったとみなしてステータスをWINDOW_WRITE_MESSAGEにしてメッセージを表示開始する
                    
                    self.window[i].width  = self.window[i].open_width #小数点以下の座標の誤差を修正するために強制的にopen時の座標数値を現在座標数値に代入してやる
                    self.window[i].height = self.window[i].open_height
            elif self.window[i].window_status == WINDOW_CLOSE:    #ステータスが「クローズ」の時は・・・・・・・・・・・・
                if self.window[i].width > 0 :#widthを0になるまで減少させていく
                        self.window[i].width -= int(self.window[i].change_x * self.window[i].close_speed)
                    
                if self.window[i].height >0 :#heightを0になるまで減少させていく
                    self.window[i].height -= int(self.window[i].change_y * self.window[i].close_speed)
                    
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].width  <= 2 and\
                    -2 <= self.window[i].height <= 2:#もしwidthとheightの値が+-2以内になったのなら
                    self.window[i].window_status = WINDOW_CLOSE_COMPLETED#ウィンドウは完全に閉めきったとみなしてステータスをWINDOW_CLOSE_COMPLETEDにする
                    
                    self.window[i].width  = 0 #小数点以下の座標の誤差を修正するために0を現在のウィンドウ縦横幅とする
                    self.window[i].height = 0
            elif self.window[i].window_status == WINDOW_MOVE:     #ステータスが「ムーブ」の時は・・・・・・・・・・・・・
                if      -3 <= self.window[i].dx - self.window[i].posx <= 3\
                    and -3 <= self.window[i].dy - self.window[i].posy <= 3: #移動先の座標(dx,dy)と現在の座標が+-3以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウ移動は完了とみなしてステータスをWINDOW_WRITE_MESSAGEにする
                    
                    self.window[i].posx = self.window[i].dx #小数点以下の座標の誤差を修正するために強制的に移動先の座標を現在座標数値に代入してやる
                    self.window[i].posy = self.window[i].dy
                    self.window[i].vx = 0       #移動速度,加速度初期化
                    self.window[i].vy = 0
                    self.window[i].vx_accel = 1
                    self.window[i].vy_accel = 1
            
            #ウィンドウ位置の更新
            if self.window[i].wait_count <= 0: #ウェイトカウンターが0以下まで減少したらウィンドウは動き出す
                self.window[i].vx *= self.window[i].vx_accel #速度に加速度を掛け合わせて変化させていく
                self.window[i].vy *= self.window[i].vy_accel
                self.window[i].posx += self.window[i].vx #ウィンドウ位置の更新
                self.window[i].posy += self.window[i].vy
            else:
                self.window[i].wait_count -= 1  #カウンターをデクリメント

    #各種ウィンドウの育成             id=windowクラスの window_idに入っている数値 ox,oy=ウィンドウ作成座標のオフセット値
    def create(self,id,ox,oy):
        func.create_master_flag_list(self) #まず先にフラグ＆データ関連のマスターリスト作成関数を呼び出す
        new_window = Window()
        if   id == WINDOW_ID_MAIN_MENU:
            new_window.update(\
            WINDOW_ID_MAIN_MENU,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_LOW_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["MENU",          CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [["GAME START"   ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "DIFFICULTY"   ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SELECT SHIP"  ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "MEDAL"        ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SCORE BOARD"  ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "STATUS"       ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "NAME ENTRY"   ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "CONFIG"       ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "REPLAY"       ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SELECT STAGE" ,CLICK_SOUND_ON ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            [ "SELECT LOOP"  ,CLICK_SOUND_ON ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            [ "BOSS MODE"    ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "EXIT"         ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            MAIN_MENU_X+ox,MAIN_MENU_Y+oy,  MAIN_MENU_X+ox,MAIN_MENU_Y+oy,   0,0,  8*8,9*11,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,   0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_SELECT_STAGE_MENU:
            new_window.update(\
            WINDOW_ID_SELECT_STAGE_MENU,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  2*8,5*8,   2,2, 1,0.5,   0,0,    0,0,    0,0,0,0,   0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_SELECT_LOOP_MENU:
            new_window.update(\
            WINDOW_ID_SELECT_LOOP_MENU,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  2*8,5*8,   2,2, 1,0.5,   0,0,    0,0,    0,0,0,0,   0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_BOSS_MODE_MENU:
            new_window.update(\
            WINDOW_ID_BOSS_MODE_MENU,\
            WINDOW_ID_SUB_ON_OFF_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [[".",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ ".",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  2*8+7,21,   2,1, 1,0.7,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_HITBOX_MENU:
            new_window.update(\
            WINDOW_ID_HITBOX_MENU,\
            WINDOW_ID_SUB_ON_OFF_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [[" ",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  2*8+7,21,   2,1, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_SELECT_DIFFICULTY:
            new_window.update(\
            WINDOW_ID_SELECT_DIFFICULTY,\
            WINDOW_ID_SUB_MULTI_SELECT_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["DIFFICULTY",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [[" ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY EASY",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "EASY",     DISP_CENTER,1, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "NORMAL",   DISP_CENTER,2, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "HARD",     DISP_CENTER,3, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY HARD",DISP_CENTER,4, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "INSAME",   DISP_CENTER,5, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  48,51,   3,3, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_GAME_OVER_RETURN:
            new_window.update(\
            WINDOW_ID_GAME_OVER_RETURN,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_LOW_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE?",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",      CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["SAVE & RETURN",CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  8*8,3*8,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_GAME_OVER_RETURN_NO_SAVE:
            new_window.update(\
            WINDOW_ID_GAME_OVER_RETURN_NO_SAVE,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_LOW_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE?",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",      CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  8*8,2*8,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_INPUT_YOUR_NAME:
            new_window.update(\
            WINDOW_ID_INPUT_YOUR_NAME,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_EDIT_TEXT,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["ENTER YOUR NAME",              CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["",                            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,[self.my_name,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,20,12,10,MES_NO_FLASH],NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  6*11+2,6*3,   3,3, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_ON,51,12,WINDOW_BUTTON_SIZE_1TEXT,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_CONFIG:
            new_window.update(\
            WINDOW_ID_CONFIG,\
            WINDOW_ID_SUB_SWITCH_TEXT_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_8,\
            ["CONFIGURATION",CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [["SCREEN MODE", CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SCREEN_MODE,OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["WINDOW","FULL SCREEN"]],\
            ["BGM VOLUME",   CLICK_SOUND_OFF,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BGM_VOL,    OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   100,[" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*3+1, STEP4*19,STEP8*3+1],\
            ["SE VOLUME",    CLICK_SOUND_OFF,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SE_VOL,     OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   7,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*4+1, STEP4*19,STEP8*4+1],\
            ["CONTROL TYPE", CLICK_SOUND_ON ,DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_CTRL_TYPE,  OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,1,   5,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*5+1, STEP4*19,STEP8*5+1],\
            ["",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["LANGUAGE",     CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_LANGUAGE,   OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["ENGLISH","JAPANESE"], ],\
            ["BOSS MODE",    CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BOSS_MODE,  OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["HIT BOX",      CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_HIT_BOX,    OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["DEBUG MODE",   CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_DEBUG_MODE, OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   3,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*11+1, STEP4*19,STEP8*11+1],\
            ["INITIALIZE",   CLICK_SOUND_ON ,DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["RETURN",       CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  ["",""]     ]           ],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  160-16,120-12,   2,2, 2,2,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,[[108,4,  IMG2,  144,8,SIZE_8,SIZE_8, 0, 14,3],[40,4,  IMG2,  8,0,SIZE_8,SIZE_8, 0,  1,1]],\
            NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_INITIALIZE:
            new_window.update(\
            WINDOW_ID_INITIALIZE,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "NAME",     CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "ALL",      CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "RETURN",   CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_YELLOW_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  48,58,   3,3, 1,0.7,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_CONFIG_GRAPHICS:
            new_window.update(\
            WINDOW_ID_CONFIG_GRAPHICS,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_LOW_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["GRAPHICS",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["FULL SCREEN",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["PARTICL",     CLICK_SOUND_ON ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  8*8,9*8+5,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_MEDAL_LIST:
            new_window.update(\
            WINDOW_ID_MEDAL_LIST,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_10,\
            [" ",    CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" Lv1",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv2",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv3",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  13*8+17,6*8+3,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            
            self.medal_list,\
            [[30     , 13   ,  IMG2,  176    ,176,SIZE_8,SIZE_8, 13, 1,1,    0,0],\
            [ 30+10*1, 13   ,  IMG2,  176+8*1,176,SIZE_8,SIZE_8, 13, 1,1,    1,0],\
            [ 30+10*2, 13   ,  IMG2,  176+8*2,176,SIZE_8,SIZE_8, 13, 1,1,    2,0],\
            [ 30+10*3, 13   ,  IMG2,  176+8*3,176,SIZE_8,SIZE_8, 13, 1,1,    3,0],\
            
            [ 30     , 13+10,  IMG2,  176+8*4,176,SIZE_8,SIZE_8, 13, 1,1,    0,1],\
            [ 30+10*1, 13+10,  IMG2,  176+8*5,176,SIZE_8,SIZE_8, 13, 1,1,    1,1],\
            [ 30+10*2, 13+10,  IMG2,  176+8*6,176,SIZE_8,SIZE_8, 13, 1,1,    2,1],\
            
            [ 30,      13+20,  IMG2,  176+8*7,176,SIZE_8,SIZE_8, 13, 1,1,    0,2],\
            [ 30+10*1, 13+20,  IMG2,  176+8*8,176,SIZE_8,SIZE_8, 13, 1,1,    1,2],\
            [ 30+10*2, 13+20,  IMG2,  176+8*9,176,SIZE_8,SIZE_8, 13, 1,1,    2,2]],\
            
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            [[100,13,  IMG2, 0,232,SIZE_8,SIZE_8, 0,  8,4],\
            [  90,13,  IMG2, 0,232,SIZE_8,SIZE_8, 0,  8,4],\
            [ 100,23,  IMG2, 0,232,SIZE_8,SIZE_8, 0,  8,4],\
            
            [  92,33,  IMG2, 200,184,SIZE_8,SIZE_8, 13,  1,1],\
            [ 100,33,  IMG2, 208,184,SIZE_8,SIZE_8, 13,  1,1],\
            [ 108,33,  IMG2, 216,184,SIZE_8,SIZE_8, 13,  1,1]],\
            
            NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_ON,27,45,5,42,\
            [[DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,  DISP_OFF,    SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA],\
            [ SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA],\
            [ DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,  DISP_OFF,SKIP_CURSOR_AREA,SKIP_CURSOR_AREA,DISP_OFF        ],\
            [ DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,  DISP_OFF,DISP_OFF,        SKIP_CURSOR_AREA,DISP_OFF        ],\
            [ DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,  DISP_OFF,SIZE3_BUTTON_1,  SIZE3_BUTTON_2,  SIZE3_BUTTON_3]],\
            
            [["","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ " BEFOREHAND 1 SHOT"," BEFOREHAND 2 SHOT"," BEFOREHAND 3 SHOT"," BEFOREHAND 4 SHOT","","","","","",""],\
            [ "  EQUIP L's SHIELD", "  2 OPTION SLOT",  " ONE POINT OF CONCENTRATION",            "",                 "","","","","",""],\
            [ " INFLAMMATION RESISTANCE+",    "RECOVERY OVER TIME",             "TWINKLE!!",            "",                 "","","","","",""]],\
            
            [["","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "事前にショットアイテム①個取得","事前にショットアイテム②個取得","事前にショットアイテム③個取得","事前にショットアイテム④個取得","","","","","",""],\
            [ "　　　エルズシ─ルド装備",      "　　スロットが②個増える",     "一点集中",                   "",                          "","","","","",""],\
            [ "炎耐性＋",                   "時間経過で回復",              "ぴかぴか光る！",              "",                          "","","","","",""]],\
            
            [[0,0,0,0,                                                                                                        0,0,0,0,0,0],\
            [ 0,0,0,0,                                                                                                        0,0,0,0,0,0],\
            [ MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,0,0,0,0,0,0],\
            [ MEDAL_EQUIPMENT_LS_SHIELD,  MEDAL_PLUS_MEDALLION,       MEDAL_CONCENTRATION,         0,                         0,0,0,0,0,0],\
            [ MEDAL_FRAME_RESIST,         MEDAL_RECOVERY_OVER_TIME,   MEDAL_TWINKLE,               0,                         0,0,0,0,0,0]])
        elif id == WINDOW_ID_EXIT:
            new_window.update(\
            WINDOW_ID_EXIT,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["EXIT GAME ??",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",        CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  51,23,   2,1, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_PAUSE_MENU:
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
            WINDOW_BETWEEN_LINE_7,\
            ["BACK TO GAMES",   CLICK_SOUND_ON ,DISP_CENTER,0,0, 7,MES_RED_FLASH],\
            
            [[ "RETURN TITLE",  CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH],\
            [  "RESTART STAGE", CLICK_SOUND_ON ,DISP_CENTER,0,0, 7,MES_NO_FLASH],\
            [  "EXIT GAME",     CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH],\
            [  " ",             CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  92,29,   2,2, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_RETURN_TITLE:
            new_window.update(\
            WINDOW_ID_EXIT,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE ??",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",           CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  51,23,   2,1, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_EQUIPMENT:
            shiplist = self.playing_ship_list
            new_window.update(\
            WINDOW_ID_EQUIPMENT,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_10,\
            ["EQUIPMENT MEDAL",CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" ",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  13*8+17,33,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            shiplist,[self.my_ship_id,DISP_ON,14,24, DISP_ON,24,14, DISP_ON,30,24],\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            self.medal_list,   NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_STATUS:
            new_window.update(\
            WINDOW_ID_STATUS,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["STATUS",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_MONOCHROME_FLASH],\
            
            [["PLAY TIME",     CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "NUMBER OF PLAY",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "TOTAL SCORE",   CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "RETURN",        CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  160-16,120-8,   2,2, 2,2,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,\
            
            [[TIME_COUNTER_TYPE_TOTAL_PLAYTIME  ,145,12 + STEP7 * 0,10,DISP_RIGHT_ALIGN],\
            [ TIME_COUNTER_TYPE_NUMBER_OF_PLAY  ,117,12 + STEP7 * 1, 7,DISP_RIGHT_ALIGN],\
            [ TIME_COUNTER_TYPE_TOTAL_SCORE     , 81,12 + STEP7 * 2, 7,DISP_RIGHT_ALIGN]],\
            
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_ON,27,105,5,102,\
            [[DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF]],\
            
            [["TOTAL PLAY TIME","","","","","","","","",""],\
            [ "NUMBER OF PLAY","","","","","","","","",""],\
            [ "TOTAL SCORE","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "?","","","","","","","","",""],\
            [ "RETURN","","","","","","","","",""]],\
            
            [["累計ゲ─ムプレイタイム","","","","","","","","",""],\
            [ "遊んだ回数","","","","","","","","",""],\
            [ "累計スコア","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "戻る","","","","","","","","",""]],\
            
            [[0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0]],\
            )
        elif id == WINDOW_ID_SELECT_SHIP:
            new_window.update(\
            WINDOW_ID_SELECT_SHIP,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT SHIP",           CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_MONOCHROME_FLASH],\
            
            [["JUSTICE PYTHON",       CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "ELEGANT PERL",         CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "PYTHON FORCE",         CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "CLASSICAL FORTRAN",    CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "AI LOVE LISP",         CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "ECLIPSING ALGOL",      CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "AUNT COBOL",           CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "BEGINNING ADA",        CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "FIRST BASIC",          CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "CUTTER SHARP 2000",    CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "LEGEND ASM",           CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "LAST RUST",            CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "RETURN",               CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  160-8,120-8,   2,2, 2,2,   0,0,    0,0,    0,0,0,0,    0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_ON,2,105,5,103,\
            [[DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF],\
            [DISP_ON,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF,DISP_OFF]],\
            
            [["JUSTICE PYTHON","","","","","","","","",""],\
            [ "ELEGANT practical extraction and report language","","","","","","","","",""],\
            [ "PYTHON4.0(4th.force)","","","","","","","","",""],\
            [ "Classical FORTRAN 1954","","","","","","","","",""],\
            [ "I Love LISP 1958","","","","","","","","",""],\
            [ "Eclipsing Binary ALGOL 1958","","","","","","","","",""],\
            [ "Aunt COBOL more better 1959","","","","","","","","",""],\
            [ "Beginning programmer Ada 1815-1983","","","","","","","","",""],\
            [ "FirstBeginnersAllpurposeSymbolicInstructionCode1964","","","","","","","","",""],\
            [ "Cutter # 2000","","","","","","","","",""],\
            [ "Legend Assembler","","","","","","","","",""],\
            [ "Last Rust","","","","","","","","",""],\
            [ "RETURN","","","","","","","","",""]],\
            
            [["正義を掲げし毒蛇","","","","","","","","",""],\
            [ "高貴なる真珠","","","","","","","","",""],\
            [ "秘められし新たなる毒蛇の力","","","","","","","","",""],\
            [ "古びし算術の理","","","","","","","","",""],\
            [ "愛すべき言葉と唇","","","","","","","","",""],\
            [ "互いに覆い隠せし光の星アルゴルよ","","","","","","","","",""],\
            [ "コボルのおばちゃま・・・・","","","","","","","","",""],\
            [ "始まりはエイダと共に","","","","","","","","",""],\
            [ "初めての言葉は物語の基礎である","","","","","","","","",""],\
            [ "鋭利な刃物は全てを切る","","","","","","","","",""],\
            [ "伝説の組み立てし者よ","","","","","","","","",""],\
            [ "これは最後へと至る道","","","","","","","","",""],\
            [ "戻る","","","","","","","","",""]],\
            
            [[0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0]],\
            )
        elif id == WINDOW_ID_SELECT_YES_NO:
            new_window.update(\
            WINDOW_ID_SELECT_YES_NO,\
            WINDOW_ID_SUB_YES_NO_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            [" ",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["NO",CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["YES",CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  28,22,   2,1, 1,1,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_PRINT_INIT_SCORE:
            new_window.update(\
            WINDOW_ID_PRINT_INIT_SCORE,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_PRINT_TEXT,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  54,18,   3,3, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_PRINT_INIT_NAME:
            new_window.update(\
            WINDOW_ID_PRINT_INIT_NAME,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_PRINT_TEXT,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE", CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["NAME ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  54,18,   3,3, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_PRINT_INIT_ALL:
            new_window.update(\
            WINDOW_ID_PRINT_INIT_ALL,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_PRINT_TEXT,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",          CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["ALL SAVE DATA ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            ox,oy,ox,oy,   0,0,  54,18,   3,3, 1,0.7,   0,0,    0,0,    0,0,0,0,     0,\
            BUTTON_DISP_OFF,0,0,0,\
            BUTTON_DISP_OFF,0,0,0,\
            
            CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
            DISP_OFF,\
            
            NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
            NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
            NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
            NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
            NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,\
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        else:
            return
        
        self.window.append(new_window)                      #ウィンドウを育成する

    #スコアボードウィンドウの育成
    def create_score_board(self,d): #引数dは難易度 difficulty
        func.create_master_flag_list(self) #まず先にフラグ＆データ関連のマスターリスト作成関数を呼び出す
        self.temp_graph_list = [] #一時的なグラフイックリストを初期化する
        func.create_medal_graph_list_for_score_board(self,d,121,12,STEP8) #次にスコアボードに記録された機体群の装備メダルリストを一時的なグラフイックリストとして作製するtemp_graph_listにリストが作成される
        new_window = Window()
        new_window.update(\
        WINDOW_ID_SCORE_BOARD,\
        WINDOW_ID_SUB_RIGHT_LEFT_PAGE_MENU,\
        WINDOW_TYPE_NORMAL,\
        WINDOW_FRAME_NORMAL,\
        WINDOW_BG_BLUE_BACK,\
        WINDOW_PRIORITY_NORMAL,\
        DIR_RIGHT_DOWN,\
        DIR_LEFT_UP,\
        WINDOW_OPEN,\
        WINDOW_BETWEEN_LINE_8,\
        [str(self.game_difficulty_list[d][LIST_DIFFICULTY_TEXT]),CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        
        [[" 1 " + str(self.score_board[d][0][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][0][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][0][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][0][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,10,MES_YELLOW_FLASH],\
        [ " 2 " + str(self.score_board[d][1][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][1][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][1][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][1][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0, 7,MES_NO_FLASH],\
        [ " 3 " + str(self.score_board[d][2][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][2][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][2][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][2][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0, 4,MES_NO_FLASH],\
        [ " 4 " + str(self.score_board[d][3][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][3][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][3][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][3][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 5 " + str(self.score_board[d][4][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][4][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][4][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][4][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 6 " + str(self.score_board[d][5][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][5][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][5][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][5][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 7 " + str(self.score_board[d][6][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][6][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][6][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][6][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 8 " + str(self.score_board[d][7][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][7][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][7][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][7][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 9 " + str(self.score_board[d][8][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][8][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][8][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][8][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ "10 " + str(self.score_board[d][9][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][9][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][9][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][9][LIST_SCORE_BOARD_CLEAR_STAGE])),CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0, 2,MES_NO_FLASH]],\
        
        NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
        0,14,2,14,   152,89,  152,89,   2,1, 2,1,   0,0,    0,0,    0,0,0,0,    0,\
        BUTTON_DISP_OFF,0,0,0,\
        BUTTON_DISP_OFF,0,0,0,\
        
        CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
        DISP_OFF,\
        
        NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
        NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
        NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
        NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
        NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
        NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
        
        self.master_flag_list,self.temp_graph_list,\
        NO_TIME_COUNTER_LIST,\
        NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
        
        COMMENT_FLAG_OFF,0,0,0,0,\
        NO_COMMENT_DISP_FLAG,\
        NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
        NO_ITEM_ID,\
        )
        
        self.window.append(new_window)                   #「SCORE BOARD」を育成する

    #リプレイファイルスロット選択ウィンドウの育成
    def create_replay_data_slot_select(self):
        func.create_master_flag_list(self) #まず先にフラグ＆データ関連のマスターリスト作成関数を呼び出す
        new_window = Window()
        new_window.update(\
        WINDOW_ID_SELECT_FILE_SLOT,\
        WINDOW_ID_SUB_NORMAL_MENU,\
        WINDOW_TYPE_NORMAL,\
        WINDOW_FRAME_NORMAL,\
        WINDOW_BG_BLUE_BACK,\
        WINDOW_PRIORITY_NORMAL,\
        DIR_RIGHT_DOWN,\
        DIR_LEFT_UP,\
        WINDOW_OPEN,\
        WINDOW_BETWEEN_LINE_7,\
        ["SLOT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        
        [["1",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "2",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "3",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "4",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "5",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "6",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "7",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
        
        NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
        63,44,63,44,   0,0,  22,67,      2,1, 2,1,   1,1,    0,0,    0,0,0,0,   0,\
        BUTTON_DISP_OFF,0,0,0,\
        BUTTON_DISP_OFF,0,0,0,\
        
        CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
        DISP_OFF,\
        
        NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
        NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
        NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
        NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
        NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
        NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
        
        self.master_flag_list,\
        NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
        NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
        
        COMMENT_FLAG_OFF,0,0,0,0,\
        NO_COMMENT_DISP_FLAG,\
        NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
        NO_ITEM_ID,\
        )
        
        self.window.append(new_window)                      #「SELECT SLOT」を育成する

    #メダル取得報告ウィンドウの育成
    def create_medal_acquisition_report_window(self,ox,oy,id,wait): #idはメダルidとなります waitはその場に留まる時間(単位はフレーム)
        u,v = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_U],self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_V] #メダルグラフイックの格納先座標u,vを取得
        imgb = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_IMGB] #イメージバンク数も取得
        if self.language == LANGUAGE_ENG: #英語の場合
            expand_width = 0
            between_l = 7
            medal_cmnt_jpn = ""
            get_cmnt_line1_jpn = ""
            get_cmnt_line2_jpn = ""
            medal_cmnt_eng = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_ENG]
            get_cmnt_line1_eng   = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_GET_ENG_LINE1]
            get_cmnt_line2_eng   = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_GET_ENG_LINE2]
            if get_cmnt_line2_eng == "": #取得条件の説明文の2行目が存在しない場合はウィンドウの縦幅の拡張は行わない
                expand_hight = 0
            else:
                expand_hight = 7 #2行目が存在する場合は縦幅を7ドット拡張する
        else: #日本語の場合
            expand_width = 43
            between_l = 13
            medal_cmnt_eng = ""
            get_cmnt_line1_eng = ""
            get_cmnt_line2_eng = ""
            medal_cmnt_jpn = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_JPN]
            get_cmnt_line1_jpn   = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_GET_JPN_LINE1]
            get_cmnt_line2_jpn   = self.medal_graph_and_comment_list[id][LIST_MEDAL_GRP_CMNT_GET_JPN_LINE2]
            if get_cmnt_line2_jpn == "": #取得条件の説明文の2行目が存在しない場合はウィンドウの縦幅の拡張は行わない
                expand_hight = 10
            else:
                expand_hight = 20 #2行目が存在する場合は縦幅を7ドット拡張する
            
        new_window = Window()
        new_window.update(\
        WINDOW_ID_MEDAL_ACQUISITION_REPORT,\
        WINDOW_ID_SUB_NORMAL_MENU,\
        WINDOW_TYPE_NORMAL,\
        WINDOW_FRAME_NORMAL,\
        WINDOW_BG_BLUE_BACK,\
        WINDOW_PRIORITY_NORMAL,\
        DIR_RIGHT_DOWN,\
        DIR_LEFT_UP,\
        WINDOW_OPEN,\
        between_l,\
        ["MEDAL GET !!",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
        
        [[medal_cmnt_eng,       CLICK_SOUND_ON ,DISP_CENTER,0, 7,10,MES_NO_FLASH],\
        [ get_cmnt_line1_eng,   CLICK_SOUND_ON ,DISP_CENTER,0,14, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_eng,   CLICK_SOUND_ON ,DISP_CENTER,0,14, 7,MES_NO_FLASH]],\
        
        [[medal_cmnt_jpn,       CLICK_SOUND_ON ,DISP_CENTER,9, 0,10,MES_NO_FLASH],\
        [ get_cmnt_line1_jpn,   CLICK_SOUND_ON ,DISP_CENTER,9, 7, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_jpn,   CLICK_SOUND_ON ,DISP_CENTER,9, 7, 7,MES_NO_FLASH]],\
        
        NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
        ox - expand_width // 2,oy - expand_hight,ox - expand_width // 2,oy - expand_hight,   0,0,  110 + expand_width,30 + expand_hight,   2,1, 1,0.4,   0,0,    0,0,    0,0.01,0,1.04,   wait,\
        BUTTON_DISP_OFF,0,0,0,\
        BUTTON_DISP_OFF,0,0,0,\
        
        CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
        DISP_OFF,\
        
        NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
        NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
        NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
        NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
        NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
        NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
        
        self.master_flag_list,\
        [[9,4,imgb,u,v,8,8,13,1,1]],\
        NO_TIME_COUNTER_LIST,\
        NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
        
        COMMENT_FLAG_OFF,0,0,0,0,\
        NO_COMMENT_DISP_FLAG,\
        NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
        NO_ITEM_ID,\
        )
        self.window.append(new_window)                      #ウィンドウを育成する

    #実績(アチーブメント)取得報告ウィンドウの育成
    def create_achievement_acquisition_report_window(self,ox,oy,id,priority,wait): #idは実績idとなります priorityはウィンドウ描画優先度(通常はWINDOW_PRIORITY_NORMAL),waitはその場に留まる時間(単位はフレーム) ox,oyはオフセット値(デフォルトは右下に表示される)
        u,v  = self.achievement_list[id][LIST_ACHIEVE_GRP_X],self.achievement_list[id][LIST_ACHIEVE_GRP_Y] #実績グラフイックの格納先座標u,vを取得
        imgb = self.achievement_list[id][LIST_ACHIEVE_IMGB] #イメージバンク数も取得
        #ゲームプレイ中に実績解除ダイアログを出すので英語オンリーで行きます（日本語フォントデカいからねぇ・・・しかたない画面が塞がっちゃうし)
        between_l = 7
        achieve_cmnt_eng       = self.achievement_list[id][LIST_ACHIEVE_COMMENT_ENG1]
        
        new_window = Window()
        new_window.update(\
        WINDOW_ID_ACHIEVEMENT_ACQUISITION_REPORT,\
        WINDOW_ID_SUB_NORMAL_MENU,\
        WINDOW_TYPE_BANNER,\
        WINDOW_FRAME_NONE,\
        WINDOW_BG_BLUE_BACK,\
        priority,\
        DIR_LEFT_UP,\
        DIR_RIGHT_DOWN,\
        WINDOW_OPEN,\
        between_l,\
        [achieve_cmnt_eng,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,-6,-7,7,MES_NO_FLASH],\
        
        NO_ITEM_TEXT,NO_ITEM_KANJI_TEXT,\
        NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
        160 - len(achieve_cmnt_eng) * 4 + ox,115 + oy,   160 - len(achieve_cmnt_eng) * 4,115 + oy,   0,0,len(achieve_cmnt_eng) * 4,6,   1,1, 1,0.4,   0,0,    0,0,    0.02,0.04,1.1,1.04,   wait,\
        BUTTON_DISP_OFF,0,0,0,\
        BUTTON_DISP_OFF,0,0,0,\
        
        CURSOR_MOVE_SE_NORMAL,CURSOR_PUSH_SE_NORMAL,CURSOR_OK_SE_NORMAL,CURSOR_CANCEL_SE_NORMAL,CURSOR_BOUNCE_SE_NORMAL,\
        DISP_OFF,\
        
        NO_SHIP_LIST,      NO_SHIP_MEDAL_LIST,\
        NO_WEAPON_LIST,    NO_WEAPON_GRAPH_LIST,\
        NO_SUB_WEAPON_LIST,NO_SUB_WEAPON_GRAPH_LIST,\
        NO_MISSILE_LIST,   NO_MISSILE_GRAPH_LIST,\
        NO_MEDAL_LIST,     NO_MEDAL_GRAPH_LIST,\
        NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
        
        self.master_flag_list,\
        NO_GRAPH_LIST,\
        NO_TIME_COUNTER_LIST,\
        NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
        
        COMMENT_FLAG_OFF,0,0,0,0,\
        NO_COMMENT_DISP_FLAG,\
        NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
        NO_ITEM_ID,\
        )
        self.window.append(new_window)                      #ウィンドウを育成する

    #メインメニューウィンドウを左にずらす
    def move_left_main_menu_window(self):
        i = func.search_window_id(self,WINDOW_ID_MAIN_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dx = 44 - 30
        self.window[i].vx = -4            #メインメニューウィンドウを左にずらしてやる
        self.window[i].vx_accel = 0.8

    #メインメニューウィンドウを右にずらす
    def move_right_main_menu_window(self):
        i = func.search_window_id(self,WINDOW_ID_MAIN_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dx = 44
        self.window[i].vx = 3.9            #メインメニューウィンドウを右にずらしてやる
        self.window[i].vx_accel = 0.8

    #ポーズメニューウィンドウを下にずらす
    def move_down_pause_menu(self):
        i = func.search_window_id(self,WINDOW_ID_PAUSE_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dy = 109
        self.window[i].vy = 9           #ポーズメニューウィンドウを下にずらしてやる
        self.window[i].vy_accel = 0.9

    #ポーズメニューウィンドウを上にずらす
    def move_up_pause_menu(self):
        i = func.search_window_id(self,WINDOW_ID_PAUSE_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dy = 70
        self.window[i].vy = -9            #ポーズメニューウィンドウを上にずらしてやる
        self.window[i].vy_accel = 0.9

    #メダルの取得判定をする関数
    def judge_medal_acquisition(self):
        if func.search_window_id(self,WINDOW_ID_MEDAL_ACQUISITION_REPORT) != -1: #メダル取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 180
        #プレイ時間で判定するメダルタイプ
        if self.total_game_playtime_seconds >= 10 * 60 and self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム10分以上なら「事前1ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_1SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_game_playtime_seconds >= 180 * 60 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム180分以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #トータルスコアで判定するタイプ
        elif self.total_score >= 2000 and self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア2000点以上なら「事前3ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_3SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_score >= 10000 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア10000点以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #ボスを倒した回数で判定するタイプ
        elif self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] == MEDAL_NO_SLOT: #1面ボスを1回以上破壊で「事前2ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_2SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #プレイ回数で判定するタイプ
        elif self.number_of_play >= 20 and self.medal_list[MEDAL_FRAME_RESIST - 1] == MEDAL_NO_SLOT: #トータルゲームプレイ回数が20以上なら「炎耐性」を取得
            self.medal_list[MEDAL_FRAME_RESIST - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_FRAME_RESIST,wait)  #メダル取得報告ウィンドウを育成
        
        #スコアスターの最大得点倍率で判定するタイプ
        elif self.max_score_star_magnification >= 7 and self.medal_list[MEDAL_PLUS_MEDALLION - 1] == MEDAL_NO_SLOT: #スコアスター最大得点倍率が7以上なら「メダル枠２増設」をゲット！
            self.medal_list[MEDAL_PLUS_MEDALLION - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            update_window.create_medal_acquisition_report_window(self,20,90,MEDAL_PLUS_MEDALLION,wait)  #メダル取得報告ウィンドウを育成

    #実績(アチーブメント)の取得判定をする関数
    def judge_achievement_acquisition(self):
        if func.search_window_id(self,WINDOW_ID_ACHIEVEMENT_ACQUISITION_REPORT) != -1: #実績取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 360
        #出撃回数(遊んだ回数)で判別するタイプ
        if self.number_of_play == 0 and self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED: #プレイ回数が0で出撃したのならFIRST CAMPAIGN「初陣」実績取得
            self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CAMPAIGN,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #ボスを倒した回数で判定するタイプ
        #1面ボスを1回以上破壊で「1面ボス撃破」実績取得
        if self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE01_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #2面ボスを1回以上破壊で「2面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ADVANCE_BASE] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE02_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #3面ボスを1回以上破壊で「3面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_VOLCANIC_BELT] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE03_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #4面ボスを1回以上破壊で「4面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_NIGHT_SKYSCRAPER] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE04_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #5面ボスを1回以上破壊で「5面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_AMPHIBIOUS_ASSAULT_SHIP] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE05_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #6面ボスを1回以上破壊で「6面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_DEEP_SEA_TRENCH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE06_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #7面ボスを1回以上破壊で「7面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_INTERMEDIATE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE07_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #8面ボスを1回以上破壊で「8面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ESCAPE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE08_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #9面ボスを1回以上破壊で「9面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_BOSS_RUSH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE09_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #ボスの累計撃破数で判定するタイプ
        #ボス累計10体撃破！
        if func.total_defeat_boss_num(self) >= 10 and self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_BOSS_10TIME,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #パワーカプセルの取得累計数で取得するタイプの実績
        #ショットカプセル10個取得
        wait = 360
        if self.get_shot_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル50個取得
        elif self.get_shot_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル100個取得
        elif self.get_shot_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル200個取得
        elif self.get_shot_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル500個取得
        elif self.get_shot_pow_num >= 500 and self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_500_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル1000個取得
        elif self.get_shot_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2000個取得
        elif self.get_shot_pow_num >= 2000 and self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2465個取得
        elif self.get_shot_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #ミサイルカプセル10個取得
        elif self.get_missile_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル50個取得
        elif self.get_missile_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル100個取得
        elif self.get_missile_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル200個取得
        elif self.get_missile_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル400個取得
        elif self.get_missile_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル765個取得
        elif self.get_missile_pow_num >= 765 and self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_765_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル1000個取得
        elif self.get_missile_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル2465個取得
        elif self.get_missile_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #シールドカプセル10個取得
        elif self.get_shield_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル50個取得
        elif self.get_shield_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル100個取得
        elif self.get_shield_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル200個取得
        elif self.get_shield_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル400個取得
        elif self.get_shield_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル530個取得
        elif self.get_shield_pow_num >= 530 and self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_530_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #初めてクローゲットで「はじめてのクロー」実績取得
        elif self.get_claw_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CLAW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル10個取得
        elif self.get_claw_num >= 10 and self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル20個取得
        elif self.get_claw_num >= 20 and self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_20_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル50個取得
        elif self.get_claw_num >= 50 and self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル100個取得
        elif self.get_claw_num >= 100 and self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        
        #武器レベルで判別して取得するタイプの実績
        #初めて5WAYバルカンショットを体験
        wait = 360
        if self.shot_level == SHOT_LV3_5WAY_VULCAN_SHOT and self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_5WAY_SHOT,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてレーザーを体験
        elif self.shot_level == SHOT_LV4_LASER and self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてツインレーザーを体験
        elif self.shot_level == SHOT_LV5_TWIN_LASER and self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_TWIN_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてシャワーレーザーを体験
        elif self.shot_level == SHOT_LV6_3WAY_LASER and self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_SHOWER_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてウェーブカッターを体験
        elif self.shot_level == SHOT_LV7_WAVE_CUTTER_LV1 and self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めて最大ウェーブカッターを体験
        elif self.shot_level == SHOT_LV10_WAVE_CUTTER_LV4 and self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_MAX_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #特殊条件を満たし各工程でのフラグが立ったら取得するタイプの実績
        #初めてパワーカプセルゲットで「はじめてのパワーカプセル回収成功！」実績取得
        wait = 360
        if self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            if self.get_shot_pow_num >= 1 or self.get_missile_pow_num >= 1 or self.get_shield_pow_num >= 1:
                self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
                pyxel.play(0,26) #実績取得音を鳴らす
                update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_POW_UP,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
                return
        
        #初めてトライアングルアイテム取得で「初めてトライアングルアイテム」実績取得
        if self.get_triangle_pow_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        #早回実績取得用フラグが立っているのならば「早回し発生実績」を取得
        #初めての早回し体験
        if self.fast_forward_flag == FLAG_ON and self.fast_forward_num == 1-1 and self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し8回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 8-1 and self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_8_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し16回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 16-1 and self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_16_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し32回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 32-1 and self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_32_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し64回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 64-1 and self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_64_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し128回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 128-1 and self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_128_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し256回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 256-1 and self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_256_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し512回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 512-1 and self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_512_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し1024回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 1024-1 and self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1024_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        
        #主にステージクリア(ボス破壊後）にフラグが立ち、そのフラグを見ることによって取得判別するタイプの実績(複数の実績が同時に解除される可能性あり)
        up_shift_line = 0 #上にシフトしていく行数を初期化
        #「ステージ中ノーダメージでクリア」フラグオンで実績取得
        if  self.no_damage_stage_clear_flag == FLAG_ON:
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR ,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60) #実績取得報告ウィンドウを育成
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR][LIST_ACHIEVE_FLAG]  = RESULTS_ACQUISITION
            self.no_damage_stage_clear_flag = FLAG_OFF  #ノーダメージでボスステージクリアフラグを下げる
            up_shift_line += 1
        #「ノーダメージでボス破壊」フラグオンで実績取得
        if self.no_damage_destroy_boss_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.no_damage_destroy_boss_flag = FLAG_OFF #ノーダメージでボス破壊フラグを下げる
            up_shift_line += 1
        #残りシールド１でギリギリクリアフラグオンで実績取得
        if self.endurance_one_cleared_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_ENDURANCE_ONE_CLEARED][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_ENDURANCE_ONE_CLEARED,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.endurance_one_cleared_flag = FLAG_OFF #残りシールド１でギリギリクリアフラグを下げる
            up_shift_line += 1
        #ボスを瞬殺したフラグオンで実績取得
        if self.boss_instank_kill_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_BOSS_INSTANK_KILL][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_BOSS_INSTANK_KILL,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.boss_instank_kill_flag = FLAG_OFF #ボスを瞬殺したフラグを下げる
            up_shift_line += 1
        #ボスのパーツをすべて破壊したフラグオンで実績取得
        if self.destroy_all_boss_parts_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            update_window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.destroy_all_boss_parts_flag = FLAG_OFF #ボスのパーツをすべて破壊したフラグを下げる
            up_shift_line += 1

    #ウィンドウのはみだしチェック（表示座標が完全に画面外になったのなら消去する）
    def clip_window(self):
        window_count = len(self.window)#ウィンドウの数を数える
        rect_ax,rect_ay = 0,0
        rect_aw,rect_ah = WINDOW_W,WINDOW_H
        for i in reversed(range(window_count)):
            #ゲームの画面(0,0)-(160,120)とウィンドウ(wx1,wy1)-(wx2,wy2)の2つの矩形の衝突判定を行い
            #衝突して一部が重なっている→ウィンドウのどこかの部分を表示しないといけないのでウィンドウは生存させる
            #衝突していない→お互いに干渉していないので画面にウィンドウが表示されることは無い→ウィンドウを消去する
            rect_bx,rect_by = self.window[i].posx,self.window[i].posy
            rect_bw,rect_bh = self.window[i].open_width,self.window[i].open_height
            
            #矩形A(ゲーム画面)と矩形B(ウィンドウ)の衝突判定を行う関数の呼び出し
            if func.collision_rect_rect(self,rect_ax,rect_ay,rect_aw,rect_ah,rect_bx,rect_by,rect_bw,rect_bh) == False:
                del self.window[i] #ウィンドウが画面外に存在するとき(2つの矩形が衝突していないとき)はインスタンスを破棄する(ウィンドウ消滅)

    #現在どのウィンドウがもつインデックス値が最前面にあるのか調べあげ,アクティブウィンドウインデックス値に登録し更新する
    def active_window(self):
        i = func.search_window_id(self,self.active_window_id) #アクティブなウィンドウIDを元にインデックス値を求める関数の呼び出し
        self.active_window_index = i           #アクティブになっているウィンドウのインデックスナンバー(i)を代入

    #セレクトカーソルの更新
    def select_cursor(self):
        # 上入力されたら  y座標を  -7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
            self.cursor_move_data = PAD_UP
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y-1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y -= self.cursor_step_y#y座標をcursor_step_y減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y -= self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            break #カーソルの移動先が見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    for ty in range(self.cursor_item_y): #現在のカーソルy座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y-(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y-(ty+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #上方向がスキップエリアで尚且つ調べる対象のitem_yが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_y -= self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)減算してカーソルを上に移動させる
                            self.cursor_item_y -= (ty+1) #現在指し示しているアイテムナンバーをty+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
            
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュを鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character += 1 #文字のアスキーコードを1増やす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        # 下入力されたら  y座標を  +7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
            self.cursor_move_data = PAD_DOWN
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y+1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y += self.cursor_step_y#y座標をcursor_step_y加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            continue #選択すべき項目テキストは見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            break #選択すべき項目テキストが見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(self.cursor_max_item_y - self.cursor_item_y): #(y軸アイテム最大値-現在のカーソルy座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y+(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y+(ty+1) > self.cursor_max_item_y:
                                break #下方向がスキップエリアで尚且つ調べる対象がmax_item_yより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)加算してカーソルを下に移動させる
                            self.cursor_item_y += (ty+1) #現在指し示しているアイテムナンバーをty+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character -= 1 #文字のアスキーコードを1減らす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(いみゅーたぶる変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        #右入力されたらcursor_pageを +1する
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_RIGHTSHOULDER):
            self.cursor_move_data = PAD_RIGHT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page += 1 #ページ数インクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page > self.cursor_page_max: #カーソルページ数が最大ページ数を超えたのなら
                    self.cursor_page = 0                    #ページ数は0にする
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数でないのなら右方向にカーソルは移動できるので・・
                    if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                        pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    self.cursor_x += self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）加算してカーソルを右に移動させる
                    self.cursor_item_x += 1 #現在指示しているアイテムナンバーを1増やす
                else:
                    if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーが最大項目数でないのなら右方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for tx in range(self.cursor_max_item_x - self.cursor_item_x): #(x軸アイテム最大値-現在のカーソルx座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x+(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x+(tx+1) > self.cursor_max_item_x:
                                break #右方向がスキップエリアで尚且つ調べる対象がmax_item_xより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_x += self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)加算してカーソルを右に移動させる
                            self.cursor_item_x += (tx+1) #現在指し示しているアイテムナンバーをtx+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_NUM:#操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k < self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MAX_NUMより小さい時は
                        k += 1 #オブジェクトの数値をインクリメント
                        if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                            pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                            pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        func.restore_master_flag_list(self)
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
                        update_se.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)
        
        #左入力されたらcursor_pageを -1する
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_LEFTSHOULDER):
            self.cursor_move_data = PAD_LEFT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page -= 1 #ページ数デクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page < 0:                    #カーソルページ数が0より小さくなったのなら
                    self.cursor_page = self.cursor_page_max                    #ページ数はmaxにする
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーx軸方向が0以外ならでないのなら左方向にカーソルは移動できるので・・
                    if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                        pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    self.cursor_x -= self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）減算してカーソルを左に移動させる
                    self.cursor_item_x -= 1#現在指示しているアイテムナンバーを1減らす
                else:
                    if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーが一番左の項目の0以外なら左方向にカーソルは移動できるので・・・
                    for tx in range(self.cursor_item_x): #現在のカーソルx座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x-(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x-(tx+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #左方向がスキップエリアで尚且つ調べる対象のitem_xが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_x -= self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)減算してカーソルを左に移動させる
                            self.cursor_item_x -= (tx+1) #現在指し示しているアイテムナンバーをtx+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE]  == OPE_OBJ_TYPE_NUM: #操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k > self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MIN_NUMより大きい時は
                        k -= 1 #オブジェクトの数値をデクリメント
                        if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                            pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_CLICK_SE_FLAG] == CLICK_SOUND_ON: #カーソル移動ボタン音がONならば
                            pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        func.restore_master_flag_list(self)
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
                        update_se.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)
        
        #ABXYスペースキーが押された場合の処理
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_B) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_Y):
            self.cursor_move_data = PAD_A
            self.cursor_decision_item_x = self.cursor_item_x #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_xに代入！
            self.cursor_decision_item_y = self.cursor_item_y #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_yに代入！
            if self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_ON_OFF:#操作テキストオブジェクトは「ON」「OFF」の二つから選ぶシンプルなタイプの時は
                    if k == 0: #k=0(off)の時はk=1(on)に、k=1(on)の時はk=0(off)にする
                        k = 1
                    else:
                        k = 0
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルok音を鳴らす
