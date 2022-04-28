import math                #三角関数などを使用したいのでインポートぉぉおお！
from random import random  #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)

import pyxel               #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
import pygame.mixer        #MP3再生するためだけに使用する予定・・・予定は未定・・・そして未定は確定に！やったあぁ！ BGMだけで使用しているサブゲームエンジン
from const        import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from define_class import * #クラス宣言モジュールの読み込み やっぱりimport *は不味いのかなぁ・・・よくわかんない

class func:
    def __init__(self):
        None

    #漢字フォントデータの読み込み
    def load_kanji_font_data(self):
        pyxel.load("assets/fonts/misaki_font_k8x12s_001.pyxres") #漢字フォントデータ(その1)を読み込みます
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
        
        pyxel.load("assets/fonts/misaki_font_k8x12s_002.pyxres") #漢字フォントデータ(その2)を読み込みます
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
        
        pyxel.load("assets/fonts/misaki_font_k8x12s_003.pyxres") #漢字フォントデータ(その3)を読み込みます
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
        
        pyxel.load("assets/fonts/misaki_font_k8x12s_004.pyxres") #漢字フォントデータ(その4)を読み込みます
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
        base_x,base_y = x,y
        for char in text:
            found = self.font_code_table.find(char) #foundにテキスト(char)を使ってフォント対応表にある位置を調べる→位置がfoundに入ります(見つからなかったらfoundに-1が入ります)
            if found >= 0 and char != '\n': #文字を見つけて尚且つ改行コードでないのなら漢字を描画し始めます
                sy = self.font_code_table[:found].count('\n') #対応表のリストの先頭から改行コードの数を数えるとその数値がY座標となります
                sx = self.font_code_table.split('\n')[sy].find(char)
                
                for i in range(8): #漢字フォントの横ドット数8
                    for j in range(12): #漢字フォントの縦ドット数12
                        if self.kanji_fonts[(sy-1)*12+j][sx*8+i] == 7: #フォントのデータは 0=黒が透明で 7=白が描画する点なので色コードが7だったらpsetで点を打ちます
                            pyxel.pset(x+i,y+j,int(col))
                
                x += 8
                if char == '\n':
                    x = base_x
                    y += 12

    #ドロップシャドウ漢字テキストの表示(影落ち漢字テキスト)
    def drop_shadow_kanji_text(self,x,y,text,col):
        func.kanji_text(self,x+1,y,  text,0)       #なんでfunc.kanji_text(self,x+1,y,  text,0)にしないとエラーが出るのか判らない・・試行錯誤で func.kanji_text(self,x+1,y,  text,0)ってやったらうまくいった・・・クラスが違うところから呼び出される関数(この場合はメソッド？)は呼び出された関数自身を示すselfを付けないといけないのかな？謎は深まる・・・
        func.kanji_text(self,x+1,y+1,text,0)
        func.kanji_text(self,x,  y,  text,col)

    #ドロップシャドウテキスト(影落ちテキスト)の表示
    def drop_shadow_text(self,x,y,text,col):
        pyxel.text(x+1,y,  text,0)
        pyxel.text(x+1,y+1,text,0)
        pyxel.text(x,  y,  text,int(col))

    #タイルマップの座標位置からキャラチップのアスキーコードを取得する
    def get_chrcode_tilemap(self,tm,x,y):         #tmはtilemapの数値,x,yは読み出す座標位置
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        num = 0
        tile_x,tile_y = pyxel.tilemap(tm).pget(x,y) #タイルマップtm 座標(x,y)に格納されているマップチップを調べ、そのマップチップが格納されている座標を取得
        num = tile_y * 32 + tile_x
        return(num)

    #タイルマップの座標位置へキャラチップのアスキーコードをタプル座標形式に変換したものをセットする(置く)
    def set_chrcode_tilemap(self,tm,x,y,num):         #tmはtilemapの数値,x,yはセット（置く）座標位置
        tile_x = num % 32   #置く場所のx座標は 32で割った余り
        tile_y = num // 32  #置く場所のy座標は 32での切り捨て除算
        pyxel.tilemap(tm).pset(x,y,(tile_x,tile_y))

    #システムデータからの数値読み込み
    def read_system_data_num(self,x,y,tm,digit):      #x,yは1の位の座標です,tmはtilemapの数値,digitは桁数です
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        num = 0
        a = 1
        for i in range(digit):
            num += (func.get_chrcode_tilemap(self,tm,x-i,y) - 16) * a
            a = a * 10
        return(num)

    #システムデータへの数値書き込み
    def write_system_data_num(self,x,y,tm,digit,num): #x,yは1の位の座標です,tmはtilemapの数値,digitは桁数 numは書き込む数値です(整数を推奨)
        a = 10
        for i in range(digit):
            n = num % a * 10 // a
            func.set_chrcode_tilemap(self,tm,x-i,y,n + 16)
            a = a * 10                      #めっちゃ判りにくいなぁ・・・試行錯誤で上手くいった？かも？です！？
                                            #書き込みテストで段々ステップアップしていくと上手くいくね☆彡
        
        #書き込みテストその１ 0からdigit桁数まで数値と桁数が増えてく digit=1なら0 digit=3なら210 digit=7なら6543210 digit=10なら9876543210
        # n = 0 
        # for i in range(digit):
            # pyxel.tilemap(0).set(x-i,y,n + 16)
            # n += 1
        
        #書き込みテストその２
        # for i in range(digit):
            # pyxel.tilemap(0).set(x-i,y,(digit - i) + 16)

    #システムデータのロード
    def load_system_data(self):
        pyxel.load("assets/system/system-data.pyxres") #システムデータを読み込む
        
        self.game_difficulty = func.get_chrcode_tilemap(self,0,0,120) - 16 #数字の[0]はアスキーコード16番なので16引いて数値としての0にしてやります
        print(self.game_difficulty)
        self.stage_number    = func.get_chrcode_tilemap(self,0,0,121) - 16
        print(self.stage_number)
        self.stage_loop      = func.get_chrcode_tilemap(self,0,0,122) - 16
        print(self.stage_loop)
        self.stage_age       = 0
        #プレイした回数を読み込む
        self.number_of_play = func.read_system_data_num(self,6,6,0,7)
        print(self.number_of_play)
        #累計得点数を読み込む
        self.total_score    = func.read_system_data_num(self,15,8,0,16)
        print(self.total_score)

        #総ゲームプレイ時間(秒)を計算する
        sec_1  = func.get_chrcode_tilemap(self,0,9,5) - 16 #秒の  1の位取得
        sec_10 = func.get_chrcode_tilemap(self,0,8,5) - 16 #秒の  10の位取得
        min_1  = func.get_chrcode_tilemap(self,0,6,5) - 16 #分の  1の位取得
        min_10 = func.get_chrcode_tilemap(self,0,5,5) - 16 #分の  10の位取得
        hour_1 = func.get_chrcode_tilemap(self,0,3,5) - 16 #時の   1の位取得
        hour_10 = func.get_chrcode_tilemap(self,0,2,5) - 16 #時の   10の位取得
        hour_100 = func.get_chrcode_tilemap(self,0,1,5) - 16 #時の   100の位取得
        hour_1000 = func.get_chrcode_tilemap(self,0,0,5) - 16 #時の   1000の位取得
        
        s = sec_10 * 10 + sec_1
        m = min_10 * 10 + min_1
        h = hour_1000 * 1000 + hour_100 * 100 + hour_10 * 10 + hour_1
        t_sec = h * 3600 + m * 60 + s
        self.total_game_playtime_seconds = t_sec
        print(self.total_game_playtime_seconds)
        #総開発テスト時間(分)を計算する
        min_1  = func.get_chrcode_tilemap(self,0,7,3) - 16 #分の  1の位取得
        min_10 = func.get_chrcode_tilemap(self,0,6,3) - 16 #分の  10の位取得
        hour_1 = func.get_chrcode_tilemap(self,0,4,3) - 16 #時の   1の位取得
        hour_10 = func.get_chrcode_tilemap(self,0,3,3) - 16 #時の   10の位取得
        hour_100 = func.get_chrcode_tilemap(self,0,2,3) - 16 #時の   100の位取得
        hour_1000 = func.get_chrcode_tilemap(self,0,1,3) - 16 #時の   1000の位取得
        hour_10000 = func.get_chrcode_tilemap(self,0,0,3) - 16 #時の   10000の位取得
        m = min_10 * 10 + min_1
        h = hour_10000 * 10000 + hour_1000 * 1000 + hour_100 * 100 + hour_10 * 10 + hour_1
        t_min = h * 60 + m
        self.total_development_testtime_min = t_min
        print(self.total_development_testtime_min)
        
        #デバッグモード＆ゴッドモード用のフラグやパラメーターの初期化とか宣言はこちらで行うようにします
        #debug_menu_status                  #デバッグパラメータの表示ステータス
                                            #0=表示しない 1=フル表示タイプ 2=簡易表示タイプ
        self.debug_menu_status             = func.get_chrcode_tilemap(self,0,0,126) - 16 #数字の[0]はアスキーコード16番なので16引いて数値としての0にしてやります
        
        #boss_collision_rect_display_flag        ボス用の当たり判定確認の為の矩形表示フラグ(デバッグ時に1にします)
        self.boss_collision_rect_display_flag = func.get_chrcode_tilemap(self,0,0,127) - 16
        #bg_collision_Judgment_flag            背景の障害物との衝突判定を行うかどうかのフラグ
                                            #0=背景の障害物との当たり判定をしない 1=行う
        self.bg_collision_Judgment_flag      = func.get_chrcode_tilemap(self,0,0,128) - 16
        #boss_test_mode                      ボス戦闘のみのテストモード 
                                            #0=オフ 1=オン scroll_countを増やさない→マップスクロールしないので敵が発生しません
                                            #イベントリストもボス専用の物が読み込まれます
        self.boss_test_mode                = func.get_chrcode_tilemap(self,0,0,129) - 16
        #no_enemy_mode                       マップチップによる敵の発生を行わないモードのフラグですです(地上の敵が出ない！)2021 03/07現在機能してない模様
                                            #0=マップスクロールによって敵が発生します
                                            #1=                    発生しません        
        self.no_enemy_mode                 = func.get_chrcode_tilemap(self,0,0,130) - 16
        #god_mode_status                    #ゴッドモードのステータス
                                            #0=ゴッドモードオフ 1=ゴッドモードオン
        self.god_mode_status               = func.get_chrcode_tilemap(self,0,0,131) - 16
        #fullscreen_mode                    #フルスクリーンでの起動モード
                                            #0=ウィンドウモードでの起動 1=フルスクリーンモードでの起動
        self.fullscreen_mode               = func.get_chrcode_tilemap(self,0,0,132) - 16
        #ctrl_type                          #コントロールパッドのタイプ
                                            #0~5
        self.ctrl_type                     = func.get_chrcode_tilemap(self,0,0,133) - 16
        #master_bgm_vol                     #BGMのマスターボリューム
                                            #0~100
        self.master_bgm_vol                = func.read_system_data_num(self,2,134,0,3)
        #master_se_vol                      #SEのマスターボリューム
                                            #0~7
        self.master_se_vol                 = func.read_system_data_num(self,2,135,0,3)
        #language                           #選択言語
                                            #0=英語 1=日本語
        self.language                      = func.get_chrcode_tilemap(self,0,0,136) - 16
        
        #メダル所有フラグの読み込み
        for i in range(10):
            self.medal_list[i] = func.get_chrcode_tilemap(self,0,0,210 + i) - 16
        
        #各機体のスロット装備済みメダルデータの読み込み
        for i in range(LOOK_AT_LOGO): #iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):        #jはスロット0からスロット6まで変化
                self.ship_equip_slot_list[i][j] = func.get_chrcode_tilemap(self,0,23 + j,11 + i) - 16
        
        #スコアボードデータの読み込み
        for i in range(GAME_INSAME+1): #iは0からGAME_INSAME+1(6)まで変化する(難易度)
            tm = 4
            for j in range(11):      #jは0から11まで変化する(順位)
                self.score_board[i][j][LIST_SCORE_BOARD_DIFFICULTY]  = i                                        #難易度ID読み込み 
                self.score_board[i][j][LIST_SCORE_BOARD_RANKING]     = func.read_system_data_num(self,1,5 + j + (i * 16),tm, 2) #順位読み込み
                
                namestr = ""
                for k in range(8):   #kは0から8まで変化する(8文字だよ)
                    st = chr(func.get_chrcode_tilemap(self,tm,3 + k,5 + j + (i * 16))+32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)
                    namestr = namestr + st
                
                # namestr = chr(pyxel.tilemap(tm).pget(3,5 + j + (i * 16))+32) 
                self.score_board[i][j][LIST_SCORE_BOARD_NAME]    = str(namestr) #アスキーコード8文字分の名前を読み込み
                
                self.score_board[i][j][LIST_SCORE_BOARD_SCORE]       = func.read_system_data_num(self,23,5 + j + (i * 16),tm, 12) #得点読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_LOOP]        = func.read_system_data_num(self,28,5 + j + (i * 16),tm, 2) #周回数読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_CLEAR_STAGE] = func.read_system_data_num(self,34,5 + j + (i * 16),tm, 2) #クリアしたステージ数読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_SHIP_USED]   = func.read_system_data_num(self,39,5 + j + (i * 16),tm, 2) #使用した機体読み込み
                
                for l in range(6): #機体に装着されたメダル装備IDの読み込み
                    self.score_board[i][j][LIST_SCORE_BOARD_SHIP_SLOT0 + l] = func.get_chrcode_tilemap(self,tm,41 + l,5 + j + (i * 16)) - 16
        
        #名前の読み込み
        namestr = ""
        for i in range(8):   #kは0から8まで変化する(8文字だよ)
            st = chr(func.get_chrcode_tilemap(self,0,0 + i,1) + 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)
            namestr = namestr + st
        self.my_name = str(namestr)
        
        #各ステージボス撃破数の読み込み
        for i in range(14):
            self.boss_number_of_defeat[i] = func.read_system_data_num(self,27,210 + i,0,4)
        
        #実績(アチーブメント)の読み込み
        for i in range(len(self.achievement_list)):
            self.achievement_list[i][LIST_ACHIEVE_FLAG] = func.get_chrcode_tilemap(self,0,0,41 + i) - 16
        
        #スコアスター最大得点倍率の読み込み
        self.max_score_star_magnification = func.read_system_data_num(self,2,137,0,3)
        
        #パワーカプセル類の累計取得数の読み込み
        self.get_shot_pow_num     = func.read_system_data_num(self,7,138,0,8) #ショットカプセル累計取得数の読み込み
        self.get_missile_pow_num  = func.read_system_data_num(self,7,139,0,8) #ミサイルカプセル累計取得数の読み込み
        self.get_shield_pow_num   = func.read_system_data_num(self,7,140,0,8) #シールドカプセル累計取得数の読み込み
        self.get_claw_num         = func.read_system_data_num(self,7,141,0,8) #クロー累計取得数の読み込み
        self.get_score_star_num   = func.read_system_data_num(self,7,142,0,8) #スコアスター累計取得数の読み込み
        self.get_triangle_pow_num = func.read_system_data_num(self,7,144,0,8) #トライアングルアイテム累計取得数の読み込み
        self.fast_forward_num     = func.read_system_data_num(self,7,145,0,8) #累計早回し発生数の読み込み
        
        # self.test_read_num = func.read_system_data_num(self,15,156,0,16) #数値の読み取りテストです

    #システムデータのセーブ
    def save_system_data(self):
        pyxel.load("assets/system/system-data.pyxres") #システムデータにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        #各種設定値書き込み 数字の[0]はアスキーコード16番なので16足してアスキーコードとしての0にしてやります
        func.set_chrcode_tilemap(self,0, 0,120,self.game_difficulty + 16)                 #難易度書き込み
        func.set_chrcode_tilemap(self,0, 0,121,self.stage_number + 16)                    #スタートステージ数書き込み
        func.set_chrcode_tilemap(self,0, 0,122,self.stage_loop + 16)                      #スタート周回数書き込み
        func.set_chrcode_tilemap(self,0, 0,126,self.debug_menu_status + 16)               #デバッグメニュー表示フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,127,self.boss_collision_rect_display_flag + 16)#ボス当たり判定矩形表示フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,128,self.bg_collision_Judgment_flag + 16)      #BGとの当たり判定フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,129,self.boss_test_mode + 16)                  #ボステストモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,130,self.no_enemy_mode + 16)                   #敵が出ないモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,131,self.god_mode_status + 16)                 #ゴッドモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,132,self.fullscreen_mode + 16)                 #フルスクリーン起動フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,133,self.ctrl_type + 16)                       #パッドコントロールタイプ書き込み
        func.write_system_data_num(self,2,134,0,3,self.master_bgm_vol)             #マスターBGMボリューム値書き込み
        func.write_system_data_num(self,2,135,0,3,self.master_se_vol)              #マスターSEボリューム値書き込み
        func.set_chrcode_tilemap(self,0 ,0,136,self.language + 16)                        #選択言語書き込み
        
        #プレイした回数を書き込む
        func.write_system_data_num(self,6,6,0,7,self.number_of_play)
        #累計得点数を書き込む
        func.write_system_data_num(self,15,8,0,16,self.total_score)
        #メダル所有フラグの書き込み
        for i in range(10):
            func.set_chrcode_tilemap(self,0, 0,210 + i,self.medal_list[i] + 16)
        
        #各機体のスロット装備済みメダルデータの書き込み
        for i in range(LOOK_AT_LOGO): #iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):        #jはスロット0からスロット6まで変化
                func.set_chrcode_tilemap(self,0, 23 + j,11 + i,self.ship_equip_slot_list[i][j] + 16)
        
        #スコアボードデータの書き込み
        for i in range(GAME_INSAME+1): #iは0からGAME_INSAME+1(6)まで変化する(難易度)
            tm = 4
            for j in range(11):      #jは0から11まで変化する(順位)
                func.write_system_data_num(self,1,5 + j + (i * 16),tm, 2,self.score_board[i][j][LIST_SCORE_BOARD_RANKING]) #順位書き込み
                
                namestr = self.score_board[i][j][LIST_SCORE_BOARD_NAME]                 #スコアボードからアスキーコード8文字分の名前を取り出す
                for k in range(8):   #kは0から8まで変化する(8文字だよ)
                    func.set_chrcode_tilemap(self,tm, 3 + k,5 + j + (i * 16),ord(namestr[k]) - 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)数字は16の差が出る
                
                func.write_system_data_num(self,23,5 + j + (i * 16),tm, 12,self.score_board[i][j][LIST_SCORE_BOARD_SCORE])       #得点書き込み
                func.write_system_data_num(self,28,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_LOOP])        #周回数書き込み
                func.write_system_data_num(self,34,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_CLEAR_STAGE]) #クリアしたステージ数書き込み
                func.write_system_data_num(self,39,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_SHIP_USED])   #使用した機体書き込み
                
                for l in range(6): #機体に装着されたメダル装備IDの書き込み
                    func.set_chrcode_tilemap(self,tm, 41 + l,5 + j + (i * 16),self.score_board[i][j][LIST_SCORE_BOARD_SHIP_SLOT0 + l] + 16)
        
        #名前の書き込み
        for i in range(8):   #kは0から8まで変化する(8文字だよ)
            func.set_chrcode_tilemap(self,0, 0 + i,1,ord(self.my_name[i]) - 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)数字は16の差が出る
        
        #各ステージボス撃破数の書き込み
        for i in range(14):
            func.write_system_data_num(self,27,210 + i,0,4,self.boss_number_of_defeat[i])
        
        #実績(アチーブメント)の書き込み
        for i in range(len(self.achievement_list)):
            func.set_chrcode_tilemap(self,0, 0,41 + i,self.achievement_list[i][LIST_ACHIEVE_FLAG] + 16)
        
        #スコアスター最大得点倍率の書き込み
        func.write_system_data_num(self,2,137,0,3,self.max_score_star_magnification)
        
        #パワーカプセル類の累計取得数の書き込み
        func.write_system_data_num(self,7,138,0,8,self.get_shot_pow_num   )  #ショットカプセル累計取得数の書き込み
        func.write_system_data_num(self,7,139,0,8,self.get_missile_pow_num)  #ミサイルカプセル累計取得数の書き込み
        func.write_system_data_num(self,7,140,0,8,self.get_shield_pow_num )  #シールドカプセル累計取得数の書き込み
        func.write_system_data_num(self,7,141,0,8,self.get_claw_num       )  #クロー累計取得数の書き込み
        func.write_system_data_num(self,7,142,0,8,self.get_score_star_num )  #スコアスター累計取得数の書き込み
        func.write_system_data_num(self,7,144,0,8,self.get_triangle_pow_num) #トライアングルアイテム累計取得数の書き込み
        func.write_system_data_num(self,7,145,0,8,self.fast_forward_num)     #累計早回し発生数の書き込み
        
        #総ゲームプレイ時間(秒)のそれぞれの桁の数値を計算する (自分でも訳が分からないよ・・・)------------------------------
        t_sec = self.total_game_playtime_seconds
        se = t_sec % 60        #se 秒は 総秒数を60で割った余り
        mi = t_sec // 60 % 60  #mi 分は 総秒数を60で割った数(切り捨て)を更に60で割った余り
        ho = t_sec // 3600     #ho 時は 総秒数を3600で割った数(切り捨て)
        #それぞれの桁の数値(0~9)を計算して求めていく
        sec_1  = se  % 10
        sec_10 = se // 10
        min_1  = mi  % 10
        min_10 = mi // 10
        hour_1 = ho % 10
        hour_10 = ho % 100 // 10
        hour_100 = ho % 1000 // 100
        hour_1000 = ho % 10000 // 1000
        #総ゲームプレイ時間(秒)を書き込んでいく
        func.set_chrcode_tilemap(self,0, 9,5,sec_1 + 16) #秒の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 8,5,sec_10 + 16) #秒の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 6,5,min_1 + 16) #分の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 5,5,min_10 + 16) #分の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 3,5,hour_1  + 16) #時の   1の位を書き込む
        func.set_chrcode_tilemap(self,0, 2,5,hour_10 + 16) #時の   10の位を書き込む
        func.set_chrcode_tilemap(self,0, 1,5,hour_100 + 16) #時の   100の位を書き込む
        func.set_chrcode_tilemap(self,0, 0,5,hour_1000 + 16) #時の   1000の位を書き込む
        
        #総開発テストプレイ時間(分)を計算します------------------------------------------------------
        self.total_development_testtime_min += self.one_game_playtime_seconds // 60 #今プレイしているゲームの時間(分)を総ゲームテスト時間に加算
        t_dev_min = self.total_development_testtime_min
        mi = t_dev_min % 60    #mi 分は 総分数を60で割った余り
        ho = t_dev_min // 60      #ho 時は 総秒数を60で割った数(切り捨て)
        #それぞれの桁の数値(0~9)を計算して求めていく
        min_1  = mi  % 10
        min_10 = mi // 10
        hour_1 = ho % 10
        hour_10 = ho % 100 // 10
        hour_100 = ho % 1000 // 100
        hour_1000 = ho % 10000 // 1000
        hour_10000 = ho % 100000 // 10000
        #総開発テストプレイ時間を書き込んでいく
        func.set_chrcode_tilemap(self,0, 7,3,min_1 + 16) #分の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 6,3,min_10 + 16) #分の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 4,3,hour_1  + 16) #時の   1の位を書き込む
        func.set_chrcode_tilemap(self,0, 3,3,hour_10 + 16) #時の   10の位を書き込む
        func.set_chrcode_tilemap(self,0, 2,3,hour_100 + 16) #時の   100の位を書き込む
        func.set_chrcode_tilemap(self,0, 1,3,hour_1000 + 16) #時の   1000の位を書き込む
        func.set_chrcode_tilemap(self,0, 0,3,hour_10000 + 16) #時の   10000の位を書き込む
        
        func.write_system_data_num(self,16,152,0,16,8777992360588341) #!############################ test write
        
        test_num = -0.123
        test_num = test_num * 1000
        test_num = test_num + 1000                             #この式と逆の方法で計算してやれば符号の付いた実数値を取り出せる
        func.write_system_data_num(self,10,162,0,10,int(test_num))    #!############################ test write マイナス符号付き実数値の数値が書き込めるかのテスト
        
        pyxel.save("assets/system/system-data.pyxres") #システムデータを書き込み

    #自機との距離を求める関数定義
    def to_my_ship_distance(self,x,y):
        dx = x - self.my_x
        dy = y - self.my_y
        distance = math.sqrt(dx * dx + dy * dy)
        return(distance)   #最初この行を return(self,distance)って記述しててエラーが出て、どうやったら良いのかわかんなかった・・・この場合はタプルになるらしい！？(良く判って無いｗ)

    #狙い撃ち弾を射出する関数定義 
    def enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
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
                new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,vx,vy, accel,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count,0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む

    #狙い撃ち弾(ゲームランクに依存)を射出する関数定義 
    def enemy_aim_bullet_rank(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
        if func.s_rndint(self,0,self.run_away_bullet_probability) != 0:
            return
        else:
            func.enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel)

    #前方3way弾を射出する関数定義 
    def enemy_forward_3way_bullet(self,ex,ey):
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1,0,            1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,-0.5*0.8,   1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,0.5*0.8,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)  

    #前方5way弾を射出する関数定義 
    def enemy_forward_5way_bullet(self,ex,ey):
        if len(self.enemy_shot) < 800:
            func.enemy_forward_3way_bullet(self,ex,ey) #まずは前方3way弾を射出
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,0.2,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)
            
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,-0.2,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)

    #狙い撃ちn-way弾を射出する関数定義
    def enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count):#ex,ey=敵の座標(弾を出す座標),theta=弾と弾の角度,n=弾の総数,div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ,div_count=分裂するまでのカウント(div_count_originにも同じ数値が入ります),div_num=分裂する回数,stop_count=その場に止まるカウント数
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
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,cvx,cvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)#敵弾リストに中央狙い弾の情報を書き込む
                    
                    for i in range((n+1) // 2):
                        #時計回り方向に i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(theta*i*0.0174) - cvy * math.sin(theta*i*0.0174)
                        rvy = cvx * math.sin(theta*i*0.0174) + cvy * math.cos(theta*i*0.0174)
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                        
                        #反時計回り方向に -i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(-(theta*i*0.0174)) - cvy * math.sin(-(theta*i*0.0174))
                        rvy = cvx * math.sin(-(theta*i*0.0174)) + cvy * math.cos(-(theta*i*0.0174))
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                    
                else:
                    #偶数弾の処理#######2way弾とか4ay弾とか6way弾とか##################################
                    for i in range(n // 2):
                        #時計回り方向に i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(theta / 2*(i+1)*0.0174) - cvy * math.sin(theta / 2*(i+1)*0.0174)
                        rvy = cvx * math.sin(theta / 2*(i+1)*0.0174) + cvy * math.cos(theta / 2*(i+1)*0.0174)
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                        
                        #反時計回り方向に -i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                        rvx = cvx * math.cos(-(theta // 2 * (i+1) * 0.0174)) - cvy * math.sin(-(theta // 2*(i+1)*0.0174))
                        rvy = cvx * math.sin(-(theta // 2 * (i+1) * 0.0174)) + cvy * math.cos(-(theta // 2*(i+1)*0.0174))
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,   1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む

    #レーザービームを発射する関数定義
    def enemy_laser(self,ex,ey,length,speed):
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(ENEMY_SHOT_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -(speed),0,    1,1,1,   0,0,0,    speed,0,0,  0, number * 2 ,PRIORITY_BOSS_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #サイン弾を射出する関数定義 
    def enemy_sin_bullet(self,ex,ey,timer,speed,intensity):
        if len(self.enemy_shot) < 800:
            new_enemy_shot = Enemy_shot()
            new_enemy_shot.update(ENEMY_SHOT_SIN,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0, 0,0,  1,1,1, 1,1,   timer,speed,intensity,  0, 0,   0,PRIORITY_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
            self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む

    #ボス用のレッドレーザービームを発射する関数定義
    def enemy_red_laser(self,ex,ey,length,speed):
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(ENEMY_SHOT_RED_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #ボス用のグリーンレーザービームを発射する関数定義
    def enemy_green_laser(self,ex,ey,length,speed):
        if len(self.enemy_shot) < 800: 
            for number in range(length):
                new_enemy_shot = Enemy_shot()
                new_enemy_shot.update(ENEMY_SHOT_GREEN_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,  0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                self.enemy_shot.append(new_enemy_shot)
        return()

    #ミサイルリスト内から同じタイプのミサイルが何発存在するのか数をカウントする関数定義
    def count_missile_type(self,missile_type1,missile_type2,missile_type3,missile_type4):
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
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + ((self.stage_loop - 1)* 16 * self.height_screen_num),n)

    #背景マップチップを消去する(NULLチップナンバーを書き込む) x,yはキャラ単位 x=(0~255) y=(0~15)
    def delete_map_chip(self,x,y):
        # func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16,0)#マップチップを消去する（0=何もない空白）を書き込む
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16 * self.height_screen_num,self.null_bg_chip_num)

    #背景(BGタイルマップのキャラチップ)を取得する (8方向フリースクロール専用)
    def get_bg_chip_free_scroll(self,x,y,bg_chip):
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
        func.set_chrcode_tilemap(self,self.reference_tilemap,x,y,n)#マップチップナンバーnを座標x,yに書き込む

    #背景マップ(BG)にアクセスする時に使用するself.bgx,self.bgyを0~255の間に収めるようにクリッピング処理する(-1とか256でタイルマップにアクセスするとエラーが出るため)
    def clip_bgx_bgy(self):
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

    #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数
    def level_up_my_shot(self):
        if self.shot_exp > SHOT_EXP_MAXIMUM:  #自機ショットの経験値は最大経験値を超えないように補正してやります
            self.shot_exp = SHOT_EXP_MAXIMUM
        if self.shot_exp < 0:              #自機ショットの経験値は0より小さくならないよう補正します
            self.shot_exp = 0             #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
        
        self.shot_level            = self.shot_table_list[self.shot_exp][0] #テーブルリストを参照して経験値に対応したショットレベルを代入する
        self.shot_speed_magnification = self.shot_table_list[self.shot_exp][1] #テーブルリストを参照して経験値に対応したショットスピード倍率を代入する
        self.shot_rapid_of_fire      = self.shot_table_list[self.shot_exp][2] #テーブルリストを参照して経験値に対応したショット連射数を代入する

    #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数
    def level_up_my_missile(self):
        if self.missile_exp > MISSILE_EXP_MAXIMUM:  #自機ミサイルの経験値は最大経験値を超えないように補正してやります
            self.missile_exp = MISSILE_EXP_MAXIMUM
        if self.missile_exp < 0:              #自機ミサイルの経験値は0より小さくならないよう補正します
            self.missile_exp = 0             #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
        
        self.missile_level            = self.missile_table_list[self.missile_exp][0] #テーブルリストを参照して経験値に対応したミサイルレベルを代入する
        self.missile_speed_magnification = self.missile_table_list[self.missile_exp][1] #テーブルリストを参照して経験値に対応したミサイルスピード倍率を代入する
        self.missile_rapid_of_fire      = self.missile_table_list[self.missile_exp][2] #テーブルリストを参照して経験値に対応したミサイル連射数を代入する

    #敵編隊出現時、現在の編隊IDナンバーとIDナンバーに対応した編隊数、そして現在の生存編隊数をenemy_formationクラスに登録する関数
    def record_enemy_formation(self,num):
        #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
        new_enemy_formation = Enemy_formation()
        new_enemy_formation.update(self.current_formation_id,num,num,num)
        self.enemy_formation.append(new_enemy_formation)
        self.current_formation_id += 1             #編隊IDを1増加させ次の編隊IDにするのです

    #敵破壊時、編隊ＩＤをみて編隊リストに登録されていた撃墜するべき総数を減少させ、全滅させたらフラグを立てて戻ってくる関数
    def check_enemy_formation_shoot_down_number(self,id):
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
        enemy_formation_count = len(self.enemy_formation)
        for i in reversed(range(enemy_formation_count)): #インスタンスを消去するのでreversedで昇順ではなく降順で調べていきます
            if id == self.enemy_formation[i].formation_id: #調べるidとリストに登録されているidが同じだったら
                self.enemy_formation[i].on_screen_formation_number -= 1 #画面上に存在する編隊数を1機減らす
                if self.enemy_formation[i].on_screen_formation_number == 0: #もし編隊がすべて画面に存在しないのなら
                    del self.enemy_formation[i]     #該当した編隊リストは必要ないのでインスタンスを消去する
                    break                       #もうこれ以上リストを調べ上げる必要はないのでbreakしてループから抜け出す

    #敵を破壊した後の処理
    def enemy_destruction(self,e):
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
        #ドットパーティクル生成
        if len(self.particle) < 1000: #パーティクル総数が1000以下なら発生させる
            for _number in range(10):
                new_particle = Particle()
                new_particle.update(PARTICLE_DOT,hit_x+4,hit_y+4,func.s_rndint(self,0,1),random() * 2 - 0.5 + hit_vx / 2,random() * 2 - 1 +hit_vy / 2,func.s_rndint(self,5,20),0,func.s_rndint(self,1,14))
                self.particle.append(new_particle)
                #update_obj.append_particle(self,PARTICLE_DOT,hit_x,hit_y,hit_vx / 2,hit_vy / 2, 0,0,0)
        
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
            self.game_status = SCENE_BOSS_EXPLOSION           
            #ボスの状態遷移フラグステータスを「BOSS_STATUS_EXPLOSION_START」ボス撃破！爆発開始！にしてやる
            self.boss[e].status = BOSS_STATUS_EXPLOSION_START
            
        
        pyxel.play(0,2)#変な爆発音を出すのだ～～～☆彡 チャンネル0 でサウンドナンバー2の音を鳴らす

    #各面のボスをBossクラスに定義して出現させる
    def born_boss(self):
        #col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8,1*8,5*8,2*8
        if       self.stage_number == STAGE_MOUNTAIN_REGION:
            new_boss = Boss()
            boss_id = 0
            boss_type = BOSS_BREEZARDIA
            boss_status = BOSS_STATUS_MOVE_LEMNISCATE_CURVE
            parts_number = 0
            main_hp = 150
            parts1_hp,parts2_hp,parts3_hp,parts4_hp = 50,50,50,50
            parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
            parts9_hp = 0
            parts1_score,parts2_score,parts3_score = 1,1,1
            parts4_score,parts5_score,parts6_score = 1,1,1
            parts7_score,parts8_score,parts9_score = 1,1,1 
            level = LV00
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,4,0,0,0  #上部メイン主砲
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,30,0,0,0 #前部グリーンレーザー砲
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
            posx,posy = -64,50
            offset_x,offset_y = 0,0
            ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
            width,height = 14*8,6*8
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h =  5 ,3*8,1*8,1*8
            col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 7*8,2*8,1*8,1*8
            col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 0,0,0,0
            col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 0,0,0,0
            
            col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8  ,1*8+5,    6*8-2,2*8
            col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 2*8  ,4*8  ,    6*8,2*8-2
            col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 7*8  ,3*8  ,   4*8  ,1*8 
            col_main4_x, col_main4_y, col_main4_w, col_main4_h  =   0  ,    0,    0,    0
            col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   0  ,    0,    0,    0
            col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   0  ,    0,    0,    0
            col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   0  ,    0,    0,    0
            col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   0  ,    0,    0,    0
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =10*8 ,5*8,  8,  8
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h =9*8-4,5*8,  8,  8
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h =5*8-3,  2,  8,  8
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h =2*8  ,1*8-6,8,  8
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =    0,  0,  0,  0
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =    0,  0,  0,  0
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =    0,  0,  0,  0
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =    0,  0,  0,  0
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =    0,  0,  0,  0
            
            main_hp_bar_offset_x,main_hp_bar_offset_y    = 8,-3
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 10*8  ,5*8+10
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y =  9*8-4,5*8+10
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y =  5*8-3, -2
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y =  2*8  ,  0
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y =     0,  0
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y =     0,  0
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y =     0,  0
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y =     0,  0
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y =     0,  0
            
            size = 0
            priority = 0
            attack_method = BOSS_ATTACK_FRONT_5WAY
            direction = 0
            acceleration = 0
            timer = 0
            degree = 0
            radian = 0
            speed = 0
            radius = 0
            flag1,flag2,flag3,flag4 = 0,0,0,0
            count1,count2,count3,count4 = 0,0,0,0
            parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
            parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
            parts9_flag = 0
            animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
            move_index = 0
            obj_time = 0
            obj_totaltime = 0
            invincible = 0
            display_time_main_hp_bar = 0
            display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
            display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
            display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
            display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
            display_time_parts9_hp_bar = 0
            
            new_boss.update(boss_id,boss_type,boss_status,
                parts_number,
                main_hp,
                parts1_hp,parts2_hp,parts3_hp,parts4_hp,
                parts5_hp,parts6_hp,parts7_hp,parts8_hp,
                parts9_hp,
                parts1_score,parts2_score,parts3_score,
                parts4_score,parts5_score,parts6_score,
                parts7_score,parts8_score,parts9_score,
                level,
                
                weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                
                posx,posy,offset_x,offset_y,
                ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                width,height,
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
                
                col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
                col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
                col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
                col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
                col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
                col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
                col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
                col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
                col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,
                
                main_hp_bar_offset_x,main_hp_bar_offset_y,
                parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
                parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
                parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
                parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
                parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
                parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
                parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
                parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
                parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,
                
                size,priority,attack_method,direction,acceleration,timer,degree,radian,speed,radius,
                flag1,flag2,flag3,flag4,
                count1,count2,count3,count4,
                parts1_flag,parts2_flag,parts3_flag,
                parts4_flag,parts5_flag,parts6_flag,
                parts7_flag,parts8_flag,parts9_flag,
                animation_number1,animation_number2,animation_number3,animation_number4,
                move_index,
                obj_time,obj_totaltime,
                invincible,
                display_time_main_hp_bar,
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar
                )
            self.boss.append(new_boss)      
            
        elif     self.stage_number == STAGE_ADVANCE_BASE or self.stage_number == STAGE_VOLCANIC_BELT:
            new_boss = Boss()
            boss_id = 0
            boss_type = BOSS_FATTY_VALGUARD
            boss_status = BOSS_STATUS_MOVE_COORDINATE_INIT
            parts_number = 0
            main_hp = 400
            parts1_hp,parts2_hp,parts3_hp,parts4_hp = 70,70,70,200
            parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
            parts9_hp = 0
            parts1_score,parts2_score,parts3_score = 1,1,1
            parts4_score,parts5_score,parts6_score = 1,1,1
            parts7_score,parts8_score,parts9_score = 1,1,1 
            level = LV00
            
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,0,0,0,0
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,0,0,0,0
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
            
            posx,posy = -64,50
            offset_x,offset_y = 0,0
            ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
            width,height = 8*8,5*8
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h = 1*8,1*8,5*8,2*8
            col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 6*8,2*8,1*8,1*8
            col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 3*8,3*8,3*8,1*8
            col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 2*8,  6,  8,  6
            
            col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8+4,1*8,5*8-4,2*8
            col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 6*8+4,2*8,1*8-4,1*8
            col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 3*8+4,3*8,3*8-4,1*8 
            col_main4_x, col_main4_y, col_main4_w, col_main4_h  = 2*8+4,  6,  8-4,  6 
            col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   8,  8,  0,  0 
            col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   8,  8,  0,  0
            col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   8,  8,  0,  0 
            col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   8,  8,  0,  0 
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =   0,2*8,2*8,  8
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h = 1*8,  0,2*8,  8
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h = 1*8,3*8,  8,  8
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h = 6*8,3*8,  8,  8
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =   0,  0,  0,  0
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =   0,  0,  0,  0
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =   0,  0,  0,  0
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =   0,  0,  0,  0
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =   0,  0,  0,  0
            
            main_hp_bar_offset_x  ,main_hp_bar_offset_y   = 8,-2
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 0,24
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y = 0,4
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y = 8,32
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y = 48+2,32
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y = 0,0
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y = 0,0
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y = 0,0
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y = 0,0
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y = 0,0
            
            size = 0
            priority = 0
            attack_method = 0
            direction = 0
            acceleration = 0
            timer = 0
            degree = 0
            radian = 0
            speed = 0
            radius = 0
            flag1,flag2,flag3,flag4 = 0,0,0,0
            count1,count2,count3,count4 = 0,0,0,0
            parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
            parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
            parts9_flag = 0
            animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
            move_index = 0
            obj_time = 0
            obj_totaltime = 0
            invincible = 0
            display_time_main_hp_bar = 0
            display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
            display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
            display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
            display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
            display_time_parts9_hp_bar = 0
            
            new_boss.update(boss_id,boss_type,boss_status,
                parts_number,
                main_hp,
                parts1_hp,parts2_hp,parts3_hp,
                parts4_hp,parts5_hp,parts6_hp,
                parts7_hp,parts8_hp,parts9_hp,
                parts1_score,parts2_score,parts3_score,
                parts4_score,parts5_score,parts6_score,
                parts7_score,parts8_score,parts9_score,
                level,
                
                weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                
                posx,posy,offset_x,offset_y,
                ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                width,height,
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
                col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
                col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
                col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
                col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
                col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
                col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
                col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
                col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
                col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,
                
                main_hp_bar_offset_x,main_hp_bar_offset_y,
                parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
                parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
                parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
                parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
                parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
                parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
                parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
                parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
                parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,
                
                size,priority,attack_method,direction,acceleration,timer,degree,radian,speed,radius,
                flag1,flag2,flag3,flag4,
                count1,count2,count3,count4,
                parts1_flag,parts2_flag,parts3_flag,
                parts4_flag,parts5_flag,parts6_flag,
                parts7_flag,parts8_flag,parts9_flag,
                animation_number1,animation_number2,animation_number3,animation_number4,
                move_index,
                obj_time,obj_totaltime,
                invincible,
                display_time_main_hp_bar,
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar
                )
            self.boss.append(new_boss)

    #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数
    def boss_get_bezier_curve_coordinate(self,i):                    
        self.boss[i].ax           = self.boss_move_data1[self.boss[i].move_index][0]#リストから新たな移動元座標を登録する
        self.boss[i].ay           = self.boss_move_data1[self.boss[i].move_index][1]
        self.boss[i].dx           = self.boss_move_data1[self.boss[i].move_index][2]#リストから新たな移動先座標を登録する
        self.boss[i].dy           = self.boss_move_data1[self.boss[i].move_index][3]
        self.boss[i].qx           = self.boss_move_data1[self.boss[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
        self.boss[i].qy           = self.boss_move_data1[self.boss[i].move_index][5]
        
        self.boss[i].obj_totaltime  = self.boss_move_data1[self.boss[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する
        
        self.boss[i].speed        = self.boss_move_data1[self.boss[i].move_index][7]#リストから移動スピードを取得し登録する
        self.boss[i].acceleration   = self.boss_move_data1[self.boss[i].move_index][8]#リストから加速度を取得し登録する
        
        self.boss[i].attack_method  = self.boss_move_data1[self.boss[i].move_index][9]#リストから攻撃方法を取得し登録する

    #ボスの耐久力バーの表示(ボスの付近にＨＰバーを描画する)
    def display_boss_hp_bar(self,x,y,hp):
        pyxel.rectb(x-1,y-1, 32+2,3, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
        pyxel.line(x,y, x + hp,y, 8) #赤色の耐久力バーの表示

    #ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)短いタイプ横16ドット
    def display_boss_hp_short_bar(self,x,y,hp):
        pyxel.line(x,y + 1, x + 12,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
        pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示

    #ボスの各部位耐久力バーの表示(破壊可能部位の付近にＨＰバーを描画する)更に短いタイプ横8ドット
    def display_boss_hp_short2_bar(self,x,y,hp):
        pyxel.line(x,y + 1, x + 4,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
        pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示

    #ゲーム全体でボスをトータル何体破壊したか計算する関数(戻り値num=トータル累計ボス破壊数)
    def total_defeat_boss_num(self):
        global num 
        num = 0
        for i in range(len(self.boss_number_of_defeat)):
            num += self.boss_number_of_defeat[i]
        
        return(num)

    #ボス撃破時にすべてのボスパーツを破壊したかどうか調べる関数
    #parts1~parts4まで調べ上げます 全てのパーツを破壊したのならTrueを返す、出来てなかったらFalseを返します
    def check_destroy_all_boss_parts(self):
        boss_hit = len(self.boss)
        for i in reversed(range (boss_hit) ):
            if self.boss[i].parts1_flag == 0 and self.boss[i].parts2_flag == 0 and self.boss[i].parts3_flag == 0 and self.boss[i].parts4_flag == 0:
                return(True)
            else:
                return(False)

    #スコア加算処理
    def add_score(self,point):
        self.score += int(point * self.score_magnification) #スコアをpoint*スコア倍率分加算する(整数値で)

    #バックグラウンド(BG)を表示するときのカメラオフセット座標値を計算する
    def screen_camera_offset(self):
        #WINDOW_H    ゲーム画面の縦幅 (定数です)
        #SHIP_H      自機の縦幅8ドット(定数です)
        #bg_height   BGスクロール面の全体としての縦幅
        #my_y        自機のy座標(BGスクロール面の一番上を0として、そこからの縦の距離)
        self.camera_offset_y = (self.bg_height - WINDOW_H) * self.my_y / (self.bg_height - SHIP_H)

    #ラスタースクロール用のデータの初期化＆生成
    def create_raster_scroll_data(self):
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
        raster_scroll_count = len(self.raster_scroll)
        for i in range(raster_scroll_count): #ラスタースクロールクラスに登録されたインスタンスのdisplayを調べていきます
            if self.raster_scroll[i].scroll_id == id: #scroll_idと調べるidが一致したのなら
                self.raster_scroll[i].display = flag #flag(0=表示しない 1=表示する)を書き込む

    #ランクに応じた数値をリストから取得する
    def get_rank_data(self):
        self.enemy_speed_mag           = self.game_rank_data_list[self.rank][LIST_RANK_E_SPEED_MAG]            #敵スピード倍率をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_speed_mag    = self.game_rank_data_list[self.rank][LIST_RANK_BULLET_SPEED_MAG]        #敵狙い撃ち弾スピード倍率をリストを参照してランク数で取得、変数に代入する
        self.return_bullet_probability = self.game_rank_data_list[self.rank][LIST_RANK_RETURN_BULLET_PROBABILITY] #敵撃ち返し弾発射確率をリストを参照してランク数で取得、変数に代入する
        self.enemy_hp_mag              = self.game_rank_data_list[self.rank][LIST_RANK_E_HP_MAG]               #敵耐久力倍率をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_append       = self.game_rank_data_list[self.rank][LIST_RANK_E_BULLET_APPEND]         #弾追加数をリストを参照してランク数で取得、変数に代入する
        self.enemy_bullet_interval     = self.game_rank_data_list[self.rank][LIST_RANK_E_BULLET_INTERVAL]        #弾発射間隔減少パーセントをリストを参照してランク数で取得、変数に代入する
        self.enemy_nway_level          = self.game_rank_data_list[self.rank][LIST_RANK_NWAY_LEVEL]             #nWAY弾のレベルをリストを参照してランク数で取得、変数に代入する

    #難易度に応じた数値をリストから取得する
    def get_difficulty_data(self):
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

    #ランクダウンさせる関数
    def rank_down(self):
        if self.rank > 0: #ランク数が0より大きいのならば
            self.rank -= 1      #ランク数をデクリメント
            func.get_rank_data(self) #ランク数が変化したのでランク数をもとにしたデータをリストから各変数に代入する関数の呼び出し

    #各ステージBGMのロード
    def load_stage_bgm(self):
        if   self.stage_number == STAGE_MOUNTAIN_REGION:
            pygame.mixer.music.load("assets/music/BGM088-100714-kongoushinkidaia-su.wav") #STAGE1 BGMファイルの読み込み
            pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        elif self.stage_number == STAGE_ADVANCE_BASE:
            pygame.mixer.music.load("assets/music/BGM056-081012-kakeroginnnogennya.wav")  #STAGE2 BGMファイルの読み込み
            pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        elif self.stage_number == STAGE_VOLCANIC_BELT:
            pygame.mixer.music.load("assets/music/BGM219-181031-hankotsunoranbu.wav")     #STAGE3 BGMファイルの読み込み
            pygame.mixer.music.set_volume(self.master_bgm_vol / 100)

    #0~9の範囲の乱数関数
    def rnd0_9(self):
        global num
        num = self.rnd0_9_num
        return(num)

    #0~99の範囲の乱数関数
    def rnd0_99(self):
        global num
        num = self.rnd0_99_num
        return(num)

    #線形合同法を使用した乱数関数 (0~65535のランダムな数値がself.rnd_seedに代入される)この乱数の周期は32768
    def s_rnd(self):
        self.rnd_seed = (self.rnd_seed * 48828125 + 129) % 65536 #129のように足す数値は絶対に奇数にするように！でないと奇数と偶数の乱数が交互に育成されるようになってしまうからね

    #s_rndint(min,max) と呼ぶと、minからmax(max自身を含む)までの間の整数が 等しい確率でランダムに返される
    def s_rndint(self,min,max):
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        func.s_rnd(self)                              #0~65535のランダムな数値がself.rnd_seedに代入される
        num_zero_to_max = self.rnd_seed % (max - min) #  0 から(max - min)までの乱数を取得
        num_min_to_max  = num_zero_to_max + min      #min から max      までの乱数を取得
        num = num_min_to_max                     #整数化します
        return (num)

    #s_random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(パーティクル系で使おうとしたけど結構動作が遅いので標準ライブラリ使ったほうがいいなぁ→結局random()を使う事にしました)
    def s_random(self):
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
        pyxel.text(x-8*3,y,"   :", int(col))
        minutes = "{:>3}".format(self.one_game_playtime_seconds // 60)
        seconds = "{:>02}".format(self.one_game_playtime_seconds % 60)
        pyxel.text(x-8*3,y,minutes, int(col))
        pyxel.text(x-8  ,y,seconds, int(col))

    #総プレイ時間の表示(秒まで表示します)
    def disp_total_game_playtime(self,x,y,col):
        pyxel.text(x-8*3,y,":  :", int(col))
        total_seconds = "{:>02}".format(self.total_game_playtime_seconds % 60)
        total_minutes = "{:>02}".format(self.total_game_playtime_seconds // 60 % 60)
        total_hours   = "{:>04}".format(self.total_game_playtime_seconds // 3600)
        pyxel.text(x-8*6+8,y,  total_hours, int(col))
        pyxel.text(x-8*3+4,y,total_minutes, int(col))
        pyxel.text(x-8    ,y,total_seconds, int(col))

    #矩形Aと矩形Bの当たり判定
    #collision rectangle to rectangle
    #矩形A(rect_ax,rect_ay,rect_aw,rect_ah)(xはx座標,yはy座標,wは横幅width,hは縦幅heightを意味します)
    #矩形B(rect_bx,rect_by,rect_bw,rect_bh)
    #1...矩形の中心座標を計算する
    #2...x軸,y軸の距離を計算する
    #3...2つの矩形のx軸,y軸のサイズの和を計算する
    #4...サイズの和と距離を比較する
    #衝突していたらTrueをしていなかったらFalseを返します
    def collision_rect_rect(self,rect_ax,rect_ay,rect_aw,rect_ah,rect_bx,rect_by,rect_bw,rect_bh):
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

    #各種ウィンドウの育成             id=windowクラスの window_idに入っている数値 ox,oy=ウィンドウ作成座標のオフセット値
    def create_window(self,id,ox,oy):
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
            ["MENU",DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [["GAME START"   ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "DIFFICULTY"   ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SELECT SHIP"  ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "MEDAL"        ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SCORE BOARD"  ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "STATUS"       ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "NAME ENTRY"   ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "CONFIG"       ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "REPLAY"       ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "SELECT STAGE" ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            [ "SELECT LOOP"  ,DISP_CENTER,0,0,3,MES_NO_FLASH],\
            [ "BOSS MODE"    ,DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "EXIT"         ,DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["1",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "2",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "3",DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            ["SELECT",DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [[".",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ ".",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_BOSS_MODE,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
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
            ["SELECT",DISP_CENTER,0,0,7,MES_RAINBOW_FLASH],\
            
            [[" ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"OFF",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_HIT_BOX,0,"ON" ,DISP_CENTER,1, 0,0, 7,10]],\
            
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
            ["DIFFICULTY",DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [[" ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY EASY",DISP_CENTER,0, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "EASY",     DISP_CENTER,1, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "NORMAL",   DISP_CENTER,2, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "HARD",     DISP_CENTER,3, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "VERY HARD",DISP_CENTER,4, 0,0, 7,10],\
            [ " ",DISP_CENTER,0,0,7,MES_NO_FLASH,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,   LIST_WINDOW_FLAG_DIFFICULTY,0, "INSAME",   DISP_CENTER,5, 0,0, 7,10]],\
            
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
            ["RETURN TITLE?",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["SAVE & RETURN",DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
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
            ["RETURN TITLE?",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["RETURN",DISP_CENTER,0,0,6,MES_NO_FLASH]],\
            
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
            ["ENTER YOUR NAME",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["",DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
            NO_ITEM_KANJI_TEXT,[self.my_name,DISP_LEFT_ALIGN,20,12,10,MES_NO_FLASH],NO_ANIMATION_TEXT,NO_SCROLL_TEXT,NO_SCRIPT,\
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
            ["CONFIGURATION",DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [["SCREEN MODE", DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SCREEN_MODE,OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["WINDOW","FULL SCREEN"]],\
            ["BGM VOLUME",   DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BGM_VOL,    OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   100,[" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*3+1, STEP4*19,STEP8*3+1],\
            ["SE VOLUME",    DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_SE_VOL,     OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,0,   100,[" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*4+1, STEP4*19,STEP8*4+1],\
            ["CONTROL TYPE", DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_CTRL_TYPE,  OPE_OBJ_TYPE_NUM,   "",DISP_LEFT_ALIGN,0,   70+4,0,7,10,1,   5,  [" "," "],               0,     DISP_OFF,DISP_OFF,DISP_ON,DISP_ON, 0,0, 0,0, STEP4*25,STEP8*5+1, STEP4*19,STEP8*5+1],\
            ["",             DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["",             DISP_LEFT_ALIGN, 0,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["LANGUAGE",     DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_LANGUAGE,   OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["ENGLISH","JAPANESE"], ],\
            ["BOSS MODE",    DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_BOSS_MODE,  OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["HIT BOX",      DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_HIT_BOX,    OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["DEBUG MODE",   DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  LIST_WINDOW_FLAG_DEBUG_MODE, OPE_OBJ_TYPE_ON_OFF,"",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   100,["OFF"," ON"]           ],\
            ["INITIALIZE",   DISP_LEFT_ALIGN,10,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            ["RETURN",       DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  ["",""]     ]           ],\
            
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
            ["INITIALIZE",DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE",      DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "NAME",       DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "ALL",        DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "",         DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "RETURN",     DISP_CENTER,0,0,7,MES_YELLOW_FLASH]],\
            
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
            ["GRAPHICS",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["FULL SCREEN",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["PARTICL",DISP_CENTER,0,0,3,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,3,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            ["",DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            [" ",DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" Lv1",DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv2",DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH],\
            [ " Lv3",DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
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
            ["EXIT GAME ??",DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO", DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
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
            ["BACK TO GAMES",  DISP_CENTER,0,0, 7,MES_RED_FLASH],\
            
            [[ "RETURN TITLE",  DISP_CENTER,0,0,10,MES_NO_FLASH],\
            [  "RESTART STAGE", DISP_CENTER,0,0, 7,MES_NO_FLASH],\
            [  "EXIT GAME",     DISP_CENTER,0,0,10,MES_NO_FLASH],\
            [  " ",             DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
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
            ["RETURN TITLE ??",DISP_CENTER,0,0,7,MES_RED_FLASH],\
            
            [["NO", DISP_CENTER,0,0,7,MES_NO_FLASH],\
            [ "YES",DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
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
            ["EQUIPMENT MEDAL",DISP_CENTER,     0,0,7,MES_MONOCHROME_FLASH],\
            
            [[" ",DISP_LEFT_ALIGN,0,0,7,MES_NO_FLASH]],\
            
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
            ["STATUS",DISP_CENTER,0,0,7,MES_MONOCHROME_FLASH],\
            
            [["PLAY TIME",     DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "NUMBER OF PLAY",DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "TOTAL SCORE",   DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "",              DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "RETURN",        DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ]],\
            
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
            WINDOW_BG_BLUE_BACK,\
            WINDOW_PRIORITY_NORMAL,\
            DIR_RIGHT_DOWN,\
            DIR_LEFT_UP,\
            WINDOW_OPEN,\
            WINDOW_BETWEEN_LINE_7,\
            ["SELECT SHIP",DISP_CENTER,0,0,7,MES_MONOCHROME_FLASH],\
            
            [["JUSTICE PYTHON",       DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "ELEGANT PERL",         DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "PYTHON FORCE",         DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "CLASSICAL FORTRAN",    DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "AI LOVE LISP",         DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "ECLIPSING ALGOL",      DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "AUNT COBOL",           DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "BEGINNING ADA",        DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "FIRST BASIC",          DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "CUTTER SHARP 2000",    DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "LEGEND ASM",           DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "LAST RUST",            DISP_LEFT_ALIGN,11,0,7,  MES_NO_FLASH,    0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ],\
            [ "RETURN",               DISP_LEFT_ALIGN,11,0,7,  MES_YELLOW_FLASH,0,0,0,0,   0,0,0,0,0,  0,0,0,0,0,  0,                           OPE_OBJ_TYPE_NONE,  "",DISP_LEFT_ALIGN,0,   70  ,0,7,10,0,   0,  [" "," "],              ]],\
            
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
            [" ",DISP_CENTER,0,0,7,MES_NO_FLASH],\
            
            [["NO",DISP_CENTER,0,0,6,MES_NO_FLASH],\
            ["YES",DISP_CENTER,0,0,10,MES_NO_FLASH]],\
            
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
            ["INITIALIZE",DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["SCORE ?",    DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            ["INITIALIZE",DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["NAME ?",    DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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
            ["INITIALIZE",DISP_CENTER,0,0,7,MES_GREEN_FLASH],\
            
            [["ALL SAVE DATA ?",    DISP_CENTER,0,0,7,MES_NO_FLASH]],\
            
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

    #スコアボードウィンドウの表示
    def window_score_board(self,d): #引数dは難易度 difficulty
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
        [str(self.game_difficulty_list[d][LIST_DIFFICULTY_TEXT]),DISP_CENTER,0,0,7,MES_NO_FLASH],\
        
        [[" 1 " + str(self.score_board[d][0][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][0][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][0][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][0][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,10,MES_YELLOW_FLASH],\
        [ " 2 " + str(self.score_board[d][1][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][1][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][1][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][1][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0, 7,MES_NO_FLASH],\
        [ " 3 " + str(self.score_board[d][2][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][2][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][2][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][2][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0, 4,MES_NO_FLASH],\
        [ " 4 " + str(self.score_board[d][3][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][3][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][3][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][3][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 5 " + str(self.score_board[d][4][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][4][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][4][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][4][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 6 " + str(self.score_board[d][5][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][5][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][5][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][5][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 7 " + str(self.score_board[d][6][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][6][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][6][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][6][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 8 " + str(self.score_board[d][7][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][7][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][7][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][7][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ " 9 " + str(self.score_board[d][8][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][8][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][8][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][8][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0,13,MES_NO_FLASH],\
        [ "10 " + str(self.score_board[d][9][LIST_SCORE_BOARD_NAME]) + str("{:>9}".format(self.score_board[d][9][LIST_SCORE_BOARD_SCORE])) + " L" + str("{:>2}".format(self.score_board[d][9][LIST_SCORE_BOARD_LOOP])) + " ST" + str("{:>2}".format(self.score_board[d][9][LIST_SCORE_BOARD_CLEAR_STAGE])),DISP_LEFT_ALIGN,0,0, 2,MES_NO_FLASH]],\
        
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

    #リプレイファイルスロット選択ウィンドウの表示
    def window_replay_data_slot_select(self):
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
        ["SLOT",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        
        [["1",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "2",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "3",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "4",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "5",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "6",DISP_CENTER,0,0,7,MES_NO_FLASH],\
        [ "7",DISP_CENTER,0,0,7,MES_NO_FLASH]],\
        
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

    #メダル取得報告ウィンドウの作成
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
        ["MEDAL GET !!",DISP_CENTER,0,0,7,MES_RED_FLASH],\
        
        [[medal_cmnt_eng,       DISP_CENTER,0, 7,10,MES_NO_FLASH],\
        [ get_cmnt_line1_eng,   DISP_CENTER,0,14, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_eng,   DISP_CENTER,0,14, 7,MES_NO_FLASH]],\
        
        [[medal_cmnt_jpn,       DISP_CENTER,9, 0,10,MES_NO_FLASH],\
        [ get_cmnt_line1_jpn,   DISP_CENTER,9, 7, 7,MES_NO_FLASH],\
        [ get_cmnt_line2_jpn,   DISP_CENTER,9, 7, 7,MES_NO_FLASH]],\
        
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

    #実績(アチーブメント)取得報告ウィンドウの作成
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
        [achieve_cmnt_eng,DISP_LEFT_ALIGN,-6,-7,7,MES_NO_FLASH],\
        
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

    #スコアボードウィンドウ育成時に使用するランクインした機体が装備しているメダルのgraph_listを作製する
    def create_medal_graph_list_for_score_board(self,d,x,y,step_y): #d=difficult(難易度)x,y=メダルを表示し始める座標(1位のSLOT1のメダルから表示し始める),y軸のドット増分数
        for i in range(10): #iは0(1位)から10(11位)まで変化する
            for j in range(ALL_SLOT5): #jは0(SLOT0)から5(SLOT5)まで変化する
                meda_id = self.score_board[d][i][LIST_SCORE_BOARD_SHIP_SLOT0 + j]
                u = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_U]
                v = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_V]
                imgb = self.medal_graph_and_comment_list[meda_id][LIST_MEDAL_GRP_CMNT_IMGB]
                self.temp_graph_list.append([x + j * 7,y + i * step_y,imgb,u,v,8,8,13,1,1])

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

    #ウィンドウIDの検索(与えられたウィンドウIDを元にしてウィンドウ群を検索しインデックスナンバーを取得する)
    def search_window_id(self,id): #id=windowクラスの window_idに入っている数値 発見できなかった時は-1を返します
        window_count = len(self.window)
        num = -1
        for i in range(window_count):
            if self.window[i].window_id == id:
                num = i
                break
        
        return num

    #ウィンドウIDを調べて一致するウィンドウIDの速度、加速度を更新する(同タイプウィンドウ移動消去モード)
    def all_move_window(self,id,vx,vy,vx_accel,vy_accel):
        window_count = len(self.window)
        for i in range(window_count):
            if self.window[i].window_id == id:
                self.window[i].vx,self.window[i].vy             = vx,vy
                self.window[i].vx_accel,self.window[i].vy_accel = vx_accel,vy_accel

    #メダルリストウィンドウで「存在するアイテム」を調べ上げコメント表示フラグテーブルを作製する関数
    def make_medal_list_window_comment_disp_flag_table(self):
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
        #ウィンドウidナンバーを元にそのウィンドウで使用していたカーソルデータのインデックス値を探し出す
        i = func.search_window_id(self,id)
        if i == -1:
            return  #もしもカーソルデータが無かったのならどうしようもないのでリターンする(1対1でカーソルとウィンドウデータを反映してるのでそれは無いと思うですけれども）
        
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
        for i in range(len(self.score_board[diff])): #ランキングデータは11位までなのでiは0~11まで変化する
            for j in range(len(self.score_board[diff])-1,i,-1):
                if self.score_board[diff][j][LIST_SCORE_BOARD_SCORE] > self.score_board[diff][j-1][LIST_SCORE_BOARD_SCORE]: #位置jの得点より前の位置j-1の得点が大きいのなら要素を入れ替える
                    for k in range(LIST_SCORE_BOARD_SHIP_SLOT5): #難易度からスロット5に装備されたメダルIDまでの12種類の要素をループしてコピー
                        self.score_board[diff][j][k],self.score_board[diff][j-1][k] = self.score_board[diff][j-1][k],self.score_board[diff][j][k]

    #プレイ中の自機リスト(playing_ship_list)を参照して自機にメダルをはめ込む（装着？）する関数 (num=メダルIDナンバー)
    def equip_medal_playing_ship(self,num):
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

    #プレイ中の自機リスト(playing_ship_list)を参照して自機からメダルを外す(パージ)する関数(num=自機のスロットナンバー)
    def purge_medal_playing_ship(self,slot_num):
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + slot_num] = MEDAL_NO_SLOT #決定ボタンが押された位置のスロットナンバーを空にする
        pyxel.play(0,18)#カーソルキャンセル音を鳴らす

    #自機に装備され,はめ込まれたメダルを左詰めにする関数(空きスロットの隙間を詰めて、空きスロットがどれだけあるのか見やすくする関数)
    def playing_ship_medal_left_justified(self):
        # start_slot = 0
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #iは0から所持スロットの最大値まで変化していきます
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_NO_SLOT: #これからはめ込む場所が空スロットの場合は・・・一つ右のスロットのメダルと現在のメダルスロットに移動させていく
                for j in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] - i): #jは0から(スロット最大値-i)まで変化していく
                    self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j + 1] #現在のスロットに一つ右横のスロットのメダルIDをコピーしていく

    #今現在プレイしているシップリスト(playing_ship_list)に機体メダルスロット装備リスト(ship_equip_slot_list)を参照しながら装備メダルの情報を読み込んでいく関数
    def read_ship_equip_medal_data(self):
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.playing_ship_list[i][LIST_SHIP_SLOT0 + j] = self.ship_equip_slot_list[i][j]

    #機体メダルスロット装備リスト(ship_equip_slot_list)に今現在プレイしているシップリスト(playing_ship_list)を参照しながら装備メダルの情報を書き込んでいく関数
    def write_ship_equip_medal_data(self):
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.ship_equip_slot_list[i][j] = self.playing_ship_list[i][LIST_SHIP_SLOT0 + j]

    #装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する関数
    def add_medal_effect_shot_bonus(self):
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
        for i in range(6): #iは0(SLOT0)から6(SLOT6)まで変化する
            if  self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_EQUIPMENT_LS_SHIELD: #L’ｓシールド装備メダルならば
                self.ls_shield_hp = 10                                                                     #L'sシールドの耐久力を10にする

    #装備されたメダルを調べ、スロット数を拡張するメダルがあればスロット数を増やし、何も無ければスロット数を初期状態にする関数
    def medal_effect_plus_medallion(self):
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
        st = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]
        for i in range(7 - self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]):
            self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + st] = MEDAL_NO_SLOT

    #メダルの取得判定をする関数
    def judge_medal_acquisition(self):
        if func.search_window_id(self,WINDOW_ID_MEDAL_ACQUISITION_REPORT) != -1: #メダル取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 180
        #プレイ時間で判定するメダルタイプ
        if self.total_game_playtime_seconds >= 10 * 60 and self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム10分以上なら「事前1ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_1SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_1SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_game_playtime_seconds >= 180 * 60 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #総プレイタイム180分以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #トータルスコアで判定するタイプ
        elif self.total_score >= 2000 and self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア2000点以上なら「事前3ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_3SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_3SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        elif self.total_score >= 10000 and self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] == MEDAL_NO_SLOT: #トータルスコア10000点以上なら「事前4ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_4SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_4SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #ボスを倒した回数で判定するタイプ
        elif self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] == MEDAL_NO_SLOT: #1面ボスを1回以上破壊で「事前2ショット」を取得
            self.medal_list[MEDAL_BEFOREHAND_2SHOT_ITEM - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_BEFOREHAND_2SHOT_ITEM,wait)  #メダル取得報告ウィンドウを育成
        
        #プレイ回数で判定するタイプ
        elif self.number_of_play >= 20 and self.medal_list[MEDAL_FRAME_RESIST - 1] == MEDAL_NO_SLOT: #トータルゲームプレイ回数が20以上なら「炎耐性」を取得
            self.medal_list[MEDAL_FRAME_RESIST - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_FRAME_RESIST,wait)  #メダル取得報告ウィンドウを育成
        
        #スコアスターの最大得点倍率で判定するタイプ
        elif self.max_score_star_magnification >= 7 and self.medal_list[MEDAL_PLUS_MEDALLION - 1] == MEDAL_NO_SLOT: #スコアスター最大得点倍率が7以上なら「メダル枠２増設」をゲット！
            self.medal_list[MEDAL_PLUS_MEDALLION - 1] = MEDAL_GET
            pyxel.play(0,25) #メダルゲットアラーム音を鳴らす
            func.create_medal_acquisition_report_window(self,20,90,MEDAL_PLUS_MEDALLION,wait)  #メダル取得報告ウィンドウを育成

    #実績(アチーブメント)の取得判定をする関数
    def judge_achievement_acquisition(self):
        if func.search_window_id(self,WINDOW_ID_ACHIEVEMENT_ACQUISITION_REPORT) != -1: #実績取得報告ウィンドウがまだ画面に存在するときはそのままリターンする
            return
        
        wait = 360
        #出撃回数(遊んだ回数)で判別するタイプ
        if self.number_of_play == 0 and self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED: #プレイ回数が0で出撃したのならFIRST CAMPAIGN「初陣」実績取得
            self.achievement_list[ACHIEVEMENT_FIRST_CAMPAIGN][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CAMPAIGN,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #ボスを倒した回数で判定するタイプ
        #1面ボスを1回以上破壊で「1面ボス撃破」実績取得
        if self.boss_number_of_defeat[STAGE_MOUNTAIN_REGION] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE01_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE01_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #2面ボスを1回以上破壊で「2面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ADVANCE_BASE] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE02_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE02_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #3面ボスを1回以上破壊で「3面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_VOLCANIC_BELT] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE03_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE03_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #4面ボスを1回以上破壊で「4面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_NIGHT_SKYSCRAPER] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE04_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE04_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #5面ボスを1回以上破壊で「5面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_AMPHIBIOUS_ASSAULT_SHIP] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE05_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE05_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #6面ボスを1回以上破壊で「6面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_DEEP_SEA_TRENCH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE06_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE06_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #7面ボスを1回以上破壊で「7面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_INTERMEDIATE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE07_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE07_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #8面ボスを1回以上破壊で「8面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_ESCAPE_FORTRESS] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE08_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE08_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #9面ボスを1回以上破壊で「9面ボス撃破」実績取得
        elif self.boss_number_of_defeat[STAGE_BOSS_RUSH] >= 1 and self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_STAGE09_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_STAGE09_BOSS,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #ボスの累計撃破数で判定するタイプ
        #ボス累計10体撃破！
        if func.total_defeat_boss_num(self) >= 10 and self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_DESTROY_BOSS_10TIME][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_DESTROY_BOSS_10TIME,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        
        #パワーカプセルの取得累計数で取得するタイプの実績
        #ショットカプセル10個取得
        wait = 360
        if self.get_shot_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル50個取得
        elif self.get_shot_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル100個取得
        elif self.get_shot_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル200個取得
        elif self.get_shot_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル500個取得
        elif self.get_shot_pow_num >= 500 and self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_500_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_500_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル1000個取得
        elif self.get_shot_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2000個取得
        elif self.get_shot_pow_num >= 2000 and self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2000_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2000_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ショットカプセル2465個取得
        elif self.get_shot_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_SHOT_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_SHOT_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #ミサイルカプセル10個取得
        elif self.get_missile_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル50個取得
        elif self.get_missile_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル100個取得
        elif self.get_missile_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル200個取得
        elif self.get_missile_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル400個取得
        elif self.get_missile_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル765個取得
        elif self.get_missile_pow_num >= 765 and self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_765_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_765_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル1000個取得
        elif self.get_missile_pow_num >= 1000 and self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1000_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1000_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #ミサイルカプセル2465個取得
        elif self.get_missile_pow_num >= 2465 and self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_2465_MISSILE_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_2465_MISSILE_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #シールドカプセル10個取得
        elif self.get_shield_pow_num >= 10 and self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル50個取得
        elif self.get_shield_pow_num >= 50 and self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル100個取得
        elif self.get_shield_pow_num >= 100 and self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル200個取得
        elif self.get_shield_pow_num >= 200 and self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_200_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_200_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル400個取得
        elif self.get_shield_pow_num >= 400 and self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_400_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_400_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #シールドカプセル530個取得
        elif self.get_shield_pow_num >= 530 and self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_530_SHIELD_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_530_SHIELD_POW,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
            
        #初めてクローゲットで「はじめてのクロー」実績取得
        elif self.get_claw_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_CLAW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_CLAW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル10個取得
        elif self.get_claw_num >= 10 and self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_10_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_10_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル20個取得
        elif self.get_claw_num >= 20 and self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_20_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_20_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル50個取得
        elif self.get_claw_num >= 50 and self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_50_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_50_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        #クローカプセル100個取得
        elif self.get_claw_num >= 100 and self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_100_CLAW_POW][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_100_CLAW_POW,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        
        #武器レベルで判別して取得するタイプの実績
        #初めて5WAYバルカンショットを体験
        wait = 360
        if self.shot_level == SHOT_LV3_5WAY_VULCAN_SHOT and self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_5WAY_SHOT][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_5WAY_SHOT,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてレーザーを体験
        elif self.shot_level == SHOT_LV4_LASER and self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてツインレーザーを体験
        elif self.shot_level == SHOT_LV5_TWIN_LASER and self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_TWIN_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_TWIN_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてシャワーレーザーを体験
        elif self.shot_level == SHOT_LV6_3WAY_LASER and self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_SHOWER_LASER][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_SHOWER_LASER,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めてウェーブカッターを体験
        elif self.shot_level == SHOT_LV7_WAVE_CUTTER_LV1 and self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        #初めて最大ウェーブカッターを体験
        elif self.shot_level == SHOT_LV10_WAVE_CUTTER_LV4 and self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_MAX_WAVE][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_MAX_WAVE,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
            return
        
        #特殊条件を満たし各工程でのフラグが立ったら取得するタイプの実績
        #初めてパワーカプセルゲットで「はじめてのパワーカプセル回収成功！」実績取得
        wait = 360
        if self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            if self.get_shot_pow_num >= 1 or self.get_missile_pow_num >= 1 or self.get_shield_pow_num >= 1:
                self.achievement_list[ACHIEVEMENT_FIRST_POW_UP][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
                pyxel.play(0,26) #実績取得音を鳴らす
                func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_POW_UP,WINDOW_PRIORITY_NORMAL,wait)  #実績取得報告ウィンドウを育成
                return
        
        #初めてトライアングルアイテム取得で「初めてトライアングルアイテム」実績取得
        if self.get_triangle_pow_num >= 1 and self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            return
        
        #早回実績取得用フラグが立っているのならば「早回し発生実績」を取得
        #初めての早回し体験
        if self.fast_forward_flag == FLAG_ON and self.fast_forward_num == 1-1 and self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_FIRST_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_FIRST_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し8回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 8-1 and self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_8_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_8_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し16回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 16-1 and self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_16_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_16_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し32回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 32-1 and self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_32_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_32_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し64回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 64-1 and self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_64_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_64_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し128回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 128-1 and self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_128_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_128_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し256回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 256-1 and self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_256_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_256_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し512回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 512-1 and self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_512_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_512_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        #早回し1024回目
        elif self.fast_forward_flag == FLAG_ON and self.fast_forward_num >= 1024-1 and self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] == RESULTS_NOT_OBTAINED:
            self.achievement_list[ACHIEVEMENT_1024_FAST_FORWARD][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0,ACHIEVEMENT_1024_FAST_FORWARD,WINDOW_PRIORITY_NORMAL,360)  #実績取得報告ウィンドウを育成
            self.fast_forward_flag == FLAG_OFF #早回実績取得用フラグを降ろす
            return
        
        #主にステージクリア(ボス破壊後）にフラグが立ち、そのフラグを見ることによって取得判別するタイプの実績(複数の実績が同時に解除される可能性あり)
        up_shift_line = 0 #上にシフトしていく行数を初期化
        #「ステージ中ノーダメージでクリア」フラグオンで実績取得
        if  self.no_damage_stage_clear_flag == FLAG_ON:
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR ,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60) #実績取得報告ウィンドウを育成
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR][LIST_ACHIEVE_FLAG]  = RESULTS_ACQUISITION
            self.no_damage_stage_clear_flag = FLAG_OFF  #ノーダメージでボスステージクリアフラグを下げる
            up_shift_line += 1
        #「ノーダメージでボス破壊」フラグオンで実績取得
        if self.no_damage_destroy_boss_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.no_damage_destroy_boss_flag = FLAG_OFF #ノーダメージでボス破壊フラグを下げる
            up_shift_line += 1
        #残りシールド１でギリギリクリアフラグオンで実績取得
        if self.endurance_one_cleared_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_ENDURANCE_ONE_CLEARED][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_ENDURANCE_ONE_CLEARED,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.endurance_one_cleared_flag = FLAG_OFF #残りシールド１でギリギリクリアフラグを下げる
            up_shift_line += 1
        #ボスを瞬殺したフラグオンで実績取得
        if self.boss_instank_kill_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_BOSS_INSTANK_KILL][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_BOSS_INSTANK_KILL,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.boss_instank_kill_flag = FLAG_OFF #ボスを瞬殺したフラグを下げる
            up_shift_line += 1
        #ボスのパーツをすべて破壊したフラグオンで実績取得
        if self.destroy_all_boss_parts_flag == FLAG_ON:
            self.achievement_list[ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS][LIST_ACHIEVE_FLAG] = RESULTS_ACQUISITION
            pyxel.play(0,26) #実績取得音を鳴らす
            func.create_achievement_acquisition_report_window(self,0,0 - up_shift_line * 6,ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS,WINDOW_PRIORITY_TOP + up_shift_line,630 - up_shift_line * 60)  #実績取得報告ウィンドウを育成
            self.destroy_all_boss_parts_flag = FLAG_OFF #ボスのパーツをすべて破壊したフラグを下げる
            up_shift_line += 1

    ################################################################ボツ関数群・・・・・・(涙)##########################################################
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
