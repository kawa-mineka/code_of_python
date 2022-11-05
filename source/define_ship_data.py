from const import *         #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class define_ship_data:
    def __init__(self):
        None

    def default_ship_list(self):          #各機体リスト(原本)
        #[[機体IDナンバー,         機体名,              機体分類,            所持フラグ,x,   y,  IMG,  初期総スロット数,総スロット数,slot*のメダルID, レベル,経験値,shot最大経験値,ミサイル最大経験値, 出撃回数,破壊回数, 撃墜点数,     飛行時間,      移動スピード,min,max,   次元シフト,サーチライト,横幅, 縦幅,    claw_max,   クロー防御,  roll,   trace, fix,    reverse,自動回復タイム,自動回復上限値,ボス内侵入,被弾後無敵時間,カプセル取得後無敵時間, カプセル引き寄せ力
        self.default_ship_list = [
            [J_PYTHON,           "JUSTICE PYTHON"    ,SHIP_FIRST_STEP,     FLAG_ON,  8,   0,  IMG2, ALL_SLOT2,     ALL_SLOT2,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [PYTHON_FORCE,       "PYTHON FORCE 4.0"  ,SHIP_NEXT_GENERATION,FLAG_OFF, 8,   0,  IMG2, ALL_SLOT4,     ALL_SLOT4,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [E_PERL,             "ELEGANT PERL"      ,SHIP_FIRST_STEP,     FLAG_OFF, 8,   0,  IMG2, ALL_SLOT2,     ALL_SLOT2,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [C_FORTRAN,          "CLASSICAL FORTRAN" ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [AI_LOVE_LISP,       "AI LOVE LISP"      ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [ECLIPSING_ALGOL,    "ECLIPSING ALGOL"   ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [AUNT_COBOL,         "AUNT COBOL"        ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [BEGINNING_ADA,      "BEGINNING ADA"     ,SHIP_EXTRA,          FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [FIRST_BASIC,        "FIRST BASIC"       ,SHIP_STANDARD,       FLAG_OFF, 8,   0,  IMG2, ALL_SLOT3,     ALL_SLOT3,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [CUTTER_SHARP_2000,  "CUTTER SHARP 2000" ,SHIP_EXTRA,          FLAG_OFF, 8,   0,  IMG2, ALL_SLOT4,     ALL_SLOT4,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [LEGEND_ASM,         "LEGEND ASM"        ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT2,     ALL_SLOT2,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [LAST_RUST,          "LAST RUST"         ,SHIP_NEXT_GENERATION,FLAG_OFF, 8,   0,  IMG2, ALL_SLOT4,     ALL_SLOT4,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [GAMBA_RUBY,         "GAMBA RUBY"        ,SHIP_STANDARD,       FLAG_OFF, 8,   0,  IMG2, ALL_SLOT2,     ALL_SLOT2,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [SHIFT_SWIFT,        "SHIFT SWIFT"       ,SHIP_NEXT_GENERATION,FLAG_OFF, 8,   0,  IMG2, ALL_SLOT3,     ALL_SLOT3,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [MAGI_FORCE,         "MAGI FORCE"        ,SHIP_EXTRA,          FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            [LOOK_AT_LOGO,       "LOOK AT LOGO"      ,SHIP_ANCENT,         FLAG_OFF, 8,   0,  IMG2, ALL_SLOT1,     ALL_SLOT1,    0,0,0,0,0,0,0,  LEVEL1,EXP0, 71,            71,             SORTIE0,BROKEN0, SHOOT_DOWN0, FLIGHT_TIME0, SPEED0, SPEED0, SPEED2, FLAG_OFF, FLAG_OFF,   SIZE_4,SIZE_4, TWO_CLAW,  FLAG_OFF,  FLAG_ON,FLAG_ON,FLAG_ON,FLAG_ON, 0,           0,           FLAG_OFF, 0,            0,                    0],
            ]

    def sub_weapon_level_data_list(self): #サブウェポンのレベルデータリスト
        #テイルショット
        #    [レベル,連射数 ,スピード ,攻撃力 ,1-2-3-5way?,加速度]
        self.sub_weapon_tail_shot_level_data_list = [
            [ 1,     1,     1.0,      1.5,     1,          1    ],
            [ 2,     1,     1.1,      1.6,     1,          1    ],
            [ 3,     2,     1.3,      1.8,     1,          1    ],
            [ 4,   2*2,     1.1,      1.9,     2,          1    ],
            [ 5,   2*2,     1.2,      2.0,     2,          1    ],
            [ 6,   2*2,     1.3,      2.1,     2,          1    ],
            [ 7,   2*3,     0.7,      2.2,     3,          1    ],
            [ 8,   2*3,     0.9,      2.3,     3,          1    ],
            [ 9,   3*3,     1.1,      2.4,     3,          1    ],
            [10,   3*3,     1.3,      2.5,     3,          1    ],]
        
        #ホーミングミサイル
        #    [レベル,連射数 ,スピード ,攻撃力 ,1-2-3-5way?,加速度]
        self.sub_weapon_homing_missile_level_data_list = [
            [ 1,     4,     0.7,      0.2,     1,          1    ],
            [ 2,     4,     0.9,      0.3,     1,          1    ],
            [ 3,     4,     1.0,      0.4,     1,          1    ],
            [ 4,   4*2,     0.9,      0.3,     2,          1    ],
            [ 5,   4*2,     1.0,      0.4,     2,          1    ],
            [ 6,   4*2,     1.1,      0.5,     2,          1    ],
            [ 7,   4*3,     0.8,      0.2,     3,          1    ],
            [ 8,   4*3,     0.9,      0.3,     3,          1    ],
            [ 9,   4*3,     1.1,      0.4,     3,          1    ],
            [10,   4*4,     1.8,      0.3,     3,          1    ],]

    def shot_table_list(self):            #ショットパワーアップテーブルリスト定義
        #ショットパワーアップテーブルのフォーマット
        #
        #x軸 [ショットレベル,ショットスピード(倍率),バルカンショットの連射数,ショットの攻撃力(倍率)]
        #y軸 self.shot_exp(通常はショットパワーアップアイテムを取るとshot_expが3増える、特殊機体で成長度が遅い2とか1しか増えない機体もあります)
        #だいたい8個取って8*3の24exp入手で次の武装にレベルアップする感じ
        # 8個入手(24exp)で初期シングルショットバルカンからレーザー
        #更に8個入手(合計16個)(48exp)でレーザーからウェーブカッター
        #更に8個入手(合計24個)(72exp)でウェーブカッターLv4になる感じなのです
        
        #Justice Pythonのショット・パワーアップテーブル表
        self.j_python_shot_table_list = [
            [0,  1,1, 1],[0,  1,2, 1],[0,1.1,2, 1],
            [0,1.2,2, 1],[0,1.2,3, 1],[0,1.2,4, 1],
            [1,1.2,2, 1],[1,1.2,3, 1],[1,1.2,3, 1],
            [1,1.3,3, 1],[1,1.3,3, 1],[1,1.3,3, 1],
            [2,1.3,3, 1],[2,1.3,3, 1],[2,1.3,3, 1],
            [2,1.3,3, 1],[2,1.3,3, 1],[2,1.3,3, 1],
            [3,1.3,3, 1],[3,1.3,3, 1],[3,1.4,3, 1],
            [3,1.4,3, 1],[3,1.4,3, 1],[3,1.5,3, 1],
            
            [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
            [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
            [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
            [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
            [5,1.5,3, 1],[5,1.5,3, 1],[5,1.5,3, 1],
            [5,1.5,3, 1],[5,1.5,3, 1],[5,1.5,3, 1],
            [5,1.5,3, 1],[6,1.5,3, 1],[6,1.5,3, 1],
            [6,1.5,3, 1],[6,1.5,3, 1],[6,1.5,3, 1],
            
            [ 7,1.2,3, 1],[ 7,1.2,3, 1],[ 7,1.2,3, 1],
            [ 7,1.3,3, 1],[ 7,1.3,3, 1],[ 7,1.3,3, 1],
            [ 8,1.3,2, 1],[ 8,1.3,3, 1],[ 8,1.3,2, 1],
            [ 8,1.3,2, 1],[ 8,1.3,2, 1],[ 8,1.3,2, 1],
            [ 9,1.4,2, 1],[ 9,1.4,2, 1],[ 9,1.4,2, 1],
            [ 9,1.4,2, 1],[ 9,1.4,2, 1],[ 9,1.4,2, 1],
            [10,1.4,2, 1],[10,1.4,2, 1],[10,1.5,2, 1],
            [10,1.5,2, 1],[10,1.5,2, 1],[10,1.5,3, 1],
            [99999],]

    def missile_table_list(self):         #ミサイルパワーアップテーブルリストの定義
        #ミサイルパワーアップテーブルのフォーマット
        #
        #x軸 [ミサイルレベル,ミサイルスピード(倍率),ミサイルの連射数,ミサイルの攻撃力(倍率)]
        #y軸 self.missile_exp(通常はショットパワーアップアイテムを取るとmissile_expが3増える、特殊機体で成長度が遅い2とか1しか増えない機体もあります)
        #だいたい8個取って8*3の24exp入手で次のミサイルにレベルアップする感じ
        # 8個入手(24exp)でノーマルミサイルからツインミサイル
        #更に8個入手(合計16個)(48exp)でツインミサイルからからマルチミサイルになる感じ・・・・かもです！
        
        #Justice Pythonのミサイル・パワーアップテーブル表
        self.j_python_missile_table_list = [
            [0,  1,1, 1],[0,  1,1, 1],[0,1.2,1, 1],
            [0,1.2,1, 1],[0,1.2,1, 1],[0,1.3,1, 1],
            [0,1.3,2, 1],[0,1.3,2, 1],[0,1.4,2, 1],
            [0,1.4,2, 1],[0,1.4,2, 1],[0,1.5,2, 1],
            [0,1.5,2, 1],[0,1.6,2, 1],[0,1.7,2, 1],
            [0,1.8,2, 1],[0,1.9,2, 1],[0,2.0,2, 1],
            [0,2.1,2, 1],[0,2.2,2, 1],[0,2.3,2, 1],
            [0,2.4,3, 1],[0,2.6,3, 1],[0,2.7,3, 1],
            
            [1,1.9,2, 1],[1,1.9,2, 1],[1,1.9,2, 1],
            [1,2.0,2, 1],[1,2.0,2, 1],[1,2.1,2, 1],
            [1,2.1,2, 1],[1,2.2,2, 1],[1,2.2,2, 1],
            [1,2.3,2, 1],[1,2.4,2, 1],[1,2.4,2, 1],
            [1,2.4,2, 1],[1,2.4,2, 1],[1,2.5,2, 1],
            [1,2.5,2, 1],[1,2.5,2, 1],[1,2.5,2, 1],
            [1,2.5,2, 1],[1,2.6,2, 1],[1,2.7,2, 1],
            [1,2.7,2, 1],[1,2.8,3, 1],[1,2.9,3, 1],
            
            [2,2.1,2, 1],[2,2.2,2, 1],[2,2.2,2, 1],
            [2,2.3,2, 1],[2,2.4,2, 1],[2,2.5,2, 1],
            [2,2.6,2, 1],[2,2.6,2, 1],[2,2.6,2, 1],
            [2,2.7,3, 1],[2,2.7,3, 1],[2,2.8,3, 1],
            [2,2.9,3, 1],[2,2.9,3, 1],[2,2.9,3, 1],
            [2,2.9,3, 1],[2,2.9,3, 1],[2,2.9,3, 1],
            [2,3.0,3, 1],[2,3.1,3, 1],[2,3.2,4, 1],
            [2,3.3,4, 1],[2,3.4,4, 1],[2,3.5,4, 1],
            [99999],]
