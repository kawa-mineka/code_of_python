###########################################################
#  update_objクラス                                       #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主に背景オブジェクトの更新を行う関数(メソッド？）ですよ～♪  #
# 2022 04/03からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random
from cv2 import dft    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

class update_obj:
    def __init__(self):
        None

    #背景の星の追加（発生＆育成）
    def append_star(self):
        if (pyxel.frame_count % 3) == 0:
            if len(self.stars) < 600:
                new_stars = Star()
                new_stars.update(WINDOW_W + 1,func.s_rndint(self,0,WINDOW_H),func.s_rndint(self,1,50))
                # new_stars.update(WINDOW_W + 1,randint(0,WINDOW_H),randint(1,50))
                self.stars.append(new_stars)

    #背景の星の更新（移動）
    def star(self):
        stars_count = len(self.stars)
        for i in reversed(range (stars_count)):
            if 0 < self.stars[i].posx and self.stars[i].posx < WINDOW_W + 2:#背景の星が画面内に存在するのか判定
            #背景の星の位置を更新する
                self.stars[i].posx -= (self.stars[i].speed) / 12 * self.star_scroll_speed #左方向にspeedを１２で割った切り捨てドット分（star_scroll_speedは倍率です）星が左に流れます
            else:
                del self.stars[i]#背景の星が画面外に存在するときはインスタンスを破棄する （流れ星消滅）

    #パーティクルの追加（発生＆育成）
    def append_particle(self,particle_type,x,y,dx,dy,life,wait,color):
        if len(self.particle) < 1000: #パーティクルの総数が1000以下なら追加発生させる
            if particle_type == PARTICLE_DOT or particle_type == PARTICLE_CIRCLE: #ドットパーティクル 円形パーティクルの追加
                new_particle = Particle()
                new_particle.update(particle_type, x+4,y+4,    func.s_rndint(self,0,1),    random() * 2 - 0.5 + dx,    random() * 2 - 1 + dy,   func.s_rndint(self,5,20), 0,  func.s_rndint(self,1,14))
                self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_LINE: #ラインパーティクル（線状の尾を引くようなパーティクルです）
                for i in range(10):
                    new_particle = Particle()
                    new_particle.update(particle_type, x-2,y+4,    1,    -0.8-random(), random()-0.2,    10,   i, 6)
                    self.particle.append(new_particle)
                    
                    #ボスにダメージを与えたとき
                    #new_particle = Particle()
                    #new_particle.update(particle_type, x-4,y+4,    1,    -0.8-random(), random()-0.2,    30,   i, 8)
                    #self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_MISSILE_DEBRIS: #ミサイルの破片の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    0,0,   7,   0,0)
                self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_BOSS_DEBRIS1: #ボスの破片1の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS2: #ボスの破片2の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS3: #ボスの破片3の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS4: #ボスの破片4の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS5: #ボスの破片5の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS6: #ボスの破片6の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)

    #パーティクルの更新
    def particle(self):
        particlecount = len(self.particle)
        for i in reversed(range(particlecount)):#パーティクルのリストの要素数を数えてその数の分だけループ処理する（delしちゃう可能性があるのでreversedするよ）
            if self.particle[i].wait == 0: #ウェイトカウンターが0になったら位置を更新（移動する）
                self.particle[i].posx += self.particle[i].vx #パーティクルの座標x,yを速度ベクトルvx,vyで位置更新する
                self.particle[i].posy += self.particle[i].vy
            else: #ウェイトカウンターがまだ残っていたのなら１減らし、移動（更新）はしないでその場に留まらせておく
                self.particle[i].wait -= 1
            
            if  self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS1:#ボスの破片の時は
                self.particle[i].vy += 0.009 #y軸下方向に徐々に加速して落ちていくようにする
            elif self.particle[i].particle_type == PARTICLE_LINE: #パーティクルタイプ ラインタイプ
                if   self.particle[i].life < 6:  #lifeが減るごとにcolorを6→12→5→1と変化させる
                    self.particle[i].color = 12
                elif self.particle[i].life < 5:
                    self.particle[i].color = 5
                elif self.particle[i].life < 4:
                    self.particle[i].color = 1
            elif self.particle[i].particle_type == PARTICLE_FIRE_SPARK: #パーティクルタイプ 大気圏突入時の火花タイプ
                if   self.particle[i].life > 14:  #lifeが減るごとにcolorを10→9→8→2→1と変化させる
                    self.particle[i].color = 10
                elif self.particle[i].life > 11:
                    self.particle[i].color = 9
                elif self.particle[i].life > 9:
                    self.particle[i].color = 8
                elif self.particle[i].life > 7:
                    self.particle[i].color = 2
                elif self.particle[i].life > 4:
                    self.particle[i].color = 1
            
            if self.particle[i].life < 10: #パーティクルの体力？生命力が10より小さい場合は
                self.particle[i].size = 0 #強制的にサイズを0にして、小さくさせる
                
            self.particle[i].life -= 1 #パーティクルの体力（生命力？）を１減少させる
            if self.particle[i].life <= 0: #パーティクルの体力が0以下になったら
                del self.particle[i] #パーティクルは消えちゃうのです・・・はかない命・・まるで火花・・・

    #背景オブジェクトの更新
    def background_object(self):
        object_count = len(self.background_object)
        for i in reversed(range(object_count)):#背景オブジェクトのリストの要素数を数えてその数の分だけループ処理する（delしちゃう可能性があるのでreversedするよ）
            
            
            if BG_OBJ_CLOUD1 <= self.background_object[i].background_object_type <= BG_OBJ_CLOUD21: #雲1~21の場合
                self.background_object[i].posx += self.background_object[i].vx
                self.background_object[i].posy += self.background_object[i].vy
                
            self.background_object[i].vx = self.background_object[i].vx * self.background_object[i].ax #速度に加速度を掛けあわせて加速もしくは減速させていく
            self.background_object[i].vy = self.background_object[i].vy * self.background_object[i].ay
            
            #オブジェクトのクリッピング処理
            if       -100 <= self.background_object[i].posx <= WINDOW_W + 100\
                and  -100 <= self.background_object[i].posx <= WINDOW_H + 100:
                continue
            else:
                del self.background_object[i] #描画範囲外になったのでインスタンスを破棄する

    #雲の追加(背景オブジェクト)
    def append_cloud(self):
        if (pyxel.frame_count % self.cloud_append_interval) == 0 and self.display_cloud_flag == DISP_ON: #表示インタバールが0になった&表示フラグがonだったのなら
            if self.cloud_quantity == 0: #雲の量が0の時は「雲小」のみ表示する
                t = func.s_rndint(self,BG_OBJ_CLOUD1,BG_OBJ_CLOUD10)
            elif self.cloud_quantity == 1: #雲の量が1の時は「雲小～中」まで表示する
                t = func.s_rndint(self,BG_OBJ_CLOUD1,BG_OBJ_CLOUD18)
            elif self.cloud_quantity == 2: #雲の量が2の時は「雲小～中～大」まで表示する
                t = func.s_rndint(self,BG_OBJ_CLOUD1,BG_OBJ_CLOUD21)
            
            y = func.s_rndint(self,0,120+30)
            new_background_object = Background_object()
            new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3*self.cloud_flow_speed,self.cloud_how_flow,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
            self.background_object.append(new_background_object)

    #タイマーフレアの更新(接触した物質の時間経過を遅くするフレアエフェクト)
    def timer_flare(self):
        if self.timer_flare_flag == 0: #タイマーフレアのフラグが建っていなかったらそのまま戻る
            return
            
        for i in range(30):
            new_particle = Particle()
            new_particle.update(PARTICLE_LINE, self.my_x+3,self.my_y+3,    1,    -random()-0.5, random()-0.5,    80,   i*6, 6)
            self.particle.append(new_particle)

    #大気圏突入時の火花の更新
    def atmospheric_entry_spark(self):
        if self.atmospheric_entry_spark_flag == SPARK_OFF: #大気圏突入時の火花のフラグが建っていなかったらそのまま戻る
            return
            
        for _i in range(10):
            new_particle = Particle()
            # new_particle.update(PARTICLE_DOT, self.my_x+1,self.my_y+5,    1,    -random() * self.side_scroll_speed * 4, (random() - 0.97) * self.vertical_scroll_speed * 8,    30,   _i // 2, 10)
            new_particle.update(PARTICLE_FIRE_SPARK, self.my_x+3,self.my_y+4,    1,    -random() * self.side_scroll_speed, -(random()+0.5)  * self.vertical_scroll_speed * 2,    2.5 * self.side_scroll_speed,   1, 10)
            
            self.particle.append(new_particle)

    #ラスタースクロールの更新
    def raster_scroll(self):
        if self.raster_scroll_flag == 0: #ラスタスクロール更新＆表示のフラグがたっていなかったらそのまま何もしないで戻る
            return
            
        raster_scroll_count = len(self.raster_scroll)
        for i in range(raster_scroll_count):#ラスタースクロールのリストの要素数を数えてその数の分だけループ処理する
            if self.raster_scroll[i].raster_type == RASTER_NORMAL: #通常のラスタースクロールの場合
                #x座標をラスタースクロールのspeedと背景の横軸スクロールspeedを掛け合わせた分だけ加減算して更新
                self.raster_scroll[i].posx += self.raster_scroll[i].speed * self.side_scroll_speed
                #y座標は現在の垂直スクロールカウント+y軸オフセット値+上から何番目のラインかを示す数値を直接指定代入する
                self.raster_scroll[i].posy = (184 - self.vertical_scroll_count // 16) + self.raster_scroll[i].scroll_line_no + self.raster_scroll[i].offset_y
                #  self.raster_scroll[i].posy = self.raster_scroll[i].offset_y + self.raster_scroll[i].scroll_line_no
                
                if self.raster_scroll[i].posx <= -self.raster_scroll[i].width: #描画ライン幅のドット数ぶん画面外までスクロールアウトしたのなら
                    self.raster_scroll[i].posx = 0 #初期値であるx座標0を代入する
                    
            elif self.raster_scroll[i].raster_type == RASTER_WAVE: #ウェーブラスタースクロールの場合
                #x座標をラスタースクロールのspeedと背景の横軸スクロールspeedを掛け合わせた分だけ加減算して更新する
                self.raster_scroll[i].posx += self.raster_scroll[i].speed *self.side_scroll_speed
                
                #y座標は現在の垂直スクロールカウント+y軸オフセット値+上から何番目のラインかを示す数値を直接指定代入する
                self.raster_scroll[i].posy = (184 - self.vertical_scroll_count // 16) + self.raster_scroll[i].scroll_line_no + self.raster_scroll[i].offset_y
                
                #ウェーブラスターで波打ってずれる分のoffset_xを計算してやる
                self.raster_scroll[i].wave_timer += self.raster_scroll[i].wave_speed #timer += speed
                self.raster_scroll[i].offset_x = self.raster_scroll[i].wave_intensity * math.sin(self.raster_scroll[i].wave_timer) # offset_x = intensity * sin(timer)
                
                if self.raster_scroll[i].posx <= -self.raster_scroll[i].width: #描画ライン幅のドット数ぶん画面外までスクロールアウトしたのなら
                    self.raster_scroll[i].posx = 0 #初期値であるx座標0を代入する

    #爆発パターンの更新→撃ち返し弾の発生
    def explosion(self):
        explosioncount = len(self.explosions)
        for i in reversed(range(explosioncount)):
            #爆発パターンを背景スクロールに合わせて移動させる
            self.explosions[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で爆発してるように見せるため）         
            self.explosions[i].explosion_count -= 1#爆発育成時に設定したカウントを1減らす
            fire_rnd = func.s_rndint(self,0,100)
            if    self.explosions[i].explosion_count == 9\
                and self.stage_loop * ALL_STAGE_NUMBER + self.stage_number >= self.return_bullet_start_loop * ALL_STAGE_NUMBER + self.return_bullet_start_stage\
                and fire_rnd <= self.return_bullet_probability: 
                #カウント9の時&return_bullet_probabilityパーセントの確率&現在のループ数とステージ数がstart_loop,start_stageの数値以上ならば撃ち返し弾を出す
                if     self.explosions[i].return_bullet_type == RETURN_BULLET_AIM\
                    or self.explosions[i].return_bullet_type == RETURN_BULLET_DELAY_AIM:
                    #自機狙い弾を1発うちかえす
                    func.enemy_aim_bullet(self,self.explosions[i].posx,self.explosions[i].posy,0,0,0,0,1)#自機狙いの撃ち返し弾発射！
                elif    self.explosions[i].return_bullet_type == RETURN_BULLET_3WAY:
                    #自機狙いの3way弾の場合は.....
                    ex = self.explosions[i].posx
                    ey = self.explosions[i].posy
                    theta = 30
                    n = 3
                    division_type = 0
                    division_count = 0
                    division_num = 0
                    stop_count = 0
                    func.enemy_aim_bullet_nway(self,ex,ey,theta,n,division_type,division_count,division_num,stop_count)
                
                if    self.explosions[i].return_bullet_type == RETURN_BULLET_DELAY_AIM:
                    #ディレイをかけた打ち返し弾を発射(ちょっと加速気味)
                    func.enemy_aim_bullet(self,self.explosions[i].posx,self.explosions[i].posy,0,0,0,10,1.01)#その場でちょっと止まって自機狙いの撃ち返し弾発射！
                
            if self.explosions[i].explosion_type == EXPLOSION_MIDDLE: #中間サイズの爆発パターンの場合は
                #1フレームごとに通常爆発パターンを追加発生させる
                new_explosion = Explosion()
                new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.explosions[i].posx + 4 + func.s_rndint(self,0,24)-12,self.explosions[i].posy + 4 + func.s_rndint(self,0,12)-6,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                self.explosions.append(new_explosion)
                
            if self.explosions[i].explosion_count == 0: #カウントが0の時は....
                del self.explosions[i] #爆発リストをDELしちゃう（お前・・消えるのか・・・？）

    #最前面(FRONT)のBGチップナンバー書き換えによる背景アニメーション(bg_rewrite_animation関数から呼び出されます)
    def front_bg_rewrite_animation(self):
        #最前面のBG書き換えアニメーション
        for w in range(WINDOW_W // 8):#横方向の調べ上げ数は 160割る8で20キャラ分調べ上げる
            for h in range(WINDOW_H // 8 * self.height_screen_num): #縦方向の調べ上げ総数は縦画面数も考慮してself.height_screen_num分掛け合わせたキャラ分だけ調べ上げる
                bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
                for i in range(bg_animation_count): #リストの総数分ループする
                    if self.scroll_type    == SCROLL_TYPE_8WAY_SCROLL_AND_RASTER:  #8方向スクロール+ラスタースクロールの場合は
                        func.get_bg_chip_free_scroll(self,w * 8,h * 8    ,0)       #座標(w,h)のマップチップのBGナンバーを取得してself.bg_chipに代入する関数の呼び出し(8方向フリースクロール専用)
                    elif self.scroll_type  == SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR:  #横3重スクロール+星スクロールの場合は
                        func.get_bg_chip(self,w * 8,h * 8    ,0)                   #座標(w,h)のマップチップのBGナンバーを取得してself.bg_chipに代入する関数の呼び出し
                    bg_ani_x     = self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                    bg_ani_y     = self.bg_animation_list[i][1] #                               y座標を変数に代入
                    bg_ani_speed = self.bg_animation_list[i][4] #                               スピードを変数に代入
                    bg_ani_num   = self.bg_animation_list[i][5] #                               パターン数を変数に代入
                    bg_ani_min   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8)
                    bg_ani_max   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8 + bg_ani_num)
                    if bg_ani_min <= self.bg_chip <= bg_ani_max: #マップチップナンバーがアニメパターンするべき最小値ナンバーから最大値ナンバーの範囲内に入っているのなら
                        #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行います
                        func.write_map_chip_free_scroll(self,self.bgx,self.bgy,bg_ani_min + pyxel.frame_count // bg_ani_speed % bg_ani_num)

    #中面(MIDDLE)の1画面分だけのBGチップを調べて書き換える背景アニメーション(bg_rewrite_animation関数から呼び出されます)
    def middle_bg_rewrite_animation(self):
        #中面(MIDDLE)のBG書き換えアニメーション
        for w in range(WINDOW_W // 8):# x座表は理論的には0~20で行けるはずなんだけど20の時書き換えると微妙に画面右端で書き換えていないのかバレるので +1してます、ハイ！
            for h in range(WINDOW_H // 8): #縦方向は1画面分だけ書き換えます
                bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
                for i in range(bg_animation_count): #リストの総数分ループする
                    bg_ani_speed = self.bg_animation_list[i][4] #アニメスピードを変数に代入
                    if pyxel.frame_count % bg_ani_speed == 0: #総フレームカウント数がbg_ani_speedで割り切れる時だけマップチップを書き換える
                        self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy + h) #座標(bgx+w,bgy+h)のマップチップのBGナンバーを取得する
                        bg_ani_x     = self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                        bg_ani_y     = self.bg_animation_list[i][1] #                               y座標を変数に代入
                        bg_ani_num   = self.bg_animation_list[i][5] #                               パターン数を変数に代入
                        bg_ani_min   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8)
                        bg_ani_max   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8 + bg_ani_num)
                        
                        if bg_ani_min <= self.bg_chip <= bg_ani_max: #マップチップナンバーがーアニメーションするべきチップナンバーの範囲内だったのなら
                            self.bg_chip += 1 #マップチップBGナンバーを+1して右横にある「次に描画するアニメパターンナンバー」にしてやる
                            #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行い,該当するチップナンバーを書き込みます
                            if self.bg_chip >= bg_ani_max: #チップナンバーの範囲を超えていたのなら
                                self.bg_chip = bg_ani_min  #一番最初のアニメパターンBGにする 
                            
                            func.set_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy + h,self.bg_chip) #座標(bgx+w,bgy+h)にBGナンバーbg_chipを書き込む

    #横1ラインだけのBGチップナンバー書き換えにより背景アニメーション(bg_rewrite_animation関数から呼び出されます)
    def one_line_bg_rewrite_animation(self):
        for w in range (WINDOW_W // 8 + 1):# x座表は理論的には0~20で行けるはずなんだけど20の時書き換えると微妙に画面右端で書き換えていないのかバレるので +1してます、ハイ！
            bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
            for i in range(bg_animation_count):
                self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy) #座標(bgx+w,bgy)のマップチップのBGナンバーを取得する
                bg_ani_x     = self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                bg_ani_y     = self.bg_animation_list[i][1] #                         y座標を変数に代入
                bg_ani_speed = self.bg_animation_list[i][4] #                        スピードを変数に代入
                bg_ani_num   = self.bg_animation_list[i][5] #                        パターン数を変数に代入
                bg_ani_min   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8)
                bg_ani_max   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8 + bg_ani_num)
                if bg_ani_min <= self.bg_chip <= bg_ani_max: #マップチップナンバーがーアニメーションするべきチップナンバーの範囲内だったのなら
                    #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行い,該当するチップナンバーを書き込みます
                    func.set_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy, bg_ani_min + pyxel.frame_count // bg_ani_speed % bg_ani_num)

    #横1ラインだけのBGチップナンバー書き換えにより背景アニメーション(bg_rewrite_animation関数から呼び出されます)(同タイミングで書き換えるのではなく1キャラナンバーづつ増加させていくタイプ)(非同期タイプ)
    def one_line_inc_bg_rewrite_animation(self): 
        for w in range (WINDOW_W // 8 + 1):# x座表は理論的には0~20で行けるはずなんだけど20の時書き換えると微妙に画面右端で書き換えていないのかバレるので +1してます、ハイ！
            bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
            for i in range(bg_animation_count):
                bg_ani_speed = self.bg_animation_list[i][4] #                               スピードを変数に代入
                if pyxel.frame_count % bg_ani_speed == 0: #総フレームカウント数がbg_ani_speedで割り切れる時だけマップチップを書き換える
                    self.bg_chip = func.get_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy) #座標(bgx+w,bgy)のマップチップのBGナンバーを取得する
                    bg_ani_x     = self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                    bg_ani_y     = self.bg_animation_list[i][1] #                         y座標を変数に代入
                    bg_ani_num   = self.bg_animation_list[i][5] #                        パターン数を変数に代入
                    bg_ani_min   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8)
                    bg_ani_max   = (bg_ani_y // 8) * 32 + (bg_ani_x // 8 + bg_ani_num)
                    
                    if bg_ani_min <= self.bg_chip <= bg_ani_max: #マップチップナンバーがーアニメーションするべきチップナンバーの範囲内だったのなら
                        self.bg_chip += 1 #マップチップBGナンバーを+1して右横にある「次に描画するアニメパターンナンバー」にしてやる
                        #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行い,該当するチップナンバーを書き込みます
                        if self.bg_chip >= bg_ani_max: #チップナンバーの範囲を超えていたのなら
                            self.bg_chip = bg_ani_min  #一番最初のアニメパターンBGにする 
                        
                        func.set_chrcode_tilemap(self,self.reference_tilemap,self.bgx + w,self.bgy,self.bg_chip)

    #BGマップチップデータ書き換えによる背景アニメーション
    def bg_rewrite_animation(self):
        #今表示したマップに書き換え対象のキャラチップが含まれていたらＢＧデータナンバーを1増やしてアニメーションさせる
        if   self.stage_number == STAGE_MOUNTAIN_REGION:        #1面 MOUNTAIN REGION
            #最前面のＢＧ書き換えアニメーション----------------------------------------
            update_obj.front_bg_rewrite_animation(self)         #最前面のBG書き換えアニメーションを行う関数の呼び出し
            
            #中間の山脈の流れる滝のアニメーション---------------------------------------
            #マップ座標のY=250だけ山脈遠景滝BGアニメーションチップを置くルールにしているのでy座標250だけ目的のマップチップがあるかをサーチして書き換える
            #(参考)drawクラスでの山脈遠景表示のコード pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  1,    0,248,    256,5,    self.bg_transparent_color)
            self.bgx = int(self.scroll_count // 32 % (256 - 20)) #bgxに山脈遠景表示時のBGマップの1番左端のx座標(0~255)が入る
            self.bgy = 250                                       #bgyに入るy座標は250で固定
            func.clip_bgx_bgy(self)                              #bgx,bgyを規格範囲内に修正する
            update_obj.one_line_bg_rewrite_animation(self)       #横1ラインだけのBG書き換えアニメーションを行う関数の呼び出し
            
        elif self.stage_number == STAGE_ADVANCE_BASE:           #2面 ADVANCE_BASE
            #最前面のＢＧ書き換えアニメーション----------------------------------------
            update_obj.front_bg_rewrite_animation(self)         #最前面のBG書き換えアニメーションを行う関数の呼び出し
            
        elif self.stage_number == STAGE_VOLCANIC_BELT:          #3面 VOLCANIC BELT
            #最前面のＢＧ書き換えアニメーション----------------------------------------
            update_obj.front_bg_rewrite_animation(self)           #最前面のBG書き換えアニメーションを行う関数の呼び出し
            
            #奥の火山の噴火アニメーション---------------------------------------------
            #奥の火山のスクロール面の表示はpyxel.bltm(-(self.scroll_count // 16) + 50,0,TM2,  0*8,216*8   ,  256*8, 15*8,0)
            #ステージ開始時のx軸スクロール座標は(self.scroll_count // 16) + 50となり、単位はドットなので
            #(int(self.scroll_count // 16) + 50) // 8 でキャラ単位にしてやる
            self.bgx = (int(self.scroll_count // 16) - 50) // 8   #bgxに奥の火山の噴火部表示を表示した時、BGマップの1番左端のx座標(0~255)が入る
            self.bgy = 216                                        #bgy座標は216から始まって1画面分下方向へ書き換える
            func.clip_bgx_bgy(self)                               #bgx,bgyを規格範囲内に修正する(別に必要ないかも？おまじないとして修正しておくですの)
            update_obj.middle_bg_rewrite_animation(self)          #中面その１(火山噴火アニメ)のBG書き換えアニメーションを行う関数の呼び出し
            
            #ゲートブリッジの誘導灯アニメーション-----------------------------------------
            #ゲートブリッジのスクロール面の表示はpyxel.bltm(-(self.scroll_count // 8) + 100,-self.camera_offset_y // 8,TM2,  0*8,239*8 -2,  256*8,120*8,0)
            #ステージ開始時のx軸スクロール座標は(self.scroll_count // 8) + 100となり、単位はドットなので
            #(int(self.scroll_count // 8) + 100) // 8 でキャラ単位にしてやる
            self.bgx = (int(self.scroll_count // 8) - 100) // 8   #bgxにゲートブリッジを表示した時、BGマップの1番左端のx座標(0~255)が入る
            self.bgy = 240                                        #bgy座標は240から始まって1画面分下方向へ書き換える
            func.clip_bgx_bgy(self)                               #bgx,bgyを規格範囲内に修正する
            update_obj.middle_bg_rewrite_animation(self)          #中面その２(ゲートブリッジの誘導灯アニメ)のBG書き換えアニメーションを行う関数の呼び出し

    #座標直接指定によるBGチップデータの書き換えアニメーション (ダミーでござる)
    def dummy_bg_animation(self):
        for i in range(15):
            func.write_map_chip_free_scroll(self,95,184-i,(64 // 8) * 32 + (144 // 8) + pyxel.frame_count * 3 % 8)
