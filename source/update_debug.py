###########################################################
#  update_debugクラス                                      #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にデバッグモードの更新を行います                        #
#  デバッグ用データ表示項目の切り替え                        #
#  デバッグ用に表示するためのパラメータ数値の更新             #
#                                                         #
# 2022 04/07からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_ship import * #主に自機関連のメソッドです(クローの追加で仕様)
from update_obj  import * #背景オブジェクト更新関数モジュール読み込み(パーティクルの追加で使用)

class update_debug:
    def __init__(self):
        None

    #デバッグモードの更新（キーボードによる表示タイプや表示非表示の切り替え）           KEY CTRL
    def debug_status(self):
        """
        デバッグモードの更新（キーボードによる表示タイプや表示非表示の切り替え）           KEY CTRL
        """
        if pyxel.btnp(pyxel.KEY_CTRL):
            if   self.debug_menu_status == 0:
                self.debug_menu_status = 1
            elif self.debug_menu_status == 1:
                self.debug_menu_status = 2
            elif self.debug_menu_status == 2:
                self.debug_menu_status = 3
            else:
                self.debug_menu_status = 0

    #デバッグモードによるキーボードやパッドでの敵や敵弾の強制追加発生
    def enemy_append(self):
        """
        デバッグモードによるキーボードやパッドでの敵や敵弾の強制追加発生
        """
        #敵タイプ1サーコインの発生  直進して斜め後退→勢いよく後退していく10機編隊      KEY 4 +++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_4) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_LEFTSTICK) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_LEFTSTICK):
                if len(self.enemy) < 400:
                    
                    self.posy = func.s_rndint(self,0,WINDOW_H - 8)
                    for number in range(10):
                        new_enemy = Enemy()
                        new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.posy,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,    0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0 ,    0,0,0,0,   E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)
                    
                    #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
                    func.record_enemy_formation(self,10)
        
        #敵タイプ2サイシーロの発生  サインカーブを描く3機編隊                        KEY 5 ++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_5):
                if len(self.enemy) < 400:
                    self.posy = func.s_rndint(self,0,WINDOW_H)
                    for number in range(3):
                        new_enemy = Enemy()
                        new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 10,((self.posy)-36) + (number * 12),0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,    0,0,0,0,   E_NO_POW,ID00 ,0,0,0    ,0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)        
        
        #敵タイプ6の発生（謎の飛翔体Ｍ54）                                         KEY 6 ++++++
        if (pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_6):
                if len(self.enemy) < 400:
                    self.posy = func.s_rndint(self,0,WINDOW_H)
                    new_enemy = Enemy()
                    new_enemy.update(6,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0, 0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,   0.5,0.05,0,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)        
        
        #敵タイプ8ツインアローの発生 追尾戦闘機                                     KEY Z ++++++
        if (pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_Z):
                if len(self.enemy) < 400:
                    self.posy = func.s_rndint(self,0,WINDOW_H)
                    new_enemy = Enemy()
                    new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0, 0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5,0,  0,    HP01,    0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ9の発生 縦軸合わせ突進タイプ                                       KEY X ++++++
        if (pyxel.frame_count % 16) == 0:
            if pyxel.btn(pyxel.KEY_X):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    80,40,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.5,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,  0, 0,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ10の発生 地面のスクランブルハッチ                                   KEY C +++++
        if (pyxel.frame_count % 64) == 0:
            if pyxel.btn(pyxel.KEY_C):
                if len(self.enemy) < 400:
                    #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）
                    #enemy_count2を射出する敵の総数です（敵総数カウンタ）
                    new_enemy = Enemy()
                    new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    170,96,0,0,    0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_26,   0.5,0,   0,    HP10,    0,0,   E_SIZE_MIDDLE32,  (func.s_rndint(self,0,130) + 10),  6, 20,    0,0,0,0,      E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ12の発生 レイブラスター  レーザービームを出して高速で逃げていく敵     KEY D ++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_RIGHTSHOULDER):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,func.s_rndint(self,0,WINDOW_H),0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   -2,(func.s_rndint(self,0,1)-0.5),       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   80 + func.s_rndint(self,0,40),0,0,     0,0,0,0,      E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ16の発生 2機一体で挟みこみ攻撃をしてくるクランパリオン                KEY T ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_T):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    WINDOW_W,0,0,0,       0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  -1.1,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,     0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    WINDOW_W,WINDOW_H-8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -1.1,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ17の発生 ロールブリッツ あらかじめ決められた場所へスプライン曲線移動   KEY Y ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_Y):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,0,     0,0,0,0,0,0,0,0,         0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,      E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,8,     0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1.05,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,16,    0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,0.95,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ18の発生 ボルダー 硬めの弾バラマキ重爆撃機                          KEY R ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_R):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(VOLDAR,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   170,10,0,0,       0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07,1,   0,    HP30,  0,0,    E_SIZE_HI_MIDDLE53,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,1,0.007,0.6,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵弾1(前方加速弾&落下弾&サインコサイン弾&グリーンカッター)の発生  KEY A ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_A):
                if len(self.enemy_shot) < 800:
                    #前方加速弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -1,0,     1.01,     1,1,    1,0, 0,1,0,                0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    #落下弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_DROP_BULLET,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -0.3,-1.1,     0.02,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    #サイン弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_SIN,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0, -1,0,       1,    1,1,    1,0,  0.06,0.06,0.6,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    #コサイン弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_COS,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0,  -1,0,      1,    1,1,    1,0,  0.06,0.06,0.6,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    #グリーンカッター
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,140,60,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -0.3,0,      1.01,    1,1,    0,0,  0,0,0,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾2(自機狙い6way弾)の発生                                   KEY B ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_B):
                if len(self.enemy_shot) < 800:
                    ex = 80
                    ey = 60
                    theta = 30
                    n = 6
                    division_type = 0
                    division_count = 0
                    division_num = 0
                    stop_count = 0
                    func.enemy_aim_bullet_nway(self,ex,ey,theta,n,division_type,division_count,division_num,stop_count)    
        
        #敵弾3(前方レーザービーム)の発生                               KEY S ----------------
        if(pyxel.frame_count % 1) == 0:
            if pyxel.btn(pyxel.KEY_S):
                if len(self.enemy_shot) < 800:
                    posy = func.s_rndint(self,0,WINDOW_H)
                    for number in range(6):
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,  -2,0,   1,  1,1,   0,0,0,    1,0,0,  0,number * 2,PRIORITY_FRONT,  0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
        
        #敵弾4(ホーミングレーザー)の発生                                KEY F -----------------
        if(pyxel.frame_count % 100) == 0:
            if pyxel.btn(pyxel.KEY_F):
                if len(self.enemy_shot) < 800:
                    posy = 60
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_HOMING_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   0.5,0.5,   1,    1,1,   0,20,0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 8,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾5(サーチレーザー)の発生                                    KEY G ------------------
        if(pyxel.frame_count % 100) == 0:
            if pyxel.btn(pyxel.KEY_G):
                if len(self.enemy_shot) < 800:
                    posx = 100
                    posy = 60
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_SEARCH_LASER,ID00, posx,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   -0.75,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾6(回転弾)の発生                                 KEY H ------------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_H):
                if len(self.enemy_shot) < 800:
                    cx = 100
                    cy = 60
                    radius = 1
                    radius_max = 80
                    radius_incremental = 0.05
                    rotation_omega_incremental = 2
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    cx = 100
                    cy = 60
                    radius = 1
                    radius_max = 80
                    radius_incremental = 0.05
                    rotation_omega_incremental = -2
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾7(分裂弾)の発生                                 KEY J ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_J):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 140,60
                    division_type        = 1   #自機狙いの3way
                    division_count       = 40 #分裂するまでのカウント数
                    division_count_origin = 40 #分裂するまでのカウント数(元数値)
                    division_num        = 10    #分裂する回数(ひ孫まで)
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -2,0,     0.96,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)            
        
        #敵弾8(狙い撃ち分裂弾弾)の発生                        KEY K ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_K):
                ex,ey        = 140,60 #弾発射初期座標
                div_type     = 1 #自機狙いの3way
                div_count    = 40 #分裂するまでのカウント数
                div_num      = 2 #ひ孫の代まで分裂します
                stop_count    = 20 #その場に留まるカウント数
                accel        = 1.02 #加速係数
                func.enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel)
        
        #敵弾9(アップ&ダウンレーザー)の発生                    KEY L ----------------
        if(pyxel.frame_count % 28) == 0:
            if pyxel.btn(pyxel.KEY_L):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 80,60
                    vx,vy =    -0.1,-0.3
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.2
                    width_max           = 40
                    height_max          = 3
                    new_enemy_shot.update(ENEMY_SHOT_UP_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 80,60
                    vx,vy =    -0.1,0.3
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.3
                    width_max           = 80
                    height_max          = 3
                    new_enemy_shot.update(ENEMY_SHOT_DOWN_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾10(ベクトルレーザー)の発生                        KEY M ----------------
        if(pyxel.frame_count % 10) == 0:
            if pyxel.btn(pyxel.KEY_M):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 100,60
                    vx,vy =    -0.7,-0.1
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.3
                    width_max           = 3
                    height_max          = 90
                    new_enemy_shot.update(ENEMY_SHOT_VECTOR_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE3,ESHOT_SIZE3, 0,0, vx,vy,     0.996,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_TOP,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #パーティクルを発生させる                              KEY P
        if(pyxel.frame_count % 1) == 0:
            if pyxel.btn(pyxel.KEY_P):
                # x = func.s_rndint(self,0,160)
                # y = func.s_rndint(self,0,120)
                
                x,y = 80,60
                dx,dy = -0.3 - random() * 2,-0.3 - random()
                life = 1000
                color = 0
                update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  dx,dy,life,0,color)
                # update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,x,y,  0,0,0,0,0)
                
                particle_number = func.s_rndint(self,0,10) + 50
                for number in range(particle_number):
                    update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,x,y,-0.5,-0.5, 0,0,0)
        
        #背景オブジェクト雲１を発生させる                        KEY E
        if(pyxel.frame_count % 6) == 0:
            if pyxel.btn(pyxel.KEY_E):
                t = func.s_rndint(self,0,20)
                y = func.s_rndint(self,0,120+30)
                
                new_background_object = Background_object()
                new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3,-0.25,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
                self.background_object.append(new_background_object)
        
        #パワーアップアイテム類を発生させる                       KEY U I O
        if(pyxel.frame_count % 8) == 0:
            if   pyxel.btn(pyxel.KEY_U): #ショットアイテム
                y = func.s_rndint(self,0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHOT_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   1,0,0,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item)    
            elif pyxel.btn(pyxel.KEY_I): #ミサイルアイテム
                y = func.s_rndint(self,0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_MISSILE_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,1,0,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item) 
            elif pyxel.btn(pyxel.KEY_O): #シールドアイテム
                y = func.s_rndint(self,0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item) 
        
        #自機クローを追加する                                KEY V
        if pyxel.btnp(pyxel.KEY_V):
            update_ship.append_claw(self)
        
        #キーボード入力によるイベントアペンドリスト書き込み  サーコイン10機編隊   KEY 0
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_0):
                new_event_append_request = Event_append_request()
                new_event_append_request.update(self.stage_count + 10,EVENT_ENEMY,CIR_COIN,WINDOW_W + 8,func.s_rndint(self,0,WINDOW_H - 8),10)
                self.event_append_request.append(new_event_append_request)#現在のstage_countから10カウント過ぎた時点でサーコインが発生するようイベントアペンドリストに追加する
