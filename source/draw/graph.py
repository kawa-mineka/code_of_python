###########################################################
#  graphクラス                                             #       
###########################################################
#  Appクラスのdraw関数から呼び出される関数群                 #
#  主に描画関係のみだけを行う関数(メソッド？）ですよ～♪        #
# 2022 04/03からファイル分割してモジュールとして運用開始      #
###########################################################
import math                     #三角関数などを使用したいのでインポートぉぉおお！
import pyxel                    #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const             import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from const.const_window      import * #主にウィンドウクラスで使用する定数定義
from const.const_visualscene import * #主にビジュアルシーンクラスで使用する定数定義
from common.func              import * #汎用性のある関数群のモジュールの読み込み

class graph:
    #IPLメッセージの表示#######################################
    def draw_ipl(self): 
        """
        IPLメッセージを表示する
        """
        #テキストスクリーンリスト全体の行数を数える
        text_number_of_lines_count = len(self.text_screen)
        #どれだけの行が画面上に流れていったのか計算します
        #標準フォントの縦ドット数は6で行間空白として1ドット取りたいので全体で縦7ドット
        #120÷7 =17.14 で画面全体では約17行表示出来ることに成ります
        if text_number_of_lines_count > 17: #テキストスクリーンの行数が17を超えていたら上にスクロールアウトしていることに成るので・・
            self.text_console_scroll_counter = text_number_of_lines_count - 17 #上にスクロールした行数を計算します      
        for i in range(text_number_of_lines_count):
            text_mes = self.text_screen[i][0]
            text_col = self.text_screen[i][1]
            pyxel.text(0,i*6 - self.text_console_scroll_counter * 6 ,str(text_mes),int(text_col)) #y軸をスクロールした行数分だけマイナス方向に補正し画面外(上方向)から前部のテキストを表示するときちんと表示されます

    #タイトルの表示#######################################
    def draw_title(self):
        """
        タイトルを表示する
        """
        for i in range(160):
            pyxel.blt(0,14 + i  * self.title_oscillation_count % 200 - self.title_slash_in_count,    IMG2,  0,192,  i*1.09,32,   pyxel.COLOR_BLACK)
        for i in range(160+1000):
            pyxel.blt(0,14 + i % 1000 * self.title_oscillation_count - self.title_oscillation_count, IMG2,  0,192,  i    ,32,   pyxel.COLOR_BLACK)
            
        #デバッグ用に現在のステージ数とループ数とその他いろいろ表示する
        #ステージ数の表示
        pyxel.text(160-3*8+8,1,"ST " + str(self.stage_number), pyxel.COLOR_ORANGE)
        #周回数の表示
        pyxel.text(160-3*8+8,8,"LP " + str(self.stage_loop), pyxel.COLOR_WHITE)
        #ボスモード選択中の表示
        pyxel.text(160-6*8,1,"BOSS " + str(self.boss_test_mode),pyxel.COLOR_RED)
        #ボスヒットボックス
        pyxel.text(160-19*3+8,8,"HITBOX " + str(self.boss_collision_rect_display_flag),pyxel.COLOR_YELLOW)
        #難易度の表示
        pyxel.text(0,1,"DIFFICULTY " + str(self.game_difficulty),pyxel.COLOR_YELLOW)

    #背景の星の表示
    def draw_star(self):
        """
        背景の星を表示する
        """
        stars_count = len(self.stars)
        for i in range(stars_count):
            pyxel.pset(self.stars[i].posx, self.stars[i].posy,int(self.stars[i].posx  // 4 % 15)) 
            #pyxel.pset(self.stars[i].posx, self.stars[i].posy,int(self.s_rndint(0,7))) 

    #背景の星の再描画表示(透明または半透明ウィンドウ表示時にその範囲が消去されたのちその範囲に存在する星を描画する)
    def redraw_star(self):
        """
        背景の星の再描画表示する
        
        (透明または半透明ウィンドウ表示時にその範囲が消去されたのちその範囲に存在する星を描画する)
        """
        stars_count = len(self.stars)
        for i in range(stars_count):
            st_x,st_y = self.stars[i].posx,self.stars[i].posy #星の座標を取り出す
            area_count = len(self.redraw_star_area) #再描画リストに登録されたエリア数を取得
            for j in range(area_count): #星の座標が再描画範囲内ならば・・・
                if  self.redraw_star_area[j].posx <= st_x <= self.redraw_star_area[j].posx + self.redraw_star_area[j].width and\
                    self.redraw_star_area[j].posy <= st_y <= self.redraw_star_area[j].posy + self.redraw_star_area[j].height:
                    
                    pyxel.pset(st_x,st_y,int(self.stars[i].posx  // 4 % 15)) #星を再描画する

    #背景の星を最前面のウィンドウ部分に再描画表示(透明または半透明ウィンドウ表示時にその範囲が消去されたのちその範囲に存在する星を描画する)
    def redraw_star_priority_top(self):
        """
        背景の星を最前面のウィンドウ部分に再描画表示する
        
        (透明または半透明ウィンドウ表示時にその範囲が消去されたのちその範囲に存在する星を描画する)
        """
        stars_count = len(self.stars)
        for i in range(stars_count):
            st_x,st_y = self.stars[i].posx,self.stars[i].posy #星の座標を取り出す
            area_count = len(self.redraw_star_area) #再描画リストに登録されたエリア数を取得
            for j in range(area_count): #星の座標が再描画範囲内&描画優先度最前面ならば・・・
                if      self.redraw_star_area[j].posx <= st_x <= self.redraw_star_area[j].posx + self.redraw_star_area[j].width\
                    and self.redraw_star_area[j].posy <= st_y <= self.redraw_star_area[j].posy + self.redraw_star_area[j].height\
                    and self.redraw_star_area[j].priority == WINDOW_PRIORITY_TOP:
                    
                    pyxel.pset(st_x,st_y,int(self.stars[i].posx  // 4 % 15)) #星を再描画する

    #自機表示
    def draw_my_ship(self):
        """
        自機を表示する
        """
        if self.invincible_counter > 0: #無敵中のカウントが0より大きい時は無敵状態なので点滅表示する
            if pyxel.frame_count % 4 == 0: #4フレーム置きに自機を表示
                pyxel.blt(self.my_x   ,self.my_y - self.camera_offset_y,IMG2,8 + ((self.my_rolling_flag) * 8),0,SHIP_W,SHIP_H,pyxel.COLOR_BLACK) #自機本体の表示
            
            self.invincible_counter -= 1 #無敵時間カウントを1減らす
        else:
            pyxel.blt(self.my_x   ,self.my_y - self.camera_offset_y,IMG2,8 + ((self.my_rolling_flag) * 8),0,SHIP_W,SHIP_H,pyxel.COLOR_BLACK) #自機本体の表示
        
        if self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST:
            pyxel.blt(self.my_x -6*8,self.my_y - self.camera_offset_y,IMG2,    208,120 + (pyxel.frame_count // 2  % 2) * 8,    6*8,8,pyxel.COLOR_BLACK) #ブーストモードイオンエンジン噴射の描画
        else:
            pyxel.blt(self.my_x   -8,self.my_y - self.camera_offset_y,IMG2,    176 + (pyxel.frame_count // 2  % 3) * 8,104,     8,8,pyxel.COLOR_BLACK) #イオンエンジン噴射の描画

    #自機弾の表示
    def draw_my_shot(self):
        """
        自機ショットを表示する
        """
        shot_count = len(self.shots)
        for i in range(shot_count):
            if   0 <= self.shot_level <= 6: #ショットがバルカンショットとレーザーの場合
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y,     IMG2,    (self.shots[i].shot_type * 8),8,      8,8,    pyxel.COLOR_NAVY)
            elif     self.shot_level == 7: #ウェーブカッターLv1の場合
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y,     IMG2,    (self.shots[i].shot_type * 8),8,      8,8,    pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 8,  IMG2,    (self.shots[i].shot_type * 8),8,      8,8,    pyxel.COLOR_NAVY)
            elif     self.shot_level == 8: #ウェーブカッターLv2の場合
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y,     IMG2,    (self.shots[i].shot_type * 8),8,      8, 8,   pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 8 , IMG2,    (self.shots[i].shot_type * 8),16,     8, 8,   pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 16, IMG2,    (self.shots[i].shot_type * 8),8,      8,-8,   pyxel.COLOR_NAVY)
            elif 9 <= self.shot_level <= 10:#ウェーブカッターLv3とLv4の場合
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y,     IMG2,    (self.shots[i].shot_type * 8),8,      8, 8,   pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 8 , IMG2,    (self.shots[i].shot_type * 8),16,     8, 8,   pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 16, IMG2,    (self.shots[i].shot_type * 8),16,     8,-8,   pyxel.COLOR_NAVY)
                pyxel.blt(self.shots[i].posx, self.shots[i].posy - self.camera_offset_y+ 24, IMG2,    (self.shots[i].shot_type * 8),8,      8,-8,   pyxel.COLOR_NAVY)

    #ミサイルの表示
    def draw_missile(self):
        """
        ミサイルを表示する
        """
        missile_count = len(self.missile)
        for i in range(missile_count):
            if 0 <= self.missile[i].missile_type <= 3:#通常ミサイル（地を這うミサイル）の表示
                pyxel.blt(self.missile[i].posx, self.missile[i].posy - self.camera_offset_y, IMG2,   (self.missile[i].missile_flag1 * 8),16,    self.missile[i].x_reverse * 8,self.missile[i].y_reverse * 8,  pyxel.COLOR_BLACK)
            elif self.missile[i].missile_type == 4:#テイルショットの表示
                pyxel.blt(self.missile[i].posx, self.missile[i].posy - self.camera_offset_y, IMG2,   24,16,    8,8,  pyxel.COLOR_NAVY)
            elif self.missile[i].missile_type == 5:#ペネトレートロケットの表示
                pyxel.blt(self.missile[i].posx, self.missile[i].posy - self.camera_offset_y, IMG2,   16,16,    8,8,  pyxel.COLOR_NAVY)
            elif self.missile[i].missile_type == 6:#サーチレーザーの表示
                if   self.missile[i].missile_flag1 == 0:#状態遷移が(直進中=0)なら前方直進レーザーの画像を表示する
                    pyxel.blt(self.missile[i].posx - 8, self.missile[i].posy - self.camera_offset_y, IMG2,   32,16,   16,8,  pyxel.COLOR_GRAY)
                elif self.missile[i].missile_flag1 == 1:#状態遷移が(屈折中=1)なら曲がっているレーザーの画像を表示
                    pyxel.blt(self.missile[i].posx    , self.missile[i].posy - self.camera_offset_y, IMG2,   48,16,   8,8  * -(self.missile[i].y_reverse),  pyxel.COLOR_GRAY)
                elif self.missile[i].missile_flag1 == 2:#状態遷移が(縦に進行中=2)なら上方向＆下方向のレーザーの画像を表示
                    pyxel.blt(self.missile[i].posx    , self.missile[i].posy - self.camera_offset_y+ (self.missile[i].y_reverse) * 8, IMG2,   88,8,    8,16 * -(self.missile[i].y_reverse),  pyxel.COLOR_GRAY)
                
            elif self.missile[i].missile_type == 7:#ホーミングミサイルの表示
                pyxel.blt(self.missile[i].posx, self.missile[i].posy - self.camera_offset_y, IMG2,   56,16,    8,8,  pyxel.COLOR_GRAY)

    #クローの表示
    def draw_claw(self):
        """
        クローを表示する
        """
        claw_count = len(self.claw)
        for i in range(claw_count):
            pyxel.blt(self.claw[i].posx, self.claw[i].posy - self.camera_offset_y,     IMG2,    184 + (((self.stage_count // 2.5 ) % 9) * 8),96,      8,8,    pyxel.COLOR_BLACK)
            #pyxel.blt(self.claw[i].posx, self.claw[i].posy - self.camera_offset_y,     IMG2,    144 + (((self.stage_count // 2.5 ) % 14) * 8),8,      8,8,    0)

    #クローショットの表示
    def draw_claw_shot(self):
        """
        クローショットを表示する
        """
        claw_shot_count = len(self.claw_shot)
        for i in range(claw_shot_count):
            pyxel.blt(self.claw_shot[i].posx, self.claw_shot[i].posy - self.camera_offset_y, IMG2,   240,0,    8,8,  pyxel.COLOR_NAVY)

    #l'sシールド表示
    def draw_ls_shield(self):
        """
        l'sシールドを表示する
        """
        if self.ls_shield_hp > 0:
            pyxel.blt(self.my_x + 8,self.my_y - 8 - self.camera_offset_y,IMG2,208 + (self.stage_count // 3) % 6 * 8,64,8,24,pyxel.COLOR_GRAY)

    #敵の表示
    def draw_enemy(self):
        """
        敵を表示する
        """
        enemy_count = len(self.enemy)
        for i in range(enemy_count):
            if   self.enemy[i].enemy_type ==  1:#敵タイプ１の表示  直進して斜め後退→勢いよく後退していく10機編隊
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,self.anime_enemy001[pyxel.frame_count % 15],40,SIZE_8,SIZE_8,pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  2:#敵タイプ２の表示  サインカーブを描く3機編隊
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,self.anime_enemy002[pyxel.frame_count % 40],24,SIZE_8,SIZE_8,pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  3:#敵タイプ３の表示  固定砲台（地面に張り付く単装砲タイプ）
                self.reverse_flag = 8
                if self.my_x > self.enemy[i].posx:
                    self.reverse_flag =-8
                    
                #論理式(enemy[i].item != 0)はitem=0の場合falseで0 item=1または2か3の場合はtrueで1となる（つまりアイテムを持っていたらカッコ内は1となる）
                #アイテム所持していれば1*24で24ドット横、つまり3キャラチップ横の黄色い固定砲台が表示される事となる
                if self.my_x == self.enemy[i].posx:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 48 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, pyxel.COLOR_BLACK)
                elif self.my_y < self.enemy[i].posy:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, pyxel.COLOR_BLACK)
                elif self.enemy[i].posy < self.my_y:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 32 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, pyxel.COLOR_BLACK)
                else:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  4:#敵タイプ４の表示  固定砲台（天井に張り付く単装砲タイプ）
                self.reverse_flag = 8
                if self.my_x > self.enemy[i].posx:
                    self.reverse_flag =-8
                    
                #論理式(enemy[i].item != 0)はitem=0の場合falseで0 item=1または2か3の場合はtrueで1となる（つまりアイテムを持っていたらカッコ内は1となる）
                #アイテム所持していれば1*24で24ドット横、つまり3キャラチップ横の黄色い固定砲台が表示される事となる
                if self.my_x == self.enemy[i].posx:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 48 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), pyxel.COLOR_BLACK)
                elif self.my_y > self.enemy[i].posy:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), pyxel.COLOR_BLACK)
                elif self.enemy[i].posy > self.my_y:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 32 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), pyxel.COLOR_BLACK)
                else:
                     pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  5:#敵タイプ５の表示  ぴょんぴょんはねるホッパーちゃんmk2
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,self.anime_enemy005[pyxel.frame_count % 40],24,SIZE_8,SIZE_8,pyxel.COLOR_BLACK)       
            elif self.enemy[i].enemy_type ==  6:#敵タイプ６の表示  謎の回転飛翔体Ｍ５４
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,24+(((self.stage_count // 30) % 2) * 8),24,SIZE_8,SIZE_8,pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  7:#敵タイプ７の表示  追尾戦闘機（サインカーブを描きつつ追尾してくる）
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,   88,32,   SIZE_8,SIZE_8,  pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  8:#敵タイプ８の表示  追尾戦闘機
                if self.enemy[i].vy < 0:
                    up_down_reverse = 8
                else:
                    up_down_reverse = -8
                            
                if   self.enemy[i].vx < 0:
                    right_left_reverse = 8
                else:
                    right_left_reverse = -8
                    
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2,   96 ,32,   right_left_reverse,up_down_reverse,  pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type ==  9:#敵タイプ９の表示  Ｙ軸を合わせた後突っ込んで来る敵機
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y, IMG2,     self.anime_enemy009[pyxel.frame_count % 40],48,    SIZE_8,SIZE_8,    pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type == 10:#敵タイプ10の表示  スクランブルハッチ地面タイプ
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y, IMG2,  112,32,  3*8,2*8,  0)
                if 0 <= self.enemy[i].enemy_flag1 <= 43:
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y, IMG2,  136+(self.enemy[i].enemy_flag1 // 6) * 8,40,  SIZE_8,SIZE_8,  pyxel.COLOR_BLACK)
                if 43 <= self.enemy[i].enemy_flag1 <= 86:
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y, IMG2,  184-(self.enemy[i].enemy_flag1 // 7) * 8,40,  SIZE_8,SIZE_8,  pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type == 11:#敵タイプ11の表示  スクランブルハッチ天井タイプ
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y, IMG2,  112,32,  3*8,-(2*8),  0)
                if 0 <= self.enemy[i].enemy_flag1 <= 43:
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y+ 8, IMG2,  136+(self.enemy[i].enemy_flag1 // 6) * 8,40,  SIZE_8,-(SIZE_8),  pyxel.COLOR_BLACK)
                if 43 <= self.enemy[i].enemy_flag1 <= 86:
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y+ 8, IMG2,  184-(self.enemy[i].enemy_flag1 // 7) * 8,40,  SIZE_8,-(SIZE_8),  pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type == 12:#敵タイプ12の表示  レーザービームを発射した後、高速で後退する敵
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y, IMG2,  144 + ((self.enemy[i].enemy_flag1 // 7) * 8),32,  SIZE_8,SIZE_8,  pyxel.COLOR_BLACK)#数値をいじったらうまくいった　良かった・・たまたまだけど               
            elif self.enemy[i].enemy_type == 13:#敵タイプ13の表示  3way弾を射出する硬い奴（ショットパワーアップアイテムを持っている）
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy - self.camera_offset_y,IMG2, 0,24, SIZE_8,SIZE_8, 0)
            elif self.enemy[i].enemy_type == 14:#敵タイプ14の表示  ゆっくり直進してくる赤いアイテムキャリアー（パワーアップアイテムを持っている）
                pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy - self.camera_offset_y,IMG2, 104                              ,104,   SIZE_8,SIZE_8,  pyxel.COLOR_BLACK) #コックピット部表示
                pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y,IMG2, 112 + (self.stage_count // 2  % 4) * 16,104,  SIZE_16,SIZE_8,  pyxel.COLOR_BLACK) #エンジンノズル＆噴射パターン表示
            elif self.enemy[i].enemy_type == 15:#敵タイプ15の表示  地面だったり天井を左右に動きながらチョット進んできて弾を撃つ移動砲台
                pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy - self.camera_offset_y,IMG2, 208 + self.stage_count // 3 % 6 * 8,32,   SIZE_8,SIZE_8,  pyxel.COLOR_BLACK)   
            elif self.enemy[i].enemy_type == 16:#敵タイプ16の表示  2機一体で挟みこみ攻撃をしてくるクランパリオン
                pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy - self.camera_offset_y,IMG2,      (self.stage_count // 2) % 4   * 8, 56,    SIZE_8 ,SIZE_8, pyxel.COLOR_BLACK)
                pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy - self.camera_offset_y,IMG2, 176 + (pyxel.frame_count // 2  % 3) * 8,104,   -(SIZE_8),SIZE_8, pyxel.COLOR_BLACK) #イオンエンジン噴射の描画
            elif self.enemy[i].enemy_type == 17:#敵タイプ17の表示  スプライン曲線で定点まで移動して離脱する敵 ロールブリッツ
                pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy - self.camera_offset_y,IMG2,      0, 32,    SIZE_8 ,SIZE_8, pyxel.COLOR_BLACK)
            elif self.enemy[i].enemy_type == 18:#敵タイプ18の表示  チョット大き目で硬いばらまき弾の敵 ボルダー
                pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy - self.camera_offset_y,IMG2,      80,48,    SIZE_40 ,SIZE_24, pyxel.COLOR_PEACH)    

    #敵の弾の表示
    def draw_enemy_shot(self,priority): #priorityの数値と一致するプライオリティナンバーを持つ敵弾だけを描画します
        """
        敵の弾の表示
        
        priorityの数値と一致するプライオリティナンバーを持つ敵弾だけを描画します
        """
        enemy_shot_count = len(self.enemy_shot)
        for i in range(enemy_shot_count):
            if self.enemy_shot[i].priority == priority:
                if   self.enemy_shot[i].enemy_shot_type == EnemyShot.LASER:            #通常レーザーの表示
                    pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   152,16,    8, 8,    pyxel.COLOR_BLACK)#敵レーザービームの表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.GREEN_LASER:      #ボスのグリーンレーザーの表示
                    pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy - self.camera_offset_y,  self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy- self.camera_offset_y  ,pyxel.COLOR_LIME) #グリーンレーザービームの表示
                    #pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy+1,self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy+1,3) #影部分の線を描画
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.RED_LASER:        #ボスのレッドレーザーの表示
                    pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy - self.camera_offset_y,  self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy- self.camera_offset_y  ,pyxel.COLOR_RED)#レッドレーザービームの表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.HOMING_LASER:     #ホーミングレーザーの表示
                    pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   200,16,    8, 8,    pyxel.COLOR_BLACK)#ホーミングレーザーの頭の表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.HOMING_LASER_TAIL:#ホーミングレーザーの尻尾の表示
                    pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   160+(self.enemy_shot[i].disappearance_count // 12) * 8,16,    8, 8,    pyxel.COLOR_BLACK)#ホーミングレーザーの尻尾の表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.SEARCH_LASER:     #サーチレーザーの表示
                    if self.enemy_shot[i].search_flag == 0: #自機サーチ完了フラグがたっていない場合は横状態のグラフイックを表示する
                        pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   216,40,    8, 8,    pyxel.COLOR_BLACK)#サーチレーザーの頭の表示(横)
                    else: ##自機サーチ完了フラグがたってたら縦状態のグラフイックを表示する
                        pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   216,48,    8, 8 * ((self.enemy_shot[i].vy < 0)-(self.enemy_shot[i].vy > 0)),    pyxel.COLOR_BLACK)#サーチレーザーの頭の表示(縦),vyの符号を求めてグラフイックを反転してます(論理式を使用)                 
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.SEARCH_LASER_TAIL:#サーチレーザーの尻尾の表示
                    if self.enemy_shot[i].search_flag == 0:
                        pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   224+8*(self.enemy_shot[i].disappearance_count < 30)+8*(self.enemy_shot[i].disappearance_count < 15),40,    8, 8,    pyxel.COLOR_BLACK)#サーチレーザーの尻尾(横)の表示
                    else:
                        pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   224+8*(self.enemy_shot[i].disappearance_count < 30)+8*(self.enemy_shot[i].disappearance_count < 15),48,    8, 8*((self.enemy_shot[i].vy < 0)-(self.enemy_shot[i].vy > 0)),    pyxel.COLOR_BLACK)#サーチレーザーの尻尾(縦)の表示,vyの符号を求めてグラフイックを反転してます(論理式を使用)
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.UP_LASER:         #アップレーザーの表示
                    pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy - self.camera_offset_y+4,  self.enemy_shot[i].posx + self.enemy_shot[i].width,self.enemy_shot[i].posy- self.camera_offset_y+4  ,pyxel.COLOR_LIME) #アップレーザーの表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.DOWN_LASER:       #ダウンレーザーの表示
                    pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy - self.camera_offset_y+4,  self.enemy_shot[i].posx + self.enemy_shot[i].width,self.enemy_shot[i].posy- self.camera_offset_y+4  ,pyxel.COLOR_ORANGE) #ダウンレーザーの表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.VECTOR_LASER:     #ベクトルレーザーの表示
                    pyxel.line(self.enemy_shot[i].posx+4,self.enemy_shot[i].posy - self.camera_offset_y,  self.enemy_shot[i].posx+4,self.enemy_shot[i].posy - self.camera_offset_y+ self.enemy_shot[i].height   ,pyxel.COLOR_RED) #ベクトルレーザーの表示
                elif self.enemy_shot[i].enemy_shot_type == EnemyShot.GREEN_CUTTER:     #ブリザーディア」が尾翼部から射出するグリーンカッターの表示
                    pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   64,56,    SIZE_16, SIZE_16,    15)
                else:                                                                   #通常弾の表示
                    pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy - self.camera_offset_y, IMG2,   32 + (self.enemy_shot[i].posx // 8) % 4 * 8,0,    8, 8,    pyxel.COLOR_GRAY)#敵通常弾の表示 posxを使用してアニメーションパターンのオフセット値を計算する                

    #ボスの表示
    def draw_boss(self):
        """
        ボスの表示
        """
        boss_count = len(self.boss)
        for i in range(boss_count):
            if   self.boss[i].boss_type == BOSS_BREEZARDIA:        #1面 ブリザーディア          (山岳地帯ボス)
                offset_x = 0 #真っ二つになる描画用のx軸オフセット値(離れた距離)をリセットする
                if self.boss[i].count2 !=0: #カウントが0だと0で割ってしまってエラーになるのでスキップする
                    offset_x = 10 - self.boss[i].count2 // 48   #count2が少なくなるごとにoffset_xが増加することに成る
                                                                #count2の数値は最初は480フレームで最終的に0となり,この計算式からoffset_xは480フレームの間で0から10まで変化することに成る
                
                pyxel.blt(self.boss[i].posx + offset_x, self.boss[i].posy - self.camera_offset_y + offset_x // 16,  IMG0,   40,184,self.boss[i].width,self.boss[i].height,    pyxel.COLOR_PEACH) #ブリザーディア前部表示
                
                if self.boss[i].parts1_flag == 1: #パーツフラグ1(右下赤砲台)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x + 10*8, self.boss[i].posy - self.camera_offset_y + 4*8,       IMG0,    152,216,    2*8,2*8,    pyxel.COLOR_PEACH)
                if self.boss[i].parts2_flag == 1: #パーツフラグ2(右下緑砲台)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x +  8*8, self.boss[i].posy - self.camera_offset_y + 4*8,       IMG0,    152,200,    2*8,2*8,    pyxel.COLOR_PEACH)
                if self.boss[i].parts3_flag == 1: #パーツフラグ3(上部主砲)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x +  4*8, self.boss[i].posy - self.camera_offset_y + self.boss[i].weapon1_cool_down_time // 100,       IMG0,     0,216,    3*8,2*8,    pyxel.COLOR_PEACH)
                if self.boss[i].parts4_flag == 1: #パーツフラグ4(上部グリーンカッター)が生存していたのなら描画する
                    #グリーンカッター本体
                    pyxel.blt(self.boss[i].posx - offset_x      , self.boss[i].posy - self.camera_offset_y     ,       IMG0,     0,232,    4*8,3*8,    pyxel.COLOR_PEACH)
                    #グリーンカッター手前にある後部ユニット部
                    pyxel.blt(self.boss[i].posx - offset_x +  1*8, self.boss[i].posy - self.camera_offset_y + 1*8,       IMG0,    32,240,    2*8,2*8,    pyxel.COLOR_PEACH)
                
            elif self.boss[i].boss_type == BOSS_FATTY_VALGUARD:    #2面 ファッティ・バルガード   (前線基地ボス)
                offset_x = 0 #真っ二つになる描画用のx軸オフセット値(離れた距離)をリセットする
                if self.boss[i].count2 !=0: #カウントが0だと0で割ってしまってエラーになるのでスキップする
                    offset_x = 10 - self.boss[i].count2 // 48   #count2が少なくなるごとにoffset_xが増加することに成る
                                                                #count2の数値は最初は480フレームで最終的に0となり,この計算式からoffset_xは480フレームの間で0から10まで変化することに成る
                
                pyxel.blt(self.boss[i].posx + offset_x, self.boss[i].posy - self.camera_offset_y + offset_x // 16,  IMG0,   64,128,8*8,5*8,    pyxel.COLOR_PEACH) #ファッティバルガード前部表示
                pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy - self.camera_offset_y                 ,  IMG0,    0,184,5*8,3*8,    pyxel.COLOR_PEACH) #ファッティバルガード後部表示 
                
                if self.boss[i].parts1_flag == 1: #パーツフラグ1(5way砲台)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy - self.camera_offset_y+ 16,       IMG0,    0,176,    2*8,8,    pyxel.COLOR_PEACH)
                if self.boss[i].parts2_flag == 1: #パーツフラグ2(尾翼レーザーユニット)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy - self.camera_offset_y,           IMG0,   16,176,    3*8,8,    pyxel.COLOR_PEACH)
                if self.boss[i].parts3_flag == 1: #パーツフラグ3(赤色爆雷ユニット)が生存していたのなら描画する
                    pyxel.blt(self.boss[i].posx - offset_x + 8, self.boss[i].posy - self.camera_offset_y + 24,    IMG0,   40,176,    2*8,8,    pyxel.COLOR_PEACH)
                
            elif self.boss[i].boss_type == BOSS_MAD_CLUBUNGER:     #3面 マッドクラブンガー       (火山地帯ボス)
                #ボスグラフイックの横方向の中心値を求める
                x_center =  self.boss[i].posx + (self.boss[i].width // 2)
                
                #左右反転時は表示する左右の方向的に1キャラ分のズレが出るので反転時は-1キャラ分のオフセット値を設定する
                #pyxel.ble関数は基本的に左から右へと描画するので反転時に右から左に描画してほしいんだけどそれは無理なので-1キャラ分(8ドット)のズレを含んで反転時でも左から右へ描画出来るよう補正値を入れてやるんドエス！
                if self.boss[i].reverse == BOSS_GRP_REVERSE: #左右反転時は表示する左右の方向的に1キャラ分のズレが出るので反転時は-1キャラ分のオフセット値を設定する
                    reverse_offset = - 8
                else:
                    reverse_offset = 0
                    
                #上部ブースターユニット表示
                pyxel.blt(self.boss[i].posx - 8 * 1 * self.boss[i].reverse, self.boss[i].posy - self.camera_offset_y + 3       + self.boss[i].tilt_now,
                            IMG0,
                            0,160,
                            self.boss[i].width * self.boss[i].reverse,2*8,
                            pyxel.COLOR_PEACH)
                
                #マッドクラブンガー本体表示
                pyxel.blt(self.boss[i].posx, self.boss[i].posy - self.camera_offset_y,
                            IMG0,
                            0,128,
                            self.boss[i].width * self.boss[i].reverse,self.boss[i].height-1*8,
                            pyxel.COLOR_PEACH)
                
                #下部ブースターユニット表示
                pyxel.blt(self.boss[i].posx - 8 * 1 * self.boss[i].reverse, self.boss[i].posy - self.camera_offset_y + 3*8 -1   - self.boss[i].tilt_now,
                            IMG0,
                            0,160,
                            self.boss[i].width * self.boss[i].reverse,2*8,
                            pyxel.COLOR_PEACH)
                
                #下部ブースター回転アニメーション表示
                pyxel.blt(x_center - (self.boss[i].reverse  * 3 * 8) + reverse_offset, self.boss[i].posy - self.camera_offset_y + 3 * 8  - self.boss[i].tilt_now,
                            IMG0,
                            64 + (pyxel.frame_count // int(4 + (self.boss[i].anime_speed_now))  % 8) * 8,   88,
                            8 * self.boss[i].reverse,16,
                            pyxel.COLOR_PEACH)
            
            
            #デバッグ用の当たり判定矩形の表示
            graph.draw_boss_collision_rectangle(self,i)    #ボス本体の当たり判定矩形を表示する関数の呼び出し

    #ボスの耐久力の表示 (同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
    def draw_boss_hp(self):
        """
        ボスの耐久力の表示 (同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
        """
        boss_count = len(self.boss)
        for i in range(boss_count):
            if self.boss[i].display_time_main_hp_bar >= 0: #ボス本体の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].main_hp / 4
                if hp > 32:
                    hp = 31
                x = self.boss[i].posx                        + self.boss[i].main_hp_bar_offset_x
                y = self.boss[i].posy - self.camera_offset_y + self.boss[i].main_hp_bar_offset_y
                func.display_boss_hp_bar(self,x,y,hp)
                self.boss[i].display_time_main_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts1_hp_bar >= 0: #パーツ１(ファッティバルガードの場合5way砲台)の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts1_hp / 12
                if hp > 12:
                    hp = 12
                x,y = self.boss[i].posx + self.boss[i].parts1_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts1_hp_bar_offset_y
                func.display_boss_hp_short_bar(self,x,y,hp)
                self.boss[i].display_time_parts1_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts2_hp_bar >= 0: #パーツ2(ファッティバルガードの場合尾翼レーザーユニット)の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts2_hp / 12
                if hp > 12:
                    hp = 12
                x,y = self.boss[i].posx + self.boss[i].parts2_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts2_hp_bar_offset_y
                func.display_boss_hp_short_bar(self,x,y,hp)
                self.boss[i].display_time_parts2_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts3_hp_bar >= 0: #パーツ3(ファッティバルガードの場合赤色爆雷ユニット)の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts3_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts3_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts3_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts3_hp_bar -= 1 #タイムカウントを１減らす         
                
            if self.boss[i].display_time_parts4_hp_bar >= 0: #パーツ4の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts4_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts4_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts4_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts4_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts5_hp_bar >= 0: #パーツ5の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts5_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts5_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts5_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts5_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts6_hp_bar >= 0: #パーツ6の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts6_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts6_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts6_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts6_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts7_hp_bar >= 0: #パーツ7の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts7_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts7_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts7_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts7_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts8_hp_bar >= 0: #パーツ8の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts8_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts8_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts8_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts8_hp_bar -= 1 #タイムカウントを１減らす
                
            if self.boss[i].display_time_parts9_hp_bar >= 0: #パーツ9の耐久力を表示するタイムカウントが残っていたのなら
                hp = self.boss[i].parts9_hp / 32
                if hp > 8:
                    hp = 8
                x,y = self.boss[i].posx + self.boss[i].parts9_hp_bar_offset_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].parts9_hp_bar_offset_y
                func.display_boss_hp_short2_bar(self,x,y,hp)
                self.boss[i].display_time_parts9_hp_bar -= 1 #タイムカウントを１減らす

    #ボス本体の当たり判定矩形の表示(i=ボスクラスのインデックス値となります)(デバッグ用)(同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
    def draw_boss_collision_rectangle(self,i):
        """
        ボス本体の当たり判定矩形の表示(デバッグ用)(同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
        
        (i=ボスクラスのインデックス値となります)
        """
        if self.boss_collision_rect_display_flag != 1: #デバッグ時に使う当たり判定矩形表示フラグがonでないのならば
            return                             #何もしないで戻ります
            
        if self.boss[i].col_main1_w != 0: #本体当たり判定1の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main1_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main1_y,self.boss[i].col_main1_w,self.boss[i].col_main1_h,self.blinking_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].col_main2_w != 0: #本体当たり判定2の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main2_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main2_y,self.boss[i].col_main2_w,self.boss[i].col_main2_h,self.blinking_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].col_main3_w != 0: #本体当たり判定3の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main3_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main3_y,self.boss[i].col_main3_w,self.boss[i].col_main3_h,self.blinking_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].col_main4_w != 0: #本体当たり判定4の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main4_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main4_y,self.boss[i].col_main4_w,self.boss[i].col_main4_h,self.blinking_color[pyxel.frame_count // 8 % 10]) 
        if self.boss[i].col_main5_w != 0: #本体当たり判定5の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main5_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main5_y,self.boss[i].col_main5_w,self.boss[i].col_main5_h,self.blinking_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].col_main6_w != 0: #本体当たり判定6の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main6_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main6_y,self.boss[i].col_main6_w,self.boss[i].col_main6_h,self.blinking_color[pyxel.frame_count // 8 % 10])    
        if self.boss[i].col_main7_w != 0: #本体当たり判定7の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main7_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main7_y,self.boss[i].col_main7_w,self.boss[i].col_main7_h,self.blinking_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].col_main8_w != 0: #本体当たり判定8の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_main8_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_main8_y,self.boss[i].col_main8_w,self.boss[i].col_main8_h,self.blinking_color[pyxel.frame_count // 8 % 10])    
            
        if self.boss[i].parts1_flag == 1:#パーツ1が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts1_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts1_y,self.boss[i].col_parts1_w,self.boss[i].col_parts1_h,self.red_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts2_flag == 1:#パーツ2が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts2_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts2_y,self.boss[i].col_parts2_w,self.boss[i].col_parts2_h,self.green_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts3_flag == 1:#パーツ3が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts3_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts3_y,self.boss[i].col_parts3_w,self.boss[i].col_parts3_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts4_flag == 1:#パーツ4が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts4_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts4_y,self.boss[i].col_parts4_w,self.boss[i].col_parts4_h,self.monochrome_flash_color[pyxel.frame_count // 8 % 15])
        if self.boss[i].parts5_flag == 1:#パーツ5が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts5_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts5_y,self.boss[i].col_parts5_w,self.boss[i].col_parts5_h,self.red_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts6_flag == 1:#パーツ6が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts6_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts6_y,self.boss[i].col_parts6_w,self.boss[i].col_parts6_h,self.green_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts7_flag == 1:#パーツ7が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts7_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts7_y,self.boss[i].col_parts7_w,self.boss[i].col_parts7_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])
        if self.boss[i].parts8_flag == 1:#パーツ8が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts8_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts8_y,self.boss[i].col_parts8_w,self.boss[i].col_parts8_h,self.monochrome_flash_color[pyxel.frame_count // 8 % 15])
        if self.boss[i].parts9_flag == 1:#パーツ9が健在なら表示する
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts9_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_parts9_y,self.boss[i].col_parts9_w,self.boss[i].col_parts9_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])
            
        if self.boss[i].col_damage_point1_w != 0: #ボスのダメージポイント(弱点)1の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point1_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_damage_point1_y,self.boss[i].col_damage_point1_w,self.boss[i].col_damage_point1_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
        if self.boss[i].col_damage_point2_w != 0: #ボスのダメージポイント(弱点)2の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point2_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_damage_point2_y,self.boss[i].col_damage_point2_w,self.boss[i].col_damage_point2_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
        if self.boss[i].col_damage_point3_w != 0: #ボスのダメージポイント(弱点)3の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point3_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_damage_point3_y,self.boss[i].col_damage_point3_w,self.boss[i].col_damage_point3_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
        if self.boss[i].col_damage_point4_w != 0: #ボスのダメージポイント(弱点)4の表示 当たり判定の横幅が0の場合はスキップして表示しない
            pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point4_x,self.boss[i].posy - self.camera_offset_y + self.boss[i].col_damage_point4_y,self.boss[i].col_damage_point4_w,self.boss[i].col_damage_point4_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])

    #爆発パターンの表示
    def draw_explosion(self,priority):
        """
        爆発パターンの表示
        
        priorityの数値と一致するプライオリティナンバーを持つ爆発パターンだけを描画します
        """
        explosion_count = len(self.explosions)
        for i in reversed(range(explosion_count)):
            if self.explosions[i].priority == priority: #指定されたプライオリティナンバーの爆発だけ表示する
                if    self.explosions[i].explosion_type == EXPLOSION_NORMAL:#敵爆発の通常タイプの爆発パターン表示
                    pyxel.blt(self.explosions[i].posx,self.explosions[i].posy - self.camera_offset_y,IMG2,136 -(self.explosions[i].explosion_count * 8)      ,0,  SIZE_8,SIZE_8,pyxel.COLOR_BLACK)
                elif  self.explosions[i].explosion_type == EXPLOSION_MIDDLE:#スクランブルハッチや重爆撃機系の敵を倒したときの中くらいの爆発パターン
                    pyxel.blt(self.explosions[i].posx,self.explosions[i].posy - self.camera_offset_y,IMG2,48  -(self.explosions[i].explosion_count // 2 * 16),176,SIZE_16,SIZE_16 * self.explosions[i].y_reverse,pyxel.COLOR_BLACK)
                elif  self.explosions[i].explosion_type == EXPLOSION_MY_SHIP:#自機爆発の爆発パターン表示
                    pyxel.blt(self.explosions[i].posx,self.explosions[i].posy - self.camera_offset_y,IMG2,240 -(self.explosions[i].explosion_count // 8 * 16),240, SIZE_16,SIZE_8,pyxel.COLOR_BLACK)
                elif  self.explosions[i].explosion_type == EXPLOSION_BOSS_PARTS_SMOKE: #ボスのパーツが爆発した後に跳んでいく煙のパターン表示
                    pyxel.blt(self.explosions[i].posx,self.explosions[i].posy - self.camera_offset_y,IMG2,120 -(self.explosions[i].explosion_count // 4 * 8)       ,168,  SIZE_8,SIZE_8,pyxel.COLOR_BLACK)

    #パーティクルの表示
    def draw_particle(self,priority):
        """
        パーティクルの表示
        
        priorityの数値と一致するプライオリティナンバーを持つパーティクルだけを描画します
        """
        particle_count = len(self.particle)
        for i in reversed(range(particle_count)):
            if self.particle[i].priority == priority: #指定されたプライオリティナンバーのパーティクルだけ表示する
                if self.particle[i].particle_type == PARTICLE_DOT: #パーティクルタイプ 1~2ドット描画タイプ
                    pyxel.pset(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,int(self.particle[i].color)) #正方形1ドット分のパーティクルを描画
                    if self.particle[i].size > 0: #sizeが0より大きかったら横長2ドット分のパーティクルを描画する
                        pyxel.pset(self.particle[i].posx + 1,self.particle[i].posy - self.camera_offset_y,int(self.particle[i].color))
                        
                elif self.particle[i].particle_type == PARTICLE_LINE or\
                    self.particle[i].particle_type == PARTICLE_FIRE_SPARK: #パーティクルタイプ ラインタイプまたは大気圏突入時の火花タイプ
                    
                    pyxel.pset(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,int(self.particle[i].color)) #正方形1ドット分のパーティクルを描画
                    
                elif self.particle[i].particle_type == PARTICLE_CIRCLE: #パーティクルタイプ 円形パーティクルタイプ
                    pyxel.circ(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,self.particle[i].size,self.particle[i].color) #半径size分の円形パーティクルを描画
                    
                elif self.particle[i].particle_type == PARTICLE_MISSILE_DEBRIS: #パーティクルタイプ ミサイルの破片
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,IMG2,184 + (7 - self.particle[i].life) * 8,0, 8,8, pyxel.COLOR_BLACK) #ミサイル破片デブリをlifeの値をアニメーションパターンオフセット値としてスプライト表示する
                    
                elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS1: #パーティクルタイプ ボスの破片その1
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,IMG2,160 + (12 - (self.particle[i].life % 12)) * 8,216, 8,8, pyxel.COLOR_BLACK) #ボス破片デブリ1をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
                    
                elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS2: #パーティクルタイプ ボスの破片その2
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,IMG2,160 + (6 - (self.particle[i].life % 6)) * 8,208, 8,8, pyxel.COLOR_BLACK) #ボス破片デブリ2をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
                    
                elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS3: #パーティクルタイプ ボスの破片その3
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,IMG2,160 + (12 - (self.particle[i].life % 12)) * 8,200, 8,8, pyxel.COLOR_BLACK) #ボス破片デブリ3をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
                    
                elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS4: #パーティクルタイプ ボスの破片その4
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,IMG2,192 + (8 - (self.particle[i].life % 8)) * 8,192, 8,8, pyxel.COLOR_BLACK) #ボス破片デブリ4をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
                    
                elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS_FREE_IMAGE: #パーティクルタイプ 自由な画像を定義できるタイプ
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy - self.camera_offset_y,self.particle[i].imgb,self.particle[i].u,self.particle[i].v, self.particle[i].width,self.particle[i].height,self.particle[i].color)

    #背景オブジェクトの表示
    def draw_background_object(self):
        """
        背景オブジェクトの表示
        """
        object_count = len(self.background_object)
        for i in reversed(range(object_count)):
            if   self.background_object[i].background_object_type == BG_OBJ_CLOUD1: #雲小1
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    240,240,    16, 9,   pyxel.COLOR_NAVY) #雲小1を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD2: #雲小2
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    232,232,    8, 8,    pyxel.COLOR_NAVY) #雲小2を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD3: #雲小3
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    224,248,    8, 8,    pyxel.COLOR_NAVY) #雲小3を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD4: #雲小4
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    200,248,    8, 8,    pyxel.COLOR_NAVY) #雲小4を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD5: #雲小5
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    192,248,    8, 8,    pyxel.COLOR_NAVY) #雲小5を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD6: #雲小6
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    176,248,    8, 8,    pyxel.COLOR_NAVY) #雲小6を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD7: #雲小7
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    184,248,    7, 8,    pyxel.COLOR_NAVY) #雲小7を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD8: #雲小8
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    224,248,    16, 8,   pyxel.COLOR_NAVY) #雲小8を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD9: #雲小9
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    240,248,    16, 8,   pyxel.COLOR_NAVY) #雲小9を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD10: #雲小10
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    224,224,    16, 8,   pyxel.COLOR_NAVY) #雲小10を描画
                
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD11: #雲中11
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    176,232,    16,16,    pyxel.COLOR_NAVY) #雲中11を描画(正方形っぽい)
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD12: #雲中12
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    240,224,    16,16,    pyxel.COLOR_NAVY) #雲中12を描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD13: #雲中13
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    192,224,    48, 8,    pyxel.COLOR_NAVY) #雲中13を描画(かなり横長)
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD14: #雲中14
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     88,248,    24, 8,    pyxel.COLOR_NAVY) #雲中14を描画(ちょこっと横長)
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD15: #雲中15
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,      0,240,    48,48,    pyxel.COLOR_NAVY) #雲中15を描画(かなり横長)
                pyxel.blt(self.background_object[i].posx +7*8,self.background_object[i].posy + 8,    1,     48,248,    8, 8,    pyxel.COLOR_NAVY) #雲中15右下の尻尾部分描画
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD16: #雲中16
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     88,216,    48, 8,    pyxel.COLOR_NAVY) #雲中16を描画(かなり横長)
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD17: #雲中17
                pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,    168,216,    24,16,    pyxel.COLOR_NAVY) #雲中17を描画(チョット正方形ッポイ？)
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD18: #雲中18
                pyxel.blt(self.background_object[i].posx    ,self.background_object[i].posy    ,  IMG1, 192,232,    48,16,    pyxel.COLOR_NAVY) #雲中18を描画(中サイズで一番大きいかも？) 
                pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy + 8,  IMG1, 232,240,    8, 8,    pyxel.COLOR_NAVY) #雲中18の尻尾を描画
                pyxel.blt(self.background_object[i].posx +2*8,self.background_object[i].posy +16,  IMG1, 208,248,    16, 8,   pyxel.COLOR_NAVY) #雲中18のお腹のあたりを描画
                
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD19: #雲大19
                pyxel.blt(self.background_object[i].posx    ,self.background_object[i].posy   ,  IMG1,   0,216,    46,24,    pyxel.COLOR_NAVY) #雲大19を描画
                pyxel.blt(self.background_object[i].posx +6*8,self.background_object[i].posy +8,  IMG1,  48,224,    8,10,    pyxel.COLOR_NAVY) #雲大19の尻尾部分を描画 
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD20: #雲大20(おにぎり雲)
                pyxel.blt(self.background_object[i].posx +2*8,self.background_object[i].posy +1  ,  IMG1,  64,209,    24,15,   pyxel.COLOR_NAVY) #雲大20の三角山頂部分描画
                pyxel.blt(self.background_object[i].posx +1*8,self.background_object[i].posy +2*8,  IMG1,  56,224,    40,16,   pyxel.COLOR_NAVY) #雲大20の中腹部分を描画 
                pyxel.blt(self.background_object[i].posx +1*8,self.background_object[i].posy +4*8,  IMG1,  56,240,    40,16,   pyxel.COLOR_NAVY) #雲大20の下腹部分を描画 
                pyxel.blt(self.background_object[i].posx   +1,self.background_object[i].posy +3*8,  IMG1,  49,232,    16,16,   pyxel.COLOR_NAVY) #雲大20のおにぎりの左足（？）部分を描画
                pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy +5*8,  IMG1,  88,248,    16, 8,   pyxel.COLOR_NAVY) #雲大20の右下の離れ小島部分を描画  
            elif self.background_object[i].background_object_type == BG_OBJ_CLOUD21: #雲大21(みぎでっかち雲)
                pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy     ,  IMG1, 136,216,    32,40,    pyxel.COLOR_NAVY) #雲大21の右頭本体部分描画
                pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy +1*8,  IMG1,  96,224,    48,18,    pyxel.COLOR_NAVY) #雲大21の中央本体部分描画
                pyxel.blt(self.background_object[i].posx +9*8,self.background_object[i].posy +2*8,  IMG1, 160,232,    16,24,    pyxel.COLOR_NAVY) #雲大21の右先端描画
                pyxel.blt(self.background_object[i].posx +3*8,self.background_object[i].posy +3*8,  IMG1, 112,240,    64,16,    pyxel.COLOR_NAVY) #雲大21の下部右描画
                pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy +2*8,  IMG1,  96,232,    24,16,    pyxel.COLOR_NAVY) #雲大21の左のしっぽ描画

    #ラスタースクロールの表示
    def draw_raster_scroll(self,priority):
        """
        ラスタースクロールの表示
        
        priorityの数値と一致するプライオリティナンバーを持つラスタースクロール面だけを描画します
        """
        if self.raster_scroll_flag == FLAG_OFF: #ラスタスクロール更新＆表示のフラグがたっていなかったらそのまま何もしないで戻る
            return
        
        raster_scroll_count = len(self.raster_scroll)
        for i in range(raster_scroll_count):#ラスタースクロールのリストの要素数を数えてその数の分だけループ処理する
            if self.raster_scroll[i].display == 1 and self.raster_scroll[i].priority == priority: #dispiay == 1(on) & priority == 引数のpriorityの時だけ描画する
                pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x,self.raster_scroll[i].posy,
                self.raster_scroll[i].img_bank,
                self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                self.raster_scroll[i].width,self.raster_scroll[i].height,
                self.raster_scroll[i].transparent_color)
                #右横に更に同じラインを描画する
                pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width,self.raster_scroll[i].posy,
                self.raster_scroll[i].img_bank,
                self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                self.raster_scroll[i].width,self.raster_scroll[i].height,
                self.raster_scroll[i].transparent_color)
                #更にその右横に同じラインを描画
                pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 2,self.raster_scroll[i].posy,
                self.raster_scroll[i].img_bank,
                self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                self.raster_scroll[i].width,self.raster_scroll[i].height,
                self.raster_scroll[i].transparent_color)
                
                pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 3,self.raster_scroll[i].posy,
                self.raster_scroll[i].img_bank,
                self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                self.raster_scroll[i].width,self.raster_scroll[i].height,
                self.raster_scroll[i].transparent_color)
                pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 4,self.raster_scroll[i].posy,
                self.raster_scroll[i].img_bank,
                self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                self.raster_scroll[i].width,self.raster_scroll[i].height,
                self.raster_scroll[i].transparent_color)
                #同じラインパターンを5個右横に並べれば違和感なくx座標を0にしても目立たないんじゃないかな？の精神！

    #パワーアップアイテム類の表示
    def draw_obtain_item(self):
        """
        パワーアップアイテム類の表示
        """
        obtain_item_count = len(self.obtain_item)
        for i in reversed(range(obtain_item_count)):
            if    self.obtain_item[i].item_type == ITEM_SHOT_POWER_UP:            #ショットパワーアップカプセル（赤）の表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2, pyxel.frame_count // 8  % 8 * 8     ,224,    8,8,pyxel.COLOR_BLACK)
            elif  self.obtain_item[i].item_type == ITEM_MISSILE_POWER_UP:         #ミサイルパワーアップカプセル（緑）の表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2, pyxel.frame_count // 8  % 8 * 8 + 64 ,224,    8,8,pyxel.COLOR_BLACK)
            elif  self.obtain_item[i].item_type == ITEM_SHIELD_POWER_UP:          #シールドパワーアップカプセル（青）の表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2, pyxel.frame_count // 8  % 8 * 8 + 128,224,    8,8,pyxel.COLOR_BLACK)
                
            elif  self.obtain_item[i].item_type == ITEM_CLAW_POWER_UP:            #クローパワーアップカプセル （黄）の表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2, pyxel.frame_count // 8  % 8 * 8     ,232,    8,8,pyxel.COLOR_BLACK)
                
            elif  self.obtain_item[i].item_type == ITEM_SCORE_STAR:               #スコアスター(得点アイテム)の表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    64,72,    8,8,pyxel.COLOR_BLACK)
            elif  self.obtain_item[i].item_type == ITEM_TRIANGLE_POWER_UP:        #トライアングルアイテム(正三角形)ショット、ミサイル、シールドの表示
                graph.draw_obtain_item_triangle_item(self,i)
                
            elif  self.obtain_item[i].item_type == ITEM_TAIL_SHOT_POWER_UP:       #テイルショットカプセルの表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    64,232,    8,8,pyxel.COLOR_GRAY)
                graph.draw_obtain_item_rotation_box(self,i)
            elif  self.obtain_item[i].item_type == ITEM_PENETRATE_ROCKET_POWER_UP:#ペネトレートロケットカプセルの表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    72,232,    8,8,pyxel.COLOR_GRAY)
                graph.draw_obtain_item_rotation_box(self,i)
            elif  self.obtain_item[i].item_type == ITEM_SEARCH_LASER_POWER_UP:    #サーチレーザーカプセルの表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    80,232,    8,8,pyxel.COLOR_GRAY)
                graph.draw_obtain_item_rotation_box(self,i)
            elif  self.obtain_item[i].item_type == ITEM_HOMING_MISSILE_POWER_UP:  #ホーミングミサイルカプセルの表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    88,232,    8,8,pyxel.COLOR_GRAY)
                graph.draw_obtain_item_rotation_box(self,i)
            elif  self.obtain_item[i].item_type == ITEM_SHOCK_BUMPER_POWER_UP:    #ショックバンパーカプセルの表示
                pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy - self.camera_offset_y,IMG2,    96,232,    8,8,pyxel.COLOR_GRAY)
                graph.draw_obtain_item_rotation_box(self,i)

    #パワーアップアイテムの回転する四角形外枠の描画表示
    def draw_obtain_item_rotation_box(self,i): #iはobtain_itemクラスのインデックス値となります
        """
        パワーアップアイテムの回転する四角形外枠の描画表示
        
        iはobtain_itemクラスのインデックス値となります
        """
        self.obtain_item[i].degree +=0.5 #0.5度回転
        self.obtain_item[i].degree = self.obtain_item[i].degree % 360#角度は３６０で割った余りとする(0~359)
        #アイテムのある座標は(x=0,y=0)となります
        #         (x1,y1)  
        #       ／    !    ＼
        #     ／     !3     ＼
        #(x2,y2)--3--ITEM--3--(x4,y4)
        #    ＼      !      ／
        #       ＼    !3    ／
        #         (x3,y3)
        x1 =   0
        y1 = - 3 - self.expansion_shrink_number[self.stage_count // 3 % 37] #expansion_shrink_numberのリストを使ってラインの点座標を大きくしたり小さくさせます
        x2 = - 3 - self.expansion_shrink_number[self.stage_count // 3 % 37]
        y2 =   0
        x3 =   0
        y3 =   3 + self.expansion_shrink_number[self.stage_count // 3 % 37]
        x4 =   3 + self.expansion_shrink_number[self.stage_count // 3 % 37]
        y4 =   0
        
        #現在の角度に従って点座標を回転させます
        rotx1 = x1 * math.cos(math.radians(self.obtain_item[i].degree)) - y1 * math.sin(math.radians(self.obtain_item[i].degree))
        roty1 = x1 * math.sin(math.radians(self.obtain_item[i].degree)) + y1 * math.cos(math.radians(self.obtain_item[i].degree))
        rotx2 = x2 * math.cos(math.radians(self.obtain_item[i].degree)) - y2 * math.sin(math.radians(self.obtain_item[i].degree))
        roty2 = x2 * math.sin(math.radians(self.obtain_item[i].degree)) + y2 * math.cos(math.radians(self.obtain_item[i].degree))
        rotx3 = x3 * math.cos(math.radians(self.obtain_item[i].degree)) - y3 * math.sin(math.radians(self.obtain_item[i].degree))
        roty3 = x3 * math.sin(math.radians(self.obtain_item[i].degree)) + y3 * math.cos(math.radians(self.obtain_item[i].degree))
        rotx4 = x4 * math.cos(math.radians(self.obtain_item[i].degree)) - y4 * math.sin(math.radians(self.obtain_item[i].degree))
        roty4 = x4 * math.sin(math.radians(self.obtain_item[i].degree)) + y4 * math.cos(math.radians(self.obtain_item[i].degree))
        
        #アイテムの座標を中心として回転四角形を描画する
        pyxel.line(self.obtain_item[i].posx +3 + rotx1,self.obtain_item[i].posy  - self.camera_offset_y+ 3 + roty1,self.obtain_item[i].posx + 3 + rotx2,self.obtain_item[i].posy - self.camera_offset_y+ 3 + roty2, self.blinking_color[pyxel.frame_count // 8 % 10])
        pyxel.line(self.obtain_item[i].posx +3 + rotx2,self.obtain_item[i].posy  - self.camera_offset_y+ 3 + roty2,self.obtain_item[i].posx + 3 + rotx3,self.obtain_item[i].posy - self.camera_offset_y+ 3 + roty3, self.blinking_color[pyxel.frame_count // 8 % 10])
        pyxel.line(self.obtain_item[i].posx +3 + rotx3,self.obtain_item[i].posy  - self.camera_offset_y+ 3 + roty3,self.obtain_item[i].posx + 3 + rotx4,self.obtain_item[i].posy - self.camera_offset_y+ 3 + roty4, self.blinking_color[pyxel.frame_count // 8 % 10])
        pyxel.line(self.obtain_item[i].posx +3 + rotx4,self.obtain_item[i].posy  - self.camera_offset_y+ 3 + roty4,self.obtain_item[i].posx + 3 + rotx1,self.obtain_item[i].posy - self.camera_offset_y+ 3 + roty1, self.blinking_color[pyxel.frame_count // 8 % 10])

    #トライアングルアイテム（ショット、ミサイル、シールド）の表示
    def draw_obtain_item_triangle_item(self,i): #iはobtain_itemクラスのインデックス値となります
        """
        トライアングルアイテム（ショット、ミサイル、シールド）の表示
        
        iはobtain_itemクラスのインデックス値となります
        """
        self.obtain_item[i].degree -= self.obtain_item[i].speed #SPEED分,右回転する
        self.obtain_item[i].degree = self.obtain_item[i].degree % 360#角度は３６０で割った余りとする(0~359)
        #アイテムのある座標(x=0,y=0)は中心となります
        #そしてアイテムを中心に半径(radius)から等角度120度ごとの円の点がそれぞれ(x1,y1)(x2,y2)(x3,y3)となります
        #         (ax,ay)赤玉  
        #          ／! ＼
        #        ／  !   ＼
        #       ／   ITEM(半径radius)
        #     ／     !      ＼
        #(bx,by)緑玉-------------(cx,cy)青玉
        #
        
        #正三角形の３頂点の座標を計算する
        if self.obtain_item[i].status == 0: #状態遷移が「画面スクロールに合わせて左に流れる状態」の時は三角形は膨張収縮する
            ax = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree))
            ay = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree))
            
            bx = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree + 120))
            by = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree + 120))
            
            cx = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree + 240))
            cy = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree + 240))
        elif 1 <= self.obtain_item[i].status <= 2: #状態遷移が「アイテム取得時の高速回転状態」から「取得アニメーション描画中」までの時は三角形はそのままで描画する
            ax = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree))
            ay = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree))
            
            bx = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree + 120))
            by = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree + 120))
            
            cx = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree + 240))
            cy = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree + 240))
        
        #self.point_in_triangle(self.my_x,self.my_y,ax,ay,bx,by,cx,cy) 外積を使った三角形の内外判定は上手くいかなかったのでボツに。。。。
        if self.obtain_item[i].status == 0 or self.obtain_item[i].status == 1:#「画面スクロールに合わせて左に流れる状態」「アイテム取得時の高速回転状態」の時
            d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))#dに自機からアイテムまでの距離が入る
            if d > self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]:#離れている距離数がトライアングルアイテムの回転半径より大きい場合は三角形の外なので普通のライン描画
                pyxel.line(self.obtain_item[i].posx + ax,self.obtain_item[i].posy - self.camera_offset_y + ay,self.obtain_item[i].posx + bx,self.obtain_item[i].posy - self.camera_offset_y+ by, self.blinking_color[pyxel.frame_count // 8 % 10])
                pyxel.line(self.obtain_item[i].posx + bx,self.obtain_item[i].posy - self.camera_offset_y + by,self.obtain_item[i].posx + cx,self.obtain_item[i].posy - self.camera_offset_y+ cy, self.blinking_color[pyxel.frame_count // 8 % 10])
                pyxel.line(self.obtain_item[i].posx + cx,self.obtain_item[i].posy - self.camera_offset_y + cy,self.obtain_item[i].posx + ax,self.obtain_item[i].posy - self.camera_offset_y+ ay, self.blinking_color[pyxel.frame_count // 8 % 10])
                #ショット赤玉表示 範囲外なので玉の回転アニメーションはしない
                pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy - self.camera_offset_y + ay -4,IMG2,  0,224,    8,8,pyxel.COLOR_BLACK)
                #ミサイル緑玉表示
                pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy - self.camera_offset_y + by -4,IMG2, 64,224,    8,8,pyxel.COLOR_BLACK)
                #シールド青玉表示
                pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy - self.camera_offset_y + cy -4,IMG2,128,224,    8,8,pyxel.COLOR_BLACK)
            else:#範囲内なので塗りつぶし三角描画
                pyxel.tri(self.obtain_item[i].posx + ax,self.obtain_item[i].posy - self.camera_offset_y + ay,self.obtain_item[i].posx + bx,self.obtain_item[i].posy - self.camera_offset_y+ by,self.obtain_item[i].posx + cx,self.obtain_item[i].posy - self.camera_offset_y+ cy,self.blinking_color[pyxel.frame_count // 8 % 10])
                
                #ショット赤玉表示 範囲内なので玉の回転アニメーションを行う
                pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy - self.camera_offset_y + ay -4,IMG2, pyxel.frame_count % 8 * 8     ,224,    8,8,pyxel.COLOR_BLACK)
                #ミサイル緑玉表示
                pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy - self.camera_offset_y + by -4,IMG2, pyxel.frame_count % 8 * 8 + 64 ,224,    8,8,pyxel.COLOR_BLACK)
                #シールド青玉表示
                pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy - self.camera_offset_y + cy -4,IMG2, pyxel.frame_count % 8 * 8 + 128,224,    8,8,pyxel.COLOR_BLACK)
        elif self.obtain_item[i].status == 2: #「取得アニメーション中」の時
            #ショット赤消滅アニメーション
            pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy - self.camera_offset_y + ay -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,pyxel.COLOR_BLACK)
            #ミサイル緑消滅アニメーション
            pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy - self.camera_offset_y + by -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,pyxel.COLOR_BLACK)
            #シールド青消滅アニメーション
            pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy - self.camera_offset_y + cy -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,pyxel.COLOR_BLACK)

    #サブウェポンセレクトゲージの表示（画面上部にいま所持しているサブウェポンアイコンを描画する）
    def draw_sub_weapon_select_gauge(self):
        """
        サブウェポンセレクトゲージの表示（画面上部にいま所持しているサブウェポンアイコンを描画する）
        """
        for i in range(5):
            #論理式(sub_weapon_list[i]が0)の場合括弧の中の値がtrue=1となるので y座標は16+1*8=24となる
            pyxel.blt(60 + i * 10,0,  IMG2, 216 + i * 8,16 + (self.sub_weapon_list[i] == 0) * 8,   8,8, pyxel.COLOR_GRAY)

    #サブウェポンセレクトガイドボックスの表示（今選択しているサブウェポンを示す四角い矩形輪郭線）
    def draw_sub_weapon_select_guidebox(self):
        """
        サブウェポンセレクトガイドボックスの表示（今選択しているサブウェポンを示す四角い矩形輪郭線）
        """
        if self.select_sub_weapon_id != -1:#サブウェポンを全く所持していない状態（id=-1）以外ならガイドボックスを点滅表示させる
            pyxel.rectb(60 -1 + self.select_sub_weapon_id * 10,-1, 10,8, self.blinking_color[pyxel.frame_count // 8 % 10])

    #スコア表示やスピード、自機耐久力などのステータスの表示（画面上部の物やリプレイ再生中とか)
    def draw_status(self):
        """
        スコア表示やスピード、自機耐久力などのステータスの表示（画面上部の物やリプレイ再生中とか)
        """
        s = "{:>7}".format(self.score)
        pyxel.text(9, 1, s, 1) #点数の影部分の表示
        if self.score >= self.hi_score: #スコアがハイスコア以上なら(ハイスコア更新状態)
            pyxel.blt(0,0, IMG2, 88,72, 8,8, pyxel.COLOR_BLACK)
            pyxel.text(8, 1, s, pyxel.COLOR_YELLOW) #黄色でスコア表示
        else:
            pyxel.blt(0,0, IMG2, 80,72, 8,8, pyxel.COLOR_BLACK)
            pyxel.text(8, 1, s, pyxel.COLOR_WHITE)  #違っていたら白色でスコア表示
        
        #自機スピード表示
        if self.my_speed == 1:
            pyxel.blt(126,-1,IMG2, 104,72, 8,8, pyxel.COLOR_BLACK)
        elif self.my_speed == 1.5:
            pyxel.blt(126,-1,IMG2, 112,72, 8,8, pyxel.COLOR_BLACK)
        elif self.my_speed == 1.75:
            pyxel.blt(126,-1,IMG2, 120,72, 8,8, pyxel.COLOR_BLACK)
        #pyxel.text(32, 1, "SPEED " + str(self.my_speed), 7)
        
        #自機シールドパワー表示
        pyxel.blt(137,0,IMG2, 72,72, 8,8, pyxel.COLOR_BLACK)
        shi = "{:>2}".format(int(self.my_shield))
        pyxel.text(148+4,1,shi,pyxel.COLOR_NAVY)
        pyxel.text(147+4,1,shi,pyxel.COLOR_WHITE)
        #ショット経験値表示
        sho = "{:>2}".format(int(self.shot_exp))
        pyxel.text(148+4,7,sho,pyxel.COLOR_NAVY)
        pyxel.text(147+4,7,sho,pyxel.COLOR_RED)
        #ミサイル経験値表示
        mis = "{:>2}".format(int(self.missile_exp))
        pyxel.text(148+4,13,mis,pyxel.COLOR_NAVY)
        pyxel.text(147+4,13,mis,pyxel.COLOR_GREEN)    
        
        if self.replay_status == REPLAY_PLAY: #リプレイ再生時に表示します
            #リプレイ再生時はreplay_dataのリスト長と現在のリプレイフレームインデックス値を表示する
            num1 = "{:>8}".format(self.replay_frame_index)
            pyxel.text(128,120-28+10,num1,pyxel.COLOR_ORANGE)
            num2 = "{:>8}".format(int(len(self.replay_data[self.replay_stage_num])))
            pyxel.text(128,120-22+10,num2,pyxel.COLOR_YELLOW)
            #「リプレイ」を点滅表示させる
            pyxel.text(160-4*6,120 - 6,"REPLAY", int(self.rainbow_flash_color[pyxel.frame_count // 8 % 10]))

    #デバッグ用ステータスの表示
    def draw_debug_status(self):
        """
        デバッグ用ステータスの表示
        """
        if self.debug_menu_status == 0: #デバッグメニュー表示ステータスが0なら表示せずリターンする
            return
        
        if self.replay_status != REPLAY_PLAY: #リプレイ再生時は邪魔なので表示しません
            #星の数の表示
            pyxel.blt(143,WINDOW_H - 8, IMG2, 64,72, 8,8, pyxel.COLOR_BLACK)
            pyxel.text(153,WINDOW_H - 6,str(len(self.stars)),pyxel.COLOR_NAVY)
            pyxel.text(152,WINDOW_H - 6,str(len(self.stars)),pyxel.COLOR_WHITE)
        
            #敵ホッパータイプのバウンドフラグの表示（地面と衝突したか？）
            pyxel.blt(131,WINDOW_H - 7, IMG2, (self.enemy_bound_collision_flag * 8),80, 8,8, pyxel.COLOR_BLACK)
        #敵の数の表示
        pyxel.blt(0,WINDOW_H - 8, IMG2, 128,72, 8,8, pyxel.COLOR_BLACK)
        pyxel.text(10,WINDOW_H - 6,str(len(self.enemy)),pyxel.COLOR_NAVY)
        pyxel.text(9 ,WINDOW_H - 6,str(len(self.enemy)),pyxel.COLOR_WHITE)
        #敵弾数の表示
        pyxel.blt(20,WINDOW_H - 8,IMG2, 136,72, 8,8, pyxel.COLOR_BLACK)
        pyxel.text(30,WINDOW_H - 6,str(len(self.enemy_shot)),pyxel.COLOR_NAVY)
        pyxel.text(29,WINDOW_H - 6,str(len(self.enemy_shot)),pyxel.COLOR_WHITE)
        #スクロールカウントの表示(ＭＡＰチップ単位)
        pyxel.blt(40,WINDOW_H -8,IMG2, 96,72, 8,8, pyxel.COLOR_BLACK)
        pyxel.text(50,WINDOW_H -6,str(((self.scroll_count // 8) -256) // 2),pyxel.COLOR_NAVY)
        pyxel.text(49,WINDOW_H -6,str(((self.scroll_count // 8) -256) // 2),pyxel.COLOR_WHITE)
        
        #ステージカウントの表示(生データ)
        pyxel.text(37,1,str(self.stage_count),pyxel.COLOR_NAVY)
        pyxel.text(36,1,str(self.stage_count),pyxel.COLOR_LIME)
        
        #自機が存在するＭＡＰ位置のＸ、Ｙ座標の表示
        #MAPの外に存在するときは強制的にＸ座標を0にしちゃう
        self.bgy = ((self.my_y + 4 ) // 8)
        self.bgx = (((self.scroll_count // 8) -256) // 2) + self.my_x // 8
        if  0 > self.bgx:
            self.bgx = 0
        if self.bgx > 255:
            self.bgx = 0
        
        self.bg_chip = func.get_chrcode_tilemap(self,0, self.bgx,self.bgy)
        pyxel.text(70,WINDOW_H - 6,str(self.bgx),pyxel.COLOR_WHITE)
        pyxel.text(85,WINDOW_H - 6,str(self.bgy),pyxel.COLOR_WHITE)
        
        #自機に重なっているキャラチップが収納されたタイルのＸ，Ｙ座標の表示
        pyxel.text(95,WINDOW_H - 6,str(self.bg_chip // 4),pyxel.COLOR_LIGHT_BLUE)
        pyxel.text(110,WINDOW_H - 6,str((self.bg_chip % 16) * 8),pyxel.COLOR_LIGHT_BLUE)
        
        #自機に重なっているキャラチップを表示
        if self.replay_status != REPLAY_PLAY: #リプレイ再生時は邪魔なので表示しません
            pyxel.blt(120,WINDOW_H - 8,IMG2, (self.bg_chip % 16) * 8,(self.bg_chip // 4), 8,8)
        
        #ミサイルタイプチェッカーのカウント数の表示 デバッグ用
        #通常ミサイルの総数
        func.count_missile_type(self,0,1,2,3)
        pyxel.text(WINDOW_W - 5, WINDOW_H - 28,str(self.type_check_quantity),pyxel.COLOR_WHITE)
        #前方高速トマホークミサイル(ペネトレートロケット)の総数
        func.count_missile_type(self,5,5,5,5)
        pyxel.text(WINDOW_W - 12,WINDOW_H - 28,str(self.type_check_quantity),pyxel.COLOR_GREEN)
        
        #ゲームステータス（ゲームの状態）の表示
        pyxel.text(0,8,str(self.game_status),pyxel.COLOR_LIGHT_BLUE)
        
        #イベントインデックス値の表示
        pyxel.text(10,8,str(self.event_index),pyxel.COLOR_YELLOW)
        #イベントデータリストの表示
        pyxel.text(20,7,str(self.event_list[self.event_index]),pyxel.COLOR_ORANGE)
        
        #編隊ＩＤと総数の表示
        pyxel.text(1,14,str(self.current_formation_id),pyxel.COLOR_ORANGE) #現時点での編隊ID
        #編隊群リストの長さの表示
        pyxel.text(1,20,str(len(self.enemy_formation)),pyxel.COLOR_PINK) #現時点での編隊ID
        
        #編隊IDリストの表示(5リストまでの暫定表示です)
        if len(self.enemy_formation) >= 1:
            pyxel.text(14,14,str(self.enemy_formation[0].formation_id),pyxel.COLOR_WHITE)
            pyxel.text(22,14,str(self.enemy_formation[0].formation_number),pyxel.COLOR_BROWN)
            pyxel.text(30,14,str(self.enemy_formation[0].on_screen_formation_number),pyxel.COLOR_RED)
            pyxel.text(38,14,str(self.enemy_formation[0].shoot_down_number),pyxel.COLOR_RED)    
        if  len(self.enemy_formation) >= 2:
            pyxel.text(14,20,str(self.enemy_formation[1].formation_id),pyxel.COLOR_WHITE)
            pyxel.text(22,20,str(self.enemy_formation[1].formation_number),pyxel.COLOR_BROWN)
            pyxel.text(30,20,str(self.enemy_formation[1].on_screen_formation_number),pyxel.COLOR_RED)
            pyxel.text(38,20,str(self.enemy_formation[1].shoot_down_number),pyxel.COLOR_RED)
        if  len(self.enemy_formation) >= 3:
            pyxel.text(14,26,str(self.enemy_formation[2].formation_id),pyxel.COLOR_WHITE)
            pyxel.text(22,26,str(self.enemy_formation[2].formation_number),pyxel.COLOR_BROWN)
            pyxel.text(30,26,str(self.enemy_formation[2].on_screen_formation_number),pyxel.COLOR_RED)
            pyxel.text(38,26,str(self.enemy_formation[2].shoot_down_number),pyxel.COLOR_RED)
        if  len(self.enemy_formation) >= 4:
            pyxel.text(14,32,str(self.enemy_formation[3].formation_id),pyxel.COLOR_WHITE)
            pyxel.text(22,32,str(self.enemy_formation[3].formation_number),pyxel.COLOR_BROWN)
            pyxel.text(30,32,str(self.enemy_formation[3].on_screen_formation_number),pyxel.COLOR_RED)
            pyxel.text(38,32,str(self.enemy_formation[3].shoot_down_number),pyxel.COLOR_RED)
        if  len(self.enemy_formation) >= 5:
            pyxel.text(14,38,str(self.enemy_formation[4].formation_id),pyxel.COLOR_WHITE)
            pyxel.text(22,38,str(self.enemy_formation[4].formation_number),pyxel.COLOR_BROWN)
            pyxel.text(30,38,str(self.enemy_formation[4].on_screen_formation_number),pyxel.COLOR_RED)
            pyxel.text(38,38,str(self.enemy_formation[4].shoot_down_number),pyxel.COLOR_RED)
        #早回しフラグの表示
        pyxel.text(160-8*3+4,19,"ADD " + str(self.add_appear_flag), pyxel.COLOR_YELLOW)
        #早回し条件が成立するまでの必要殲滅編隊数の表示
        pyxel.text(160-8*3+4,25,"NUM " + str(self.fast_forward_destruction_num), pyxel.COLOR_ORANGE)
        
        #1プレイ時間の表示(秒まで表示します)
        func.disp_one_game_playtime(self,160,31,10)
        
        #総プレイ時間の表示(秒まで表示します)
        func.disp_total_game_playtime(self,160,37,13)
        
        #総開発テストプレイ時間の表示(分まで表示します)
        playing_min = self.one_game_playtime_seconds // 60 #今プレイしているゲームの時間(分)を計算
        pyxel.text(160-8*3,79,"   :", pyxel.COLOR_BROWN)
        testplay_hours   =  "{:>5}".format((self.total_development_testtime_min  + playing_min) // 60)
        testplay_minutes =  "{:>02}".format((self.total_development_testtime_min + playing_min)  % 60)
        pyxel.text(160-8*4,79,testplay_hours  , pyxel.COLOR_PINK)
        pyxel.text(160-8  ,79,testplay_minutes, pyxel.COLOR_PINK)
        
        # システムデータ数値読み取りテスト
        # pyxel.text(60,107,"TEST " + str(self.test_read_num), 9)
        
        #ステージ数の表示
        pyxel.text(160-8*3+8,43,"ST " + str(self.stage_number), pyxel.COLOR_ORANGE)
        #周回数の表示
        pyxel.text(160-8*3+8,49,"LP " + str(self.stage_loop), pyxel.COLOR_WHITE)
        
        #ワールドマップBGのxy座標の表示
        world_x = "{:>3}".format(int(self.scroll_count        // 8 % 256))
        pyxel.text(160-16,55,"X",8)
        pyxel.text(160-12,55,world_x,pyxel.COLOR_WHITE)
        world_y = "{:>3}".format(int(self.vertical_scroll_count // 8 % 256))
        pyxel.text(160-16,61,"Y",8)
        pyxel.text(160-12,61,world_y,pyxel.COLOR_WHITE)
        
        #背景山のx座標
        mou_x = "{:>3}".format(int(self.mountain_x))
        pyxel.text(160-20,67,"MX",pyxel.COLOR_RED)
        pyxel.text(160-12,67,mou_x,pyxel.COLOR_YELLOW)
        
        #ランクの表示
        pyxel.text(160-16,73,"RA" + str(self.rank), pyxel.COLOR_WHITE)
        
        #装備メダルの表示
        for i in range(6):#iは0から6(SLOT6)まで変化する
            medal_id = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i]
            pyxel.blt(0 + i * 8,104,IMG2,168 + medal_id * 8,176, 8,8,  pyxel.COLOR_GRAY)
        
        #スコアスターが出る総数の表示
        pyxel.text(50,108,"SC=STAR " + str(self.inc_shot_exp_medal),pyxel.COLOR_RED)
        
        
        if self.debug_menu_status != 2: #デバッグメニュー表示ステータスが2の時は表示しない
            #1番目のクローの座標の表示
            if self.claw_number >= 1:
                pyxel.text(0,WINDOW_H - 13,str(self.claw[0].posx),pyxel.COLOR_LIGHT_BLUE)
                pyxel.text(0,WINDOW_H - 20,str(self.claw[0].posy),pyxel.COLOR_LIGHT_BLUE)
            #2番目のクローの座標の表示
            # if self.claw_number >= 2:
                # pyxel.text(72,WINDOW_H - 13,str(self.claw[1].posx),5)
                # pyxel.text(72,WINDOW_H - 20,str(self.claw[1].posy),5)
        
        if self.debug_menu_status == 2 and self.replay_status == REPLAY_RECORD: #デバッグメニュー表示ステータスが2尚且つリプレイ記録中の時だけ表示する
            #コントロールパッド操作データの表示
            replay_count = len(self.replay_recording_data[self.replay_stage_num])
            if replay_count >= 2: #入力履歴はカウント２になったらデータが1個(2バイト)記録されるので取り出すことが出来るぞ！
                input_pad_data_h = bin(self.replay_recording_data[self.replay_stage_num][replay_count-2]) #パッド入力データHighByteを2進数に変換します
                input_pad_data_l = bin(self.replay_recording_data[self.replay_stage_num][replay_count-1]) #パッド入力データLowByteを2進数に変換します
                input_pad_data_h = input_pad_data_h.lstrip("0b")      #文字列の頭からバイナリー文字の"ob"を取り除きます lstripで先頭から取り除くって判りにくい・・・lstripのlってなんやねん・・・
                input_pad_data_l = input_pad_data_l.lstrip("0b")
                input_pad_data_h = "{:0>8}".format(input_pad_data_h) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                input_pad_data_l = "{:0>8}".format(input_pad_data_l) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                pyxel.text(0  ,120-14,input_pad_data_h, pyxel.COLOR_YELLOW)
                pyxel.text(4*8,120-14,input_pad_data_l, pyxel.COLOR_LIME)
            #コントロールパッド操作データ履歴の表示
            if replay_count >= 4:
                input_pad_data_h = bin(self.replay_recording_data[self.replay_stage_num][replay_count-4]) #パッド入力データHighByteを2進数に変換します
                input_pad_data_l = bin(self.replay_recording_data[self.replay_stage_num][replay_count-3]) #パッド入力データLowByteを2進数に変換します
                input_pad_data_h = input_pad_data_h.lstrip("0b")      #文字列の頭からバイナリー文字の"ob"を取り除きます lstripで先頭から取り除くって判りにくい・・・lstripのlってなんやねん・・・
                input_pad_data_l = input_pad_data_l.lstrip("0b")
                input_pad_data_h = "{:0>8}".format(input_pad_data_h) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                input_pad_data_l = "{:0>8}".format(input_pad_data_l) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                pyxel.text(0  ,120-20,input_pad_data_h, pyxel.COLOR_WHITE)
                pyxel.text(4*8,120-20,input_pad_data_l, pyxel.COLOR_WHITE)
            if replay_count >= 6:
                input_pad_data_h = bin(self.replay_recording_data[self.replay_stage_num][replay_count-6]) #パッド入力データHighByteを2進数に変換します
                input_pad_data_l = bin(self.replay_recording_data[self.replay_stage_num][replay_count-5]) #パッド入力データLowByteを2進数に変換します
                input_pad_data_h = input_pad_data_h.lstrip("0b")      #文字列の頭からバイナリー文字の"ob"を取り除きます lstripで先頭から取り除くって判りにくい・・・lstripのlってなんやねん・・・
                input_pad_data_l = input_pad_data_l.lstrip("0b")
                input_pad_data_h = "{:0>8}".format(input_pad_data_h) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                input_pad_data_l = "{:0>8}".format(input_pad_data_l) #文字列を整形します 0ゼロ埋め >右寄せ 8桁
                pyxel.text(0  ,120-26,input_pad_data_h, pyxel.COLOR_WHITE)
                pyxel.text(4*8,120-26,input_pad_data_l, pyxel.COLOR_WHITE)
        
        if self.debug_menu_status == 3: #デバッグメニュー表示ステータスが3の時だけ表示する
            #漢字表示テスト
            func.kanji_text(self,0,36,"文字列を分割できる関数",pyxel.COLOR_WHITE)
            func.kanji_text(self,0,50,"関数を使って文字列を編集",pyxel.COLOR_LIGHT_BLUE)
            func.kanji_text(self,0,63,"文字列を分割できる関数",pyxel.COLOR_ORANGE)
            func.kanji_text(self,0,76,"文字列を大文字・小文字に変換できる",pyxel.COLOR_GREEN)
            func.kanji_text(self,0,88,"保存したキャンバス",pyxel.COLOR_GRAY)
        
        #漢字フォントデータの表示テスト
        # for y in range(120):
            # for x in range(160):
                # col = self.kanji_fonts[y+pyxel.frame_count % 900][x+pyxel.frame_count % 300]
                # if col == 7:
                    # pyxel.pset(x,y,int(col))
        
        
        # 乱数0_9ルーレットの表示
        # pyxel.text(80,120-26,str(self.rnd0_9_num),9)
        #乱数0_99ルーレットの表示
        # pyxel.text(90,120-26,str(self.rnd0_99_num),10)
        
        #線形合同法で最初に使用した元となる乱数種の表示
        pyxel.text(140,120-35,"SD" + str(self.master_rnd_seed),11)
        #線形合同法乱数の表示
        # self.s_rnd()#線形合同法による乱数関数の呼び出し
        # rd_num = "{:>6}".format(str(self.rnd_seed))
        # pyxel.text(136,120-29,rd_num,3)
        
        # pyxel.text(0,120-39,str(self.s_rndint(10,600)),8)
        #今現在の乱数の表示
                
        # pyxel.text(0,120-35,"RND" + str(self.rnd_seed),11)
        
        #リプレイデータのサイズ表示
        if self.replay_status == REPLAY_RECORD:  #録画時はreplay_recording_dataのリスト長を表示する
            num = "{:>8}".format(int(len(self.replay_recording_data[self.replay_stage_num])))
            pyxel.text(128,120-22+8,num,pyxel.COLOR_RED)

    #BGチップデータ書き換えアニメーション実装のために作ったダミーテスト関数 画面左から2列目の縦1列を取得し、そのＢＧデータを画面左端1列目に表示する
    def draw_dummy_put_bg_xy(self):
        """
        BGチップデータ書き換えアニメーション実装のために作ったダミーテスト関数 画面左から2列目の縦1列を取得し、そのＢＧデータを画面左端1列目に表示する
        """
        if self.scroll_type == SCROLL_TYPE_8WAY_SCROLL_AND_RASTER: #全方向フリースクロール＋ラスタースクロールの場合
            for h in range(15): #縦は15キャラ分 8ドット*15キャラ=120ドット
                self.get_bg_chip_free_scroll(8,h * 8,0)#画面左端＋１のマップチップのBGの数値を取得する
                bg_num = "{:>3}".format(self.bg_chip)
                pyxel.text(16,h * 8,bg_num,pyxel.COLOR_WHITE)
                
                pyxel.text(30,h * 8,str(self.bgx), 8)
                pyxel.text(46,h * 8,str(self.bgy), 8)
                pyxel.text(60,h * 8,str((self.bg_chip  % 32) * 8), 9)
                pyxel.text(75,h * 8,str((self.bg_chip // 32) * 8), 9)
                
                pyxel.blt(0,h * 8, 1,    (self.bg_chip  % 32) * 8,(self.bg_chip // 32) * 8, 8,8, pyxel.COLOR_BLACK)#画面左端＋１にBGマップチップを描画する

    #WARNING警告ダイアログの表示(ボス出現)
    def draw_warning_dialog(self):
        """
        WARNING警告ダイアログの表示(ボス出現)
        """
        if self.warning_dialog_display_time <= 0: #WARNING表示時間が0以下だったらリターンする
            return
            
        for i in range(8*8):
            pyxel.blt(48+i,48+(self.warning_dialog_logo_time // 2) + i // 64 + self.warning_dialog_logo_time * i,    IMG2,     64+i,120,                     1,8 -(self.warning_dialog_logo_time // 2) - i // 68,   pyxel.COLOR_BLACK)
            
        warning_mes1 = "Unidentified flying object approaching"
        warning_mes2 = "Destroy if necessary!"
        lenstr1 = len(warning_mes1)
        lenstr2 = len(warning_mes2)
        
        pyxel.text(4 +  self.warning_dialog_text_time // 1,59,    warning_mes1[0:lenstr1 - int(self.warning_dialog_text_time //2.5)],pyxel.COLOR_WHITE)
        pyxel.text(40 + self.warning_dialog_text_time // 1,66,    warning_mes2[0:lenstr2 - int(self.warning_dialog_text_time //2.5)],pyxel.COLOR_WHITE)
        
        self.warning_dialog_display_time -= 1   #WARNING表示時間を1減らす      
        
        if self.warning_dialog_logo_time > 0:   #ロゴ表示に掛ける時間が0より大きいのなら
            self.warning_dialog_logo_time -= 1 #WARNINGグラフイックロゴ表示に掛ける時間を1減らす
            
        if self.warning_dialog_text_time > 0:   #テキスト表示に掛ける時間が0より大きいのなら
            self.warning_dialog_text_time -= 1 #WARNINGテキスト表示に掛ける時間を1減らす

    #STAGE CLEARダイアログの表示(ステージクリア！)
    def draw_stage_clear_dialog(self):
        """
        STAGE CLEARダイアログの表示(ステージクリア！)
        """
        if self.stage_clear_dialog_display_time <= 0: #STAGE CLEAR表示時間が0以下だったらリターンする
            return
        
        #画像「STAGE」の表示
        for i in range(8):
            pyxel.blt(40    + self.stage_clear_dialog_logo_time1 / 16 * i,48 + i,     IMG2,    128,    120 +i,   8,1,   pyxel.COLOR_BLACK)
        for i in range(8):
            pyxel.blt(40 + 8 + self.stage_clear_dialog_logo_time1 / 8  * i,48 + i,     IMG2,    128 + 8,120 +i,   8,1,   pyxel.COLOR_BLACK)
        for i in range(8):
            pyxel.blt(40 +16 + self.stage_clear_dialog_logo_time1 / 4  * i,48 + i,     IMG2,    128 +16,120 +i,   8,1,   pyxel.COLOR_BLACK)
        for i in range(8):
            pyxel.blt(40 +24 + self.stage_clear_dialog_logo_time1 / 2  * i,48 + i,     IMG2,    128 +24,120 +i,   8,1,   pyxel.COLOR_BLACK)
        for i in range(8):
            pyxel.blt(40 +32 + self.stage_clear_dialog_logo_time1     * i,48 + i,     IMG2,    128 +32,120 +i,   8,1,   pyxel.COLOR_BLACK)
        
        if self.stage_clear_dialog_logo_time1 > 0:   #ロゴ表示時間その1が0より大きいのなら
            self.stage_clear_dialog_logo_time1 -= 1 #1減らす
        
        #画像「CLEAR」の表示
        if self.stage_clear_dialog_logo_time1 <= 0:   #ロゴ表示時間その1の数値が0以下の場合は画像「STAGE」は表示し終わったので「CLEAR」を表示開始する
            for i in range(8):
                pyxel.blt(40 +40 + self.stage_clear_dialog_logo_time2 / 16 * i,48 + i,     IMG2,    128 +40,120 +i,   8,1,   pyxel.COLOR_BLACK)
            for i in range(8):
                pyxel.blt(40 +48 + self.stage_clear_dialog_logo_time2 / 8  * i,48 + i,     IMG2,    128 +48,120 +i,   8,1,   pyxel.COLOR_BLACK)
            for i in range(8):
                pyxel.blt(40 +56 + self.stage_clear_dialog_logo_time2 / 4  * i,48 + i,     IMG2,    128 +56,120 +i,   8,1,   pyxel.COLOR_BLACK)
            for i in range(8):
                pyxel.blt(40 +64 + self.stage_clear_dialog_logo_time2 / 2  * i,48 + i,     IMG2,    128 +64,120 +i,   8,1,   pyxel.COLOR_BLACK)
            for i in range(8):
                pyxel.blt(40 +72 + self.stage_clear_dialog_logo_time2     * i,48 + i,     IMG2,    128 +72,120 +i,   8,1,   pyxel.COLOR_BLACK)
            
            if self.stage_clear_dialog_logo_time2 > 0:   #ロゴ表示時間その2が0より大きいのなら
                self.stage_clear_dialog_logo_time2 -= 1 #1減らす
        #任務完了！速やかに次のステージへ移動せよ
        #
        #う～～～～ん・・・イマイチ文字列操作の仕方がよくわからない・・適当な数値補正入れて現状は上手く見せてるだけだけど
        stage_clear_mes1 = "MISSION COMPLETE!!"
        stage_clear_mes2 = "Move quickly to the next stage!!"
        lenstr1 = len(stage_clear_mes1)
        lenstr2 = len(stage_clear_mes2)
        
        if self.stage_clear_dialog_logo_time2 == 0:   #ロゴ表示時間その2が0なら「STAGE CLEAR」の表示は終わったのでメッセージの表示を始める
            pyxel.text(46,59,    stage_clear_mes1[0:- int(self.stage_clear_dialog_text_time / self.stage_clear_dialog_text_time_master * lenstr1) - 1],pyxel.COLOR_WHITE)
            pyxel.text(20,66,    stage_clear_mes2[0:- int(self.stage_clear_dialog_text_time / self.stage_clear_dialog_text_time_master * lenstr2) - 1],pyxel.COLOR_WHITE)
            
            self.stage_clear_dialog_display_time -= 1    #STAGE CLEAR表示時間を1減らす
            if self.stage_clear_dialog_display_time == 0: #STAGE CLEAR表示時間が0になったら
                self.game_status = Scene.STAGE_CLEAR_FADE_OUT #ゲームステータスを「ステージクリア後のフェードアウト」にする
            
            if self.stage_clear_dialog_text_time > 0:   #テキスト表示に掛ける時間が0より大きいのなら
                self.stage_clear_dialog_text_time -= 1 #STAGE CLEARテキスト表示に掛ける時間を1減らす

    #一時停止・ポーズメッセージの表示
    def draw_pause_message(self):
        """
        一時停止・ポーズメッセージの表示
        """
        pyxel.text(80-8, 32, "PAUSE", pyxel.COLOR_WHITE)
        self.star_scroll_speed -= 0.01 #ポーズをかけると星のスクロールスピードの倍率を毎フレームごと0.01減らしていく
        if self.star_scroll_speed < 0:
            self.star_scroll_speed = 0 #0以下になったら強制的に0を代入
        #a=self.s_rndint(0,100)
        #if a == 0:
        pyxel.text(0, 42, "The space-time interference system still",pyxel.COLOR_WHITE)
        pyxel.text(0, 50, "  seems to take a long time to work on",pyxel.COLOR_WHITE)
        pyxel.text(0, 58, "    a much more distant object.", pyxel.COLOR_WHITE)         #時空干渉システムはやはりはるか遠くの天体に作用するのに時間が掛るようだ

    #タイトルメッセージの表示(何かボタン押してね～)
    def draw_title_message(self):
        """
        タイトルメッセージの表示(何かボタン押してね～)
        """
        pyxel.text(20, 52, "CODE OF PYTHON POWED BY PYXEL",pyxel.COLOR_WHITE)
        pyxel.text(20, 72, "PROJECT MINE 2020",pyxel.COLOR_WHITE)
        pyxel.text(40, 100, "HIT ANY KEY",self.blinking_color[pyxel.frame_count // 8 % 10])

    #ウィンドウの表示
    def draw_window(self,priority,draw_num): #priorityの数値と一致するプライオリティナンバーを持つウィンドウだけを描画します
        """
        ウィンドウの表示
        
        priorityの数値と一致するプライオリティナンバーを持つウィンドウだけを描画します
        draw_num=(ORDINARY_SUPERPOSITION=そのまま普通に重ね合わせて表示)(BLACK_RECTANGLE_FILL=「黒矩形塗りつぶし」した後表示する)
        """
        window_count = len(self.window)
        for i in range(window_count):
            #priorityの数値と一致する、尚且つ下地が有色(透明でない)ウィンドウだけを描画します
            #下地が透明、または半透明のウィンドウは真っ黒な四角で塗りつぶし→背景の星をその範囲だけ再描画→透明、半透明のウィンドウだけで描画するメソッドを呼び出して描画する
            if self.window[i].window_priority != priority:#window_priorityの数値と引数のpriorityが一致しなかったら何もしないで次のウィンドウ描画に移る
                continue
            
            #下地が有色のウィンドウを描画します
            if self.window[i].window_bg == WINDOW_BG_BLUE_BACK or (self.window[i].window_bg != WINDOW_BG_BLUE_BACK and draw_num == ORDINARY_SUPERPOSITION):
                #ウィンドウ下地描画###############################################################
                for h in range (int(self.window[i].height // 8 + 1)):
                    for w in range (int(self.window[i].width // 8 + 1)) :
                        pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy + h * 8,            
                            IMG2,
                            96 + self.window[i].window_bg * 32,88,
                            SIZE_8,SIZE_8, pyxel.COLOR_GRAY)
                
                #ウィンドウ外枠フレーム描画###############################################################
                if self.window[i].window_frame == WINDOW_FRAME_NORMAL: #ウィンドウフレーム表示有の場合は外枠を表示する
                    #ウィンドウ横パーツ描画#############################################################
                    for w in range(int(self.window[i].width // 8 + 1)):
                        #上部の横パーツ描画
                        pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy,                         
                            IMG2,
                            96 + self.window[i].window_bg * 32,80,
                                SIZE_8,SIZE_8, pyxel.COLOR_GRAY)
                            #下部の横パーツ描画
                        pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy + self.window[i].height,
                            IMG2,
                            96 + self.window[i].window_bg * 32,96,
                            SIZE_8,SIZE_8, pyxel.COLOR_GRAY)
                    
                    #ウィンドウ縦パーツ描画####################################################
                    for h in range(int(self.window[i].height // 8 + 1)):
                        #左の縦パーツ描画
                        pyxel.blt(self.window[i].posx                      ,self.window[i].posy + h * 8,
                            IMG2,
                            80 + self.window[i].window_bg * 32,88,
                            SIZE_8,SIZE_8, pyxel.COLOR_GRAY)
                        #右の縦パーツ描画
                        pyxel.blt(self.window[i].posx + self.window[i].width,self.window[i].posy + h * 8,
                            IMG2,
                            104 + self.window[i].window_bg * 32,88,
                            SIZE_8,SIZE_8, pyxel.COLOR_GRAY)
                    
                    #################ウィンドウ四隅の角の描画#####################################
                    #左上のウィンドウパーツの描画
                    pyxel.blt(self.window[i].posx                      ,self.window[i].posy                        ,
                        IMG2,
                        80  + self.window[i].window_bg * 32,80,
                        SIZE_8,SIZE_8,  pyxel.COLOR_GRAY)
                    #右上のウィンドウパーツの描画
                    pyxel.blt(self.window[i].posx + self.window[i].width,self.window[i].posy                        ,
                        IMG2,
                        104 + self.window[i].window_bg * 32,80,
                        SIZE_8,SIZE_8,  pyxel.COLOR_GRAY)
                    #左下のウィンドウパーツの描画
                    pyxel.blt(self.window[i].posx                      ,self.window[i].posy + self.window[i].height ,
                        IMG2,
                        80  + self.window[i].window_bg * 32,96,
                        SIZE_8,SIZE_8,  pyxel.COLOR_GRAY)
                    #左下のウィンドウパーツの描画
                    pyxel.blt(self.window[i].posx + self.window[i].width ,self.window[i].posy + self.window[i].height  ,
                        IMG2,
                        104 + self.window[i].window_bg * 32,96,
                        SIZE_8,SIZE_8,  pyxel.COLOR_GRAY)
                
                #ベクターグラフイックスの表示
                if self.window[i].vector_grp != "": #ベクターグラフイック表示を行うリストが空でないのならば表示を始める
                    for j in range(len(self.window[i].vector_grp)): #vector_grpの長さの分ループ処理する
                        open_rate_x = self.window[i].width  / self.window[i].open_width  #開閉率(横軸)
                        open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                        if   self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_LINE:    #LINE命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #始点座標の取得
                            x2,y2  = self.window[i].vector_grp[j][3],self.window[i].vector_grp[j][4] #終点座標の取得
                            colkey = self.window[i].vector_grp[j][5] #描画色の取得
                            pyxel.line(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,self.window[i].posx + x2 * open_rate_x,self.window[i].posy + y2 * open_rate_y,colkey) #ライン描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_PSET:    #PSET命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #座標の取得
                            colkey = self.window[i].vector_grp[j][3] #描画色の取得
                            pyxel.pset(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,colkey) #点描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_BOX:     #BOX命令
                            x,y           = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #座標の取得
                            width,height  = self.window[i].vector_grp[j][3],self.window[i].vector_grp[j][4] #横幅縦幅の取得
                            colkey = self.window[i].vector_grp[j][5] #描画色の取得
                            pyxel.rectb(self.window[i].posx + x * open_rate_x,self.window[i].posy + y * open_rate_y,width * open_rate_x,height * open_rate_y,colkey) #矩形描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_BOXF:    #BOXFILL命令
                            x,y           = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #座標の取得
                            width,height  = self.window[i].vector_grp[j][3],self.window[i].vector_grp[j][4] #横幅縦幅の取得
                            colkey = self.window[i].vector_grp[j][5] #描画色の取得
                            pyxel.rect(self.window[i].posx + x * open_rate_x,self.window[i].posy + y * open_rate_y,width * open_rate_x,height * open_rate_y,colkey) #矩形描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_CIRCLE:  #CIRCLE命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #中心座標の取得
                            r      = self.window[i].vector_grp[j][3]                                 #半径の取得
                            colkey = self.window[i].vector_grp[j][4]                                 #描画色の取得
                            pyxel.circb(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,r * open_rate_x * open_rate_y,colkey) #円描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_CIRCLEF: #CIRCLEF命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #中心座標の取得
                            r      = self.window[i].vector_grp[j][3]                                 #半径の取得
                            colkey = self.window[i].vector_grp[j][4]                                 #描画色の取得
                            pyxel.circ(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,r * open_rate_x * open_rate_y,colkey) #塗りつぶし円描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_TRI:     #TRIANGLE命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #座標1の取得
                            x2,y2  = self.window[i].vector_grp[j][3],self.window[i].vector_grp[j][4] #座標2の取得
                            x3,y3  = self.window[i].vector_grp[j][5],self.window[i].vector_grp[j][6] #座標3の取得
                            colkey = self.window[i].vector_grp[j][7] #描画色の取得
                            pyxel.trib(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,self.window[i].posx + x2 * open_rate_x,self.window[i].posy + y2 * open_rate_y,self.window[i].posx + x3 * open_rate_x,self.window[i].posy + y3 * open_rate_y,colkey) #三角形描画
                        elif self.window[i].vector_grp[j][0] == LIST_WINDOW_VECTOR_GRP_TRIF:    #TRIANGLE FILL命令
                            x1,y1  = self.window[i].vector_grp[j][1],self.window[i].vector_grp[j][2] #座標1の取得
                            x2,y2  = self.window[i].vector_grp[j][3],self.window[i].vector_grp[j][4] #座標2の取得
                            x3,y3  = self.window[i].vector_grp[j][5],self.window[i].vector_grp[j][6] #座標3の取得
                            colkey = self.window[i].vector_grp[j][7] #描画色の取得
                            pyxel.tri(self.window[i].posx + x1 * open_rate_x,self.window[i].posy + y1 * open_rate_y,self.window[i].posx + x2 * open_rate_x,self.window[i].posy + y2 * open_rate_y,self.window[i].posx + x3 * open_rate_x,self.window[i].posy + y3 * open_rate_y,colkey) #塗りつぶし三角形描画
                
                #タイトルバーの表示######################################
                if   self.window[i].title_text[LIST_WINDOW_TEXT_FLASH]  == MES_NO_FLASH:        #テキスト点滅無しの場合
                    col = self.window[i].title_text[LIST_WINDOW_TEXT_COLOR]
                else:                                                                           #テキスト点滅系の場合
                    flash_type = self.window[i].title_text[LIST_WINDOW_TEXT_FLASH]              #flash_typeを元にカラーコードを取得
                    col = func.get_flashing_type_color_code(self,flash_type)
                
                if self.window[i].window_type == WINDOW_TYPE_BANNER:
                    text_len = len(self.window[i].title_text[LIST_WINDOW_TEXT]) #テキストの文字数を取得
                    num = int(text_len * (self.window[i].width / self.window[i].open_width)) #ウィンドウの開き具合から計算して文字列の左側から何文字取得するか計算する num=左端から取り出す文字数
                    text = str(self.window[i].title_text[LIST_WINDOW_TEXT]) #文字列全体を取り出す
                    text2 = text[:num] #文字列の左側からnumの数だけ文字を取り出す
                    func.drop_shadow_text(self,self.window[i].posx + self.window[i].title_text[LIST_WINDOW_TEXT_OX] + 5,self.window[i].posy + self.window[i].title_text[LIST_WINDOW_TEXT_OY] + 5,text2,col)
                else:
                    func.drop_shadow_text(self,self.window[i].posx + self.window[i].title_text[LIST_WINDOW_TEXT_OX] + 5 + self.window[i].width // 2 - len(self.window[i].title_text[LIST_WINDOW_TEXT]) * 2,self.window[i].posy + self.window[i].title_text[LIST_WINDOW_TEXT_OY] + 5,str(self.window[i].title_text[LIST_WINDOW_TEXT]),col)
                
                #ステータスがテキストメッセージの表示中,閉じ中,移動中,ウィンドウオープン完了の時はアイテムテキストを表示する
                if      self.window[i].window_status == WINDOW_WRITE_MESSAGE\
                    or  self.window[i].window_status == WINDOW_CLOSE\
                    or  self.window[i].window_status == WINDOW_MOVE\
                    or  self.window[i].window_status == WINDOW_OPEN_COMPLETED:
                    for j in range(len(self.window[i].item_text)): #textの長さの分ループ処理する
                        if self.window[i].item_text[j][LIST_WINDOW_TEXT]  != "": #ウィンドウテキストの表示をする 文字列が存在しないのなら次の行へとスキップループする
                            if   self.window[i].item_text[j][LIST_WINDOW_TEXT_FLASH]  == MES_NO_FLASH:        #テキスト点滅無しの場合
                                col = self.window[i].item_text[j][LIST_WINDOW_TEXT_COLOR]
                            else:                                                                         #テキスト点滅系の場合
                                flash_type = self.window[i].item_text[j][LIST_WINDOW_TEXT_FLASH]              #flash_typeを元にカラーコードを取得
                                col = func.get_flashing_type_color_code(self,flash_type)
                            
                            if self.window[i].item_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_CENTER:
                                func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OX] + 5 + self.window[i].width // 2 - len(self.window[i].item_text[j][LIST_WINDOW_TEXT]) * 2,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT]),col)
                            elif self.window[i].item_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_LEFT_ALIGN:
                                func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OX] + 5  ,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT]),col)
                        
                        if     self.window[i].window_id_sub == WINDOW_ID_SUB_ON_OFF_MENU\
                            or self.window[i].window_id_sub == WINDOW_ID_SUB_MULTI_SELECT_MENU: #「ON」「OFF」のトグルスイッチ式メニュー,ハイライト付きマルチメニューの場合はオブジェクト表示
                            
                            flag_index = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                            if self.window[i].flag_list[flag_index] == self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_COMPARE]: #フラグの数値とリストに登録されているパラメーター数値を比較して・・・
                                col = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_ON_COLOR] #同じ数値ならオンの色
                            else:
                                col = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_OFF_COLOR]  #違っていたならオフの色
                            
                            if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_ALIGN] == DISP_CENTER:
                                func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX] + 5 + self.window[i].width // 2 - len(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT]) * 2,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT]),col)
                            elif self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_ALIGN] == DISP_LEFT_ALIGN:
                                func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX] + 5  ,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT]),col)
                        elif self.window[i].window_id_sub == WINDOW_ID_SUB_SWITCH_TEXT_MENU: #上下操作でカーソルが上下し左右でそれぞれの項目に対応したテキストが切り替わり表示されるメニュータイプの場合
                            flag_index = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                            k = self.window[i].flag_list[flag_index]
                            if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_ON_OFF: #「ON」「OFF」の二つから選ぶシンプルなタイプ
                                if k == 0: #kの値がゼロの時はOFFなので・・
                                    col = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_OFF_COLOR] #描画色はOFF時の色とします
                                else: #Kの値が0以外の時はONと扱うので
                                    col = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_ON_COLOR]  #描画色はON時の色とします
                                
                                if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_ALIGN] == DISP_CENTER:
                                    func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX] + 5 + self.window[i].width // 2 - len(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_SWITCH_TEXT][k]) * 2,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_SWITCH_TEXT][k]),col)
                                elif self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_ALIGN] == DISP_LEFT_ALIGN:
                                    func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX] + 5  ,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str(self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_SWITCH_TEXT][k]),col)
                            elif self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] ==  OPE_OBJ_TYPE_NUM: #数値を増減させて選択するタイプ
                                col = self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_OFF_COLOR] #描画色はOFF時の色とします
                                str_k = "{:>3}".format(k)
                                func.drop_shadow_text(self,self.window[i].posx + self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX] + 5  ,self.window[i].posy + 5 + (j+1) * self.window[i].between_line,str_k,col) #3桁の整数で右寄せで表示
                                
                                #各方向矢印表示フラグが立っていた時はそれぞれの方向の矢印（テキスト）を描画する
                                if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_FLAG]    == DISP_ON:
                                    func.drop_shadow_text(self,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_X]   ,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_Y]     ,"^",col)
                                if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_FLAG]  == DISP_ON:
                                    func.drop_shadow_text(self,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_X] ,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_Y]   ,"v",col)
                                if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] == DISP_ON:
                                    func.drop_shadow_text(self,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_X],self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_Y]  ,">",col)
                                if self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  == DISP_ON:
                                    func.drop_shadow_text(self,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_X] ,self.window[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_Y]   ,"<",col)
                
                #ステータスがテキストメッセージの表示中,閉じ中,移動中,ウィンドウオープン完了の時はアイテム漢字テキストを表示する
                if      self.window[i].window_status == WINDOW_WRITE_MESSAGE\
                    or  self.window[i].window_status == WINDOW_CLOSE\
                    or  self.window[i].window_status == WINDOW_MOVE\
                    or  self.window[i].window_status == WINDOW_OPEN_COMPLETED:
                    for j in range(len(self.window[i].item_kanji_text)): #item_kanji_textの長さの分ループ処理する
                        if self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT]  != "": #ウィンドウテキストの表示をする 文字列が存在しないのなら次の行へとスキップループする
                            if   self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_FLASH]  == MES_NO_FLASH:        #テキスト点滅無しの場合
                                col = self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_COLOR]
                            else:                                                                         #テキスト点滅系の場合
                                flash_type = self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_FLASH]              #flash_typeを元にカラーコードを取得
                                col = func.get_flashing_type_color_code(self,flash_type)
                            
                            if self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_CENTER:
                                func.drop_shadow_kanji_text(self,self.window[i].posx + self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_OX] + self.window[i].width // 2 - len(self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT]) * 4,self.window[i].posy + (j+1) * self.window[i].between_line,str(self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT]),col)
                            elif self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_LEFT_ALIGN:
                                func.drop_shadow_kanji_text(self,self.window[i].posx + self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT_OX]  ,self.window[i].posy + (j+1) * self.window[i].between_line,str(self.window[i].item_kanji_text[j][LIST_WINDOW_TEXT]),col)
                
                #ウィンドウタイプがテキスト編集の入力待ちのタイプはさらに入力メッセージ(edit_text)の文字列を表示する
                if     self.window[i].window_type   == WINDOW_TYPE_EDIT_TEXT:
                    if self.window[i].edit_text[LIST_WINDOW_TEXT]  != "": #ウィンドウテキストの表示をする 文字列が存在しないのなら次の行へとスキップループする
                        if   self.window[i].edit_text[LIST_WINDOW_TEXT_FLASH]  == MES_NO_FLASH:        #テキスト点滅無しの場合
                            col = self.window[i].edit_text[LIST_WINDOW_TEXT_COLOR]
                        else:                                                                          #テキスト点滅系の場合
                            flash_type = self.window[i].edit_text[LIST_WINDOW_TEXT_FLASH]              #flash_typeを元にカラーコードを取得
                            col = func.get_flashing_type_color_code(self,flash_type)
                        
                        if self.window[i].edit_text[LIST_WINDOW_TEXT_ALIGN] == DISP_CENTER:
                            func.drop_shadow_text(self,self.window[i].posx + self.window[i].edit_text[LIST_WINDOW_TEXT_OX]     + self.window[i].width // 2 - len(self.window[i].edit_text[LIST_WINDOW_TEXT]) * 2,self.window[i].posy + self.window[i].edit_text[LIST_WINDOW_TEXT_OY]   ,str(self.window[i].edit_text[LIST_WINDOW_TEXT]),col)
                        elif self.window[i].edit_text[LIST_WINDOW_TEXT_ALIGN] == DISP_LEFT_ALIGN:
                            func.drop_shadow_text(self,self.window[i].posx + self.window[i].edit_text[LIST_WINDOW_TEXT_OX]     ,self.window[i].posy + self.window[i].edit_text[LIST_WINDOW_TEXT_OY]    ,str(self.window[i].edit_text[LIST_WINDOW_TEXT]),col)
                
                #OKボタンの表示
                if self.window[i].ok_button_disp_flag == BUTTON_DISP_ON: #OKボタン表示フラグが立っているのならば・・・
                    if self.window[i].ok_button_size == WINDOW_BUTTON_SIZE_1TEXT: #ボタンサイズが半角テキストの場合
                        u,v = 224 + (pyxel.frame_count // 3 % 8) * SIZE_4,184
                        w,h = SIZE_4,SIZE_6
                        pyxel.blt(self.window[i].posx + self.window[i].ok_button_x,self.window[i].posy + self.window[i].ok_button_y,IMG2,u,v,w,h,pyxel.COLOR_GRAY)
                
                #グラフイックキャラ,グラフイックパターン,画像の表示などなど
                if self.window[i].graph_list != "": #ウィンドウグラフイック表示を行うリストが空でないのならば表示を始める
                    for j in range(len(self.window[i].graph_list)): #graph_listの長さの分ループ処理する
                        ox,oy  = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_OX],self.window[i].graph_list[j][LIST_WINDOW_GRAPH_OY]#表示オフセット座標取得
                        imgb   = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_IMGB]#参照イメージバンク値取得
                        u,v    = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_U],self.window[i].graph_list[j][LIST_WINDOW_GRAPH_V]#グラフイックデーター収納座標取得
                        w,h    = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_W],self.window[i].graph_list[j][LIST_WINDOW_GRAPH_H]#幅と縦を取得
                        colkey = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_COLKEY]#透明色取得
                        ani_num = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_ANIME_FRAME_NUM]#アニメーション枚数取得
                        ani_speed = self.window[i].graph_list[j][LIST_WINDOW_GRAPH_ANIME_SPEED]#アニメーションスピード取得
                        u_offset = (pyxel.frame_count // ani_speed % ani_num) * w #アニメ枚数とアニメスピード、描画幅から参照すべきグラフイックデーター収納座標のオフセット値を求める
                        open_rate_x = self.window[i].width  / self.window[i].open_width  #開閉率(横軸)
                        open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                        pyxel.blt(self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,imgb,u + u_offset,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #グラフイック表示
                
                #メダルの表示
                if self.window[i].medal_graph_list != []: #メダルグラフイックリストが空でないのならば表示を始める
                    for j in range(len(self.window[i].medal_graph_list)): #medal_graph_listの長さの分ループ処理する
                        ox,oy     = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_OX],self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_OY]#表示オフセット座標取得
                        imgb      = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_IMGB]#参照イメージバンク値取得
                        u,v       = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_U] ,self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_V]#グラフイックデーター収納座標取得
                        w,h       = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_W] ,self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_H]#幅と縦を取得
                        colkey    = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_COLKEY]#透明色取得
                        ani_num   = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_ANIME_FRAME_NUM]#アニメーション枚数取得
                        ani_speed = self.window[i].medal_graph_list[j][LIST_WINDOW_GRAPH_ANIME_SPEED]#アニメーションスピード取得
                        u_offset = (pyxel.frame_count // ani_speed % ani_num) * w #アニメ枚数とアニメスピード、描画幅から参照すべきグラフイックデーター収納座標のオフセット値を求める
                        open_rate_x = self.window[i].width / self.window[i].open_width   #開閉率(横軸)
                        open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                        if self.window[i].medal_list[j] == 1:#メダルリストを見て所持フラグが立っているのなら表示する
                            pyxel.blt(self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,imgb,u + u_offset,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #グラフイック表示
                
                #自機グラフイック,機体名,装備メダルの表示
                if self.window[i].ship_list != []: #シップリストが空でないのならば表示を始める
                    idnum  = self.window[i].ship_medal_list[LIST_SHIP_MEDAL_SHIP_ID] #自機ＩＤナンバー取得
                    
                    #自機グラフイックの表示
                    ox,oy  = self.window[i].ship_medal_list[LIST_SHIP_SHIP_DISP_OX],self.window[i].ship_medal_list[LIST_SHIP_SHIP_DISP_OY]#表示オフセット座標取得
                    imgb   = self.window[i].ship_list[idnum][LIST_SHIP_GRP_IMGB]#参照イメージバンク値取得
                    u,v    = self.window[i].ship_list[idnum][LIST_SHIP_GRAPH_U],self.window[i].ship_list[idnum][LIST_SHIP_GRAPH_V]#自機グラフイックデーター収納座標取得
                    w,h    = 8,8 #幅と縦を取得
                    colkey = 0 #透明色取得
                    open_rate_x = self.window[i].width / self.window[i].open_width   #開閉率(横軸)
                    open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                    if self.window[i].ship_medal_list[LIST_SHIP_SHIP_GRAPH_DISP_FLAG] == DISP_ON: #自機グラフイック表示フラグが建っていたら表示する
                        pyxel.blt(self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,imgb,u,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #グラフイック表示
                    
                    #機体名の表示
                    ox,oy    = self.window[i].ship_medal_list[LIST_SHIP_SHIP_NAME_DISP_OX],self.window[i].ship_medal_list[LIST_SHIP_SHIP_NAME_DISP_OY]#表示オフセット座標取得
                    nametext = self.window[i].ship_list[idnum][LIST_SHIP_NAME] #機体名取得
                    if self.window[i].ship_medal_list[LIST_SHIP_SHIP_NAME_DISP_FLAG] == DISP_ON: #機体名表示フラグが建っていたら表示する
                        func.drop_shadow_text(self,self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,nametext,7) #機体名表示
                    
                    #装備メダルの表示
                    ox,oy   = self.window[i].ship_medal_list[LIST_SHIP_MEDAL_DISP_OX],self.window[i].ship_medal_list[LIST_SHIP_MEDAL_DISP_OY]#表示オフセット座標取得
                    for j in range(self.window[i].ship_list[idnum][LIST_SHIP_SLOT_NUM]):
                        medal_id = self.window[i].ship_list[idnum][LIST_SHIP_SLOT0 + j] #まずメダルIDを取得する
                        open_rate_x = self.window[i].width / self.window[i].open_width   #開閉率(横軸)
                        open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                        u = self.medal_graph_and_comment_list[medal_id][LIST_MEDAL_GRP_CMNT_U]
                        v = self.medal_graph_and_comment_list[medal_id][LIST_MEDAL_GRP_CMNT_V]
                        imgb = self.medal_graph_and_comment_list[medal_id][LIST_MEDAL_GRP_CMNT_IMGB]
                        w,h    = 8,8 #幅と縦を取得
                        colkey = pyxel.COLOR_GRAY #透明色取得
                        pyxel.blt((self.window[i].posx + ox + j * 10 ) * open_rate_x,self.window[i].posy + oy * open_rate_y,imgb,u + u_offset,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #メダルグラフイック表示
                        # pyxel.text(self.window[i].posx + ox + j * 10,self.window[i].posy + oy,str(medal_id),7)
                
                #パッドアサインリストを参考にしてそのパッドボタンのアイコンを表示する
                if self.window[i].pad_assign_list != []: #パッドアサインリストが空でないのなら表示を始める
                    for j in range(len(self.window[i].pad_assign_graph_list)): #pad_assign_listの長さの分ループ処理する
                        ox,oy  = self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_OX],   self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_OY]#表示オフセット座標取得
                        imgb   = self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_IMGB]  #参照イメージバンク値取得
                        u,v    = self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_U],    self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_V] #ボタングラフイックデーター収納座標取得
                        w,h    = self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_W],    self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_H] #幅と縦を取得
                        colkey = self.window[i].pad_assign_graph_list[j][LIST_WINDOW_GRAPH_COLKEY] #透明色取得
                        open_rate_x = self.window[i].width / self.window[i].open_width   #開閉率(横軸)
                        open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                        pyxel.blt(self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,imgb,u,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #グラフイック表示
                
                #今カーソルが指し示しているアイテムの説明文の表示
                if      self.window[i].window_status == WINDOW_WRITE_MESSAGE\
                    or  self.window[i].window_status == WINDOW_CLOSE\
                    or  self.window[i].window_status == WINDOW_MOVE\
                    or  self.window[i].window_status == WINDOW_OPEN_COMPLETED:
                    if self.window[i].comment_flag == COMMENT_FLAG_ON: #説明文コメントを表示するフラグが立っているのならば・・・
                        cx = self.cursor_item_x
                        cy = self.cursor_item_y
                        if self.window[i].comment_disp_flag[cy][cx] == DISP_ON: #カーソルの位置からそのアイテムの個々の表示フラグを見て表示する指示が立ってたら説明文を表示する
                            if self.language == LANGUAGE_ENG: #選択言語が英語の場合
                                co_x = self.window[i].comment_ox_eng + self.window[i].posx
                                co_y = self.window[i].comment_oy_eng + self.window[i].posy
                                co_str = self.window[i].comment_list_eng[cy][cx]
                                func.drop_shadow_text(self,co_x,co_y,co_str,7)
                            else:                            #日本語の場合
                                co_x = self.window[i].comment_ox_jpn + self.window[i].posx
                                co_y = self.window[i].comment_oy_jpn + self.window[i].posy
                                co_str = self.window[i].comment_list_jpn[cy][cx]
                                func.drop_shadow_kanji_text(self,co_x,co_y,co_str,7)
                
                #時間やカウンター類の表示
                if self.window[i].time_counter_list != []: #タイム＆カウンター群リストが空でないのならば表示を始める
                    open_rate_x = self.window[i].width / self.window[i].open_width   #開閉率(横軸)
                    open_rate_y = self.window[i].height / self.window[i].open_height #開閉率(縦軸)
                    for j in range(len(self.window[i].time_counter_list)): #time_counter_listの長さの分ループ処理する
                        ox,oy = self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_OX],self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_OY]#表示オフセット座標取得
                        col   = self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_COLOR]#描画色取得
                        if self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_TYPE] == TIME_COUNTER_TYPE_TOTAL_PLAYTIME:           #総プレイ時間の表示(秒まで表示します)
                            func.disp_total_game_playtime(self,self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,col)
                        elif self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_TYPE] == TIME_COUNTER_TYPE_NUMBER_OF_PLAY:         #プレイした回数の表示
                            str_number_of_play = "{:>7}".format(int(self.number_of_play))
                            func.drop_shadow_text(self,self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,str_number_of_play,col)
                        elif self.window[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_TYPE] == TIME_COUNTER_TYPE_TOTAL_SCORE:         #累計スコアの表示
                            str_total_score = "{:>16}".format(int(self.total_score))
                            func.drop_shadow_text(self,self.window[i].posx + ox * open_rate_x,self.window[i].posy + oy * open_rate_y,str_total_score,col)
                
                # #スクロールするテキストの表示
                # if self.window[i].scroll_text  != "": #スクロールテキストリストが空でないのならば表示を始める
                #     all_line_num = len(self.window[i].scroll_text)         #スクロールする文章の全体の行数を求める
                #     all_text_size = all_line_num * self.window[i].between_line #スクロールするテキストの全体の画像ドット数(縦幅)を求める
                #     for j in range (all_line_num):
                #         disp_text = self.window[i].scroll_text[j][0]
                #         dis_x = self.window[i].posx + self.window[i].text_disp_x
                #         dis_y = self.window[i].posy + self.window[i].between_line * j - self.window[i].text_disp_scrolled_dot + self.window[i].text_disp_y
                        
                #         #アライメントオフセット値の計算
                #         if   self.window[i].scroll_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_CENTER:     #中央表示
                #             dis_offset_x = self.window[i].width // 2 - len(disp_text) * 2 + 5
                #         elif self.window[i].scroll_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_LEFT_ALIGN: #左詰め
                #             dis_offset_x = 0
                #         elif self.window[i].scroll_text[j][LIST_WINDOW_TEXT_ALIGN] == DISP_RIGHT_ALIGN:#右詰め
                #             dis_offset_x = -(len(disp_text)  * 8)
                #         else:
                #             dis_offset_x = 0
                        
                #         if 40 <=  dis_y <= 90:
                #             if abs(dis_y -   85) <= 6:
                #                 func.drop_shadow_text(self,dis_x + dis_offset_x,dis_y,disp_text,7)
                #             elif abs(dis_y - 85) <= 8:
                #                 func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,6)
                #             elif abs(dis_y - 85) <= 17:
                #                 func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,12)
                #             elif abs(dis_y - 85) <= 30:
                #                 func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,5)
                #             else:
                #                 func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,1)
                
            #下地が透明または半透明の場合＆「黒矩形塗りつぶし」した後表示の場合は黒く塗りつぶされたウィンドウを描く
            elif self.window[i].window_bg != WINDOW_BG_BLUE_BACK and draw_num == BLACK_RECTANGLE_FILL:
                pyxel.rect(self.window[i].posx,self.window[i].posy,self.window[i].width + 9,self.window[i].height + 9,pyxel.COLOR_BLACK)

    #セレクトカーソルの表示
    def draw_select_cursor(self):
        """
        セレクトカーソルの表示
        """
        if   self.cursor_type == CURSOR_TYPE_NORMAL:    #セレクトカーソルを表示するかどうかのフラグが建っていたらカーソルを表示する
            pyxel.blt(self.cursor_x, self.cursor_y,     IMG2,    184 + (((pyxel.frame_count // 2.5 ) % 9) * 8),96,      8,8,    pyxel.COLOR_BLACK)
        elif self.cursor_type == CURSOR_TYPE_UNDER_BAR: #アンダーバータイプのカーソルの表示
            pyxel.text(self.cursor_x, self.cursor_y,"_", int(self.rainbow_flash_color[pyxel.frame_count // 8 % 10]))
        elif self.cursor_type == CURSOR_TYPE_BOX_FLASH: #点滅囲み矩形タイプカーソルの表示
            if self.cursor_size == CURSOR_SIZE_NORMAL: #通常サイズ
                pyxel.rectb(self.cursor_x,self.cursor_y, 10,10, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
            elif self.cursor_size == CURSOR_SIZE_RIGHT2_EXPAND: #右に2キャラ分拡張サイズ
                pyxel.rectb(self.cursor_x   ,self.cursor_y, 30,10, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
            elif self.cursor_size == CURSOR_SIZE_LEFT1_RIGHT1_EXPAND: #左右に1キャラ分拡張サイズ
                pyxel.rectb(self.cursor_x-10,self.cursor_y, 30,10, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
            elif self.cursor_size == CURSOR_SIZE_LEFT2_EXPAND: #左に2キャラ分拡張サイズ
                pyxel.rectb(self.cursor_x-20,self.cursor_y, 30,10, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画

    #ゲームオーバーダイアログを表示する
    def draw_gameover_dialog(self):
        """
        ゲームオーバーダイアログを表示する
        """
        pyxel.blt(47, 48, IMG2, 0,72, 64,8, pyxel.COLOR_BLACK)

    #フェードイン＆フェードアウト用のエフェクトスクリーン用描画関数(未使用)
    def draw_fade_in_out_screen(self):
        """
        フェードイン＆フェードアウト用のエフェクトスクリーン用描画関数(未使用)
        """
        for lx in range(self.fade_in_out_counter):
            for ly in range(15): #y軸は15キャラ分なので15回繰り返す
                pyxel.blt(self.fade_in_out_counter // 8 * 8  - lx*8 -8,ly*8,   IMG2,   self.fade_in_out_counter // 8 * 4,248,   8,8,   pyxel.COLOR_GRAY)
        
        if self.fade_in_out_counter > 160 * 3 + 8 * 3:
                self.fade_complete_flag = FLAG_ON #右端まで描画したら完了フラグを立てる
        else:
            self.fade_in_out_counter += 3 #開始x軸（キャラ単位）を1増やして右の列に移る
        return()

    #縦フェードイン用のエフェクトスクリーン描画関数
    def draw_vertical_fade_in_screen(self):
        """
        縦フェードイン用のエフェクトスクリーン描画
        """
        for ly in range(self.fade_in_out_counter):
            for lx in range(20):#x軸は20キャラ分なので20回繰り返す
                pyxel.blt(lx*8,self.fade_in_out_counter // 8  - ly*8,   IMG2,   self.fade_in_out_counter // 8,248,   8,8,   pyxel.COLOR_GRAY)
        
        if self.fade_in_out_counter > 120 * 16:
                self.fade_complete_flag = FLAG_ON #下端まで描画したら完了フラグを立てる
        else:
            self.fade_in_out_counter += 16 #開始y軸（キャラ単位）を1増やして下の行に移る
        return()

    #シャドウイン用のエフェクトスクリーン用描画関数
    def draw_shadow_in_screen(self,shadow_width,col):
        """
        シャドウイン用のエフェクトスクリーン用描画
        """
        for lx in range(self.shadow_in_out_counter):
            pyxel.rect(0,          0,           lx,WINDOW_H,    col)#左側の長方形描画
            pyxel.rect(WINDOW_W-lx,0,           lx,WINDOW_H,    col)#右側の長方形描画
        if self.shadow_in_out_counter == (WINDOW_W - shadow_width) // 2:
                self.shadow_in_out_complete_flag = 1 #右端まで描画したら完了フラグを立てる
        else:
            if (pyxel.frame_count % 2) == 0:
                self.shadow_in_out_counter += 1 #カウンタを1増やす
        return()

    #シャドウアウト用のエフェクトスクリーン用描画関数
    def draw_shadow_out_screen(self,shadow_width,col):
        """
        シャドウアウト用のエフェクトスクリーン用描画
        """
        pyxel.rect(              - self.shadow_in_out_counter,0,           WINDOW_W // 2,WINDOW_H,    col)#左側の長方形描画
        pyxel.rect(WINDOW_W // 2 + self.shadow_in_out_counter,0,           WINDOW_W // 2,WINDOW_H,    col)#右側の長方形描画
        if self.shadow_in_out_counter == shadow_width:
                self.shadow_in_out_complete_flag = 1 #右端まで描画したら完了フラグを立てる
        else:
            if (pyxel.frame_count % 2) == 0:
                self.shadow_in_out_counter += 1 #カウンタを1増やす
        return()

    #ビジュアルシーンの表示
    def draw_visualscene(self,priority): #priorityの数値と一致するプライオリティナンバーを持つビジュアルシーンだけを描画します
        """
        ビジュアルシーンの表示
        
        priorityの数値と一致するプライオリティナンバーを持つビジュアルシーンだけを描画します
        """
        visualscene_count = len(self.visualscene)
        for i in range(visualscene_count):
                #ベクターグラフイックスの表示
                if self.visualscene[i].vector_grp != "": #ベクターグラフイック表示を行うリストが空でないのならば表示を始める
                    for j in range(len(self.visualscene[i].vector_grp)): #vector_grpの長さの分ループ処理する
                        open_rate_x = self.visualscene[i].width  / self.visualscene[i].open_width  #開閉率(横軸)
                        open_rate_y = self.visualscene[i].height / self.visualscene[i].open_height #開閉率(縦軸)
                        if   self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_LINE:    #LINE命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #始点座標の取得
                            x2,y2  = self.visualscene[i].vector_grp[j][3],self.visualscene[i].vector_grp[j][4] #終点座標の取得
                            colkey = self.visualscene[i].vector_grp[j][5] #描画色の取得
                            pyxel.line(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,self.visualscene[i].posx + x2 * open_rate_x,self.visualscene[i].posy + y2 * open_rate_y,colkey) #ライン描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_PSET:    #PSET命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #座標の取得
                            colkey = self.visualscene[i].vector_grp[j][3] #描画色の取得
                            pyxel.pset(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,colkey) #点描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_BOX:     #BOX命令
                            x,y           = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #座標の取得
                            width,height  = self.visualscene[i].vector_grp[j][3],self.visualscene[i].vector_grp[j][4] #横幅縦幅の取得
                            colkey = self.visualscene[i].vector_grp[j][5] #描画色の取得
                            pyxel.rectb(self.visualscene[i].posx + x * open_rate_x,self.visualscene[i].posy + y * open_rate_y,width * open_rate_x,height * open_rate_y,colkey) #矩形描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_BOXF:    #BOXFILL命令
                            x,y           = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #座標の取得
                            width,height  = self.visualscene[i].vector_grp[j][3],self.visualscene[i].vector_grp[j][4] #横幅縦幅の取得
                            colkey = self.visualscene[i].vector_grp[j][5] #描画色の取得
                            pyxel.rect(self.visualscene[i].posx + x * open_rate_x,self.visualscene[i].posy + y * open_rate_y,width * open_rate_x,height * open_rate_y,colkey) #矩形描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_CIRCLE:  #CIRCLE命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #中心座標の取得
                            r      = self.visualscene[i].vector_grp[j][3]                                 #半径の取得
                            colkey = self.visualscene[i].vector_grp[j][4]                                 #描画色の取得
                            pyxel.circb(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,r * open_rate_x * open_rate_y,colkey) #円描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_CIRCLEF: #CIRCLEF命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #中心座標の取得
                            r      = self.visualscene[i].vector_grp[j][3]                                 #半径の取得
                            colkey = self.visualscene[i].vector_grp[j][4]                                 #描画色の取得
                            pyxel.circ(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,r * open_rate_x * open_rate_y,colkey) #塗りつぶし円描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_TRI:     #TRIANGLE命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #座標1の取得
                            x2,y2  = self.visualscene[i].vector_grp[j][3],self.visualscene[i].vector_grp[j][4] #座標2の取得
                            x3,y3  = self.visualscene[i].vector_grp[j][5],self.visualscene[i].vector_grp[j][6] #座標3の取得
                            colkey = self.visualscene[i].vector_grp[j][7] #描画色の取得
                            pyxel.trib(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,self.visualscene[i].posx + x2 * open_rate_x,self.visualscene[i].posy + y2 * open_rate_y,self.visualscene[i].posx + x3 * open_rate_x,self.visualscene[i].posy + y3 * open_rate_y,colkey) #三角形描画
                        elif self.visualscene[i].vector_grp[j][0] == LIST_VISUALSCENE_VECTOR_GRP_TRIF:    #TRIANGLE FILL命令
                            x1,y1  = self.visualscene[i].vector_grp[j][1],self.visualscene[i].vector_grp[j][2] #座標1の取得
                            x2,y2  = self.visualscene[i].vector_grp[j][3],self.visualscene[i].vector_grp[j][4] #座標2の取得
                            x3,y3  = self.visualscene[i].vector_grp[j][5],self.visualscene[i].vector_grp[j][6] #座標3の取得
                            colkey = self.visualscene[i].vector_grp[j][7] #描画色の取得
                            pyxel.tri(self.visualscene[i].posx + x1 * open_rate_x,self.visualscene[i].posy + y1 * open_rate_y,self.visualscene[i].posx + x2 * open_rate_x,self.visualscene[i].posy + y2 * open_rate_y,self.visualscene[i].posx + x3 * open_rate_x,self.visualscene[i].posy + y3 * open_rate_y,colkey) #塗りつぶし三角形描画
                
                #グラフイックキャラ,グラフイックパターン,画像の表示などなど
                if self.visualscene[i].grp != "": #ビジュアルシーングラフイック表示を行うリストが空でないのならば表示を始める
                    for j in range(len(self.visualscene[i].grp)): #grの長さの分ループ処理する
                        ox,oy       = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_OX],self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_OY]#表示オフセット座標取得
                        imgb        = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_IMGB]#参照イメージバンク値取得
                        u,v         = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_U],self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_V]#グラフイックデーター収納座標取得
                        w,h         = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_W],self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_H]#幅と縦を取得
                        colkey      = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_COLKEY]#透明色取得
                        ani_num     = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_ANIME_FRAME_NUM]#アニメーション枚数取得
                        ani_speed   = self.visualscene[i].grp[j][LIST_VISUALSCENE_GRAPH_ANIME_SPEED]#アニメーションスピード取得
                        u_offset    = (pyxel.frame_count // ani_speed % ani_num) * w #アニメ枚数とアニメスピード、描画幅から参照すべきグラフイックデーター収納座標のオフセット値を求める
                        open_rate_x = self.visualscene[i].width  / self.visualscene[i].open_width  #開閉率(横軸)
                        open_rate_y = self.visualscene[i].height / self.visualscene[i].open_height #開閉率(縦軸)
                        pyxel.blt(self.visualscene[i].posx + ox * open_rate_x,self.visualscene[i].posy + oy * open_rate_y,imgb,u + u_offset,v,int(w * open_rate_x),int(h * open_rate_y),colkey) #グラフイック表示
                
                #スクロールするテキストの表示(言語が英語の時に字幕フラグが立っていたら日本語の字幕も表示する)
                if   self.visualscene[i].scroll_text  != "" and self.language == LANGUAGE_ENG: #スクロールテキストリストが空でない&選択言語が英語ならば表示を始める
                    all_line_num = len(self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG])         #スクロールする文章の全体の行数を求める
                    between_line = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_BETWEEN_LINE_ENG] #テキストの行間ドット数を求める
                    for j in range (all_line_num):
                        disp_text = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG][j][LIST_VS_TEXT] #このあたりの添え字の指定が判りにくいのう・・・多次元配列が判らん・・・こまめにprint命令でコンソール出力して確認していくしかないわめ！
                        dis_x = self.visualscene[i].posx
                        dis_y = self.visualscene[i].posy + between_line * j - self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG]
                        # dis_y = self.visualscene[i].posy
                        # print (" ")
                        # print ("disp visuaulscene text")
                        # print(disp_text)
                        # print (" ")
                        #アライメントオフセット値の計算
                        if   self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG][j][LIST_VS_TEXT_ALIGN] == DISP_CENTER:      #中央表示
                            dis_offset_x = self.visualscene[i].open_width // 2 - len(disp_text) * 2
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG][j][LIST_VS_TEXT_ALIGN] == DISP_LEFT_ALIGN:  #左詰め
                            dis_offset_x = 0
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG][j][LIST_VS_TEXT_ALIGN] == DISP_RIGHT_ALIGN: #右詰め
                            dis_offset_x = self.visualscene[i].open_width      - len(disp_text) * 4
                        else:
                            dis_offset_x = 0
                        
                        if 40 <=  dis_y <= 90:
                            if abs(dis_y -   85) <= 6:
                                func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,7)
                            elif abs(dis_y - 85) <= 8:
                                func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,6)
                            elif abs(dis_y - 85) <= 17:
                                func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,12)
                            elif abs(dis_y - 85) <= 30:
                                func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,5)
                            else:
                                func.drop_shadow_text(self,dis_x + dis_offset_x ,dis_y,disp_text,1)
                    
                    #字幕表示フラグが立っていたら日本語字幕の表示を行う\
                    if self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_FLAG] ==  SUBTITLES_ON: 
                        subtitle_index = int(self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_COUNT1] // 7) #字幕表示用のカウンタを8で割った数値(切り捨て)が字幕データのインデックス値となる
                        subtitle_text  = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_SUBTITLES_JPN][subtitle_index][LIST_VS_TEXT] #このあたりの添え字の指定が判りにくいのう・・・多次元配列が判らん・・・こまめにprint命令でコンソール出力して確認していくしかないわめ！
                        dis_x = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_X]
                        dis_y = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_Y]
                        
                        #アライメントオフセット値の計算
                        if   self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_SUBTITLES_JPN][subtitle_index][LIST_VS_TEXT_ALIGN] == DISP_CENTER:      #中央表示
                            dis_offset_x = self.visualscene[i].open_width // 2 - len(subtitle_text) // 2 * 7
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_SUBTITLES_JPN][subtitle_index][LIST_VS_TEXT_ALIGN] == DISP_LEFT_ALIGN:  #左詰め
                            dis_offset_x = 0
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_SUBTITLES_JPN][subtitle_index][LIST_VS_TEXT_ALIGN] == DISP_RIGHT_ALIGN: #右詰め
                            dis_offset_x = self.visualscene[i].open_width      - len(subtitle_text) * 4
                        else:
                            dis_offset_x = 0
                        
                        print(subtitle_text)
                        func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,subtitle_text,7) #日本語字幕の表示
                    
                elif self.visualscene[i].scroll_text  != "" and self.language == LANGUAGE_JPN: #スクロールテキストリストが空でない&選択言語が日本語ならば表示を始める
                    all_line_num = len(self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN])         #スクロールする文章の全体の行数を求める
                    between_line = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_BETWEEN_LINE_JPN] #テキストの行間ドット数を求める
                    for j in range (all_line_num):
                        disp_text = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN][j][LIST_VS_TEXT] #このあたりの添え字の指定が判りにくいのう・・・多次元配列が判らん・・・こまめにprint命令でコンソール出力して確認していくしかないわめ！
                        dis_x = self.visualscene[i].posx
                        dis_y = self.visualscene[i].posy + between_line * j - self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_JPN]
                        # dis_y = self.visualscene[i].posy
                        # print (" ")
                        # print ("disp visuaulscene text")
                        # print(disp_text)
                        # print (" ")
                        #アライメントオフセット値の計算
                        if   self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN][j][LIST_VS_TEXT_ALIGN] == DISP_CENTER:      #中央表示
                            dis_offset_x = int((self.visualscene[i].open_width - (len(disp_text)* 8)) // 2) 
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN][j][LIST_VS_TEXT_ALIGN] == DISP_LEFT_ALIGN:  #左詰め
                            dis_offset_x = 0
                        elif self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN][j][LIST_VS_TEXT_ALIGN] == DISP_RIGHT_ALIGN: #右詰め
                            dis_offset_x = int(self.visualscene[i].open_width      - len(disp_text) * 8)
                        else:
                            dis_offset_x = 0
                        
                        if 40 <=  dis_y <= 90:
                            if abs(dis_y -   85) <= 6:
                                func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,disp_text,7)
                            elif abs(dis_y - 85) <= 8:
                                func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,disp_text,6)
                            elif abs(dis_y - 85) <= 17:
                                func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,disp_text,12)
                            elif abs(dis_y - 85) <= 30:
                                func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,disp_text,5)
                            else:
                                func.drop_shadow_kanji_text(self,dis_x + dis_offset_x ,dis_y,disp_text,1)
                
                self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_BETWEEN_LINE_JPN] #テキストの行間ドット数を求める