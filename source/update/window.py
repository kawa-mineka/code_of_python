###########################################################
#  windowクラス                                           #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にウィンドウの更新を行う関数(メソッド？）ですよ～♪        #
#  あとウィンドウシステムで使用するセレクトカーソルとかも      #
# 2022 04/05からファイル分割してモジュールとして運用開始      #
###########################################################
import math               #三角関数などを使用したいのでインポートぉぉおお！
from random import random #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel              #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン

from const.const       import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from const.const_window      import * #主にウィンドウクラスで使用する定数定義の読み込み

from common.func         import * #汎用性のある関数群のモジュールの読み込み
from update.sound import * #CONFIGでSEボリュームを変化させたときSEを鳴らすために使用します
from update.btn   import * #カーソル移動時の方向パッド入力(キーリピート付き)を調べる時に使用します

class window:
    def __init__(self):
        None

    #ウィンドウの更新
    def window(self):
        """
        ウィンドウの更新
        """
        window_count = len(self.window)
        for i in range(window_count):
            if   self.window[i].window_status == WINDOW_OPEN or self.window[i].window_status == WINDOW_WRITE_MESSAGE:     #ステータスが「オープン」の時は・・・・・・・・・・・・
                if self.window[i].width < self.window[i].open_width:#widthをopen_widthの数値になるまで増加させていく
                    self.window[i].width += self.window[i].change_x * self.window[i].open_speed
                
                if self.window[i].height < self.window[i].open_height:#heightをopen_heightの数値になるまで増加させていく
                    self.window[i].height += self.window[i].change_y * self.window[i].open_speed
                
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
                
                #ウィンドウの下地が透明または半透明の時は「背景の星を再描画するエリアの範囲」の更新を行う
                if self.window[i].window_bg == WINDOW_BG_TRANSLUCENT or self.window[i].window_bg == WINDOW_BG_LOW_TRANSLUCENT:
                    if func.search_window_id_star_redraw(self,self.window[i].window_id) == -1: #背景の星を再描画するエリアの範囲リストに現在のウィンドウIDが存在しないのなら新規作成する
                        new_star_redraw = Redraw_star_area()
                        new_star_redraw.update(self.window[i].window_id,self.window[i].posx,self.window[i].posy,self.window[i].width,self.window[i].height,self.window[i].window_priority)
                        self.redraw_star_area.append(new_star_redraw) #「背景の星を再描画するエリアの範囲」を育成する
                        # print("star_redraw_window_num = " + str(len(self.redraw_star_area)))
                    
                    j = func.search_window_id_star_redraw(self,self.window[i].window_id) #jにwindow_idに対応したredraw_star_areaのインデックス値が入る
                    if j != -1: #存在する時だけ更新する
                        self.redraw_star_area[j].posx, self.redraw_star_area[j].posy   = self.window[i].posx, self.window[i].posy
                        self.redraw_star_area[j].width,self.redraw_star_area[j].height = self.window[i].width-30,self.window[i].height
                
            else:
                self.window[i].wait_count -= 1  #カウンターをデクリメント
            
            # #スクロールテキストに何かテキストが入っている時はスクロールドットカウンタを増やしていく
            # if self.window[i].scroll_text  != "":
            #     if self.window[i].text_scroll_speed != 0: #スクロールスピードが0の時は何もしない(0で割り算をしてエラーになっちゃう為)
            #         if int(pyxel.frame_count % self.window[i].text_scroll_speed) == 0:
            #             self.window[i].text_disp_scrolled_dot += 1  #スクロールテキストのスクロールしたドットカウンタを1増やしていく

    #各種ウィンドウの育成             id=windowクラスの window_idに入っている数値 ox,oy=ウィンドウ作成座標のオフセット値
    def create(self,id,ox,oy):
        """
        各種ウィンドウの育成
        
        id=windowクラスの window_idに入っている数値(それぞれのウィンドウに付けられた個別ウィンドウID)
        ox,oy=ウィンドウ作成座標のオフセット値
        """
        func.create_master_flag_list(self) #まず先にフラグ＆データ関連のマスターリスト作成関数を呼び出す
        new_window = Window()
        if   id == WINDOW_ID_MAIN_MENU:                 #メインメニューウィンドウ
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
            0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,   0,0,0,0,\
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
            
            NO_VECTOR_GRP,\
            # [[LIST_WINDOW_VECTOR_GRP_LINE,60,60,100,90,pyxel.COLOR_WHITE],[LIST_WINDOW_VECTOR_GRP_BOXF,6,6,40,30,pyxel.COLOR_YELLOW],[LIST_WINDOW_VECTOR_GRP_CIRCLE,6,6,10,pyxel.COLOR_RED],[LIST_WINDOW_VECTOR_GRP_CIRCLEF,26,26,20,pyxel.COLOR_GRAY],[LIST_WINDOW_VECTOR_GRP_TRI,0,0, 80,10, 40,100,pyxel.COLOR_RED ]],\
            
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
        elif id == WINDOW_ID_SELECT_STAGE_MENU:         #ステージセレクトウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "4",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "5",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "6",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "7",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "8",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "9",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "A",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_SELECT_LOOP_MENU:          #周回数セレクトウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_BOSS_MODE_MENU:            #ボスモードON/OFFウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [[".",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ ".",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_HITBOX_MENU:               #当たり判定表示ON/OFFウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [[" ",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_SELECT_DIFFICULTY:         #難易度選択ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["DIFFICULTY",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [[" ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY EASY",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "EASY",     DISP_CENTER,1, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "NORMAL",   DISP_CENTER,2, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "HARD",     DISP_CENTER,3, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY HARD",DISP_CENTER,4, 0,0, 7,10],\
            [ " ",        CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "INSAME",   DISP_CENTER,5, 0,0, 7,10]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_GAME_OVER_RETURN:          #ゲームオーバー後タイトルへ戻るウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE?",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",      CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["SAVE & RETURN",CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_GAME_OVER_RETURN_NO_SAVE:  #ゲームオーバー後タイトルへ戻るウィンドウ(リプレイ保存付き)
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE?",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",      CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_INPUT_YOUR_NAME:           #名前入力ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["ENTER YOUR NAME",              CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["",                            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,[self.my_name,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,20,12,10,MES_NO_FLASH],NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_CONFIG:                    #コンフィグウィンドウ
            new_window.update(\
            WINDOW_ID_CONFIG,\
            WINDOW_ID_SUB_SWITCH_TEXT_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NORMAL,\
            WINDOW_BG_TRANSLUCENT,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_8,\
            ["CONFIGURATION",CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [["SCREEN MODE", CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SCREEN_MODE,OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["WINDOW","FULL SCREEN"]],\
            ["BGM VOLUME",   CLICK_SOUND_OFF,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BGM_VOL,    OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   100,[" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*3+1, STEP4*19,STEP8*3+1],\
            ["SE VOLUME",    CLICK_SOUND_OFF,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SE_VOL,     OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   7,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*4+1, STEP4*19,STEP8*4+1],\
            ["JOYPAD ASSIGN",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["LANGUAGE",     CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_LANGUAGE,   OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["ENGLISH","JAPANESE"], ],\
            ["BOSS MODE",    CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BOSS_MODE,  OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["HIT BOX",      CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_HIT_BOX,    OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["DEBUG MODE",   CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_DEBUG_MODE, OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   3,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*11+1, STEP4*19,STEP8*11+1],\
            ["INITIALIZE",   CLICK_SOUND_ON ,DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["RETURN",       CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  ["",""]     ]           ],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
            NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,[[108,4,  IMG2,  144,8,SIZE_8,SIZE_8, 0, 14,3],[40,4,  IMG2,  8,0,SIZE_8,SIZE_8, 0,  1,1]],\
            NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_INITIALIZE:                #初期化ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "NAME",     CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "ALL",      CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "RETURN",   CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_YELLOW_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_CONFIG_GRAPHICS:           #グラフイックス設定ウィンドウ(現時点では未使用)
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
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
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_MEDAL_LIST:                #メダルリストウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_10,\
            [" ",    CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" Lv1",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv2",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv3",CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
            
            NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
            [ "事前にショットアイテム１個取得","事前にショットアイテム２個取得","事前にショットアイテム３個取得","事前にショットアイテム４個取得","","","","","",""],\
            [ "　　　エルズシールド装備",      "　　スロットが２個増える",     "一点集中",                   "",                          "","","","","",""],\
            [ "炎耐性＋",                   "時間経過で回復",              "ぴかぴか光る！",              "",                          "","","","","",""]],\
            
            [[0,0,0,0,                                                                                                        0,0,0,0,0,0],\
            [ 0,0,0,0,                                                                                                        0,0,0,0,0,0],\
            [ MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,0,0,0,0,0,0],\
            [ MEDAL_EQUIPMENT_LS_SHIELD,  MEDAL_PLUS_MEDALLION,       MEDAL_CONCENTRATION,         0,                         0,0,0,0,0,0],\
            [ MEDAL_FRAME_RESIST,         MEDAL_RECOVERY_OVER_TIME,   MEDAL_TWINKLE,               0,                         0,0,0,0,0,0]])
        elif id == WINDOW_ID_EXIT:                      #退出終了ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["EXIT GAME ??",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO",         CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",        CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_PAUSE_MENU:                #ポーズメニューウィンドウ
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
        elif id == WINDOW_ID_RETURN_TITLE:              #タイトルへ戻るウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["RETURN TITLE ??",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO",            CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",           CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_EQUIPMENT:                 #装備ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_10,\
            ["EQUIPMENT MEDAL",CLICK_SOUND_ON ,DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" ",             CLICK_SOUND_ON ,DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
            NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,
            NO_GRAPH_LIST,NO_TIME_COUNTER_LIST,\
            NO_EQUIP_MEDAL_GRAPH_LIST,NO_EQUIP_MEDAL_COMMENT_LIST,\
            
            COMMENT_FLAG_OFF,0,0,0,0,\
            NO_COMMENT_DISP_FLAG,\
            NO_COMMENT_LIST_ENG,NO_COMMENT_LIST_JPN,\
            NO_ITEM_ID,\
            )
        elif id == WINDOW_ID_STATUS:                    #ステータス表示ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
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
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
            NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
            
            [["累計ゲームプレイタイム","","","","","","","","",""],\
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
        elif id == WINDOW_ID_SELECT_SHIP:               #自機選択ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
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
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
            NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
        elif id == WINDOW_ID_SELECT_YES_NO:             #はい/いいえ選択ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            [" ",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["NO",CLICK_SOUND_ON ,DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["YES",CLICK_SOUND_ON ,DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_PRINT_INIT_SCORE:          #スコア初期化ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_PRINT_INIT_NAME:           #名前初期化ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE", CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["NAME ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_PRINT_INIT_ALL:            #全てを初期化ウィンドウ
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
            0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["INITIALIZE",          CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["ALL SAVE DATA ?",    CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        elif id == WINDOW_ID_JOYPAD_ASSIGN:             #ジョイパッドボタン割り当て設定ウィンドウ
            new_window.update(\
            WINDOW_ID_MAIN_MENU,\
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
            ["JOYPAD ASSIGN"        ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [["FIRE - SUB WEAPON"   ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "MISSILE"             ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "MAIN WEAPON CHANGE"  ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "SUB WEAPON CHANGE"   ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "SPEED"               ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ ""                    ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "PAUSE"               ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "CLAW STYLE"          ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "CLAW DISTANCE"       ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ ""                    ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,3,MES_NO_FLASH],\
            [ "DEFAULT"             ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,3,MES_NO_FLASH],\
            [ "ALL CLEAR"           ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_NO_FLASH],\
            [ "SAVE - RETURN"       ,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,11,0,7,MES_YELLOW_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
            
            [[LIST_WINDOW_VECTOR_GRP_LINE  ,XBJ_X001,XBJ_Y001 ,XBJ_X002,XBJ_Y002 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X002,XBJ_Y002 ,XBJ_X003,XBJ_Y003 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X003,XBJ_Y003 ,XBJ_X004,XBJ_Y004 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X004,XBJ_Y004 ,XBJ_X005,XBJ_Y005 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X005,XBJ_Y005 ,XBJ_X006,XBJ_Y006 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X006,XBJ_Y006 ,XBJ_X007,XBJ_Y007 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X007,XBJ_Y007 ,XBJ_X008,XBJ_Y008 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X003,XBJ_Y003 ,XBJ_X009,XBJ_Y009 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X009,XBJ_Y009 ,XBJ_X010,XBJ_Y010 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X010,XBJ_Y010 ,XBJ_X008,XBJ_Y008 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X008,XBJ_Y008 ,XBJ_X011,XBJ_Y011 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X011,XBJ_Y011 ,XBJ_X012,XBJ_Y012 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X012,XBJ_Y012 ,XBJ_X013,XBJ_Y013 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X013,XBJ_Y013 ,XBJ_X014,XBJ_Y014 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X014,XBJ_Y014 ,XBJ_X015,XBJ_Y015 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X015,XBJ_Y015 ,XBJ_X016,XBJ_Y016 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X016,XBJ_Y016 ,XBJ_X017,XBJ_Y017 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X017,XBJ_Y017 ,XBJ_X018,XBJ_Y018 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X018,XBJ_Y018 ,XBJ_X019,XBJ_Y019 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X019,XBJ_Y019 ,XBJ_X020,XBJ_Y020 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X020,XBJ_Y020 ,XBJ_X021,XBJ_Y021 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X021,XBJ_Y021 ,XBJ_X022,XBJ_Y022 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X022,XBJ_Y022 ,XBJ_X023,XBJ_Y023 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X023,XBJ_Y023 ,XBJ_X024,XBJ_Y024 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X024,XBJ_Y024 ,XBJ_X025,XBJ_Y025 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X025,XBJ_Y025 ,XBJ_X026,XBJ_Y026 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X026,XBJ_Y026 ,XBJ_X027,XBJ_Y027 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X027,XBJ_Y027 ,XBJ_X028,XBJ_Y028 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X028,XBJ_Y028 ,XBJ_X029,XBJ_Y029 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X029,XBJ_Y029 ,XBJ_X030,XBJ_Y030 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X030,XBJ_Y030 ,XBJ_X031,XBJ_Y031 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X031,XBJ_Y031 ,XBJ_X032,XBJ_Y032 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X032,XBJ_Y032 ,XBJ_X033,XBJ_Y033 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X033,XBJ_Y033 ,XBJ_X034,XBJ_Y034 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X034,XBJ_Y034 ,XBJ_X035,XBJ_Y035 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X035,XBJ_Y035 ,XBJ_X036,XBJ_Y036 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X036,XBJ_Y036 ,XBJ_X037,XBJ_Y037 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X037,XBJ_Y037 ,XBJ_X038,XBJ_Y038 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X038,XBJ_Y038 ,XBJ_X039,XBJ_Y039 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X039,XBJ_Y039 ,XBJ_X040,XBJ_Y040 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X040,XBJ_Y040 ,XBJ_X041,XBJ_Y041 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X041,XBJ_Y041 ,XBJ_X042,XBJ_Y042 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X042,XBJ_Y042 ,XBJ_X043,XBJ_Y043 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X043,XBJ_Y043 ,XBJ_X044,XBJ_Y044 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X044,XBJ_Y044 ,XBJ_X045,XBJ_Y045 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X045,XBJ_Y045 ,XBJ_X046,XBJ_Y046 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X046,XBJ_Y046 ,XBJ_X047,XBJ_Y047 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X047,XBJ_Y047 ,XBJ_X048,XBJ_Y048 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X048,XBJ_Y048 ,XBJ_X049,XBJ_Y049 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X049,XBJ_Y049 ,XBJ_X050,XBJ_Y050 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X050,XBJ_Y050 ,XBJ_X051,XBJ_Y051 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X051,XBJ_Y051 ,XBJ_X052,XBJ_Y052 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X052,XBJ_Y052 ,XBJ_X053,XBJ_Y053 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X053,XBJ_Y053 ,XBJ_X054,XBJ_Y054 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X054,XBJ_Y054 ,XBJ_X055,XBJ_Y055 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X055,XBJ_Y055 ,XBJ_X060,XBJ_Y060 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X049,XBJ_Y049 ,XBJ_X056,XBJ_Y056 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X056,XBJ_Y056 ,XBJ_X057,XBJ_Y057 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X057,XBJ_Y057 ,XBJ_X058,XBJ_Y058 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X058,XBJ_Y058 ,XBJ_X059,XBJ_Y059 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X059,XBJ_Y059 ,XBJ_X060,XBJ_Y060 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X060,XBJ_Y060 ,XBJ_X061,XBJ_Y061 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X061,XBJ_Y061 ,XBJ_X062,XBJ_Y062 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X062,XBJ_Y062 ,XBJ_X063,XBJ_Y063 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X063,XBJ_Y063 ,XBJ_X064,XBJ_Y064 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X064,XBJ_Y064 ,XBJ_X001,XBJ_Y001 ,pyxel.COLOR_DARK_BLUE],\
            
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X100,XBJ_Y100 ,XBJ_X101,XBJ_Y101 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X101,XBJ_Y101 ,XBJ_X102,XBJ_Y102 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X103,XBJ_Y103 ,XBJ_X104,XBJ_Y104 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X104,XBJ_Y104 ,XBJ_X105,XBJ_Y105 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X106,XBJ_Y106 ,XBJ_X107,XBJ_Y107 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X107,XBJ_Y107 ,XBJ_X108,XBJ_Y108 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X109,XBJ_Y109 ,XBJ_X110,XBJ_Y110 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X110,XBJ_Y110 ,XBJ_X111,XBJ_Y111 ,pyxel.COLOR_DARK_BLUE],\
            
            
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC00,XBJ_YC00 ,XBJ_R0  ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC00,XBJ_YC00 ,XBJ_R0A ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC01,XBJ_YC01 ,XBJ_R1 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC02,XBJ_YC02 ,XBJ_R2 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC03,XBJ_YC03 ,XBJ_R3 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC04,XBJ_YC04 ,XBJ_R4 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC05,XBJ_YC05 ,XBJ_R5 ,pyxel.COLOR_DARK_BLUE],\
            
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC06,XBJ_YC06 ,XBJ_R6 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC07,XBJ_YC07 ,XBJ_R7 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC08,XBJ_YC08 ,XBJ_R8 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_CIRCLE ,XBJ_XC09,XBJ_YC09 ,XBJ_R9 ,pyxel.COLOR_DARK_BLUE],\
            
            
            ],\
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
            self.pad_assign_list,self.pad_assign_graph_list,\
            
            NO_ITEM_LIST,      NO_ITEM_GRAPH_LIST,\
            
            self.master_flag_list,[[120,51,  IMG2,  32,88,SIZE_8,SIZE_8, 0, 1,1],[129,42,  IMG2,  40,88,SIZE_8,SIZE_8, 0, 1,1],[112,41,  IMG2,  32,96,SIZE_8,SIZE_8, 0, 1,1],[120,30,  IMG2,  40,96,SIZE_8,SIZE_8, 0, 1,1]],\
            NO_TIME_COUNTER_LIST,\
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
            
            [["SHOT AND SUB WEAPON BUTTON","","","","","","","","",""],\
            [ "MISSILE BUTTON","","","","","","","","",""],\
            [ "MAIN WEAPON CHANGE BUTTON","","","","","","","","",""],\
            [ "SUB WEAPON CHANGE BUTTON","","","","","","","","",""],\
            [ "SPEED CHANGE BUTTON","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "GAME PAUSE BUTTON","","","","","","","","",""],\
            [ "CALW STYLE CHANGE BUTTON","","","","","","","","",""],\
            [ "CLAW DISTANCE CHANGE BUTTON","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "DEFAULT","","","","","","","","",""],\
            [ "ALL CLEAR","","","","","","","","",""],\
            [ "SAVE RETURN","","","","","","","","",""]],\
            
            [["ショット発射ボタン","","","","","","","","",""],\
            [ "ミサイル発射ボタン","","","","","","","","",""],\
            [ "メインウェポンの変更ボタン","","","","","","","","",""],\
            [ "サブウェポンの変更ボタン","","","","","","","","",""],\
            [ "スピードチェンジボタン","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "一時停止ボタン","","","","","","","","",""],\
            [ "クロースタイルチェンジ","","","","","","","","",""],\
            [ "クローの間隔調整","","","","","","","","",""],\
            [ "","","","","","","","","",""],\
            [ "初期設定に戻します","","","","","","","","",""],\
            [ "全てのボタンを設定無しにします","","","","","","","","",""],\
            [ "セーブします","","","","","","","","",""]],\
            
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
        elif id == WINDOW_ID_TITLE_TEXT:                #タイトルで表示されるテキスト群
            new_window.update(\
            WINDOW_ID_TITLE_TEXT,\
            WINDOW_ID_SUB_NORMAL_MENU,\
            WINDOW_TYPE_NORMAL,\
            WINDOW_FRAME_NONE,\
            WINDOW_BG_NONE,\
            WINDOW_PRIORITY_TITLE_BACK,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            0,0,0,0,0,0,32,0,0,0, 0,80,160,100,0,0,0,0,  0,0,0,0,\
            WINDOW_BETWEEN_LINE_7,\
            ["PROJECT MINE 2020",          CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [[ "HIT ANY KEY"         ,CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_YELLOW_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
            
            ox,oy+101,  ox,oy+101,   0,0,  160,30,   1,1, 0.5,0.6,   0,0,    0,0,    0,0,0,0,   0,\
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
        else:
            return
        self.window.append(new_window)                  #ウィンドウを育成する

    #スコアボードウィンドウの育成
    def create_score_board(self,d): #引数dは難易度 difficulty
        """
        スコアボードウィンドウの育成
        
        dは難易度 difficulty
        """
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
        0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
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
        
        NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
        """
        リプレイファイルスロット選択ウィンドウの育成
        """
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
        0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
        WINDOW_BETWEEN_LINE_7,\
        ["SLOT",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        
        [["1",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "2",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "3",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "4",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "5",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "6",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "7",  CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
        
        NO_ITEM_KANJI_TEXT,NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        
        self.window.append(new_window)                      #「SELECT SLOT」を育成する

    #メダル取得報告ウィンドウの育成
    def create_medal_acquisition_report_window(self,ox,oy,id,wait): #idはメダルidとなります waitはその場に留まる時間(単位はフレーム)
        """
        メダル取得報告ウィンドウの育成
        
        ox,oyは表示座標のオフセット値
        idはメダルidとなります
        waitはその場に留まる時間(単位はフレーム)
        """
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
        0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
        between_l,\
        ["MEDAL GET !!",CLICK_SOUND_ON ,DISP_CENTER,0,0,7,MES_RED_FLASH],\
        
        [[medal_cmnt_eng,       CLICK_SOUND_ON ,DISP_CENTER,0, 7,10,MES_NO_FLASH],\
        [ get_cmnt_line1_eng,   CLICK_SOUND_ON ,DISP_CENTER,0,14, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_eng,   CLICK_SOUND_ON ,DISP_CENTER,0,14, 7,MES_NO_FLASH]],\
        
        [[medal_cmnt_jpn,       CLICK_SOUND_ON ,DISP_CENTER,9, 0,10,MES_NO_FLASH],\
        [ get_cmnt_line1_jpn,   CLICK_SOUND_ON ,DISP_CENTER,9, 7, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_jpn,   CLICK_SOUND_ON ,DISP_CENTER,9, 7, 7,MES_NO_FLASH]],\
        
        NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
        """
        実績(アチーブメント)取得報告ウィンドウの育成
        
        idは実績idとなります
        priorityはウィンドウ描画優先度(通常はWINDOW_PRIORITY_NORMAL)
        waitはその場に留まる時間(単位はフレーム)
        ox,oyはオフセット値(デフォルトは右下に表示される)
        """
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
        0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,  0,0,0,0,\
        between_l,\
        [achieve_cmnt_eng,CLICK_SOUND_ON ,DISP_LEFT_ALIGN,-6,-7,7,MES_NO_FLASH],\
        
        NO_ITEM_TEXT,NO_ITEM_KANJI_TEXT,\
        NO_EDIT_TEXT,NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,NO_VECTOR_GRP,\
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
        NO_PAD_ASSIGN_LIST,NO_PAD_ASSIGN_GRAPH_LIST,\
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
        """
        メインメニューウィンドウを左にずらす
        """
        i = func.search_window_id(self,WINDOW_ID_MAIN_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dx = 44 - 30
        self.window[i].vx = -4            #メインメニューウィンドウを左にずらしてやる
        self.window[i].vx_accel = 0.8

    #メインメニューウィンドウを右にずらす
    def move_right_main_menu_window(self):
        """
        メインメニューウィンドウを右にずらす
        """
        i = func.search_window_id(self,WINDOW_ID_MAIN_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dx = 44
        self.window[i].vx = 3.9            #メインメニューウィンドウを右にずらしてやる
        self.window[i].vx_accel = 0.8

    #ポーズメニューウィンドウを下にずらす
    def move_down_pause_menu(self):
        """
        ポーズメニューウィンドウを下にずらす
        """
        i = func.search_window_id(self,WINDOW_ID_PAUSE_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dy = 109
        self.window[i].vy = 9           #ポーズメニューウィンドウを下にずらしてやる
        self.window[i].vy_accel = 0.9

    #ポーズメニューウィンドウを上にずらす
    def move_up_pause_menu(self):
        """
        ポーズメニューウィンドウを上にずらす
        """
        i = func.search_window_id(self,WINDOW_ID_PAUSE_MENU)
        self.window[i].window_status = WINDOW_MOVE
        self.window[i].dy = 70
        self.window[i].vy = -9            #ポーズメニューウィンドウを上にずらしてやる
        self.window[i].vy_accel = 0.9

    #メダルの取得判定をする関数
    def judge_medal_acquisition(self):
        """
        メダルの取得判定をする関数
        """
        if func.search_window_id(self,WINDOW_ID_MEDAL_ACQUISITION_REPORT) != -1: #メダル取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 180
        #プレイ時間で判定するメダルタイプ
        if self.total_game_playtime_seconds >= 10 * 60 and self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム10分以上なら「事前1ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_1SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_game_playtime_seconds >= 180 * 60 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム180分以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #トータルスコアで判定するタイプ
        elif self.total_score >= 2000 and self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア2000点以上なら「事前3ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_3SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_score >= 10000 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア10000点以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #ボスを倒した回数で判定するタイプ
        elif self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] == MEDAL_NO_SLOT: #1面ボスを1回以上破壊で「事前2ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_2SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #プレイ回数で判定するタイプ
        elif self.number_of_play >= 20 and self.medal_list[MEDAL_FRAME_RESIST - 1] == MEDAL_NO_SLOT: #トータルゲームプレイ回数が20以上なら「炎耐性」を取得
            self.medal_list[MEDAL_FRAME_RESIST - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_FRAME_RESIST,wait)  #メダル取得報告ウィンドウを育成
        
        #スコアスターの最大得点倍率で判定するタイプ
        elif self.max_score_star_magnification >= 7 and self.medal_list[MEDAL_PLUS_MEDALLION - 1] == MEDAL_NO_SLOT: #スコアスター最大得点倍率が7以上なら「メダル枠２増設」をゲット！
            self.medal_list[MEDAL_PLUS_MEDALLION - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            window.create_medal_acquisition_report_window(self,20,90,MEDAL_PLUS_MEDALLION,wait)  #メダル取得報告ウィンドウを育成

    #実績(アチーブメント)の取得判定をする関数
    def judge_achievement_acquisition(self):
        """
        実績(アチーブメント)の取得判定をする関数
        """
        if func.search_window_id(self,WINDOW_ID_ACHIEVEMENT_ACQUISITION_REPORT) != -1: #実績取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 360
        #出撃回数(遊んだ回数)で判別するタイプ
        if self.number_of_play == 0 and self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED: #プレイ回数が0で出撃したのならFIRST CAMPAIGN「初陣」実績取得
            self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CAMPAIGN,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #ボスを倒した回数で判定するタイプ
        #1面ボスを1回以上破壊で「1面ボス撃破」実績取得
        if self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE01_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #2面ボスを1回以上破壊で「2面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ADVANCE_BASE] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE02_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #3面ボスを1回以上破壊で「3面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_VOLCANIC_BELT] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE03_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #4面ボスを1回以上破壊で「4面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_NIGHT_SKYSCRAPER] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE04_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #5面ボスを1回以上破壊で「5面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_AMPHIBIOUS_ASSAULT_SHIP] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE05_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #6面ボスを1回以上破壊で「6面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_DEEP_SEA_TRENCH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE06_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #7面ボスを1回以上破壊で「7面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_INTERMEDIATE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE07_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #8面ボスを1回以上破壊で「8面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ESCAPE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE08_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #9面ボスを1回以上破壊で「9面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_BOSS_RUSH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE09_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #ボスの累計撃破数で判定するタイプ
        #ボス累計10体撃破！
        if func.total_defeat_boss_num(self) >= 10 and self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_BOSS_10TIME,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #パワーカプセルの取得累計数で取得するタイプの実績
        #ショットカプセル10個取得
        wait = 360
        if self.get_shot_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル50個取得
        elif self.get_shot_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル100個取得
        elif self.get_shot_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル200個取得
        elif self.get_shot_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル500個取得
        elif self.get_shot_pow_num >= 500 and self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_500_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル1000個取得
        elif self.get_shot_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2000個取得
        elif self.get_shot_pow_num >= 2000 and self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2465個取得
        elif self.get_shot_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #ミサイルカプセル10個取得
        elif self.get_missile_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル50個取得
        elif self.get_missile_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル100個取得
        elif self.get_missile_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル200個取得
        elif self.get_missile_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル400個取得
        elif self.get_missile_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル765個取得
        elif self.get_missile_pow_num >= 765 and self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_765_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル1000個取得
        elif self.get_missile_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル2465個取得
        elif self.get_missile_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #シールドカプセル10個取得
        elif self.get_shield_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル50個取得
        elif self.get_shield_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル100個取得
        elif self.get_shield_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル200個取得
        elif self.get_shield_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル400個取得
        elif self.get_shield_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル530個取得
        elif self.get_shield_pow_num >= 530 and self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_530_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #初めてクローゲットで「はじめてのクロー」実績取得
        elif self.get_claw_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CLAW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル10個取得
        elif self.get_claw_num >= 10 and self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル20個取得
        elif self.get_claw_num >= 20 and self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_20_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル50個取得
        elif self.get_claw_num >= 50 and self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル100個取得
        elif self.get_claw_num >= 100 and self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        
        #武器レベルで判別して取得するタイプの実績
        #初めて5WAYバルカンショットを体験
        wait = 360
        if self.shot_level == SHOT_LV3_5WAY_VULCAN_SHOT and self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_5WAY_SHOT,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてレーザーを体験
        elif self.shot_level == SHOT_LV4_LASER and self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてツインレーザーを体験
        elif self.shot_level == SHOT_LV5_TWIN_LASER and self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_TWIN_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてシャワーレーザーを体験
        elif self.shot_level == SHOT_LV6_3WAY_LASER and self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_SHOWER_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてウェーブカッターを体験
        elif self.shot_level == SHOT_LV7_WAVE_CUTTER_LV1 and self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めて最大ウェーブカッターを体験
        elif self.shot_level == SHOT_LV10_WAVE_CUTTER_LV4 and self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_MAX_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #特殊条件を満たし各工程でのフラグが立ったら取得するタイプの実績
        #初めてパワーカプセルゲットで「はじめてのパワーカプセル回収成功！」実績取得
        wait = 360
        if self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            if self.get_shot_pow_num >= 1 or self.get_missile_pow_num >= 1 or self.get_shield_pow_num >= 1:
                self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
                pyxel.play(0,26) #実績取得音を鳴らす
                window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_POW_UP,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
                return
        
        #初めてトライアングルアイテム取得で「初めてトライアングルアイテム」実績取得
        if self.get_triangle_pow_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        #早回実績取得用フラグが立っているのならば「早回し発生実績」を取得
        #初めての早回し体験
        if self.fast_forward_flag == FLAG_ON and self.fast_forward_num == 1-1 and self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し8回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 8-1 and self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_8_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し16回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 16-1 and self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_16_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し32回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 32-1 and self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_32_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し64回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 64-1 and self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_64_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し128回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 128-1 and self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_128_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し256回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 256-1 and self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_256_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し512回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 512-1 and self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_512_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し1024回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 1024-1 and self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1024_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        
        #主にステージクリア(ボス破壊後）にフラグが立ち、そのフラグを見ることによって取得判別するタイプの実績(複数の実績が同時に解除される可能性あり)
        up_shift_line = 0 #上にシフトしていく行数を初期化
        #「ステージ中ノーダメージでクリア」フラグオンで実績取得
        if  self.no_damage_stage_clear_flag == FLAG_ON:
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR ,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60) #実績取得報告ウィンドウを育成
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR][LIST_ACHIEVE_FLAG]  = RESULTS_ACQUISITION
            self.no_damage_stage_clear_flag = FLAG_OFF  #ノーダメージでボスステージクリアフラグを下げる
            up_shift_line += 1
        #「ノーダメージでボス破壊」フラグオンで実績取得
        if self.no_damage_destroy_boss_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.no_damage_destroy_boss_flag = FLAG_OFF #ノーダメージでボス破壊フラグを下げる
            up_shift_line += 1
        #残りシールド１でギリギリクリアフラグオンで実績取得
        if self.endurance_one_cleared_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_ENDURANCE_ONE_CLEARED][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_ENDURANCE_ONE_CLEARED,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.endurance_one_cleared_flag = FLAG_OFF #残りシールド１でギリギリクリアフラグを下げる
            up_shift_line += 1
        #ボスを瞬殺したフラグオンで実績取得
        if self.boss_instank_kill_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_BOSS_INSTANK_KILL][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_BOSS_INSTANK_KILL,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.boss_instank_kill_flag = FLAG_OFF #ボスを瞬殺したフラグを下げる
            up_shift_line += 1
        #ボスのパーツをすべて破壊したフラグオンで実績取得
        if self.destroy_all_boss_parts_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            window.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.destroy_all_boss_parts_flag = FLAG_OFF #ボスのパーツをすべて破壊したフラグを下げる
            up_shift_line += 1

    #ウィンドウのはみだしチェック（表示座標が完全に画面外になったのなら消去する）
    def clip_window(self):
        """
        ウィンドウのはみだしチェック（表示座標が完全に画面外になったのなら消去する）
        """
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
                #同じウィンドウIDがredraw_star_areaリストの中に存在するのならそのインスタンスも消去して「星を再描画するエリア情報」も消去する
                j = func.search_window_id_star_redraw(self,self.window[i].window_id) #jにwin_idに対応したredraw_star_areaのインデックス値が入る
                if j != -1: # 存在するのならば・・・
                    del self.redraw_star_area[j] #「星を再描画するエリア情報」redraw_star_areaインスタンスも破棄する
                    # print("star_redraw_window_num = " + str(len(self.redraw_star_area)))
                
                del self.window[i] #ウィンドウが画面外に存在するとき(2つの矩形が衝突していないとき)はインスタンスを破棄する(ウィンドウ消滅)

    #現在どのウィンドウがもつインデックス値が最前面にあるのか調べあげ,アクティブウィンドウインデックス値に登録し更新する
    def active_window(self):
        """
        現在どのウィンドウがもつインデックス値が最前面にあるのか調べあげ,アクティブウィンドウインデックス値に登録し更新する
        
        self.active_window_indexに現在アクティブになっているウィンドウのインデックスナンバー(i)が代入される
        """
        i = func.search_window_id(self,self.active_window_id) #アクティブなウィンドウIDを元にインデックス値を求める関数の呼び出し
        self.active_window_index = i           #アクティブになっているウィンドウのインデックスナンバー(i)を代入

    #ウィンドウIDを元にそのウィンドウの描画優先度を最前面にする
    def change_window_priority_top(self,id): #idはウィンドウidとなります そのidのウィンドウが存在しない場合は何もしない
        """
        ウィンドウIDを元にそのウィンドウの描画優先度を最前面にする
        
        idはウィンドウidとなります そのidのウィンドウが存在しない場合は何もしない
        """
        i = func.search_window_id(self,id) #iにウィンドウIDを元にしたインデックス値が入る 存在しなかったら-1が帰ってくる
        if i != -1: #そのウィンドウが存在したのならば
            self.window[i].window_priority = WINDOW_PRIORITY_TOP #描画優先度を一番前の最前面にする

    #ウィンドウIDを元にそのウィンドウの描画優先度を普通にする
    def change_window_priority_normal(self,id): #idはウィンドウidとなります そのidのウィンドウが存在しない場合は何もしない
        """
        ウィンドウIDを元にそのウィンドウの描画優先度を普通にする
        
        idはウィンドウidとなります そのidのウィンドウが存在しない場合は何もしない
        """
        i = func.search_window_id(self,id) #iにウィンドウIDを元にしたインデックス値が入る 存在しなかったら-1が帰ってくる
        if i != -1: #そのウィンドウが存在したのならば
            self.window[i].window_priority = WINDOW_PRIORITY_NORMAL #描画優先度を普通(通常)にする

    #セレクトカーソルの更新
    def select_cursor(self):
        """
        セレクトカーソルの更新
        """
        # 上入力されたら  y座標を  -7する(1キャラ分)
        # if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
        if btn.keypad_up(self) == True:
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
                    
                else: #!上方向の限界位置で上入力された時の処理の開始------------------------------------------------------------もうちょっと調整がいるかもしれない---
                    self.cursor_repeat_time_count = 40                   #カーソルリピートタイムカウントを初期状態に戻す
                    self.keypad_repeat_num = 40
                    self.cursor_y = self.cursor_y + self.cursor_step_y * self.cursor_max_item_y         #カーソルのy座標最下段項目の座標にする
                    self.cursor_item_y = self.cursor_max_item_y                         #カーソルアイテムyをy軸最大項目にしてカーソル位置を最下段にワープさせる
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
                else: #上方向の限界位置で上入力された時の処理の開始---------------------------------------------------------------
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
                        if character == 96+1: #入力できる文字(アスキーコード)は32~96の間のみとする
                            character = 32
                        
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else: #上方向の限界位置で上入力された時の処理の開始---------------------------------------------------------------
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        # 下入力されたら  y座標を  +7する(1キャラ分)
        # if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
        if btn.keypad_down(self) == True:
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
                    
                else: #!下方向の限界位置で下入力された時の処理の開始----------------------------------------------もうちょっと調整がいるかもしれない-----------------
                    self.cursor_repeat_time_count = 40                   #カーソルリピートタイムカウントを初期状態に戻す
                    self.keypad_repeat_num = 40
                    self.cursor_y = self.cursor_y - self.cursor_step_y * self.cursor_max_item_y #カーソルのy座標最上段項目の座標にする
                    self.cursor_item_y = 0                                                      #カーソルアイテムyを0にしてカーソル位置を最上段にワープさせる
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)        #カーソル跳ね返り音を鳴らす
                
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
                else: #下方向の限界位置で下入力された時の処理の開始---------------------------------------------------------------
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
                        character -= 1 #文字のアスキーコードを1減らす（今カーソルのあるアルファベットのアスキーコードを1減らす BはAに CはBに DはCに EはDになる)
                        if character == 32-1: #入力できる文字(アスキーコード)は32~96の間のみとする
                            character = 96
                        
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(いみゅーたぶる変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else: #下方向の限界位置で下入力された時の処理の開始---------------------------------------------------------------
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        #右入力されたらcursor_pageを +1する
        # if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_RIGHTSHOULDER):
        if btn.keypad_right(self) == True:
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
                        sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD:
                if self.cursor_repeat_time_count <= 8: #パッドを押し続けてリピートタイムが8以下になったら
                    self.cursor_y = self.cursor_y + self.cursor_step_y * (self.cursor_max_item_y -  self.cursor_item_y)    #カーソルのy座標最下段項目の座標にする
                    self.cursor_item_y = self.cursor_max_item_y                                                            #カーソルアイテムyをy軸最大項目にしてカーソル位置を最下段にワープさせる
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)                                   #カーソル跳ね返り音を鳴らす
        
        #左入力されたらcursor_pageを -1する
        # if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_LEFTSHOULDER):
        if btn.keypad_left(self) == True:
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
                        sound.se(self,2,SE_WAVE_CUTTER,self.master_se_vol)
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD:
                if self.cursor_repeat_time_count <= 8: #パッドを押し続けてリピートタイムが8以下になったら
                    self.cursor_y = self.cursor_y - self.cursor_step_y * self.cursor_item_y   #カーソルのy座標最上段項目の座標にする
                    self.cursor_item_y = 0                                                    #カーソルアイテムyをy軸最小項目にしてカーソル位置を最上段にワープさせる
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)      #カーソル跳ね返り音を鳴らす
        
        #ABXY,BACK,START,スペースキーが押された場合の処理
        self.cursor_button_data = BTN_NONE
        
        if     pyxel.btnp(pyxel.KEY_SPACE):
            self.cursor_button_data = BTN_KEYBOARD_SPACE
            window.select_cursor_push_button(self)
        elif   pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_A):
            self.cursor_button_data = BTN_A
            window.select_cursor_push_button(self)
        elif   pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_B):
            self.cursor_button_data = BTN_B
            window.select_cursor_push_button(self)
        elif   pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_X):
            self.cursor_button_data = BTN_X
            window.select_cursor_push_button(self)
        elif   pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_Y):
            self.cursor_button_data = BTN_Y
            window.select_cursor_push_button(self)
            
            #パッドアサインモードフラグが立っている時はパッド割り当てでBACKボタンやSTARTボタンLEFT SHOULDER,RIGHT SHOULDERボタンも「決定」ボタンとして使用したいので以下の処理も行います
        elif (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_BACK) and (self.cursor_pad_assign_mode == FLAG_ON))          or (pyxel.btnp(pyxel.GAMEPAD2_BUTTON_BACK) and (self.cursor_pad_assign_mode == FLAG_ON)):
            self.cursor_button_data = BTN_BACK
            window.select_cursor_push_button(self)
        elif (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START) and (self.cursor_pad_assign_mode == FLAG_ON))         or (pyxel.btnp(pyxel.GAMEPAD2_BUTTON_START) and (self.cursor_pad_assign_mode == FLAG_ON)):
            self.cursor_button_data = BTN_START
            window.select_cursor_push_button(self)
        elif (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER) and (self.cursor_pad_assign_mode == FLAG_ON))  or (pyxel.btnp(pyxel.GAMEPAD2_BUTTON_LEFTSHOULDER) and (self.cursor_pad_assign_mode == FLAG_ON)):
            self.cursor_button_data = BTN_LEFTSHOULDER
            window.select_cursor_push_button(self)
        elif (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) and (self.cursor_pad_assign_mode == FLAG_ON)) or (pyxel.btnp(pyxel.GAMEPAD2_BUTTON_RIGHTSHOULDER) and (self.cursor_pad_assign_mode == FLAG_ON)):
            self.cursor_button_data = BTN_RIGHTSHOULDER
            window.select_cursor_push_button(self)
        else:
            self.cursor_button_data = BTN_NONE

    #セレクトカーソル移動時,ボタンを押した後の処理を行う
    def select_cursor_push_button(self):
        """
        セレクトカーソル移動時,ボタンを押した後の処理を行う
        """
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

    #パッドアサイングラフイックリストをリフレッシュ！する！
    def refresh_pad_assign_graph_list(self):
        """
        パッドアサイングラフイックリストをリフレッシュ！する！
        """
        self.pad_assign_graph_list =[
            [ 90, 11 + self.pad_assign_list[0] * 7 , IMG2,8 * 0,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[1] * 7 , IMG2,8 * 1,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[2] * 7 , IMG2,8 * 2,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[3] * 7 , IMG2,8 * 3,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[4] * 7 , IMG2,8 * 4,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[5] * 7 , IMG2,8 * 5,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[6] * 7 , IMG2,8 * 6,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[7] * 7 , IMG2,8 * 7,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            [ 90, 11 + self.pad_assign_list[8] * 7 , IMG2,8 * 8,104, SIZE_8,SIZE_8, pyxel.COLOR_BLACK],\
            ]