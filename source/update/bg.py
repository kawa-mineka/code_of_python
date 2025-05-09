###########################################################
#  bgクラス                                                #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  BGアクセス関連の更新を行うメソッド                        #
#                                                         #
# 2024 02/11からファイル分割してモジュールとして運用開始      #
###########################################################
# import math                  #三角関数などを使用したいのでインポートぉぉおお！
# from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel                   #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import *      #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class bg:
    #タイルマップの座標位置からキャラチップのアスキーコードを取得する
    def get_chrcode_tilemap(self,tm,x,y):         #tmはtilemapの数値,x,yは読み出す座標位置
        """
        タイルマップの座標位置からキャラチップのアスキーコードを取得する
        
        tmはtilemapの数値\\
        x,yは読み出す座標位置
        """
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        num = 0
        tile_x,tile_y = pyxel.tilemaps[tm].pget(x,y) #タイルマップtm 座標(x,y)に格納されているマップチップを調べ、そのマップチップが格納されている座標を取得 pyxel 2.0.0以降は(tm)ではなく[tm]にするべきッポイ？？？？
        
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
        self.bg_chip = bg.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
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
        
        self.bg_chip = bg.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
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
        bg.set_chrcode_tilemap(self,self.reference_tilemap,x,y + ((self.stage_loop - 1)* 16 * self.height_screen_num),n)

    #背景マップチップを消去する(NULLチップナンバーを書き込む) x,yはキャラ単位 x=(0~255) y=(0~15)
    def delete_map_chip(self,x,y):
        """
        背景マップチップを消去する(NULLチップナンバーを書き込む)
        
        x,yはキャラ単位 x=(0~255) y=(0~15)
        """
        # bg.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16,0)#マップチップを消去する（0=何もない空白）を書き込む
        bg.set_chrcode_tilemap(self,self.reference_tilemap,x,y + (self.stage_loop - 1)* 16 * self.height_screen_num,self.null_bg_chip_num)

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
        
        self.bg_chip = bg.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx,self.bgy)
        return(self,x,y,bg_chip)

    #背景マップチップに書き込む関数(8方向フリースクロール専用)x,yはキャラ単位 x=(0~255) y=(0~255) n=(0~255)マップチップナンバー
    def write_map_chip_free_scroll(self,x,y,n):
        """
        背景マップチップに書き込む関数(8方向フリースクロール専用)
        
        x,yはキャラ単位 x=(0~255) y=(0~255)\\
        n=(0~255)マップチップナンバー
        """
        bg.set_chrcode_tilemap(self,self.reference_tilemap,x,y,n)#マップチップナンバーnを座標x,yに書き込む

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
                chip_num = bg.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w,mpy + h) #BGキャラチップのナンバー取得
                if chip_num == MOVE_POINT_BG_NUM: #もし移動点だったのなら
                    bg.delete_map_chip(self,mpx + w,mpy + h) #「移動点」マップチップを消去する
                    
                    #一つ右隣にあるチップナンバーが「移動点の連番」なので取得する
                    serial_num = bg.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w + 1,mpy + h) #移動点の連番を取得
                    serial_num -= ZERO_BG_CHR_NUM
                    self.boss_bg_move_point.append([int(serial_num),w,h])
                    point_num += 1 #移動ポイント数をインクリメント
                    bg.delete_map_chip(self,mpx + w + 1,mpy + h) #「移動点の連番」マップチップを消去する
                    
                elif chip_num == CONTROL_POINT_NUM: #もし制御点だったのなら
                    bg.delete_map_chip(self,mpx + w,mpy + h) #「制御点」マップチップを消去する
                    
                    #一つ右隣にあるチップナンバーが「制御点の連番」なので取得する
                    serial_num = bg.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w + 1,mpy + h) #移動点の連番を取得
                    serial_num -= ZERO_BG_CHR_NUM
                    self.boss_bg_move_control_point.append([int(serial_num),w,h])
                    control_num += 1 #制御ポイント数をインクリメント
                    bg.delete_map_chip(self,mpx + w + 1,mpy + h) #「制御点の連番」マップチップを消去する
        
        self.boss_bg_move_point.sort()         #「移動点の連番」を基準にソートする sort()はリスト型のメソッドだよん
        self.boss_bg_move_control_point.sort() #「制御点の連番」を基準にソートする sort()はリスト型のメソッドだよん

    #BG書き換えを使用して背景アニメーションをさせるアニメーションマーカーの座標をタイルマップから調べてリストに登録していく
    #self.bg_animation_cordinateのフォーマット
    #[[マーカーのアスキーコード0,bgx,bgy,anime_ptn_num,anime_ptn_num_offset,speed,tmap,u,v,w,h],
    # [マーカーのアスキーコード1,bgx,bgy,anime_ptn_num,anime_ptn_num_offset,speed,tmap,u,v,w,h],
    # [マーカーのアスキーコード2,bgx,bgy,anime_ptn_num,anime_ptn_num_offset,speed,tmap,u,v,w,h],
    # ]
    #
    #マーカーのアスキーコードは連番となっています
    #bgx,bgy              = マーカーがタイルマップでどこにあるかの座標値(x,yともに0~255の整数値)
    #anime_ptn_num        = アニメーション枚数
    #anime_ptn_num_offset = アニメーション枚数のオフセット値(どれだけの枚数がずれたところから始まるのかの指定)
    #speed                = アニメーションスピード 1で毎フレーム書き換え
    #tmap                 = タイルマップ値
    #u,v                  = BGパターンが収納されている座標u(横),v(縦)
    #w,h                  = BGパターンの横幅w、縦幅h
    #
    #
    #
    def search_bg_animation_marker_cordinate(self):
        """
        BG書き換えを使用して背景アニメーションをさせる時の座標をタイルマップから調べてリストに登録していく
        """
        if self.bg_animation_pre_define_list[self.stage_number - 1][1] == PREDEF_BGANIME_OFF: #BGアニメーションチップを調べないステージならば直ぐに帰ります
            return
        
        mark_chip_num_min = int(self.bg_animation_pre_define_list[self.stage_number - 1][2]) #調査していく最小のキャラチップナンバーをリストから取り出します
        mark_chip_num_max = int(self.bg_animation_pre_define_list[self.stage_number - 1][3]) #調査していく最大のキャラチップナンバーをリストから取り出します
        search_x          = int(self.bg_animation_pre_define_list[self.stage_number - 1][4]) #調べていく範囲(矩形）のx座標
        search_y          = int(self.bg_animation_pre_define_list[self.stage_number - 1][5]) #                     y座標
        search_width      = int(self.bg_animation_pre_define_list[self.stage_number - 1][6]) #                   範囲横幅w
        search_height     = int(self.bg_animation_pre_define_list[self.stage_number - 1][7]) #                       縦幅h
        marker = mark_chip_num_min
        
        mpx,mpy     = 0,0 #サーチ用の座標を初期化
        
        print("chip min ",end="")
        print(mark_chip_num_min)
        print("chip max ",end="")
        print(mark_chip_num_max)
        print("marker ",end="")
        print(marker)
        print("loop_num ",end="")
        print(mark_chip_num_max - mark_chip_num_min)
        
        print("search x,y =  ",end="")
        print(search_x,search_y)
        print("width,height = ",end="")
        print(search_width,search_height)
        
        for i in range(int(mark_chip_num_max - mark_chip_num_min)):
            for search_x in range(search_width): #x軸方向はsearch_xからsearch_width個分調べていく
                for search_y in range(search_height): #y軸方向はsearch_yからsearch_height個分調べ上げていく
                    chip = bg.get_chrcode_tilemap(self,self.reference_tilemap,search_x,search_y) #BGキャラチップのナンバー取得
                    # print("chip")
                    # print(chip)
                    if   chip == marker + i: #タイルマップに書き込まれたキャラコードと調べ上げるマーカーキャラコードが一致したのならば
                        anime_ptn_num        = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][1]) # アニメーション枚数取得
                        anime_ptn_num_offset = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][2]) # アニメーション枚数オフセット値取得
                        speed                = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][3]) # アニメーションスピード取得
                        tmap                 = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][4]) # タイルマップナンバー取得
                        u                    = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][5]) # BGパターンが収納されている座標u(横)
                        v                    = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][6]) # BGパターンが収納されている座標v(縦)
                        w                    = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][7]) # W(横幅)
                        h                    = int(self.bg_animation_pre_define_list[self.stage_number - 1][8][i][8]) # h(縦幅)
                        self.bg_animation_cordinate.append([marker + i,search_x,search_y,anime_ptn_num,anime_ptn_num_offset,speed,tmap,u,v,w,h])
        
        # for i in range(int(mark_chip_num_max - mark_chip_num_min)):
        #     for w in range(255): #x軸方向は0~255まで調べ上げていく
        #         for h in range(255): #y軸方向も0~255まで調べ上げていく
        #             chip = bg.get_chrcode_tilemap(self,self.reference_tilemap,mpx + w,mpy + h) #BGキャラチップのナンバー取得
        #             # print("chip")
        #             # print(chip)
        #             if   chip == marker + i: #タイルマップに書き込まれたキャラコードと調べ上げるマーカーが一致したのならば
        #                 self.bg_animation_cordinate.append([marker + i,w,h])

    #アニメーションマーカーの座標が今現在表示されている背景BG内かどうか調べる
    def check_bg_anime_maraker(self,x,y):
        """
        アニメーションマーカーの座標が今現在表示されている背景BG内に存在するかどうか調べる
        
        x,y=アニメーションマーカーの座標値(0~255)
        
        存在するのならTrue,存在しないのならFalseを返します
        """
        if   self.stage_number == STAGE_MOUNTAIN_REGION:        #1面 MOUNTAIN REGION
            return False
        elif self.stage_number == STAGE_ADVANCE_BASE:           #2面 ADVANCE_BASE
            return False
        elif self.stage_number == STAGE_VOLCANIC_BELT:          #3面 VOLCANIC_BELT
            return False
        elif self.stage_number == STAGE_NIGHT_SKYSCRAPER:       #4面 NIGHT_SKYSCRAPER
            #メインスクロール面----------------------------------------------------------------------------
            self.bgx = int(self.scroll_count  // 8 % (256 -20)) #bgxに現在のメインスクロール面の1番左端のx座標(0~255)が入る
            self.bgy = 48                                       #bgy座標は48から始まって1画面分下方向を調べ上げる
            bg.clip_bgx_bgy(self)                               #bgx,bgyを規格範囲内に修正する
            if  self.bgx <= x <= self.bgx + 20:                 #もしx座標が現在のメインスクロール面の1番左端のx座標から20キャラ分(横１画面分)に入っているのならば
                return True
            else:
                return False
        else:
            return False
        
        # bg_x = (((self.scroll_count // 8) -256) // 2)
        # bg_y = 



