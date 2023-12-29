import math  # 三角関数などを使用したいのでインポートぉぉおお！
import os
from random import random  # random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)

# import pygame.mixer  # MP3再生するためだけに使用する予定・・・予定は未定・・・そして未定は確定に！やったあぁ！ BGMだけで使用しているサブゲームエンジン
import pyxel  # グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import *  # 定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from const_window import * #主にウィンドウクラスで使用する定数定義
from define_class import * # クラス宣言モジュールの読み込み やっぱりimport *は不味いのかなぁ・・・よくわかんない


class func:
    def __init__(self):
        None

    #漢字フォントデータの読み込み
    def load_kanji_font_data(self):
        """
        漢字フォントデータの読み込み
        """
        pyxel.load(os.path.abspath("./assets/fonts/misaki_font_k8x12s_001.pyxres")) #漢字フォントデータ(その1)を読み込みます
        # pyxel.load("./assets/fonts/misaki_font_k8x12s_001.pyxres") #漢字フォントデータ(その1)を読み込みます
        # self.kanji_fonts = [] #漢字フォントリストデータをまずは初期化して使えるようにします この方法だとダメだわ
        self.kanji_fonts = [[None for col in range(752)] for row in range(1128)] #横752,縦1128の空っぽの漢字フォントデータリストを作成します(Pythonクックブックで奨められている書き方ですのんって、判りにくいよなぁ・・これ)
        
        for y in range(256):  #左端A列のk8x12s_jisx0208___001a.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(0,0)
            for x in range(256):
                col = pyxel.image(0).pget(x,y)
                self.kanji_fonts[y+0][x+0] = col #ぐへぇ最初, self.kanji_fonts[x][y] = colってやってた・・リストの最初の[]はy軸になるんだよね・考えてみればそうだったｗ 嵌りどころだわ～～～～
        for y in range(256):  #左端A列のk8x12s_jisx0208___002a.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(0,256)
            for x in range(256):
                col = pyxel.image(1).pget(x,y)
                self.kanji_fonts[y+256][x+0] = col
        for y in range(256):  #左端A列のk8x12s_jisx0208___003a.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(0,512)
            for x in range(256):
                col = pyxel.image(2).pget(x,y)
                self.kanji_fonts[y+512][x+0] = col
        
        pyxel.load(os.path.abspath("./assets/fonts/misaki_font_k8x12s_002.pyxres")) #漢字フォントデータ(その2)を読み込みます
        # pyxel.load("./assets/fonts/misaki_font_k8x12s_002.pyxres") #漢字フォントデータ(その2)を読み込みます
        for y in range(256):  #左端A列の  k8x12s_jisx0208___004a.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(0,768)
            for x in range(256):
                col = pyxel.image(0).pget(x,y)
                self.kanji_fonts[y+768][x+0] = col
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___001b.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(256,0)
            for x in range(256):
                col = pyxel.image(1).pget(x,y)
                self.kanji_fonts[y+0][x+256] = col
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___002b.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(256,256)
            for x in range(256):
                col = pyxel.image(2).pget(x,y)
                self.kanji_fonts[y+256][x+256] = col
        
        pyxel.load(os.path.abspath("./assets/fonts/misaki_font_k8x12s_003.pyxres")) #漢字フォントデータ(その3)を読み込みます
        # pyxel.load("./assets/fonts/misaki_font_k8x12s_003.pyxres") #漢字フォントデータ(その3)を読み込みます
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___003b.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(256,512)
            for x in range(256):
                col = pyxel.image(0).pget(x,y)
                self.kanji_fonts[y+512][x+256] = col
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___004b.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(256,768)
            for x in range(256):
                col = pyxel.image(1).pget(x,y)
                self.kanji_fonts[y+768][x+256] = col
        for y in range(256):  #右端C列の  k8x12s_jisx0208___001c.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(512,0)
            for x in range(752-512):
                col = pyxel.image(2).pget(x,y)
                self.kanji_fonts[y+0][x+512] = col
        
        pyxel.load(os.path.abspath("./assets/fonts/misaki_font_k8x12s_004.pyxres")) #漢字フォントデータ(その4)を読み込みます
        # pyxel.load("./assets/fonts/misaki_font_k8x12s_004.pyxres") #漢字フォントデータ(その4)を読み込みます
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___002c.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(512,256)
            for x in range(752-512):
                col = pyxel.image(0).pget(x,y)
                self.kanji_fonts[y+256][x+512] = col
        for y in range(256):  #真ん中B列のk8x12s_jisx0208___003c.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(512,512)
            for x in range(752-512):
                col = pyxel.image(1).pget(x,y)
                self.kanji_fonts[y+512][x+512] = col
        for y in range(256):  #右端C列の  k8x12s_jisx0208___004c.pngを読みだしてフォントデータリストに書き込んでいきます 書き込みオフセット値は(512,768)
            for x in range(752-512):
                col = pyxel.image(2).pget(x,y)
                self.kanji_fonts[y+768][x+512] = col

    #漢字テキストの表示
    def kanji_text(self,x,y,text,col):
        """
        漢字を含んだ文章文字の表示
        
        x,y=表示座標\\xxx
        text=表示するテキスト\\
        col=pyxelのカラーコード 
        """
        base_x,base_y = x,y
        sx,sy = 0,0
        for char in text:
            found = self.font_code_table.find(char) #foundにテキスト(char)を使ってフォント対応表にある位置を調べる→位置がfoundに入ります(見つからなかったらfoundに-1が入ります)
            if found >= 0 and char != '\n': #文字を見つけて尚且つ改行コードでないのなら漢字を描画し始めます
                sy = self.font_code_table[:found].count('\n') #対応表のリストの先頭から改行コードの数を数えるとその数値がY座標となります
                sx = self.font_code_table.split('\n')[sy].find(char)
                
                for i in range(8): #漢字フォントの横ドット数8
                    for j in range(12): #漢字フォントの縦ドット数12
                        if self.kanji_fonts[(sy-1)*12+j][sx*8+i] == 7: #フォントのデータは 0=黒が透明で 7=白が描画する点なので色コードが7だったらpsetで点を打ちます
                            if 0 <= y+j <= WINDOW_H and col != 0: #y軸座標値が表示画面内、なおかつ指定色が黒以外ならば
                                
                                #print (int(y+j))
                                new_col = self.attrib_line_col[int(y+j)][int((x+i) % 2)]
                                #print (new_col)
                                pyxel.pset(x+i,y+j,int(new_col))
                            else:
                                pyxel.pset(x+i,y+j,int(col))
                
                x += 8
                if char == '\n':
                    x = base_x
                    y += 12

    #ドロップシャドウ漢字テキストの表示(影落ち漢字テキスト)
    def drop_shadow_kanji_text(self,x,y,text,col):
        """
        漢字を含んだ文章文字(影落ちあり)の表示
        
        x,y=表示座標\\
        text=表示するテキスト\\
        col=pyxelのカラーコード 
        """
        func.kanji_text(self,x+1,y,  text,0)       #なんでfunc.kanji_text(self,x+1,y,  text,0)にしないとエラーが出るのか判らない・・試行錯誤で func.kanji_text(self,x+1,y,  text,0)ってやったらうまくいった・・・クラスが違うところから呼び出される関数(この場合はメソッド？)は呼び出された関数自身を示すselfを付けないといけないのかな？謎は深まる・・・
        func.kanji_text(self,x+1,y+1,text,0)
        func.kanji_text(self,x,  y,  text,col)

    #ドロップシャドウテキスト(影落ちテキスト)の表示
    def drop_shadow_text(self,x,y,text,col):
        """
        影落ちありの文章文字の表示
        
        x,y = 表示座標\\
        text = 表示するテキスト\\
        col = pyxelのカラーコード 
        """
        pyxel.text(x+1,y,  text,0)
        pyxel.text(x+1,y+1,text,0)
        pyxel.text(x,  y,  text,int(col))

    #タイトルデモで漢字テキスト表示時にライン毎ごとの色指定を行う
    def set_title_scroll_jpn_text_color(self,start_line):
        """
        タイトルデモで漢字テキスト表示時にライン毎ごとの色指定を行う
        
        start_line = グラデーション指定を行う開始ラインの数値
        """
        self.attrib_line_col[start_line - 10] = [1,0]
        self.attrib_line_col[start_line - 9] = [0,1]
        self.attrib_line_col[start_line - 8] = [1,0]
        self.attrib_line_col[start_line - 7] = [0,1]
        self.attrib_line_col[start_line - 6] = [1,0]
        
        self.attrib_line_col[start_line - 5] = [1,0]
        self.attrib_line_col[start_line - 4] = [0,1]
        self.attrib_line_col[start_line - 3] = [1,0]
        self.attrib_line_col[start_line - 2] = [0,1]
        self.attrib_line_col[start_line - 1] = [1,0]
        
        self.attrib_line_col[start_line + 0] = [1,1]
        self.attrib_line_col[start_line + 1] = [1,1]
        self.attrib_line_col[start_line + 2] = [1,1]
        self.attrib_line_col[start_line + 3] = [1,1]
        self.attrib_line_col[start_line + 4] = [1,1]
        
        self.attrib_line_col[start_line + 5] = [1,1]
        self.attrib_line_col[start_line + 6] = [1,1]
        self.attrib_line_col[start_line + 7] = [1,1]
        self.attrib_line_col[start_line + 8] = [1,1]
        self.attrib_line_col[start_line + 9] = [1,1]
        
        self.attrib_line_col[start_line + 10] = [1,5]
        self.attrib_line_col[start_line + 11] = [5,1]
        self.attrib_line_col[start_line + 12] = [1,5]
        self.attrib_line_col[start_line + 13] = [5,1]
        self.attrib_line_col[start_line + 14] = [1,5]
        
        self.attrib_line_col[start_line + 15] = [5,5]
        self.attrib_line_col[start_line + 16] = [5,5]
        self.attrib_line_col[start_line + 17] = [5,5]
        self.attrib_line_col[start_line + 18] = [5,5]
        self.attrib_line_col[start_line + 19] = [5,5]
        
        
        self.attrib_line_col[start_line + 20] = [12,12]
        self.attrib_line_col[start_line + 21] = [12,12]
        self.attrib_line_col[start_line + 22] = [12,12]
        self.attrib_line_col[start_line + 23] = [12,12]
        self.attrib_line_col[start_line + 24] = [12,12]
        
        
        self.attrib_line_col[start_line + 25] = [6,12]
        self.attrib_line_col[start_line + 26] = [12,6]
        self.attrib_line_col[start_line + 27] = [6,6]
        self.attrib_line_col[start_line + 28] = [6,6]
        self.attrib_line_col[start_line + 29] = [6,6]
        
        self.attrib_line_col[start_line + 30] = [7,7]
        self.attrib_line_col[start_line + 31] = [7,7]
        self.attrib_line_col[start_line + 32] = [7,7]
        self.attrib_line_col[start_line + 33] = [7,7]
        self.attrib_line_col[start_line + 34] = [7,7]
        
        self.attrib_line_col[start_line + 35] = [7,7]
        self.attrib_line_col[start_line + 36] = [7,7]
        self.attrib_line_col[start_line + 37] = [7,7]
        self.attrib_line_col[start_line + 38] = [7,7]
        self.attrib_line_col[start_line + 39] = [7,7]
        
        self.attrib_line_col[start_line + 40] = [7,7]
        self.attrib_line_col[start_line + 41] = [7,7]
        self.attrib_line_col[start_line + 42] = [7,7]
        self.attrib_line_col[start_line + 43] = [7,7]
        self.attrib_line_col[start_line + 44] = [7,7]

    #横ライン単位でのアトリビュートリスト(色情報)に色指定をする(タイリングパターン定義もできます)
    def set_attrib_line_col(self,left_col,right_col):
        """
        横ライン単位でのアトリビュートリスト(色情報)に色指定をする(タイリングパターン定義もできます)
        
        left_col  = 左側のタイルパターン色\\
        right_col = 右側のタイルパターン色
        """
        for i in range(WINDOW_H):
            if i % 2 == 0:
                self.attrib_line_col[i] = [left_col,right_col] #偶数ラインの場合
            else:
                self.attrib_line_col[i] = [right_col,left_col] #奇数ラインの場合
        
        print(self.attrib_line_col) #デバッグ用にコンソール表示

    #タイルマップの座標位置からキャラチップのアスキーコードを取得する
    def get_chrcode_tilemap(self,tm,x,y):         #tmはtilemapの数値,x,yは読み出す座標位置
        """
        タイルマップの座標位置からキャラチップのアスキーコードを取得する
        
        tmはtilemapの数値\\
        x,yは読み出す座標位置
        """
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        num = 0
        tile_x,tile_y = pyxel.tilemap(tm).pget(x,y) #タイルマップtm 座標(x,y)に格納されているマップチップを調べ、そのマップチップが格納されている座標を取得
        num = tile_y * 32 + tile_x
        return(num)

    #タイルマップの座標位置へキャラチップのアスキーコードをタプル座標形式に変換したものをセットする(置く)
    def set_chrcode_tilemap(self,tm,x,y,num):         #tmはtilemapの数値,x,yはセット（置く）座標位置
        """
        タイルマップの座標位置へキャラチップのアスキーコードをタプル座標形式に変換したものをセットする
        
        tmはtilemapの数値\\
        x,yはセットする座標
        """
        tile_x = num % 32   #置く場所のx座標は 32で割った余り
        tile_y = num // 32  #置く場所のy座標は 32での切り捨て除算
        # pyxel.tilemap(tm).pset(x,y,(tile_x,tile_y)) pyxel 2.0.0以降はあんまり使わない方が良いらしい？
        pyxel.tilemaps[tm].pset(x,y,(tile_x,tile_y)) #pyxel 2.0.0以降はこういう風にするべきッポイ？？？？

    #パッドのボタンが押されたかどうか調べる関数定義 押されていたらTrue 押されていなかったFalseを返します
    def push_pad_btn(self,action_id):  #action_idはそれぞれのボタンアクションに割り当てられたIDです (例)ACT_SHOTは1,ACT_MISSILEは2,ACT_SHOT_AND_SUB_WEAPONは3などなど・・・
        """
        パッドのボタンが押されたかどうか調べる\\
        押されていたらTrue 押されていなかったFalseを返します
        
        action_idはそれぞれのボタンアクションに割り当てられたIDです\\
        (例)ACT_SHOTは1,ACT_MISSILEは2,ACT_SHOT_AND_SUB_WEAPONは3などなど
        """
        list_count = len(self.pad_assign_list)#list_countにpad_assign_listの長さが入る
        for i in range (list_count): #pad_assign_listの長さの回数だけループ
            btn_id = self.pad_assign_list[i] #どの様なボタンIDが割り当てられているか取り出す
            if action_id == btn_id: #アクションIDとボタンIDが一致したら、「割り当てられたボタンID」が押されているか？どうか？を調べはじめる
                if i == BTN_A:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_B:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_B):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_X:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_X):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_Y:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_BACK:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_BACK):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_START:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_LEFTSHOULDER:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_RIGHTSHOULDER:
                    if pyxel.btn(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER):
                        return (True)
                    else:
                        return (False)
        
        return (False)

    #パッドのボタンが押されて離されたかどうか調べる関数定義 押されて話されたらTrue そうでなかったらFalseを返します
    def push_pad_btnp(self,action_id): #action_idはそれぞれのボタンアクションに割り当てられたIDです (例)ACT_SHOTは1,ACT_MISSILEは2,ACT_SHOT_AND_SUB_WEAPONは3などなど・・・
        """
        パッドのボタンが押されたて離されたかどうか調べる\\
        押されていたらTrue 押されていなかったFalseを返します
        
        action_idはそれぞれのボタンアクションに割り当てられたIDです\\
        (例)ACT_SHOTは1,ACT_MISSILEは2,ACT_SHOT_AND_SUB_WEAPONは3などなど
        """
        #ポーズボタンをABXYボタンなどに割り当てるとポーズを掛けた瞬間にキャンセルされてポーズウィンドウが閉じてゲーム本編に戻るバグですが・・・
        #2022 12/04現在このメソッドは特に問題ないように思えます
        #STARTボタンを押すことによるポーズを掛ける、解除するも問題ない感じ
        #
        #update_window.select_cursor(self)内のABXY,BACK,START,スペースキーが押された場合の処理
        # elif   pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_START):
        #     self.cursor_button_data = BTN_START
        #     update_window.select_cursor_push_button(self)このソースコード群を
        #コメントアウトするときちんと動作するのでこの部分が問題かと・・・
        #
        # まぁ良く判んないんだけどねぇ～～～～～☆彡
        #
        list_count = len(self.pad_assign_list)#list_countにpad_assign_listの長さが入る
        for i in range (list_count): #pad_assign_listの長さの回数だけループ
            btn_id = self.pad_assign_list[i] #どの様なボタンIDが割り当てられているか取り出す
            if action_id == btn_id: #アクションIDとボタンIDが一致したら、「割り当てられたボタンID」が押されているか？どうか？を調べはじめる
                if i == BTN_A:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_B:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_X:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_Y:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_BACK:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_BACK):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_START:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_LEFTSHOULDER:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER):
                        return (True)
                    else:
                        return (False)
                
                if i == BTN_RIGHTSHOULDER:
                    if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER):
                        return (True)
                    else:
                        return (False)
        return (False)

    #自機との距離を求める関数定義
    def to_my_ship_distance(self,x,y):
        """
        自機との距離を求める
        
        x,y=自機との距離を求める座標位置 帰り値として距離が戻ってきます
        """
        dx = x - self.my_x
        dy = y - self.my_y
        distance = math.sqrt(dx * dx + dy * dy)
        return(distance)   #最初この行を return(self,distance)って記述しててエラーが出て、どうやったら良いのかわかんなかった・・・この場合はタプルになるらしい！？(良く判って無いｗ)

    #狙い撃ち弾を射出する関数定義 
    def enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
        """
        自機狙い撃ち弾を射出する関数定義
        
        ex,ey=敵の座標\\
        div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ\\
        div_count=分裂するまでのカウント\\
        div_num=分裂する回数\\
        stop_count=その場に止まるカウント数\\
        accel=弾の加速度 1.0で加速無し 1.1とかだと段々加速していく 0.9とかだと段々減速していく
        """
        if len(self.enemy_shot) < 800:
            #目標までの距離を求めdに代入します
            d = math.sqrt((self.my_x - ex) * (self.my_x - ex) + (self.my_y - ey) * (self.my_y - ey))
            #速さが一定値speedになる様に速度(vx,vy)を求める
            #目標までの距離dが0の時は何もせずに戻る
            if d == 0:
                return
            else:
                #敵と自機との距離dとx,y座標との差からvx,vyの増分を計算する
                vx = ((self.my_x - ex) / (d * 1))
                vy = ((self.my_y - ey) / (d * 1))
                
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,vx,vy, accel,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count,0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む

    #狙い撃ち弾(ゲームランクに依存)を射出する関数定義 
    def enemy_aim_bullet_rank(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
        """
        自機狙い撃ち弾(ゲームランクに依存)を射出する関数定義
        
        ex,ey=敵の座標\\
        div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ\\
        div_count=分裂するまでのカウント\\
        div_num=分裂する回数\\
        stop_count=その場に止まるカウント数
        accel=弾の加速度 1.0で加速無し 1.1とかだと段々加速していく 0.9とかだと段々減速していく
        """
        if func.s_rndint(self,0,self.run_away_bullet_probability) != 0:
            return
        else:
            func.enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel)

    #前方3way弾を射出する関数定義 
    def enemy_forward_3way_bullet(self,ex,ey):
        """
        前方3way弾を射出する関数定義 
        
        ex,ey=敵の座標
        """
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1,0,            1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,-0.5*0.8,   1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,0.5*0.8,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)  

    #前方5way弾を射出する関数定義 
    def enemy_forward_5way_bullet(self,ex,ey):
        """
        前方5way弾を射出する関数定義 
        
        ex,ey=敵の座標
        """
        if len(self.enemy_shot) < 800:
            func.enemy_forward_3way_bullet(self,ex,ey) #まずは前方3way弾を射出
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,0.2,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,-0.2,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)

    #狙い撃ちn-way弾を射出する関数定義
    def enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count):#ex,ey=敵の座標(弾を出す座標),theta=弾と弾の角度,n=弾の総数,div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ,div_count=分裂するまでのカウント(div_count_originにも同じ数値が入ります),div_num=分裂する回数,stop_count=その場に止まるカウント数
        """
        狙い撃ちn-way弾を射出する
        
        ex,ey=敵の座標(弾を出す座標)\\
        theta=弾と弾の角度\\
        n=弾の総数\\
        div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ\\
        div_count=分裂するまでのカウント\\
        div_num=分裂する回数\\
        stop_count=その場に止まるカウント数
        """
        if len(self.enemy_shot) < 800:
            #1度 = (1 × 3.14) ÷ 180 = 0.017453292519943295ラジアン
            #1度は約0.0174ラジアンと設定する
            
            #目標までの距離を求める dに距離が入る
            d = math.sqrt((self.my_x - ex) * (self.my_x - ex) + (self.my_y - ey) * (self.my_y - ey))
            
            #速さが一定値speedになる様に速度(vx,vy)を求める
            if d == 0:
                return #目標までの距離dが0の時は何もせずに戻る
            else:
                #敵と自機との距離とx座標、y座標との差から中心の基本速度ベクトル(cvx,cvx)を計算するcentralvx,centralvy
                cvx = ((self.my_x - ex) / (d * 1))
                cvy = ((self.my_y - ey) / (d * 1))
                
                if n % 2 == 1:
                    #奇数弾の処理#######3way弾とか5way弾とか7way弾とか##################################
                    #まず最初に中央の弾を発射する
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,cvx,cvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)#敵弾リストに中央狙い弾の情報を書き込む
                    
                    for i in range((n+1) // 2):
                        #時計回り方向に i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(theta*i*0.0174) - cvy * math.sin(theta*i*0.0174)
                        rvy = cvx * math.sin(theta*i*0.0174) + cvy * math.cos(theta*i*0.0174)
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                        
                        #反時計回り方向に -i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(-(theta*i*0.0174)) - cvy * math.sin(-(theta*i*0.0174))
                        rvy = cvx * math.sin(-(theta*i*0.0174)) + cvy * math.cos(-(theta*i*0.0174))
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                    
                else:
                    #偶数弾の処理#######2way弾とか4ay弾とか6way弾とか##################################
                    for i in range(n // 2):
                        #時計回り方向に i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(theta / 2*(i+1)*0.0174) - cvy * math.sin(theta / 2*(i+1)*0.0174)
                        rvy = cvx * math.sin(theta / 2*(i+1)*0.0174) + cvy * math.cos(theta / 2*(i+1)*0.0174)
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                        
                        #反時計回り方向に -i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(-(theta // 2 * (i+1) * 0.0174)) - cvy * math.sin(-(theta // 2*(i+1)*0.0174))
                        rvy = cvx * math.sin(-(theta // 2 * (i+1) * 0.0174)) + cvy * math.cos(-(theta // 2*(i+1)*0.0174))
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(EnemyShot.NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,   1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む

    #レーザービームを発射する関数定義
    def enemy_laser(self,ex,ey,length,speed):
        """
        レーザービームを発射する関数定義
        
        ex,ey=敵の座標\\
        length=レーザーの長さ\\
        speed=レーザーのスピード(数値がマイナスで右方向に発射)
        """
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(EnemyShot.LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -(speed),0,    1,1,1,   0,0,0,    speed,0,0,  0, number * 2 ,PRIORITY_BOSS_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #サイン弾を射出する関数定義 
    def enemy_sin_bullet(self,ex,ey,timer,speed,intensity):
        """
        サイン弾を射出
        
        ex,ey=敵の座標\\
        timer=時間(三角関数系で使用)\\
        speed=速度(三角関数系で使用)\\
        intensity=振れ幅(三角関数系で使用)
        """
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.SIN,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0, 0,0,  1,1,1, 1,1,   timer,speed,intensity,  0, 0,   0,PRIORITY_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む

    #ボス用のレッドレーザービームを発射する関数定義
    def enemy_red_laser(self,ex,ey,length,speed):
        """
        ボス用のレッドレーザービームを発射する関数定義
        
        ex,ey=敵の座標\\
        length=レーザーの長さ\\
        speed=レーザーのスピード(数値がマイナスで右方向に発射)
        """
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(EnemyShot.RED_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #ボス用のグリーンレーザービームを発射する関数定義
    def enemy_green_laser(self,ex,ey,length,speed):
        """
        ボス用のグリーンレーザービームを発射
        
        ex,ey=敵の座標\\
        length=レーザーの長さ\\
        speed=レーザーのスピード(数値がマイナスだと右方向に発射)
        """
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(EnemyShot.GREEN_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,  0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #敵ホーミングレーザーの発射
    def enemy_homing_laser(self,ex,ey,performance):
        """
        敵ホーミングレーザーの発射
        
        ex,ey=敵の座標\\
        performance=レーザーの誘導性能(20くらいが良いかも!?)
        """
        if len(self.enemy_shot) < 800:
            posy = 60
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(EnemyShot.HOMING_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   0.5,0.5,   1,    1,1,   0,performance,0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 8,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)

    #敵アップレーザーの発射
    def enemy_up_laser(self,ex,ey,vx,vy,expansion,width_max,height_max):
        """
        敵アップレーザーの発射
        
        ex,ey=敵の座標\\
        vx,vy=速度ベクトル\\
        expansion=広がっていくドット数\\
        width_max=アップレーザーの横幅の最大値\\
        height_max=アップレーザーの縦幅の最大値
        """
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            division_type         = 0
            division_count        = 0
            division_count_origin = 0
            division_num          = 0
            new_enemy_shot.update(EnemyShot.UP_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
            self.enemy_shot.append(new_enemy_shot)

    #敵ダウンレーザーの発射
    def enemy_down_laser(self,ex,ey,vx,vy,expansion,width_max,height_max):
        """
        敵ダウンレーザーの発射
        
        ex,ey=敵の座標\\
        vx,vy=速度ベクトル\\
        expansion=広がっていくドット数\\
        width_max=ダウンレーザーの横幅の最大値\\
        height_max=ダウンレーザーの縦幅の最大値
        """
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            division_type         = 0
            division_count        = 0
            division_count_origin = 0
            division_num          = 0
            new_enemy_shot.update(EnemyShot.DOWN_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
            self.enemy_shot.append(new_enemy_shot)

    #ミサイルリスト内から同じタイプのミサイルが何発存在するのか数をカウントする関数定義
    def count_missile_type(self,missile_type1,missile_type2,missile_type3,missile_type4):
        """
        ミサイルリスト内から同じタイプのミサイルが何発存在するのか数をカウントする
        
        missile_type1,missile_type2,missile_type3,missile_type4=引数は0を代入してこのメソッドを呼んでください\\
        帰り値 quantity=現時点で同じタイプのミサイルが存在する数値が戻ってきます
        """
        quantity = 0
        self.type_check_quantity = 0
        missile_count = len(self.missile)#ミサイルリストの総数を数える
        for i in range (missile_count):
            if     self.missile[i].missile_type == missile_type1 or self.missile[i].missile_type == missile_type2\
                or self.missile[i].missile_type == missile_type3 or self.missile[i].missile_type == missile_type4:
                quantity += 1#変数（個数）を１増やして勘定していく
            
            self.type_check_quantity = quantity
        return (self,quantity)

    #与えられたcx,cy座標を元に敵の全x,y座標を調べてx座標が一致した敵が存在するか調べる関数(サーチレーザー向け)
    def search_laser_enemy_cordinate(self,cx,cy):
        """
        与えられたcx,cy座標を元に敵の全x,y座標を調べてx座標が一致した敵が存在するか調べる関数(サーチレーザー向け)
        
        cx,cy=調べる元となる座標
        """
        self.search_laser_flag = 0       #x軸が一致した敵を発見したかどうかのフラグ
        self.search_laser_y_direction = 0 #上下どちらかに曲げるかの反転値 -1=上方向 1=下方向
        enemy_count = len(self.enemy)
        for i in range (enemy_count):
            if -2 <= self.enemy[i].posx - cx <= 2:#敵の中でx座標がほぼ一致したものを発見したのなら
                if self.enemy[i].posy >= cy:#レーザーのy座標より敵のy座標が大きいのなら発見フラグを立てy軸の向きを加算(下方向)にする
                    self.search_laser_flag = 1
                    self.search_laser_y_direction = 1
                else:#レーザーのy座標より敵のy座標が小さいのなら発見フラグを立てy軸の向きを減算(上方向)にする
                    self.search_laser_flag = 1
                    self.search_laser_y_direction = -1
        return()

    #与えられたcx,cy座標を元に敵の全x,y座標から距離を求め一番近い敵の座標を調べる関数(ホーミングミサイル向け)
    def search_homing_missile_enemy_cordinate(self,cx,cy):
        """
        与えられたcx,cy座標を元に敵の全x,y座標から距離を求め一番近い敵の座標を調べる関数(ホーミングミサイル向け)
        
        cx,cy=調べる元となる座標
        """
        self.search_homing_missile_flag = 0 #狙い撃つ敵を発見したかどうかのフラグ 0=未発見 1=発見
        self.search_homing_missile_tx = 200 #狙い撃つ敵のx座標が入る TargetX
        self.search_homing_missile_ty =  60 #狙い撃つ敵のy座標が入る TargetY
        self.min_distance = 200           #現時点での計算して求めた敵までの距離の最小値が入る
        enemy_count = len(self.enemy)
        for i in range (enemy_count):
            #目標までの距離を求める dに距離が入る
            d = abs(math.sqrt((self.enemy[i].posx - cx) * (self.enemy[i].posx - cx) + (self.enemy[i].posy - cy) * (self.enemy[i].posy - cy)))
            if self.min_distance > d:
                self.min_distance = d#敵までの距離の最小値を更新したので記録する
                self.search_homing_missile_tx = self.enemy[i].posx#狙い撃つ敵の座標をtx,tyに代入する
                self.search_homing_missile_ty = self.enemy[i].posy
                
                self.search_homing_missile_flag = 1 #狙い撃つ敵を発見したのでフラグを立てる
            
        return()

    #背景(BGタイルマップのキャラチップ)を取得する
    def get_bg_chip(self,x,y,bg_chip):
        """
        背景(BGタイルマップのキャラチップ)を取得する
        
        x,y=座標値(x=0~160)(y=0~120)\\
        bg_chip=キャラチップのアスキーコード
        """
        self.bgx = (((self.scroll_count // 8) -256) // 2) + x // 8
        #x座標を8で割った切り捨て値がBGマップでのx座標となる
        #(self.scroll_count // 8) -256) // 2)      この数値がスクロールした分x座標オフセット値となる
        
        self.bgy = (y // 8)
        #Y座標を8で割った切り捨て数値がBGマップでのy座標となる
        #bgxがMAPの外に存在するときは強制的にbgxを0にしちゃう(マイナスの値や256以上だとエラーになるため)
        if  0 > self.bgx:
            self.bgx = 0
        if self.bgx > 255:
            self.bgx = 0
        #bgyがMAPの外に存在するときは強制的にbgyを一番上の座標か一番下の座標にしちゃう(マイナスの値や15より大きいと（まぁ他の面のマップデータにアクセスするのでエラーにはなりませんが・・・）だとエラーになるため)
        if self.bgy < 0:
            self.bgy = 0
        if self.bgy > 255:
            self.bgy = 255
        
        if self.stage_loop == 2:
            self.bgy += 16 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        elif self.stage_loop == 3:
            self.bgy += 32 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
        return(self,x,y,bg_chip)

    #背景(BGタイルマップのキャラチップ)を取得し、更に障害物かどうかを判別する
    def check_bg_collision(self,x,y,bg_chip,collision_flag):
        """
        背景(BGタイルマップのキャラチップ)を取得し、更に障害物かどうかを判別する
        
        x,y=座標値(x=0~160)(y=0~120)\\
        bg_chip=キャラチップのアスキーコード\\
        collision_flag=コリジョンフラグ\\
        
        帰り値として
        bg_chip=キャラチップのアスキーコード\\
        collision_flag =(0=当たってない 1=接触しちゃった！)が戻ってくる
        """
        self.collision_flag = 0#コリジョンフラグ（障害物と接触したかどうかのフラグ）を初期化 (0=当たってない 1=接触しちゃった！)
        
        self.bgy = y // 8#bgy座標はy座標を8で割った切り捨て値としてその位置にあるＢＧ（バックグラウンド（背景チップ））をチェックする
        self.bgx = (((self.scroll_count // 8) -256) // 2) + x // 8
        #(self.scroll_count // 8) -256) // 2)=x=0      現在表示されている画面のＸ座標値0がＢＧマップのこの値と同じになる
        #bgxがMAPの外に存在するときは強制的にbgxを0にしちゃう(マイナスの値や256以上だとエラーになるため)
        if  0 > self.bgx:
            self.bgx = 0
        if self.bgx > 255:
            self.bgx = 0
        
        #bgyがMAPの外に存在するときは強制的にbgyを一番上の座標か一番下の座標にしちゃう(マイナスの値や15より大きいと（まぁ他の面のマップデータにアクセスするのでエラーにはなりませんが・・・）だとエラーになるため)
        if  0 > self.bgy:
            self.bgy = 0
        if self.bgy > 255:
            self.bgy = 255
        
        if self.stage_loop == 2:
            self.bgy += 16 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        elif self.stage_loop == 3:
            self.bgy += 32 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        
        self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
        #bgx,bgyの座標のキャラチップナンバーをゲット！
        
        if (self.bg_chip // 4) >= self.bg_obstacle_y: #(bg_chip // 4)でキャラチップのＹ座標になるんです
            self.collision_flag = 1             #y座標がbg_obstacle_yより大きかったら障害物に当たったとみなす
        
        return(self,x,y,bg_chip,collision_flag)

    #背景マップチップに書き込む関数x,yはキャラ単位 x=(0~255) y=(0~255) n=(0~255)マップチップナンバー
    def write_map_chip(self,x,y,n):
        """
        背景マップチップに書き込む関数
        
        x,yはキャラ単位 x=(0~255) y=(0~255)\\
        n=(0~255)マップチップナンバー
        """
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + ((self.stage_loop - 1)* 16 * self.height_screen_num),n)

    #背景マップチップを消去する(NULLチップナンバーを書き込む) x,yはキャラ単位 x=(0~255) y=(0~15)
    def delete_map_chip(self,x,y):
        """
        背景マップチップを消去する(NULLチップナンバーを書き込む)
        
        x,yはキャラ単位 x=(0~255) y=(0~15)
        """
        # func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16,0)#マップチップを消去する（0=何もない空白）を書き込む
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16 * self.height_screen_num,self.null_bg_chip_num)

    #背景(BGタイルマップのキャラチップ)を取得する (8方向フリースクロール専用)
    def get_bg_chip_free_scroll(self,x,y,bg_chip):
        """
        背景(BGタイルマップのキャラチップ)を取得する (8方向フリースクロール専用)
        
        x,y=座標値(x=0~160)(y=0~120)\\
        bg_chip=キャラチップのアスキーコード
        """
        #x座標を8で割った切り捨て値がBGマップでのx座標となる
        self.bgx = int(self.scroll_count         // 8 % (256 -20)) + x // 8
        
        #Y座標を8で割った切り捨て値がBGマップでのy座標となる
        self.bgy = int(self.vertical_scroll_count  // 8 % 256) + y // 8
        
        #bgx,bgyのクリッピング処理
        #bgxがMAPの外に存在するときは強制的にbgxを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
        if  self.bgx < 0:
            self.bgx = 0
        if self.bgx > 255:
            self.bgx = 255
        #bgyがMAPの外に存在するときは強制的にbgyを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
        if self.bgy < 0:
            self.bgy = 0
        if self.bgy > 255:
            self.bgy = 255
        
        self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
        return(self,x,y,bg_chip)

    #背景マップチップに書き込む関数(8方向フリースクロール専用)x,yはキャラ単位 x=(0~255) y=(0~255) n=(0~255)マップチップナンバー
    def write_map_chip_free_scroll(self,x,y,n):
        """
        背景マップチップに書き込む関数(8方向フリースクロール専用)
        
        x,yはキャラ単位 x=(0~255) y=(0~255)\\
        n=(0~255)マップチップナンバー
        """
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y,n)#マップチップナンバーnを座標x,yに書き込む

    #背景マップ(BG)にアクセスする時に使用するself.bgx,self.bgyを0~255の間に収めるようにクリッピング処理する(-1とか256でタイルマップにアクセスするとエラーが出るため)
    def clip_bgx_bgy(self):
        """
        背景マップ(BG)にアクセスする時に使用するself.bgx,self.bgyを0~255の間に収めるようにクリッピング処理する(-1とか256でタイルマップにアクセスするとエラーが出るため)
        """
        #bgx,bgyのクリッピング処理
        #bgxがMAPの外に存在するときは強制的にbgxを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
        if  self.bgx < 0:
            self.bgx = 0
        if self.bgx > 255:
            self.bgx = 255
        #bgyがMAPの外に存在するときは強制的にbgyを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
        if self.bgy < 0:
            self.bgy = 0
        if self.bgy > 255:
                self.bgy = 255  

    #背景タイルマップ(BG)に埋め込まれたボス用移動座標を調べてリストに登録していく関数
    def search_boss_bg_move_point(self):
        """
        背景タイルマップ(BG)に埋め込まれたボス用移動座標を調べてリストに登録していく
        """
        mpx,mpy     = 0,0 #サーチ用の座標を初期化
        point_num   = 0   #移動ポイント数の初期化
        control_num = 0   #制御点ポイント数の初期化
        
        if self.stage_loop == 2:
            mpy += 16 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        elif self.stage_loop == 3:
            mpy += 32 * self.height_screen_num #縦1置画面分のbgy値は16なので周回数を考慮して縦画面数分掛けたものを代入する
        
        for w in range(255): #x軸方向は0~255まで調べ上げていく
            for h in range(WINDOW_H // 8 * self.height_screen_num): #y軸方向は15×縦スクロールする画面数ぶん調べ上げていく
                chip_num = func.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w,mpy + h) #BGキャラチップのナンバー取得
                if chip_num == MOVE_POINT_BG_NUM: #もし移動点だったのなら
                    func.delete_map_chip(self,mpx + w,mpy + h) #「移動点」マップチップを消去する
                    
                    #一つ右隣にあるチップナンバーが「移動点の連番」なので取得する
                    serial_num = func.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w + 1,mpy + h) #移動点の連番を取得
                    serial_num -= ZERO_BG_CHR_NUM
                    self.boss_bg_move_point.append([int(serial_num),w,h])
                    point_num += 1 #移動ポイント数をインクリメント
                    func.delete_map_chip(self,mpx + w + 1,mpy + h) #「移動点の連番」マップチップを消去する
                    
                elif chip_num == CONTROL_POINT_NUM: #もし制御点だったのなら
                    func.delete_map_chip(self,mpx + w,mpy + h) #「制御点」マップチップを消去する
                    
                    #一つ右隣にあるチップナンバーが「制御点の連番」なので取得する
                    serial_num = func.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w + 1,mpy + h) #移動点の連番を取得
                    serial_num -= ZERO_BG_CHR_NUM
                    self.boss_bg_move_control_point.append([int(serial_num),w,h])
                    control_num += 1 #制御ポイント数をインクリメント
                    func.delete_map_chip(self,mpx + w + 1,mpy + h) #「制御点の連番」マップチップを消去する
        
        self.boss_bg_move_point.sort()         #「移動点の連番」を基準にソートする sort()はリスト型のメソッドだよん
        self.boss_bg_move_control_point.sort() #「制御点の連番」を基準にソートする sort()はリスト型のメソッドだよん

    #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数
    def level_up_my_shot(self):
        """
        自機ショットの経験値を調べ可能な場合レベルアップをさせる
        """
        if self.shot_exp > SHOT_EXP_MAXIMUM:  #自機ショットの経験値は最大経験値を超えないように補正してやります
            self.shot_exp = SHOT_EXP_MAXIMUM
        if self.shot_exp < 0:              #自機ショットの経験値は0より小さくならないよう補正します
            self.shot_exp = 0             #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
        
        self.shot_level            = self.shot_table_list[self.shot_exp][0] #テーブルリストを参照して経験値に対応したショットレベルを代入する
        self.shot_speed_magnification = self.shot_table_list[self.shot_exp][1] #テーブルリストを参照して経験値に対応したショットスピード倍率を代入する
        self.shot_rapid_of_fire      = self.shot_table_list[self.shot_exp][2] #テーブルリストを参照して経験値に対応したショット連射数を代入する

    #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数
    def level_up_my_missile(self):
        """
        自機ミサイルの経験値を調べ可能な場合レベルアップをさせる
        """
        if self.missile_exp > MISSILE_EXP_MAXIMUM:  #自機ミサイルの経験値は最大経験値を超えないように補正してやります
            self.missile_exp = MISSILE_EXP_MAXIMUM
        if self.missile_exp < 0:              #自機ミサイルの経験値は0より小さくならないよう補正します
            self.missile_exp = 0             #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
        
        self.missile_level            = self.missile_table_list[self.missile_exp][0] #テーブルリストを参照して経験値に対応したミサイルレベルを代入する
        self.missile_speed_magnification = self.missile_table_list[self.missile_exp][1] #テーブルリストを参照して経験値に対応したミサイルスピード倍率を代入する
        self.missile_rapid_of_fire      = self.missile_table_list[self.missile_exp][2] #テーブルリストを参照して経験値に対応したミサイル連射数を代入する

    #敵編隊出現時、現在の編隊IDナンバーとIDナンバーに対応した編隊数、そして現在の生存編隊数をenemy_formationクラスに登録する関数
    def record_enemy_formation(self,num):
        """
        敵編隊出現時、現在の編隊IDナンバーとIDナンバーに対応した編隊数、そして現在の生存編隊数をenemy_formationクラスに登録する
        
        num = 編隊ナンバー
        """
        #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
        new_enemy_formation = Enemy_formation()
        new_enemy_formation.update(self.current_formation_id,num,num,num)
        self.enemy_formation.append(new_enemy_formation)
        self.current_formation_id += 1             #編隊IDを1増加させ次の編隊IDにするのです

    #敵破壊時、編隊ＩＤをみて編隊リストに登録されていた撃墜するべき総数を減少させ、全滅させたらフラグを立てて戻ってくる関数
    def check_enemy_formation_shoot_down_number(self,id):
        """
        敵破壊時、編隊ＩＤをみて編隊リストに登録されていた撃墜するべき総数を減少させ、全滅させたらフラグを立てて戻ってくる
        
        id=編隊id 編隊を全滅させたのならself.enemy_extermination_flag = FLAG_ONとなる
        """
        enemy_formation_count = len(self.enemy_formation)
        for i in reversed(range(enemy_formation_count)): #インスタンスを消去するのでreversedで昇順ではなく降順で調べていきます
            if id == self.enemy_formation[i].formation_id: #調べるidとリストに登録されているidが同じだったら
                self.enemy_formation[i].shoot_down_number -= 1        #撃墜するべき編隊総数を1減らす
                self.enemy_formation[i].on_screen_formation_number -= 1 #それと同時に撃墜されたことで画面上に存在する編隊も1機減るのでこちらも1減らす
                if self.enemy_formation[i].shoot_down_number == 0: #もし編隊をすべて撃墜したのなら
                    self.enemy_extermination_flag = FLAG_ON #殲滅フラグを建てる
                    del self.enemy_formation[i]     #該当した編隊リストは必要ないのでインスタンスを消去する
                    break                       #もうこれ以上リストを調べ上げる必要はないのでbreakしてループから抜け出す

    #敵が画面から消える時、編隊ＩＤをみて編隊リストに登録されていた「画面上に存在する編隊数」を減少させ0になったらインスタンスを破棄する関数です
    #まぁ所属する編隊idナンバーを見て編隊がもう存在しなかったリストからインスタンスを破棄するって事ですわん
    def check_enemy_formation_exists(self,id):
        """
        敵が画面から消える時、編隊ＩＤをみて編隊リストに登録されていた「画面上に存在する編隊数」を減少させ0になったらインスタンスを破棄する
        
        id=編隊id
        """
        enemy_formation_count = len(self.enemy_formation)
        for i in reversed(range(enemy_formation_count)): #インスタンスを消去するのでreversedで昇順ではなく降順で調べていきます
            if id == self.enemy_formation[i].formation_id: #調べるidとリストに登録されているidが同じだったら
                self.enemy_formation[i].on_screen_formation_number -= 1 #画面上に存在する編隊数を1機減らす
                if self.enemy_formation[i].on_screen_formation_number == 0: #もし編隊がすべて画面に存在しないのなら
                    del self.enemy_formation[i]     #該当した編隊リストは必要ないのでインスタンスを消去する
                    break                       #もうこれ以上リストを調べ上げる必要はないのでbreakしてループから抜け出す

    #敵を破壊した後の処理
    def enemy_destruction(self,e):
        """
        敵を破壊した後の処理
        
        e=敵リストenemyのインデックス値となります 例enemy[e]\\
        ループ内から呼ばれることを想定してるためです
        """
        # 引数のeは敵リストenemyのインデックス値となります 例enemy[e]
        #ここから敵機破壊処理となります###################################################
        #自機ショットや自機ミサイル、クローショットが敵に当たり敵の耐久力が0以下になったらその座標に爆発を生成する
        if   self.enemy[e].enemy_size == E_SIZE_NORMAL:         #標準的な大きさの敵8x8ドットの敵を倒したとき
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.enemy[e].posx,self.enemy[e].posy,0,0,10,self.return_bullet,0,  1,1)
            self.explosions.append(new_explosion)      
        elif self.enemy[e].enemy_size == E_SIZE_MIDDLE32:       #スクランブルハッチを倒したとき
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy,0,0,10*2,self.return_bullet,0,  1,1)
            self.explosions.append(new_explosion)
        elif self.enemy[e].enemy_size == E_SIZE_MIDDLE32_Y_REV: #天井のスクランブルハッチを倒したとき
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy,0,0,10*2,self.return_bullet,0,  1,-1)
            self.explosions.append(new_explosion)
        elif self.enemy[e].enemy_size == E_SIZE_HI_MIDDLE53:    #重爆撃機タイプを倒したとき 大型爆発パターン2個育成
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4 ,self.enemy[e].posy + 4,0,0,10*2,self.return_bullet,0,  1,1)
            self.explosions.append(new_explosion)
            new_explosion = Explosion()
            new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 28,self.enemy[e].posy + 4,0,0,10*2,self.return_bullet,0,  1,1)
            self.explosions.append(new_explosion)
        
        #敵編隊殲滅フラグを強制的に初期化する
        self.enemy_extermination_flag = FLAG_OFF
        #編隊機の場合は撃墜するべき総数に達したのかどうかを調べ上げる（編隊全部殲滅した？）
        if self.enemy[e].formation_id != 0:#編隊機の場合は以下の処理をする
            func.check_enemy_formation_shoot_down_number(self,self.enemy[e].formation_id) 
        
        #早回しの条件チェック
        if self.enemy_extermination_flag == FLAG_ON and self.fast_forward_destruction_num !=0: #もし編隊殲滅フラグON,「敵編隊殲滅必要数」が0以外ならば
            self.fast_forward_destruction_num -= 1                               #1編隊を殲滅させたので「敵編隊殲滅必要数」を1減少さる
            for i in range(self.fast_forward_destruction_num):
                #次に出現する敵のタイマーをfast_forward_destruction_num分先まで早回し時のパラメーター分減少させる(全体的に編隊群が速く出現する感じ)
                #ただし減少させたタイマー値が現在のタイマー値であるstage_countより小さくなってしまうとこれ以降のイベントが実行されなくなるので
                #早回し処理は行わずそのままの値にしておく
                if self.stage_count < self.event_list[self.event_index + i][0] - self.fast_forward_destruction_count:
                    self.event_list[self.event_index + i][0] -= self.fast_forward_destruction_count
            
            if self.fast_forward_destruction_num == 0: #「敵編隊殲滅必要数」が0になったら・・・・
                self.add_appear_flag   = FLAG_ON #「早回し敵発生フラグ」をonにする
                self.fast_forward_flag = FLAG_ON #早回し実績取得用にフラグを立てる
        
        #アイテム育成############################################################
        if   (self.enemy[e].formation_id   == 0 and self.enemy[e].item == E_SHOT_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_SHOT_POW):
            #ショットパワーアップアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            if self.appeared_shot_pow < self.inc_shot_exp_medal: #現時点で出現したショットパワーカプセルの数(appeared_shot_pow)が事前にゲット出来るショットアイテム数(inc_shot_exp_medal)より小さい場合は・・・
                born_item = ITEM_SCORE_STAR    #スコアスター(得点アイテム)を育成
            else:
                born_item = ITEM_SHOT_POWER_UP #ショットアイテムを育成
            new_obtain_item.update(born_item,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   1,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
            self.appeared_shot_pow += 1 #得点アイテムでもショットパワーカプセルでもカプセルを出したことには変わりないので「出現したショットカプセル数」を1インクリメントする
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_MISSILE_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_MISSILE_POW):
            #ミサイルパワーアップアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_MISSILE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,1,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SHIELD_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_SHIELD_POW):
            #シールドパワーアップアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_SHIELD_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_CLAW_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_CLAW_POW):
            #クローアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_CLAW_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_TRIANGLE_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_TRIANGLE_POW):
            #トライアングルアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_TRIANGLE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.3,0,   8,8,   1,   0.9,  0.3,   0,0,  0.5,0,15, 0,0,   1,1,1,  0,0,2 * 60, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_TAIL_SHOT_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_TAIL_SHOT_POW):
            #テイルショットアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_TAIL_SHOT_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_PENETRATE_ROCKET_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_PENETRATE_ROCKET_POW):
            #ペネトレートロケットアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_PENETRATE_ROCKET_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SEARCH_LASER_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_SEARCH_LASER_POW):
            #サーチレーザーアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_SEARCH_LASER_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_HOMING_MISSILE_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_HOMING_MISSILE_POW):
            #ホーミングミサイルアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_HOMING_MISSILE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)
        elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SHOCK_BUMPER_POW) or (self.enemy_extermination_flag == FLAG_ON and self.enemy[e].item == E_SHOCK_BUMPER_POW):
            #ショックバンパーアイテムを持っているのならアイテムを育成する
            new_obtain_item = Obtain_item()
            new_obtain_item.update(ITEM_SHOCK_BUMPER_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
            self.obtain_item.append(new_obtain_item)

    #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数
    def enemy_get_bezier_curve_coordinate(self,enemy_type,i): #enemy_type=敵のタイプナンバー,i=インデックスナンバ値         
        """
        敵をベジェ曲線で移動させるために必要な座標をリストから取得する
        
        enemy_type=敵のタイプナンバー\\
        i=インデックスナンバ値 
        """
        self.enemy_move_data = self.enemy_move_data_list[enemy_type][1]
        self.enemy[i].ax           = self.enemy_move_data[self.enemy[i].move_index][0]#リストから新たな移動元座標を登録する
        self.enemy[i].ay           = self.enemy_move_data[self.enemy[i].move_index][1]
        self.enemy[i].dx           = self.enemy_move_data[self.enemy[i].move_index][2]#リストから新たな移動先座標を登録する
        self.enemy[i].dy           = self.enemy_move_data[self.enemy[i].move_index][3]
        self.enemy[i].qx           = self.enemy_move_data[self.enemy[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
        self.enemy[i].qy           = self.enemy_move_data[self.enemy[i].move_index][5]
        
        self.enemy[i].obj_totaltime  = self.enemy_move_data[self.enemy[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する
        
        self.enemy[i].move_speed    = self.enemy_move_data[self.enemy[i].move_index][7]#リストから移動スピードを取得し登録する
        self.enemy[i].acceleration   = self.enemy_move_data[self.enemy[i].move_index][8]#リストから加速度を取得し登録する
        
        self.enemy[i].attack_method  = self.enemy_move_data[self.enemy[i].move_index][9]#リストから攻撃方法を取得し登録する

    #敵17をベジェ曲線で移動させるために必要な座標をリストから取得する関数
    def enemy17_get_bezier_curve_coordinate(self,i):
        """
        敵17をベジェ曲線で移動させるために必要な座標をリストから取得する
        
        i=enemyクラスのインデックス値(ループ処理中から呼ばれるためです)
        """
        self.enemy[i].ax           = self.enemy_move_data17[self.enemy[i].move_index][0]#リストから新たな移動元座標を登録する
        self.enemy[i].ay           = self.enemy_move_data17[self.enemy[i].move_index][1]
        self.enemy[i].dx           = self.enemy_move_data17[self.enemy[i].move_index][2]#リストから新たな移動先座標を登録する
        self.enemy[i].dy           = self.enemy_move_data17[self.enemy[i].move_index][3]
        self.enemy[i].qx           = self.enemy_move_data17[self.enemy[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
        self.enemy[i].qy           = self.enemy_move_data17[self.enemy[i].move_index][5]
        
        self.enemy[i].obj_totaltime  = self.enemy_move_data17[self.enemy[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する
        
        self.enemy[i].move_speed    = self.enemy_move_data17[self.enemy[i].move_index][7]#リストから移動スピードを取得し登録する
        self.enemy[i].acceleration   = self.enemy_move_data17[self.enemy[i].move_index][8]#リストから加速度を取得し登録する
        
        self.enemy[i].attack_method  = self.enemy_move_data17[self.enemy[i].move_index][9]#リストから攻撃方法を取得し登録する

    #ボスにショットを当てた後の処理(ドットパーティクル育成、背景の星をオマケで追加,ボス本体のHPが0以下になった時の処理などなど)
    def boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy): #e=ボスのクラスのインデックス値 hit_x,hit_y=パーティクル育成座標 hit_vx,hit_vy=パーティクル育成時に使用する散らばり具合の速度
        """
        ボスにショットを当てた後の処理(ドットパーティクル育成、背景の星をオマケで追加,ボス本体のHPが0以下になった時の処理などなど)
        
        e=ボスのクラスのインデックス値\\
        hit_x,hit_y=パーティクルを育成する座標\\
        hit_vx,hit_vy=パーティクル育成時に使用する散らばり具合の速度
        """
        #ドットパーティクル生成
        if len(self.particle) < 1000: #パーティクル総数が1000以下なら発生させる
            for _number in range(10):
                new_particle = Particle()
                new_particle.update(PARTICLE_DOT,PRIORITY_FRONT,hit_x+4,hit_y+4,func.s_rndint(self,0,1),random() * 2 - 0.5 + hit_vx / 2,random() * 2 - 1 +hit_vy / 2,func.s_rndint(self,5,20),0,func.s_rndint(self,1,14),0,0,0,0,0,0,0,0,0, 0,0)
                self.particle.append(new_particle)
                #update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,hit_x,hit_y,hit_vx / 2,hit_vy / 2, 0,0,0)
        
        #オマケで背景の星も追加するぞ～～☆彡
        if len(self.stars) < 600:
            new_stars = Star()
            new_stars.update(WINDOW_W - 1,func.s_rndint(self,0,WINDOW_H),func.s_rndint(self,1,50))
            self.stars.append(new_stars)
        
        if self.boss[e].main_hp <= 0:#ボス本体のHPが0以下になったのなら
            for _number in range(60):#爆発パターンを60個育成
                new_explosion = Explosion()
                new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[e].posx + self.boss[e].width / 2 + func.s_rndint(self,0,50) -25,self.boss[e].posy + self.boss[e].height / 2 + func.s_rndint(self,0,50) -25,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                self.explosions.append(new_explosion)
            
            #もうボスは爆発開始しちゃうので当たり判定は無くなり無敵状態となる！（爆発して無敵状態になるとは・・・矛盾しておる・・・）
            self.boss[e].invincible = 1
            #スコア加算（あとあといろんなスコアシステム実装する予定だよ）
            self.score += 1
            
            #リプレイ再生時は飛ばす処理
            if self.replay_status != REPLAY_PLAY: #リプレイ再生している時は撃破数加算処理＆ボスノーダメージ実績チェックを行わない
                self.boss_number_of_defeat[self.stage_number] += 1 #ボス撃破数を1増やします
                if self.boss_battle_damaged_flag == FLAG_OFF: #ボスをノーダメージで破壊したのなら///
                    self.no_damage_destroy_boss_flag = FLAG_ON #ノーダメージでボスを破壊した！フラグをON（なんか二度手間だなぁ・・・・)
                
                if self.stage_battle_damaged_flag == FLAG_OFF: #ステージをノーダメージでクリアしたのなら
                    self.no_damage_stage_clear_flag  = FLAG_ON #ノーダメージステージクリアフラグをON
                
                if self.my_shield == 1: #ボスを破壊した時点でシールド残り値が１だったなら
                    self.endurance_one_cleared_flag = FLAG_ON #残りシールド１でギリギリクリアフラグをON
                
                if self.boss_battle_time <=  20 * 60: #ボスを20秒以内で倒したのなら
                    self.boss_instank_kill_flag = FLAG_ON #ボスを瞬殺したフラグをON
                
                if func.check_destroy_all_boss_parts(self) == True: #ボスのパーツをすべて破壊したのなら
                    self.destroy_all_boss_parts_flag = FLAG_ON #ボスのパーツを全部破壊したフラグをON
            
            #ゲームステータス(状態遷移)を「SCENE_BOSS_EXPLOSION」ボスキャラ爆発中！にする
            self.game_status = Scene.BOSS_EXPLOSION           
            #ボスの状態遷移フラグステータスを「BOSS_STATUS_EXPLOSION_START」ボス撃破！爆発開始！にしてやる
            self.boss[e].status = BOSS_STATUS_EXPLOSION_START

    #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数
    def boss_get_bezier_curve_coordinate(self,i):
        """
        ボスをベジェ曲線で移動させるために必要な座標をリストから取得する
        
        i=bossクラスのインデックス値(ループ処理中から呼ばれるためです)
        """
        self.boss[i].ax           = self.boss_move_data1[self.boss[i].move_index][0]#リストから新たな移動元座標を登録する
        self.boss[i].ay           = self.boss_move_data1[self.boss[i].move_index][1]
        self.boss[i].dx           = self.boss_move_data1[self.boss[i].move_index][2]#リストから新たな移動先座標を登録する
        self.boss[i].dy           = self.boss_move_data1[self.boss[i].move_index][3]
        self.boss[i].qx           = self.boss_move_data1[self.boss[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
        self.boss[i].qy           = self.boss_move_data1[self.boss[i].move_index][5]
        
        self.boss[i].obj_totaltime  = self.boss_move_data1[self.boss[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する
        
        self.boss[i].speed          = self.boss_move_data1[self.boss[i].move_index][7]#リストから移動スピードを取得し登録する
        self.boss[i].acceleration   = self.boss_move_data1[self.boss[i].move_index][8]#リストから加速度を取得し登録する
        
        self.boss[i].attack_method  = self.boss_move_data1[self.boss[i].move_index][9]#リストから攻撃方法を取得し登録する

    #ボスをベジェ曲線でBG背景マップにマークされた通過ポイント座標をリストから取得する関数
    def boss_bg_move_get_bezier_curve_coordinate(self,i):
        """
        ボスをベジェ曲線でBG背景マップにマークされた通過ポイント座標をリストから取得する
        
        i=bossクラスのインデックス値(ループ処理中から呼ばれるためです)
        """
        self.boss[i].ax           = self.boss_bg_move_point[self.boss[i].move_index][1] * 8         #リストから新たな移動元座標を登録する(8倍してキャラクター単位からドット単位に変換する)
        self.boss[i].ay           = self.boss_bg_move_point[self.boss[i].move_index][2] * 8
        self.boss[i].dx           = self.boss_bg_move_point[self.boss[i].move_index + 1][1] * 8     #リストから新たな移動先座標を登録する(8倍してキャラクター単位からドット単位に変換する)
        self.boss[i].dy           = self.boss_bg_move_point[self.boss[i].move_index + 1][2] * 8
        
        self.boss[i].qx           = self.boss_bg_move_control_point[self.boss[i].move_index][1] * 8 #リストから2次ベジェ曲線用の制御点座標を登録する(8倍してキャラクター単位からドット単位に変換する)
        self.boss[i].qy           = self.boss_bg_move_control_point[self.boss[i].move_index][2] * 8
        
        self.boss[i].obj_totaltime  = 170   #リストから移動に掛けるトータルタイムを取得し登録する
        
        self.boss[i].speed          = 1.0   #リストから移動スピードを取得し登録する
        self.boss[i].acceleration   = 1.0 #リストから加速度を取得し登録する

    #ボスの耐久力バーの表示(ボスの付近にＨＰバーを描画する)
    def display_boss_hp_bar(self,x,y,hp):
        """
        ボスの耐久力バーの表示(ボスの付近にＨＰバーを描画する)
        
        x,y=表示座標\\
        hp=耐久力値
        """
        pyxel.rectb(x-1,y-1, 32+2,3, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
        pyxel.line(x,y, x + hp,y, 8) #赤色の耐久力バーの表示

    #ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)短いタイプ横16ドット
    def display_boss_hp_short_bar(self,x,y,hp):
        """
        ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)短いタイプ横16ドット
        
        x,y=表示座標\\
        hp=耐久力値
        """
        pyxel.line(x,y + 1, x + 12,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
        pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示

    #ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)更に短いタイプ横8ドット
    def display_boss_hp_short2_bar(self,x,y,hp):
        """
        ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)更に短いタイプ横8ドット
        
        x,y=表示座標\\
        hp=耐久力値
        """
        pyxel.line(x,y + 1, x + 4,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
        pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示

    #ゲーム全体でボスをトータル何体破壊したか計算する関数(戻り値num=トータル累計ボス破壊数)
    def total_defeat_boss_num(self):
        """
        ゲーム全体でボスをトータル何体破壊したか計算する関数(戻り値num=トータル累計ボス破壊数)
        
        戻り値num=トータル累計ボス破壊数
        """
        global num 
        num = 0
        for i in range(len(self.boss_number_of_defeat)):
            num += self.boss_number_of_defeat[i]
        
        return(num)

    #ボス撃破時にすべてのボスパーツを破壊したかどうか調べる関数
    #parts1~parts4まで調べ上げます 全てのパーツを破壊したのならTrueを返す、出来てなかったらFalseを返します
    def check_destroy_all_boss_parts(self):
        """
        ボス撃破時にすべてのボスパーツを破壊したかどうか調べる
        
        parts1~parts4まで調べ上げます 全てのパーツを破壊したのならTrueを返す、出来てなかったらFalseを返します
        """
        boss_hit = len(self.boss)
        for i in reversed(range (boss_hit) ):
            if self.boss[i].parts1_flag == 0 and self.boss[i].parts2_flag == 0 and self.boss[i].parts3_flag == 0 and self.boss[i].parts4_flag == 0:
                return(True)
            else:
                return(False)

    #スコア加算処理
    def add_score(self,point):
        """
        スコア加算処理
        
        point=取得得点
        """
        self.score += int(point * self.score_magnification) #スコアをpoint*スコア倍率分加算する(整数値で)

    #バックグラウンド(BG)を表示するときのカメラオフセット座標値を計算する
    def screen_camera_offset(self):
        """
        バックグラウンド(BG)を表示するときのカメラオフセット座標値を計算する
        
        self.camera_offset_yに計算されたカメラオフセット座標値が代入されます
        """
        #WINDOW_H    ゲーム画面の縦幅 (定数です)
        #SHIP_H      自機の縦幅8ドット(定数です)
        #bg_height   BGスクロール面の全体としての縦幅
        #my_y        自機のy座標(BGスクロール面の一番上を0として、そこからの縦の距離)
        self.camera_offset_y = (self.bg_height - WINDOW_H) * self.my_y / (self.bg_height - SHIP_H)

    #ラスタースクロール用のデータの初期化＆生成
    def create_raster_scroll_data(self):
        """
        各ステージ用のラスタスクロール用のデータ群を初期化＆作成します
        """
        if self.stage_number == STAGE_MOUNTAIN_REGION:     #1面STAGE_MOUNTAIN_REGIONのラスタースクロール用の設定値の初期化
            new_raster_scroll = Raster_scroll()
            for i in range(24-1):
                new_raster_scroll = Raster_scroll()
                new_raster_scroll.update(0,RASTER_NORMAL,1,RASTER_SCROLL_ON,  i,23,   0,0,    0,0,    IMG1,    96,112+i,   160,1,    -0.1 -(0.03 * i) ,15,   0,0,0)
                self.raster_scroll.append(new_raster_scroll)  #湖面のラスタースクロール用の横ライン（縦24ライン分）を育成する
            
            for i in range(24-1):
                new_raster_scroll = Raster_scroll()
                new_raster_scroll.update(1,RASTER_NORMAL,1,RASTER_SCROLL_ON,  i,23,  0,0,  0,-80,  IMG1,   96,112+i,   160,1,    -0.05 -(0.01 * i) ,15,    0,0,0)
                self.raster_scroll.append(new_raster_scroll)  #成層圏と大気圏の境目のラスタースクロール用の横ライン（縦24ライン分）を育成する（湖面と同じグラフイックだけど・・）
            
            for i in range(40-1):
                new_raster_scroll = Raster_scroll()
                new_raster_scroll.update(2,RASTER_WAVE,0,RASTER_SCROLL_ON,    i,39,  0,0,   0,-38,  IMG1,   144,72+i,   14*8,1,    -0.35,13,    0,0.01,(i-20)*0.4)
                self.raster_scroll.append(new_raster_scroll)  #雲ウェーブラスタースクロール用の横ライン(縦40ライン分)を育成する
            
        elif self.stage_number == STAGE_VOLCANIC_BELT:      #3面STAGE_VOLCANIC_BELTのラスタースクロール用の設定値の初期化
            new_raster_scroll = Raster_scroll()
            for i in range(16-1):
                new_raster_scroll = Raster_scroll()
                new_raster_scroll.update(0,RASTER_WAVE,0,RASTER_SCROLL_ON,    i,16-1,  0,0,   0,-89,  IMG0,   192,48+i,   6*8,1,    -0.08,13,    0,0.02,i*0.4)
                self.raster_scroll.append(new_raster_scroll)  #火山の湖面ウェーブラスタースクロール用の横ライン(縦16ライン分)を育成する

    #ラスタースクロールの表示のon/off(search_id,flag)
    def disp_control_raster_scroll(self,id,flag):
        """
        ラスタースクロールの表示のon/off(search_id,flag)
        
        search_id=ラスタースクロールクラスに登録したID\\
        flag=(FLAG_OFF=ラスタスクロールを表示しないFLAG_ON=表示する)
        """
        raster_scroll_count = len(self.raster_scroll)
        for i in range(raster_scroll_count): #ラスタースクロールクラスに登録されたインスタンスのdisplayを調べていきます
            if self.raster_scroll[i].scroll_id == id: #scroll_idと調べるidが一致したのなら
                self.raster_scroll[i].display = flag #flag(0=表示しない 1=表示する)を書き込む

    #ランクに応じた数値をリストから取得する
    def get_rank_data(self):
        """
        ランクに応じた数値をリストから取得する
        """
        self.enemy_speed_mag           = self.game_rank_data_list[self.rank][LIST_RANK_E_SPEED_MAG]            #敵スピード倍率をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_speed_mag    = self.game_rank_data_list[self.rank][LIST_RANK_BULLET_SPEED_MAG]        #敵狙い撃ち弾スピード倍率をリストを参照してランク数で取得、変数に代入する
        self.return_bullet_probability = self.game_rank_data_list[self.rank][LIST_RANK_RETURN_BULLET_PROBABILITY] #敵撃ち返し弾発射確率をリストを参照してランク数で取得、変数に代入する
        self.enemy_hp_mag              = self.game_rank_data_list[self.rank][LIST_RANK_E_HP_MAG]               #敵耐久力倍率をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_append       = self.game_rank_data_list[self.rank][LIST_RANK_E_BULLET_APPEND]         #弾追加数をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_interval     = self.game_rank_data_list[self.rank][LIST_RANK_E_BULLET_INTERVAL]        #弾発射間隔減少パーセントをリストを参照してランク数で取得、変数に代入する
        self.enemy_nway_level          = self.game_rank_data_list[self.rank][LIST_RANK_NWAY_LEVEL]             #nWAY弾のレベルをリストを参照してランク数で取得、変数に代入する

    #難易度に応じた数値をリストから取得する
    def get_difficulty_data(self):
        """
        難易度に応じた数値をリストから取得する
        """
        self.start_bonus_shot         = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_SHOT]           #初期ショットボーナスをリストを参照し難易度に合わせて取得、変数に代入する
        self.start_bonus_missile      = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_MISSILE]        #初期ミサイルボーナスをリストを参照し難易度に合わせて取得、変数に代入する
        self.start_bonus_shield       = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_SHIELD]         #初期シールドボーナスをリストを参照し難易度に合わせて取得、変数に代入する
        self.start_claw               = self.game_difficulty_list[self.game_difficulty][LIST_START_CLAW]                #初期クローボーナスをリストを参照し難易度に合わせて取得、変数に代入する
        self.repair_shield            = self.game_difficulty_list[self.game_difficulty][LIST_REPAIR_SHIELD]             #ステージクリア後に回復するシールド値をリストを参照し難易度に合わせて取得、変数に代入する
        self.return_bullet            = self.game_difficulty_list[self.game_difficulty][LIST_RETURN_BULLET]             #撃ち返し弾の有無とありの時の種類をリストを参照し難易度に合わせて取得、変数に代入する
        self.score_magnification      = self.game_difficulty_list[self.game_difficulty][LIST_SCORE_MAGNIFICATION]        #スコア倍率をリストを参照し難易度に合わせて取得、変数に代入する
        self.rank_up_frame            = self.game_difficulty_list[self.game_difficulty][LIST_RANK_UP_FRAME]             #ランク上昇フレーム数をリストを参照し難易度に合わせて取得、変数に代入する
        self.rank                     = self.game_difficulty_list[self.game_difficulty][LIST_START_RANK]                #ゲームスタート時のランク数をリストを参照し難易度に合わせて取得、変数に代入する
        self.invincible_time          = self.game_difficulty_list[self.game_difficulty][LIST_DAMAGE_AFTER_INVINCIBLE_TIME] #被弾後の無敵時間をリストを参照し難易度に合わせて取得、変数に代入する
        self.get_item_invincible_time = self.game_difficulty_list[self.game_difficulty][LIST_GET_ITEM_INVINCIBLE_TIME]    #アイテム取得後の無敵時間をリストを参照し難易度に合わせて取得、変数に代入する
        self.item_erace_bullet_flag   = self.game_difficulty_list[self.game_difficulty][LIST_ITEM_ERACE_BULLET]          #パワーアップアイテムが敵弾を消去するかどうか？のフラグをリストを参照し難易度に合わせて取得、変数に代入する
        self.rank_limit               = self.game_difficulty_list[self.game_difficulty][LIST_RANK_LIMIT]                #ランク数の上限値をリストを参照し難易度に合わせて取得、変数に代入する
        self.return_bullet_start_loop = self.game_difficulty_list[self.game_difficulty][LIST_RETURN_BULLET_START_LOOP]    #撃ち返しを始めてくるループ数をリストを参照し難易度に合わせて取得、変数に代入する
        self.return_bullet_start_stage= self.game_difficulty_list[self.game_difficulty][LIST_RETURN_BULLET_START_STAGE]    #撃ち返しを始めてくるステージ数をリストを参照し難易度に合わせて取得、変数に代入する
        self.rank_down_need_damage    = self.game_difficulty_list[self.game_difficulty][LIST_RANK_DOWN_NEED_DAMAGE]       #1ランクダウンに必要なダメージ数をリストを参照し難易度に合わせて取得、変数に代入する
        self.loop_power_control       = self.game_difficulty_list[self.game_difficulty][LIST_LOOP_POWER_CONTROL]         #次のループに移る時のパワーアップ調整関連の動作の仕方をリストを参照し難易度に合わせて取得、変数に代入する
        self.item_range_of_attraction = self.game_difficulty_list[self.game_difficulty][LIST_ITEM_RANGE_OF_ATTRACTION]    #アイテムを引き寄せる範囲をリストを参照し難易度に合わせて取得、変数に代入する
        self.pow_item_bounce_num      = self.game_difficulty_list[self.game_difficulty][LIST_ITEM_BOUNCE_NUM]            #アイテムの跳ね返り回数をリストを参照し難易度に合わせて取得、変数に代入する

    #ステージデータリストから各ステージの設定データを取り出す
    def get_stage_data(self):
        """
        ステージデータリストから各ステージの設定データを取り出す
        """
        self.start_my_x                   = self.stage_data_list[self.stage_number - 1][ 1] #ステージスタート時の自機の座標(自由に縦スクロールできるステージは背景BGマップ左上を原点としての座標位置となります)
        self.start_my_y                   = self.stage_data_list[self.stage_number - 1][ 2]
        self.bg_obstacle_y                = self.stage_data_list[self.stage_number - 1][ 3] #BG障害物とみなすＹ座標位置をリストを参照して取得、変数に代入する
        self.reference_tilemap            = self.stage_data_list[self.stage_number - 1][ 4] #BGにアクセスするときどのタイルマップを使用するかの数値をリストを参照して取得、変数に代入する
        self.scroll_type                  = self.stage_data_list[self.stage_number - 1][ 5] #スクロールの種類をリストを参照して取得、変数に代入する
        self.star_scroll_flag             = self.stage_data_list[self.stage_number - 1][ 6] #背景のスクロールする星々を表示するかのフラグをリストを参照して取得、変数に代入する
        self.raster_scroll_flag           = self.stage_data_list[self.stage_number - 1][ 7] #背景のラスタースクロールを表示するかのフラグをリストを参照して取得、変数に代入する
        self.disp_flag_bg_front           = self.stage_data_list[self.stage_number - 1][ 8] #BG背景(手前)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
        self.disp_flag_bg_middle          = self.stage_data_list[self.stage_number - 1][ 9] #BG背景(中間)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
        self.disp_flag_bg_back            = self.stage_data_list[self.stage_number - 1][10] #BG背景(奥)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
        self.atmospheric_entry_spark_flag = self.stage_data_list[self.stage_number - 1][11] #大気圏突入時の火花を発生させるかどうかのフラグをリストを参照して取得、変数に代入する
        self.null_bg_chip_num             = self.stage_data_list[self.stage_number - 1][12] #背景マップチップを消去するときに使うチップ番号をリストを参照して取得、変数に代入する
        self.bg_height                    = self.stage_data_list[self.stage_number - 1][13] #縦自由スクロールステージにおける背景の縦の高さ(BackGroundHeight)(自機はこのドット分だけBGマップを縦方向に自由に移動できると考えてくださいですの)をリストを参照して取得、変数に代入する
        self.height_screen_num            = self.stage_data_list[self.stage_number - 1][14] #縦の画面数をリストを参照して取得、変数に代入する(MOUNTAIN_REGIONみたいなフリースクロールステージなどはダミー値の9999が入る)
        self.bg_enemy_bone_type           = self.stage_data_list[self.stage_number - 1][15] #背景BGスクロールで敵をどのように出現させるかどうかのバリエーション

    #ランクダウンさせる関数
    def rank_down(self):
        """
        ランクダウンさせる
        """
        if self.rank > 0: #ランク数が0より大きいのならば
            self.rank -= 1      #ランク数をデクリメント
            func.get_rank_data(self) #ランク数が変化したのでランク数をもとにしたデータをリストから各変数に代入する関数の呼び出し

    #0~9の範囲の乱数関数
    def rnd0_9(self):
        """
        0~9の範囲の乱数関数
        
        帰り値として0~9の整数の乱数が戻ってきます
        """
        global num
        num = self.rnd0_9_num
        return(num)

    #0~99の範囲の乱数関数
    def rnd0_99(self):
        """
        0~99の範囲の乱数関数
        
        帰り値として0~99の整数の乱数が戻ってきます
        """
        global num
        num = self.rnd0_99_num
        return(num)

    #線形合同法を使用した乱数関数 (0~65535のランダムな数値がself.rnd_seedに代入される)この乱数の周期は32768
    def s_rnd(self):
        """
        線形合同法を使用した乱数関数 (0~65535のランダムな数値がself.rnd_seedに代入される)この乱数の周期は32768
        """
        self.rnd_seed = (self.rnd_seed * 48828125 + 129) % 65536 #129のように足す数値は絶対に奇数にするように！でないと奇数と偶数の乱数が交互に育成されるようになってしまうからね

    #s_rndint(min,max) と呼ぶと、minからmax(max自身を含む)までの間の整数が 等しい確率でランダムに返される
    def s_rndint(self,min,max):
        """
        s_rndint(min,max) と呼ぶと、minからmax(max自身を含む)までの間の整数が 等しい確率でランダムに返される
        """
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        func.s_rnd(self)                              #0~65535のランダムな数値がself.rnd_seedに代入される
        num_zero_to_max = self.rnd_seed % (max - min) #  0 から(max - min)までの乱数を取得
        num_min_to_max  = num_zero_to_max + min      #min から max      までの乱数を取得
        num = num_min_to_max                     #整数化します
        return (num)

    #s_random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(パーティクル系で使おうとしたけど結構動作が遅いので標準ライブラリ使ったほうがいいなぁ→結局random()を使う事にしました)
    def s_random(self):
        """
        s_random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(パーティクル系で使おうとしたけど結構動作が遅いので標準ライブラリ使ったほうがいいなぁ→結局random()を使う事にしました)
        """
        global num
        num_0_1  =  self.rnd0_9() /10        #小数点1桁目の乱数を取得(0~9)
        num_0_01 =  self.rnd0_9() / 100       #小数点2桁目の乱数を取得(0~9)
        num_0_001 =  self.rnd0_9() / 1000     #小数点3桁目の乱数を取得(0~9)
        num_0_0001 =  self.rnd0_9() / 10000    #小数点4桁目の乱数を取得(0~9)
        num_0_00001 =  self.rnd0_9() / 100000  #小数点5桁目の乱数を取得(0~9)
        num = num_0_1 + num_0_01 + num_0_001 + num_0_0001 + num_0_00001 #全ての桁数を足し合わせると小数点5桁までの乱数となる(0.00000~0.99999)
        return (num)

    #点滅系カラーコードの取得
    def get_flashing_type_color_code(self,flash_type):
        """
        点滅系カラーコードの取得
        
        flash_type=フラッシュタイプのカラーコードを入れてください MES_****_FLASHなどの定数でお願いします
        """
        global col
        if flash_type == MES_BLINKING_FLASH:                     #テキスト点滅の場合
            col = self.blinking_color[pyxel.frame_count // 4 % 10]
        elif flash_type == MES_YELLOW_FLASH:                     #テキスト黄色点滅の場合
            col = self.yellow_flash_color[pyxel.frame_count // 4 % 10]
        elif flash_type == MES_RED_FLASH:                        #テキスト赤い点滅の場合
            col = self.red_flash_color[pyxel.frame_count // 4 % 10]
        elif flash_type == MES_GREEN_FLASH:                      #テキスト緑で点滅の場合
            col = self.green_flash_color[pyxel.frame_count // 4 % 10]
        elif flash_type == MES_MONOCHROME_FLASH:                 #テキスト白黒で点滅の場合
            col = self.monochrome_flash_color[pyxel.frame_count // 4 % 10]
        elif flash_type == MES_RAINBOW_FLASH:                    #テキスト虹色に点滅の場合
            col = self.rainbow_flash_color[pyxel.frame_count // 4 % 10]
        else:                                                    #該当しない場合は白色(7)にする
            col = 7
        
        return (col)

    #1プレイ時間の表示(秒まで表示します)
    def disp_one_game_playtime(self,x,y,col):
        """
        1プレイ時間の表示(秒まで表示します)
        
        x,y=表示する座標
        col=表示色
        """
        pyxel.text(x-8*3,y,"   :", int(col))
        minutes = "{:>3}".format(self.one_game_playtime_seconds // 60)
        seconds = "{:>02}".format(self.one_game_playtime_seconds % 60)
        pyxel.text(x-8*3,y,minutes, int(col))
        pyxel.text(x-8  ,y,seconds, int(col))

    #総プレイ時間の表示(秒まで表示します)
    def disp_total_game_playtime(self,x,y,col):
        """
        総プレイ時間の表示(秒まで表示します)
        
        x,y=表示する座標\\
        col=表示色
        """
        pyxel.text(x-8*3,y,":  :", int(col))
        total_seconds = "{:>02}".format(self.total_game_playtime_seconds % 60)
        total_minutes = "{:>02}".format(self.total_game_playtime_seconds // 60 % 60)
        total_hours   = "{:>04}".format(self.total_game_playtime_seconds // 3600)
        pyxel.text(x-8*6+8,y,  total_hours, int(col))
        pyxel.text(x-8*3+4,y,total_minutes, int(col))
        pyxel.text(x-8    ,y,total_seconds, int(col))

    #矩形Aと矩形Bの当たり判定 矩形A(rect_ax,rect_ay,rect_aw,rect_ah)(xはx座標,yはy座標,wは横幅width,hは縦幅heightを意味します)矩形B(rect_bx,rect_by,rect_bw,rect_bh) 衝突していたらTrueをしていなかったらFalseを返します
    def collision_rect_rect(self,rect_ax,rect_ay,rect_aw,rect_ah,rect_bx,rect_by,rect_bw,rect_bh):
        """
        矩形Aと矩形Bの当たり判定
        
        矩形A(rect_ax,rect_ay,rect_aw,rect_ah)(xはx座標,yはy座標,wは横幅width,hは縦幅heightを意味します)\\
        矩形B(rect_bx,rect_by,rect_bw,rect_bh)\\
        帰り値 True=衝突した False=衝突していない
        """
        #collision rectangle to rectangle
        #矩形A(rect_ax,rect_ay,rect_aw,rect_ah)(xはx座標,yはy座標,wは横幅width,hは縦幅heightを意味します)
        #矩形B(rect_bx,rect_by,rect_bw,rect_bh)
        #1...矩形の中心座標を計算する
        #2...x軸,y軸の距離を計算する
        #3...2つの矩形のx軸,y軸のサイズの和を計算する
        #4...サイズの和と距離を比較する
        #衝突していたらTrueをしていなかったらFalseを返します
        
        #1..矩形の中心座標を計算する
        #矩形Aの中心座標(center_ax,center_ay)
        #矩形Bの中心座標(center_bx,center_by)
        center_ax = rect_ax + rect_aw // 2
        center_ay = rect_ay + rect_ah // 2
        center_bx = rect_bx + rect_bw // 2
        center_by = rect_by + rect_bh // 2
        #2..x軸,y軸の距離を計算する「座標間の距離」ではなく「X座標間の距離」と「Y座標間の距離」を計算する
        distance_x = abs(center_ax - center_bx)
        distance_y = abs(center_ay - center_by)
        #3...2つの矩形のx軸,y軸のサイズの和を計算する
        size_sum_x = rect_aw + rect_bw // 2
        size_sum_y = rect_ah + rect_bh // 2
        #4...サイズの和と距離を比較する
        #    矩形どうしが衝突している条件は
        #        「x軸の距離がx軸のサイズの和よりも小さい」
        #        「y軸の距離がy軸のサイズの和よりも小さい」の2つの条件を満たしている時に衝突していると判断します
        if distance_x < size_sum_x and distance_y < size_sum_y:
            return True
        else:
            return False

    #ゲーム関連のフラグ＆データリストを作成する
    def create_master_flag_list(self):
        """
        ゲーム関連のフラグ＆データリストを作成する
        """
        self.master_flag_list[LIST_WINDOW_FLAG_DEBUG_MODE]  = self.debug_menu_status  #デバッグモードの有無フラグをリスト登録
        self.master_flag_list[LIST_WINDOW_FLAG_GOD_MODE]    = self.god_mode_status    #ゴッドモードの有無フラグをリスト登録
        self.master_flag_list[LIST_WINDOW_FLAG_HIT_BOX]     = self.boss_collision_rect_display_flag #ヒットボックス表示モードの有無フラグをリスト登録
        self.master_flag_list[LIST_WINDOW_FLAG_BOSS_MODE]   = self.boss_test_mode     #ボスモードの有無フラグをリスト登録
        self.master_flag_list[LIST_WINDOW_FLAG_START_STAGE] = self.stage_number       #スタートステージ数をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_START_LOOP]  = self.stage_loop         #スタートスループ数をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_START_AGE]   = self.stage_age          #スタート年代をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_DIFFICULTY]  = self.game_difficulty    #ゲーム難易度をリストに登録
        
        self.master_flag_list[LIST_WINDOW_FLAG_SCREEN_MODE] = self.fullscreen_mode    #フルスクリーン起動モードフラグをリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_BGM_VOL]     = self.master_bgm_vol     #マスターBGMボリューム数値をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_SE_VOL]      = self.master_se_vol      #マスターSEボリューム数値をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_CTRL_TYPE]   = self.ctrl_type          #パッドコントロールパターン値をリストに登録
        self.master_flag_list[LIST_WINDOW_FLAG_LANGUAGE]    = self.language           #選択言語をリストに登録

    #マスターフラグ＆データリストを個別の変数にリストアさせる
    def restore_master_flag_list(self):
        """
        マスターフラグ＆データリストを個別の変数にリストアさせる
        """
        self.debug_menu_status = self.master_flag_list[LIST_WINDOW_FLAG_DEBUG_MODE]              #デバッグモードの有無フラグをリストから参照してリストア
        self.god_mode_status   = self.master_flag_list[LIST_WINDOW_FLAG_GOD_MODE]                #ゴッドモードの有無フラグをリストから参照してリストア
        self.boss_collision_rect_display_flag = self.master_flag_list[LIST_WINDOW_FLAG_HIT_BOX]  #ヒットボックス表示モードの有無フラグをリストから参照してリストア
        self.boss_test_mode    = self.master_flag_list[LIST_WINDOW_FLAG_BOSS_MODE]               #ボスモードの有無フラグをリストから参照してリストア
        self.stage_number      = self.master_flag_list[LIST_WINDOW_FLAG_START_STAGE]             #スタートステージ数をリストにから参照してリストア
        self.stage_loop        = self.master_flag_list[LIST_WINDOW_FLAG_START_LOOP]              #スタートスループ数をリストにから参照してリストア
        self.stage_age         = self.master_flag_list[LIST_WINDOW_FLAG_START_AGE]               #スタート年代をリストにから参照してリストア
        self.game_difficulty   = self.master_flag_list[LIST_WINDOW_FLAG_DIFFICULTY]              #ゲーム難易度をリストにから参照してリストア
        
        self.fullscreen_mode   = self.master_flag_list[LIST_WINDOW_FLAG_SCREEN_MODE]             #フルスクリーン起動モードフラグをリストから参照してリストア
        self.master_bgm_vol    = self.master_flag_list[LIST_WINDOW_FLAG_BGM_VOL]                 #マスターBGMボリューム数値をリストから参照してリストア
        self.master_se_vol     = self.master_flag_list[LIST_WINDOW_FLAG_SE_VOL]                  #マスターSEボリューム数値をリストから参照してリストア
        self.ctrl_type         = self.master_flag_list[LIST_WINDOW_FLAG_CTRL_TYPE]               #パッドコントロールパターン値をリストから参照してリストア
        self.language          = self.master_flag_list[LIST_WINDOW_FLAG_LANGUAGE]                #選択言語をリストから参照してリストア

    #リプレイモードの為に今現在のステータスを退避しておく(リプレイ再生の直前に呼び出されます)(テンポラリ臨時変数に保存しておく)
    def backup_status_data_for_replay_mode(self):
        """
        リプレイモードの為に今現在のステータスを退避しておく(リプレイ再生の直前に呼び出されます)(テンポラリ臨時変数に保存しておく)
        """
        self.temp_my_ship_id       = self.my_ship_id         #自機の種類を退避保存
        self.temp_stage_number     = self.stage_number       #ステージナンバー退避保存
        self.temp_stage_loop       = self.stage_loop         #ループ数退避保存
        self.temp_boss_test_mode   = self.boss_test_mode     #ボステストモード退避保存
        self.temp_game_difficulty  = self.game_difficulty    #ゲーム難易度退避保存
        #今現在の自機の装備メダルを退避保存する
        for i in range(6):#iは0から6(SLOT6)まで変化する
            medal_id = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i]
            self.temp_my_ship_medal[i] = medal_id

    #リプレイ再生後記録しておいたステータスを復帰させる(リプレイ再生が終わったら呼び出されます)(テンポラリ臨時変数から引き出す)
    def restore_status_data_for_replay_mode(self):
        """
        リプレイ再生後記録しておいたステータスを復帰させる(リプレイ再生が終わったら呼び出されます)(テンポラリ臨時変数から引き出す)
        """
        self.my_ship_id       = self.temp_my_ship_id         #自機の種類リストア
        self.stage_number     = self.temp_stage_number       #ステージナンバーリストア
        self.stage_loop       = self.temp_stage_loop         #ループ数リストア
        self.boss_test_mode   = self.temp_boss_test_mode     #ボステストモードリストア
        self.game_difficulty  = self.temp_game_difficulty    #ゲーム難易度リストア
        #あと今現在の自機の種類と装備メダルをリストアしなくては・・・
        #自機の装備メダルをリストアする
        for i in range(6):#iは0から6(SLOT6)まで変化する
            medal_id = self.temp_my_ship_medal[i]
            self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] = medal_id

    #スコアボードウィンドウ育成時に使用するランクインした機体が装備しているメダルのgraph_listを作製する
    def create_medal_graph_list_for_score_board(self,d,x,y,step_y): #d=difficult(難易度)x,y=メダルを表示し始める座標(1位のSLOT1のメダルから表示し始める),y軸のドット増分数
        """
        スコアボードウィンドウ育成時に使用するランクインした機体が装備しているメダルのgraph_listを作製する
        
        d = difficult(難易度)\\
        x,y = メダルを表示し始める座標(1位のSLOT1のメダルから表示し始める)\\
        step_y = y軸のドット増分数
        """
        for i in range(10): #iは0(1位)から10(11位)まで変化する
            for j in range(ALL_SLOT5): #jは0(SLOT0)から5(SLOT5)まで変化する
                meda_id = self.score_board[d][i][LIST_SCORE_BOARD_SHIP_SLOT0 + j]
                u = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_U]
                v = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_V]
                imgb = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_IMGB]
                self.temp_graph_list.append([x + j * 7,y + i * step_y,imgb,u,v,8,8,13,1,1])

    #ウィンドウIDの検索(与えられたウィンドウIDを元にしてウィンドウ群を検索しインデックスナンバーを取得する)
    def search_window_id(self,id): #id=windowクラスの window_idに入っている数値 発見できなかった時は-1を返します
        """
        ウィンドウIDの検索(与えられたウィンドウIDを元にしてウィンドウ群を検索しインデックスナンバーを取得する)
        
        id=windowクラスの window_idに入っている数値
        発見できなかった時は帰り値としてnum=-1を返します
        """
        window_count = len(self.window)
        num = -1
        for i in range(window_count):
            if self.window[i].window_id == id:
                num = i
                break
        
        return num

    #ウィンドウIDを調べて一致するウィンドウIDの速度、加速度を更新する(同タイプウィンドウ移動消去モード)
    def all_move_window(self,id,vx,vy,vx_accel,vy_accel):
        """
        ウィンドウIDを調べて一致するウィンドウIDの速度、加速度を更新する(同タイプウィンドウ移動消去モード)
        
        id=windowクラスの window_idに入っている数値\\
        vx,vy=速度ベクトル\\
        vx_accel,vy_accel=加速度
        """
        window_count = len(self.window)
        for i in range(window_count):
            if self.window[i].window_id == id:
                self.window[i].vx,self.window[i].vy             = vx,vy
                self.window[i].vx_accel,self.window[i].vy_accel = vx_accel,vy_accel

    #背景のスター再描画範囲リストにウィンドウIDが存在するか検索する(与えられたウィンドウIDを元にしてスターリドローエリア群を検索しインデックスナンバーを取得する)
    def search_window_id_star_redraw(self,id): #id=windowクラスの window_idに入っている数値 発見できなかった時は-1を返します
        """
        背景のスター再描画範囲リストにウィンドウIDが存在するか検索する(与えられたウィンドウIDを元にしてスターリドローエリア群を検索しインデックスナンバーを取得する)
        
        id=windowクラスの window_idに入っている数値
        発見できなかった時は-1を返します
        """
        area_count = len(self.redraw_star_area)
        num = -1
        if self.redraw_star_area == []: #まだリストに何も登録されていなくて空リストだったら直ぐにリターンする
            return num
        
        for i in reversed(range(area_count)):
            if self.redraw_star_area[i].window_id == id:
                num = i
                break
        
        return num

    #メダルリストウィンドウで「存在するアイテム」を調べ上げコメント表示フラグテーブルを作製する関数
    def make_medal_list_window_comment_disp_flag_table(self):
        """
        メダルリストウィンドウで「存在するアイテム」を調べ上げコメント表示フラグテーブルを作製する
        """
        i = func.search_window_id(self,WINDOW_ID_MEDAL_LIST) #メダルリストウィンドウをIDを元にインデックス番号を調べる
        if i != -1: #メダルリストが存在するときは「存在するアイテム」を調べ上げて、テーブルを作製開始する
            for j in range(len(self.window[i].medal_graph_list)): #medal_graph_listの長さの分ループ処理する
                item_x = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_ITEM_X] #アイテムのx座標取得
                item_y = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_ITEM_Y] #アイテムのy座標取得
                if self.window[i].medal_list[j] == 1:#メダルリストを見て所持フラグが立っているのならcomment_disp_flagのアイテムの存在すべき座標にDISP_ONを書き込む
                    self.window[i].comment_disp_flag[item_y + 2][item_x] = DISP_ON #y座標の0は自機のメダル表示欄,1はウィンドウ枠,2~3が所持メダル表示欄となるのでitem_y+2がコメント表示フラグのy座標となるわけです（ややこしい・・・）
                else:
                    self.window[i].comment_disp_flag[item_y + 2][item_x] = DISP_OFF
            
        else: #メダルリストが存在しなかったらどうしようもない・・・ので・・・リターン戻るのですよ・・・orz
            return

    #カーソル関係の数値を変数にセットする関数
    def set_cursor_data(self,cu_type,cu_move_direction,posx,posy,step_x,step_y,page,page_max,item_x,item_y,d_item_x,d_item_y,max_item_x,max_item_y,color,menu_layer):
        """
        カーソル関係の数値を変数にセットする
        
        cu_type=カーソルの種類\\
        cu_move_direction=カーソルの動く方向\\
        posx,posy=カーソルの初期座標\\
        step_x,step_y=カーソルの移動ステップドット数(横方向,縦方向)\\
        page,page_max=いま指し示しているページナンバー,セレクトカーソルで捲ることが出来る最多ページ数\\
        item_x,item_y=いま指し示しているアイテムナンバー(x,y軸方向)\\
        d_item_x=ボタンが押されて「決定」されたアイテムのナンバーx軸方向\\
        d_item_y=ボタンが押されて「決定」されたアイテムのナンバーy軸方向\\
        max_item_x,max_item_y=それぞれの軸方向の最大項目数\\
        color=セレクトカーソルの色\\
        menu_layer=現在選択中のメニューの階層の数値が入ります
        """
        self.cursor_type = cu_type
        self.cursor_move_direction = cu_move_direction
        self.cursor_x = posx
        self.cursor_y = posy
        self.cursor_step_x = step_x
        self.cursor_step_y = step_y
        self.cursor_page = page
        self.cursor_page_max = page_max
        self.cursor_item_x = item_x
        self.cursor_item_y = item_y
        self.cursor_decision_item_x = d_item_x
        self.cursor_decision_item_y = d_item_y
        self.cursor_max_item_x = max_item_x
        self.cursor_max_item_y = max_item_y
        self.cursor_color = color
        self.cursor_menu_layer = menu_layer

    #現在のカーソルの状態データ群をcursorクラスのリストに記録する(PUSH)cursorクラスのリストはLastInFastOut形式となってます「後入先出（LIFO）」
    #引数のidはウィンドウIDナンバーです
    def push_cursor_data(self,id):
        """
        現在のカーソルの状態データ群をcursorクラスのリストに記録する(PUSH)cursorクラスのリストはLastInFastOut形式となってます「後入先出（LIFO）」
        
        id=ウィンドウIDナンバー
        """
        new_cursor = Cursor()
        new_cursor.update(\
        id,self.cursor_type,\
        self.cursor_x,self.cursor_y,\
        self.cursor_step_x,self.cursor_step_y,\
        self.cursor_page,self.cursor_page_max,\
        self.cursor_item_x,self.cursor_item_y,\
        self.cursor_max_item_x,self.cursor_max_item_y,\
        self.cursor_decision_item_x,self.cursor_decision_item_y,\
        self.cursor_color,self.cursor_menu_layer,self.cursor_move_direction)
        self.cursor.append(new_cursor)

    #cursorクラスのリストに記録されたカーソルデータ群を現在のカーソルデータに代入して前のウィンドウでのカーソル位置に戻してやります(POP)
    #引数のidはウィンドウIDナンバーです
    def pop_cursor_data(self,id):
        """
        cursorクラスのリストに記録されたカーソルデータ群を現在のカーソルデータに代入して前のウィンドウでのカーソル位置に戻してやります(POP)
        
        id=ウィンドウIDナンバー
        """
        #ウィンドウidナンバーを元にそのウィンドウで使用していたカーソルデータのインデックス値を探し出す
        window_count = len(self.window)
        print ("window count")
        print(window_count)
        
        cursor_stack_count = len(self.cursor)
        print ("cursor stack count")
        print(cursor_stack_count)
        print (self.cursor)
        
        print ("search window id")
        print (id)
        
        i = func.search_window_id(self,id)
        if i == -1:
            return  #もしもカーソルデータが無かったのならどうしようもないのでリターンする(1対1でカーソルとウィンドウデータを反映してるのでそれは無いと思うですけれども）
        
        print ("active window index")
        print (i)
        
        self.cursor_type = self.cursor[i].cursor_type
        self.cursor_x,self.cursor_y = self.cursor[i].posx,self.cursor[i].posy
        self.cursor_step_x,self.cursor_step_y = self.cursor[i].step_x,self.cursor[i].step_y
        self.cursor_page,self.cursor_page_max = self.cursor[i].page,self.cursor[i].page_max
        self.cursor_item_x,self.cursor_item_y = self.cursor[i].item_x,self.cursor[i].item_y
        self.cursor_max_item_x,self.cursor_max_item_y = self.cursor[i].max_item_x,self.cursor[i].max_item_y
        self.cursor_decision_item_x,self.cursor_decision_item_y = self.cursor[i].decision_item_x,self.cursor[i].decision_item_y
        self.cursor_color,self.cursor_menu_layer,self.cursor_move_direction =  self.cursor[i].color,self.cursor[i].menu_layer,self.cursor[i].move_direction
        del self.cursor[i] #カーソルデータをPOPし終わったのでインスタンスを削除する
        self.cursor_decision_item_y = UNSELECTED  #一番新しい層の選択アイテムを未選択にする

    #スコアボードへの書き込み ランク外である11位にスコアを書き込む関数(スコアボードは10位までしか表示されないのでこの状態では表示されませんバブルソートしてね)
    def recoard_score_board(self):
        """
        スコアボードへの書き込み ランク外である11位にスコアを書き込む関数(スコアボードは10位までしか表示されないのでこの状態では表示されませんバブルソートしてね)
        """
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_NAME]        = self.my_name
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SCORE]       = self.score
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_LOOP]        = self.stage_loop
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_CLEAR_STAGE] = self.stage_number
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_USED]   = self.my_ship_id
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT0]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT1]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT1]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT2]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT2]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT3]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT3]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT4]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT4]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT5]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT5]

    #スコアボードの点数によるバブルソート 11位に今プレイしたゲームの得点を書き込みその後この関数を呼び出し→順位の11がどの位置に移動したかチェック→その位置にカーソル移動させてネームエントリー→そしてリストに書き込む
    def score_board_bubble_sort(self,diff): #diffは難易度です
        """
        スコアボードの点数によるバブルソート 11位に今プレイしたゲームの得点を書き込みその後この関数を呼び出し→順位の11がどの位置に移動したかチェック→その位置にカーソル移動させてネームエントリー→そしてリストに書き込む
        """
        for i in range(len(self.score_board[diff])): #ランキングデータは11位までなのでiは0~11まで変化する
            for j in range(len(self.score_board[diff])-1,i,-1):
                if self.score_board[diff][j][LIST_SCORE_BOARD_SCORE] > self.score_board[diff][j-1][LIST_SCORE_BOARD_SCORE]: #位置jの得点より前の位置j-1の得点が大きいのなら要素を入れ替える
                    for k in range(LIST_SCORE_BOARD_SHIP_SLOT5): #難易度からスロット5に装備されたメダルIDまでの12種類の要素をループしてコピー
                        self.score_board[diff][j][k],self.score_board[diff][j-1][k] = self.score_board[diff][j-1][k],self.score_board[diff][j][k]

    #プレイ中の自機リスト(playing_ship_list)を参照して自機にメダルをはめ込む（装着？）する関数 (num=メダルIDナンバー)
    def equip_medal_playing_ship(self,num):
        """
        プレイ中の自機リスト(playing_ship_list)を参照して自機にメダルをはめ込む（装着？）する
        
        num=メダルIDナンバー
        """
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #既にスロットに同じメダルがはめ込まれていないか調べ上げる
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == num: #これからはめ込むメダルがすでにはめ込まれていたら・・・
                pyxel.play(0,20)#カーソル衝突を鳴らしてはめ込まずそのままリターンする
                return          #リターンする
        
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #空きスロットを探す
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_NO_SLOT: #スロットを小さいナンバーの方から調べていって空スロットがあったのなら
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] = num #空きスロットにメダルIDナンバーを書き込みしてはめ込む！
                pyxel.play(0,17)#カーソルOK音を鳴らす
                return
        
        pyxel.play(0,20)#カーソル衝突音を鳴らす
        return

    #プレイ中の自機リスト(playing_ship_list)を参照して自機からメダルを外す(パージ)する関数(slot_num=自機のスロットナンバー)
    def purge_medal_playing_ship(self,slot_num):
        """
        プレイ中の自機リスト(playing_ship_list)を参照して自機からメダルを外す(パージ)する
        
        slot_num=自機のスロットナンバー
        """
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + slot_num] = MEDAL_NO_SLOT #決定ボタンが押された位置のスロットナンバーを空にする
        pyxel.play(0,18)#カーソルキャンセル音を鳴らす

    #自機に装備され,はめ込まれたメダルを左詰めにする関数(空きスロットの隙間を詰めて、空きスロットがどれだけあるのか見やすくする関数)
    def playing_ship_medal_left_justified(self):
        """
        自機に装備され,はめ込まれたメダルを左詰めにする(空きスロットの隙間を詰めて、空きスロットがどれだけあるのか見やすくする)
        """
        # start_slot = 0
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #iは0から所持スロットの最大値まで変化していきます
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_NO_SLOT: #これからはめ込む場所が空スロットの場合は・・・一つ右のスロットのメダルと現在のメダルスロットに移動させていく
                for j in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] - i): #jは0から(スロット最大値-i)まで変化していく
                    self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j + 1] #現在のスロットに一つ右横のスロットのメダルIDをコピーしていく

    #今現在プレイしているシップリスト(playing_ship_list)に機体メダルスロット装備リスト(ship_equip_slot_list)を参照しながら装備メダルの情報を読み込んでいく関数
    def read_ship_equip_medal_data(self):
        """
        今現在プレイしているシップリスト(playing_ship_list)に機体メダルスロット装備リスト(ship_equip_slot_list)を参照しながら装備メダルの情報を読み込んでいく
        """
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.playing_ship_list[i][LIST_SHIP_SLOT0 + j] = self.ship_equip_slot_list[i][j]

    #機体メダルスロット装備リスト(ship_equip_slot_list)に今現在プレイしているシップリスト(playing_ship_list)を参照しながら装備メダルの情報を書き込んでいく関数
    def write_ship_equip_medal_data(self):
        """
        機体メダルスロット装備リスト(ship_equip_slot_list)に今現在プレイしているシップリスト(playing_ship_list)を参照しながら装備メダルの情報を書き込んでいく
        """
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.ship_equip_slot_list[i][j] = self.playing_ship_list[i][LIST_SHIP_SLOT0 + j]

    #装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する関数
    def add_medal_effect_shot_bonus(self):
        """
        装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する
        """
        for i in range(6): #iは0から6(SLOT6)まで変化する
            if  self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_1SHOT_ITEM: #事前ショット1アイテムゲットメダルならば
                self.inc_shot_exp_medal += 1                                                                 #ショット経験値を増やす数値を+1する
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_2SHOT_ITEM:
                self.inc_shot_exp_medal += 2
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_3SHOT_ITEM:
                self.inc_shot_exp_medal += 3
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_4SHOT_ITEM:
                self.inc_shot_exp_medal += 4
        
        self.shot_exp += self.inc_shot_exp_medal #ショット経験値をメダルの効果のぶん加算する

    #装備されたメダルを調べ、L’ｓシールド装備メダルを作動させる関数
    def medal_effect_ls_shield(self):
        """
        装備されたメダルを調べ、L’ｓシールド装備メダルを作動させる
        """
        for i in range(6): #iは0(SLOT0)から6(SLOT6)まで変化する
            if  self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_EQUIPMENT_LS_SHIELD: #L’ｓシールド装備メダルならば
                self.ls_shield_hp = 10                                                                     #L'sシールドの耐久力を10にする

    #装備されたメダルを調べ、スロット数を拡張するメダルがあればスロット数を増やし、何も無ければスロット数を初期状態にする関数
    def medal_effect_plus_medallion(self):
        """
        装備されたメダルを調べ、スロット数を拡張するメダルがあればスロット数を増やし、何も無ければスロット数を初期状態にする
        """
        for i in range(6): #iは0(SLOT0)から6(SLOT6)まで変化する
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_PLUS_MEDALLION: #スロット増加メダルならば・・・
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_INIT_SLOT_NUM] + 2                     #空きスロット増加メダルは初期総スロット数＋2つ分空きスロットに増やす
                return
            else:
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_INIT_SLOT_NUM] #現在の総スロット数は初期スロット数とする

    #現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする関数
    #例 LIST_SHIP_SLOT_NUMの数値である「総スロット数」が2だったらSLOT0からSLOT1までは使用するのでそのままにして,SLOT2からSLOT6までゼロクリアする
    #現時点での確保しているスロット数は7
    def zero_clear_out_of_range_slot(self):
        """
        現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする
        """
        st = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]
        for i in range(7 - self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]):
            self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + st] = MEDAL_NO_SLOT

    #!###############################################################ボツ関数群・・・・・・(涙)##########################################################
    #外積を計算する関数 self.cpに結果が入る(バグありなので使えないっぽい・・・この関数)
    def cross_product_calc_function(self,ax,ay,bx,by,cx,cy):
        self.cp = (ax - cx) * (by - cy) - (bx - cx) * (ay - cy)
        return()

    #三角形と点の当たり判定を行う関数(ax,ay)(bx,by)(cx,cy)=三角形の各頂点の座標,px,py=三角形の中か外にあるかどうかを判定するポイント用座標)
    #(バグあるので使えないっいぽい。。。この関数・・・ボツダナ)
    def point_in_triangle(self,px,py,ax,ay,bx,by,cx,cy):
        #
        #
        #C++だとこんな感じ
        #
        #外積を計算して符号だけ返す
        #float sign (fPoint a, fPoint b, fPoint c)
        #{
        #    return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y);
        #}
        #3辺のベクトルと判定ポイントと頂点結んだベクトルの外積を求め全ての符号が同じならbool値でtrue,違っていたらfalseを返す 
        #bool PointInTriangle (fPoint p, fPoint a, fPoint b, fPoint c)
        #{
        #    float d1,d2,d3
        #    bool has_negative, has_positive;
        # 
        #    d1 = sign(p, a, b);
        #    d2 = sign(p, b, c);
        #    d3 = sign(p, c, a);
        #    has_negative = (d1 < 0) || (d2 < 0) || (d3 < 0);
        #    has_positive = (d1 > 0) || (d2 > 0) || (d3 > 0);
        # 
        #    return !(has_negative && has_positive);
        #}
        
        self.cp = 0                    #外積計算用変数を初期化
        self.point_inside_triangle_flag = 0 #判別用のフラグを初期化 
        
        self.cross_product_calc_function(px,py,ax,ay,bx,by)
        d1 = self.cp
        self.cross_product_calc_function(px,py,bx,by,cx,cy)
        d2 = self.cp
        self.cross_product_calc_function(px,py,cx,cy,ax,ay)
        d3 = self.cp
        if (d1 < 0 and d2 < 0 and d3 < 0) or (d1 > 0 and d2 > 0 and d3 > 0):#d1~d3が全てマイナスの数値 または d1~d3が全てプラスの数値だったら
            self.point_inside_triangle_flag = 1 #三角形の内側に点があった！のでフラグをon
        else:
            self.point_inside_triangle_flag = 0 #三角形の外側だった・・・・のでフラグをoff   

    #自機を追尾してくる敵キャラ用のvx,vyの増分とdir（方向）を求める関数   まだ未完成