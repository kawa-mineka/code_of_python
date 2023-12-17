from enum import IntEnum,auto 

#!定数の定義関連##################################################################################################
WINDOW_W = 160    #ゲームウィンドウの横サイズ
WINDOW_H = 120    #ゲームウィンドウの縦サイズ
SHIP_H = 8        #自機の縦サイズ
SHIP_W = 8        #自機の横サイズ
MOVE_LIMIT = 20   #前方に進める限界距離

MAIN_MENU_X = 44 #メインメニューのx座標
MAIN_MENU_Y = 15 #メインメニューのy座標

#アイテムのマップチップナンバーアドレス(場所)定義
SHOT_POW_BG_NUM         = (0 / 8) * 32 + ( 8 / 8)  #マップチップ x8y0 ショットアイテム 公式は(y/8)*32 + (x/8)となります
MISSILE_POW_BG_NUM      = (0 / 8) * 32 + (16 / 8)  #マップチップx16y0 ミサイルアイテム
SHIELD_POW_BG_NUM       = (0 / 8) * 32 + (24 / 8)  #マップチップx24y0 シールドアイテム
CLAW_POW_BG_NUM         = (0 / 8) * 32 + (32 / 8)  #マップチップx32y0 クローアイテム

TAIL_SHOT_BG_NUM        = (0 / 8) * 32 + (48 / 8)  #マップチップx48y0 テイルショットアイテム
PENETRATE_ROCKET_BG_NUM = (0 / 8) * 32 + (56 / 8)  #マップチップx56y0 ペネトレートロケットアイテム
SEARCH_LASER_BG_NUM     = (0 / 8) * 32 + (64 / 8)  #マップチップx64y0 サーチレーザーアイテム
HOMING_MISSILE_BG_NUM   = (0 / 8) * 32 + (72 / 8)  #マップチップx72y0 ホーミングミサイルアイテム
SHOCK_BUMPER_BG_NUM     = (0 / 8) * 32 + (80 / 8)  #マップチップx80y0 ショックバンパーアイテム
TRIANGLE_POW_BG_NUM     = (0 / 8) * 32 + (88 / 8)  #マップチップx88y0 トライアングルアイテム

#ボス移動ポイント指定用マップチップナンバーアドレス(場所)定義
MOVE_POINT_BG_NUM       = (0 / 8) * 32 + (112 / 8) #移動点(ムーブポイント)   公式は(y/8)*32 + (x/8)となります
CONTROL_POINT_NUM       = (0 / 8) * 32 + (120 / 8) #制御点(コントロールポイント)
ZERO_BG_CHR_NUM         = (8 / 8) * 32 +   (0 / 8) #BGチップの「0」が描かれたタイルチップナンバー

ALL_STAGE_NUMBER = 10 #全ステージ数(撃ち返し弾を出すとき ループ数×ALL_STAGE_NUMBER+ステージ数を計算して撃ち返すのか撃ち返さないのか判断します)

SHOT_EXP_MAXIMUM = 71 #自機ショットの最大経験値（この数値を超えちゃダメだよ）
                #例 self.j_python_shot_table_listのy軸の最大値がこの数と一致します
                #これより大きい数値にしちゃうとindex erroerになっちゃうからね
MISSILE_EXP_MAXIMUM = 71 #自機ミサイルの最大経験値（この数値を超えちゃダメだよ）
                #例 self.j_python_missile_table_listのy軸の最大値がこの数と一致します
                #これより大きい数値にしちゃうとindex erroerになっちゃうからね
SUB_WEAPON_LEVEL_MAXIMUM = 10 #自機サブウェポンのレベルの最大値
                    #例 self.sub_weapon_tail_shot_level_data_listのy軸の最大値がこの数と一致します
                    #これより大きい数値にしちゃうとindex out of range erroerになっちゃうからね

# ゲームステータス関連の定数定義 game_statusに代入されます 20231217より列挙型でautoを使用して自動で定数定義するようにしました(中に入る数字はどんな数値でも良い為です)
# CIR_COIN           =  1  #無人編隊戦闘機 サーコイン（サークルコイン）
# SCENE_IPL               =  0    #IPL(Initial Program Load)
# SCENE_SPLASH_LOGO       =  1    #起動処理中（スプラッシュロゴ表示）

# SCENE_TITLE_INIT        = 10    #タイトル表示に必要な初期化をする
# SCENE_TITLE_FIRST       = 11    #タイトルロゴグラフイックをアニメーションさせて表示中(初回起動)
# SCENE_TITLE_HIT_ANY_BTN = 12    #タイトルを表示した後、何かしらのボタンの入力待ち状態

# SCENE_TITLE_SECOND      = 13    #タイトルロゴグラフイックをアニメーションさせて表示中(2回目以降)
# SCENE_TITLE_MENU_SELECT = 14    #タイトルメニュー選択中
# SCENE_SELECT_LOAD_SLOT  = 15    #リプレイ再生に必要なリプレイファイルをどのスロットからロードするのか？選択待ち
# SCENE_CREDIT            = 16    #クレジットタイトル表示中

# SCENE_CONFIG            = 20    #設定メニュー表示中

# SCENE_DEBUG_CONGIG      = 30    #デバッグモード設定メニュー表示中

# SCENE_TITLE_DEMO        = 40    #タイトルデモ表示中（ストーリーとかのビジュアルシーン）
# SCENE_ADVERTISE_DEMO    = 41    #アドバタイズデモ（コンピュータによるゲームの宣伝の為のリプレイ再生）
# SCENE_MIDDLE_DEMO       = 42    #中間デモ中

# SCENE_GAME_START_INIT   = 50    #ゲーム開始前の初期化    スコアやシールド値、ショットレベルやミサイルレベルなどの初期化
# SCENE_STAGE_START_INIT  = 51    #ステージ開始前の初期化   自機の座標や各リストの初期化、カウンター類の初期化
# SCENE_START             = 52    #ゲーム開始(スタートダイアログを出したり、自機の出現アニメーションとか)
# SCENE_PLAY              = 53    #ゲームプレイ中
# SCENE_BOSS_APPEAR       = 54    #ボスキャラ現れる！
# SCENE_BOSS_BATTLE       = 55    #ボスキャラと戦闘中
# SCENE_BOSS_EXPLOSION    = 56    #ボスキャラ爆発中！
# SCENE_PAUSE             = 57    #一時中断中
# SCENE_EXPLOSION         = 58    #被弾して爆発中（ゲーム自体はまだ進行している）
# SCENE_RESTORATION       = 59    #復活中(自機は点滅状態で無敵状態だよ)

# SCENE_GAME_OVER           = 60 #ゲームオーバーメッセージ表示中（ゲームはまだ進行している）
# SCENE_GAME_OVER_FADE_OUT  = 61 #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をフェードアウトさせていく）
# SCENE_GAME_OVER_SHADOW_IN = 62 #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をシャドウインさせていく）
# SCENE_GAME_OVER_STOP      = 63 #ゲームオーバーメッセージ表示中（ゲーム自体は停止している）
# SCENE_RETURN_TITLE        = 64 #ゲームオーバーになりタイトルに戻るかどうかカーソルを出して選択待ち
# SCENE_SELECT_SAVE_SLOT    = 65 #タイトルに戻る前にリプレイファイルどのスロットにセーブするのか選択待ち

# SCENE_STAGE_CLEAR               = 70 #ステージクリア
# SCENE_STAGE_CLEAR_MOVE_MY_SHIP  = 71 #ステージクリア後、自機がステージクリア画像左上まで自動に動いていくシーン
# SCENE_STAGE_CLEAR_MY_SHIP_BOOST = 72 #ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン
# SCENE_STAGE_CLEAR_FADE_OUT      = 73 #ステージクリア後のフェードアウト

# SCENE_CONTINUE    = 80   #コンティニューメッセージ表示中

# SCENE_ENDING      = 90   #エンディング表示中

# SCENE_STAFF_ROLL  = 100  #スタッフロール表示中

# SCENE_GAME_QUIT_START              = 900 #ゲーム終了工程開始
# SCENE_GAME_QUIT_WAIT               = 901 #ゲーム終了工程待ち(終了サウンドが再生完了するのを待ちますです)

# SCENE_GAME_QUIT                    = 999 #ゲーム終了(スリーナインで終了 汽車は～♪闇を抜けて～～光の海へ～～～☆彡)

#!ゲームステータス関連の定数定義 game_statusに代入されます#######################################################################
#2023 12/16より別クラスにて列挙型を使用し自動で任意の数値を定義するようにしました
class Scene(IntEnum):
    IPL               = auto()    #IPL(Initial Program Load)
    SPLASH_LOGO       = auto()    #起動処理中（スプラッシュロゴ表示）
    
    TITLE_INIT        = auto()    #タイトル表示に必要な初期化をする
    TITLE_FIRST       = auto()    #タイトルロゴグラフイックをアニメーションさせて表示中(初回起動)
    TITLE_HIT_ANY_BTN = auto()    #タイトルを表示した後、何かしらのボタンの入力待ち状態
    
    TITLE_SECOND      = auto()    #タイトルロゴグラフイックをアニメーションさせて表示中(2回目以降)
    TITLE_MENU_SELECT = auto()    #タイトルメニュー選択中
    SELECT_LOAD_SLOT  = auto()    #リプレイ再生に必要なリプレイファイルをどのスロットからロードするのか？選択待ち
    CREDIT            = auto()    #クレジットタイトル表示中
    
    CONFIG            = auto()    #設定メニュー表示中
    
    DEBUG_CONGIG      = auto()    #デバッグモード設定メニュー表示中
    
    TITLE_DEMO        = auto()    #タイトルデモ表示中（ストーリーとかのビジュアルシーン）
    ADVERTISE_DEMO    = auto()    #アドバタイズデモ（コンピュータによるゲームの宣伝の為のリプレイ再生）
    MIDDLE_DEMO       = auto()    #中間デモ中
    
    GAME_START_INIT   = auto()    #ゲーム開始前の初期化    スコアやシールド値、ショットレベルやミサイルレベルなどの初期化
    STAGE_START_INIT  = auto()    #ステージ開始前の初期化   自機の座標や各リストの初期化、カウンター類の初期化
    START             = auto()    #ゲーム開始(スタートダイアログを出したり、自機の出現アニメーションとか)
    PLAY              = auto()    #ゲームプレイ中
    BOSS_APPEAR       = auto()    #ボスキャラ現れる！
    BOSS_BATTLE       = auto()    #ボスキャラと戦闘中
    BOSS_EXPLOSION    = auto()    #ボスキャラ爆発中！
    PAUSE             = auto()    #一時中断中
    EXPLOSION         = auto()    #被弾して爆発中（ゲーム自体はまだ進行している）
    RESTORATION       = auto()    #復活中(自機は点滅状態で無敵状態だよ)
    
    GAME_OVER           = auto() #ゲームオーバーメッセージ表示中（ゲームはまだ進行している）
    GAME_OVER_FADE_OUT  = auto() #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をフェードアウトさせていく）
    GAME_OVER_SHADOW_IN = auto() #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をシャドウインさせていく）
    GAME_OVER_STOP      = auto() #ゲームオーバーメッセージ表示中（ゲーム自体は停止している）
    RETURN_TITLE        = auto() #ゲームオーバーになりタイトルに戻るかどうかカーソルを出して選択待ち
    SELECT_SAVE_SLOT    = auto() #タイトルに戻る前にリプレイファイルどのスロットにセーブするのか選択待ち
    
    STAGE_CLEAR               = auto() #ステージクリア
    STAGE_CLEAR_MOVE_MY_SHIP  = auto() #ステージクリア後、自機がステージクリア画像左上まで自動に動いていくシーン
    STAGE_CLEAR_MY_SHIP_BOOST = auto() #ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン
    STAGE_CLEAR_FADE_OUT      = auto() #ステージクリア後のフェードアウト
    
    CONTINUE    = auto()   #コンティニューメッセージ表示中
    
    ENDING      = auto()   #エンディング表示中
    
    STAFF_ROLL  = auto()   #スタッフロール表示中
    
    GAME_QUIT_START              = auto()  #ゲーム終了工程開始
    GAME_QUIT_WAIT               = auto()  #ゲーム終了工程待ち(終了サウンドが再生完了するのを待ちますです)
    
    GAME_QUIT                    = auto()  #ゲーム終了
    
#!ゲームモードの定数定義#########################################################################
CHORNICLE_MODE    = 0   #クロニクルモード
ACRADE_MODE       = 1   #アーケードモード
CARAVAN_MODE      = 2   #キャラバンモード
HIGHSCORE_MODE    = 3   #ハイスコアモード
PRACTICE_MODE     = 4   #プラクティスモード
LONGDIVE_MODE     = 5   #ロングダイブモード
INFINITY_MODE     = 6   #インフィニティモード
FREESTYLE_MODE    = 7   #フリースタイルモード
MISSILE_MODE      = 8   #ミサイルモード
NOPOWERUP_MODE    = 9   #ノーパワーアップモード

#!自機のIDナンバー定義 ##########################################################################
J_PYTHON          =  0   #Justice Python
E_PERL            =  1   #Elegant Perl(practical extraction and report language)
PYTHON_FORCE      =  2   #Python4.0(4th.force)
C_FORTRAN         =  3   #Classical FORTRAN 1954
AI_LOVE_LISP      =  4   #AI love LISP 1958
ECLIPSING_ALGOL   =  5   #Eclipsing Binary ALGOL 1958
AUNT_COBOL        =  6   #Aunt COBOL more better 1959
BEGINNING_ADA     =  7   #Beginning programmer Ada 1815-1983
FIRST_BASIC       =  8   #First Beginners All purpose Symbolic Instruction Code 1964
CUTTER_SHARP_2000 =  9   #Cutter # 2000
LEGEND_ASM        = 10   #Legend Assembler
LAST_RUST         = 11   #Last Rust
GAMBA_RUBY        = 12   #GAMBA Ruby New Generation IDOL
SHIFT_SWIFT       = 13   #SHIFT timer SWIFT space
MAGI_FORCE        = 14   #MAGI FORCE power is dream
LOOK_AT_LOGO      = 15   #LOOK AT THE TURTLE LOGO! 1967

#自機、機体分類
SHIP_FIRST_STEP      = 0 #初期機体
SHIP_STANDARD        = 1 #標準機体
SHIP_ANCENT          = 2 #古代機体
SHIP_EXTRA           = 3 #特殊機体
SHIP_NEXT_GENERATION = 4 #次世代機体

#各機体リストを参照するときに使用するインデックスナンバーの定数定義 window[i].ship_list[ここで定義した定数]
LIST_SHIP_ID                       =  0 #機体IDナンバー
LIST_SHIP_NAME                     =  1 #機体名
LIST_SHIP_CLASS                    =  2 #機体分類
LIST_SHIP_OWNED                    =  3 #所有フラグ 0=未所有 1=所有                 この項目はシステムデータとしてセーブされます
LIST_SHIP_GRAPH_U                  =  4 #画像データが入っているx座標(u)
LIST_SHIP_GRAPH_V                  =  5 #画像データが入っているy座標(v)
LIST_SHIP_GRP_IMGB                 =  6 #画像データが入っているイメージバンク数
LIST_SHIP_INIT_SLOT_NUM            =  7 #初期状態での総スロット数
LIST_SHIP_SLOT_NUM                 =  8 #総スロット数
LIST_SHIP_SLOT0                    =  9 #スロット0に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT1                    = 10 #スロット1に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT2                    = 11 #スロット2に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT3                    = 12 #スロット3に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT4                    = 13 #スロット4に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT5                    = 14 #スロット5に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_SLOT6                    = 15 #スロット6に装備しているメダルIDが入ります     この項目はシステムデータとしてセーブされます
LIST_SHIP_LEVEL                    = 16 #機体のレベル                                この項目はシステムデータとしてセーブされます
LIST_SHIP_EXP                      = 17 #機体の経験値(総獲得点数って感じです)          この項目はシステムデータとしてセーブされます
LIST_SHIP_MAX_SHOT_EXP             = 18 #ショット経験値の最大値(これを超えてはいけない)
LIST_SHIP_MAX_MISSILE_EXP          = 19 #ミサイル経験値の最大値(これを超えてはいけない)
LIST_SHIP_SORTIE                   = 20 #出撃回数                                    この項目はシステムデータとしてセーブされます
LIST_SHIP_BROKEN                   = 21 #破壊回数                                    この項目はシステムデータとしてセーブされます
LIST_SHIP_SHOOT_DOWN               = 22 #撃墜点数                                    この項目はシステムデータとしてセーブされます
LIST_SHIP_FLIGHT_TIME              = 23 #飛行時間                                    この項目はシステムデータとしてセーブされます

LIST_SHIP_SPEED                    = 24 #機体の移動スピード
LIST_SHIP_SPEED_MIN                = 25 #機体の移動スピード(最小値)
LIST_SHIP_SPEED_MAX                = 26 #機体の移動スピード(最大値)

LIST_SHIP_SHIFT_FLAG               = 27 #次元シフト可能フラグ
LIST_SHIP_SEARCH_LIGHT             = 28 #サーチライト可能フラグ
LIST_SHIP_SIZE_X                   = 29 #機体の横サイズ(自機当たり判定の目安となります)
LIST_SHIP_SIZE_Y                   = 30 #機体の縦サイズ(自機当たり判定の目安となります)

LIST_SHIP_CLAW_MAX                 = 31 #装備できるクローの最大値
LIST_SHIP_CLAW_DEFENCE             = 32 #クローで防御できるかのフラグ
LIST_SHIP_CLAW_ROLLING             = 33 #ローリングクロー使用可能かどうかのフラグ
LIST_SHIP_CLAW_TRACE               = 34 #トレースクロー使用可能かどうかのフラグ
LIST_SHIP_CLAW_FIX                 = 35 #フイックスクロー使用可能かどうかのフラグ
LIST_SHIP_CLAW_REVERSE             = 36 #リバースクロー使用可能かどうかのフラグ

LIST_SHIP_AUTO_REPAIR_TIME         = 37 #シールド自動回復タイム(このフレーム数ぶん時間がたつとシールドが１回復する)0の場合は回復機能なし
LIST_SHIP_AUTO_REPAIR_MAX          = 38 #シールド自動回復の上限値（自動回復ではこのシールド値以上には回復しない)

LIST_SHIP_BOSS_REBUILDING          = 39 #ボスキャラのプログラムを書き替え内部に侵入できるかどうかのフラグ

LIST_SHIP_HYPER_ARM_TIME           = 40 #被弾後の無敵時間(ハイパーアーム状態の時間)
LIST_SHIP_ITEM_GET_INVINCIBLE      = 41 #アイテムカプセル取得後の無敵時間
LIST_SHIP_ITEM_RANGE_OF_ATTRACTION = 42 #アイテムを引き寄せる範囲

#機体レベル
LEVEL0,LEVEL1,LEVEL2,LEVEL3,LEVEL4,LEVEL5 = 0,1,2,3,4,5
#機体経験値,出撃回数,破壊回数,撃墜点数,飛行時間
EXP0,SORTIE0,BROKEN0,SHOOT_DOWN0,FLIGHT_TIME0 = 0,0,0,0,0
#移動スピード
SPEED0,SPEED1,SPEED2,SPEED3,SPEED4,SPEED5 = 0,1,2,3,4,5
SPEED6,SPEED7,SPEED8,SPEED9,SPEED10,SPEED11 = 6,7,8,9,10,11
SPEED12,SPEED13,SPEED14,SPEED15,SPEED16,SPEED17 = 12,13,14,15,16,17
SPEED18,SPEED19,SPEED20,SPEED21,SPEED22,SPEED23 = 18,19,20,21,22,23
SPEED24,SPEED25,SPEED26,SPEED27,SPEED27,SPEED29 = 24,25,26,27,28,29
SPEED30,SPEED31,SPEED32,SPEED33,SPEED34,SPEED35 = 30,31,32,33,34,35

#周回数
LOOP01,LOOP02,LOOP03,LOOP04,LOOP05,LOOP06,LOOP07,LOOP08,LOOP09,LOOP10 =  1, 2, 3, 4, 5, 6, 7, 8, 9,10
LOOP11,LOOP12,LOOP13,LOOP14,LOOP15,LOOP16,LOOP17,LOOP18,LOOP19,LOOP20 = 11,12,13,14,15,16,17,18,19,20
LOOP21,LOOP22,LOOP23,LOOP24,LOOP25,LOOP26,LOOP27,LOOP28,LOOP29,LOOP30 = 21,22,23,24,25,26,27,28,29,30

#言語選択
LANGUAGE_ENG         = 0 #英語
LANGUAGE_JPN         = 1 #日本語

#各機体に装備されているメダルや自機のグラフイックを表示するときに使うリストを参照するときに使用するインデックスナンバーの定数定義（言ってる意味が分からぬぅうう！）window[i].ship_medal_list
LIST_SHIP_MEDAL_SHIP_ID         =  0 #自機IDナンバーがコピーされて入ります

LIST_SHIP_SHIP_GRAPH_DISP_FLAG  =  1 #自機グラフイックを表示するかどうかのフラグ
LIST_SHIP_SHIP_DISP_OX          =  2 #自機を表示し始める位置 x座標(ウィンドウ原点からのオフセット値)
LIST_SHIP_SHIP_DISP_OY          =  3 #自機を表示し始める位置 y座標(ウィンドウ原点からのオフセット値)

LIST_SHIP_SHIP_NAME_DISP_FLAG   =  4 #機体名を表示するかどうかのフラグ
LIST_SHIP_SHIP_NAME_DISP_OX     =  5 #機体名を表示し始める位置 x座標(ウィンドウ原点からのオフセット値)
LIST_SHIP_SHIP_NAME_DISP_OY     =  6 #機体名を表示し始める位置 y座標(ウィンドウ原点からのオフセット値)

LIST_SHIP_MEDAL_GRAPH_DISP_FLAG =  7 #メダルグラフイックを表示するかどうかのフラグ
LIST_SHIP_MEDAL_DISP_OX         =  8 #自機に装備されているメダルを表示し始める位置 x座標(ウィンドウ原点からのオフセット値)
LIST_SHIP_MEDAL_DISP_OY         =  9 #自機に装備されているメダルを表示し始める位置 y座標(ウィンドウ原点からのオフセット値)

#メダル＆コメントリストを参照するときに使用するインデックスナンバーの定数定義 self.medal_graph_and_comment_list[medal_id][ここで定義した定数]
LIST_MEDAL_GRP_CMNT_ID            =  0 #メダルIDナンバー
LIST_MEDAL_GRP_CMNT_U             =  1 #画像データが収納されているx座標(u)
LIST_MEDAL_GRP_CMNT_V             =  2 #画像データが収納されているx座標(v)
LIST_MEDAL_GRP_CMNT_IMGB          =  3 #画像データが収納されているイメージバンク数
LIST_MEDAL_GRP_CMNT_ENG           =  4 #メダルに対する英語コメント
LIST_MEDAL_GRP_CMNT_JPN           =  5 #メダルに対する日本語コメント
LIST_MEDAL_GRP_CMNT_GET_ENG_LINE1 =  6 #メダル取得時に表示されるダイアログウィンドウのコメント(英語)1行目
LIST_MEDAL_GRP_CMNT_GET_ENG_LINE2 =  7 #2行目
LIST_MEDAL_GRP_CMNT_GET_JPN_LINE1 =  8 #メダル取得時に表示されるダイアログウィンドウのコメント(日本語)1行目
LIST_MEDAL_GRP_CMNT_GET_JPN_LINE2 =  9 #2行目

#!キーアイテムの定数定義 ########################################################
KEY_ITEM_PUNCHED_CARD               =  0 #パンチカード
KEY_ITEM_MAGNETIC_CORE_MEMORY       =  1 #磁気コアメモリ
KEY_ITEM_MAGNETIC_BUBBLE_MEMORY     =  2 #磁気バブルメモリ
KEY_ITEM_CASSETLE_TAPE_IEC_TYPE_I   =  3 #ノーマルテープ
KEY_ITEM_CASSETLE_TAPE_IEC_TYPE_II  =  4 #ハイポジションテープ
KEY_ITEM_CASSETLE_TAPE_IEC_TYPE_III =  5 #フェリクロームカセットテープ
KEY_ITEM_CASSETLE_TAPE_IEC_TYPE_IV  =  6 #メタルカセットテープ
KEY_ITEM_QUICK_DISC                 =  7 #クイックディスク
KEY_ITEM_JAZ                        =  8 #JAZ
KEY_ITEM_DAT                        =  9 #DAT デジタルオーディオテープ
KEY_ITEM_3INCH_FLOPPY_DISK          = 10 #3インチフロッピーディスク
KEY_ITEM_PD                         = 11 #PD Phase-change Dual or Phase-change Disc
KEY_ITEM_MD                         = 12 #Micro Drive
KEY_ITEM_KANJI_ROM_CARTRIDGE        = 13 #漢字ROMカートリッジ HBI-K21

#称号
NOVICE        = 0 #ノービス        入門者
ASPIRANT      = 1 #アスパイラント   志を持つ者
BATTLER       = 2 #バトラー        兵士
FIGHTER       = 3 #ファイター      闘士
ADEPT         = 4 #アデプト        熟練者
CHEVALIER     = 5 #シェバリアー    騎士
VETERAN       = 6 #ベテラン        軍人
WARRIOR       = 7 #ウォーリア      勇士
SWORDMAN      = 8 #ソードマン      剣士
HERO          = 9 #ヒーロー        英雄
SWASHBUCKLER  =10 #スワッシュバックラー 暴れ者
CHAMPION      =12 #チャンピオン    勝者
MYRMIDON      =11 #マーミダン      忠臣
SUPERHERO     =13 #スーパーヒーロー 勇者
PALADIN       =14 #パラディン      親衛隊騎士
LOAD          =15 #ロード          君主
MASTER_LOAD   =16 #マスターロード   大君主

#!実績(アチーブメント)のIDナンバー定数定義
ACHIEVEMENT_FIRST_CAMPAIGN           =  0 #初陣!  初めての出撃!
ACHIEVEMENT_DESTROY_STAGE01_BOSS     =  1 #ステージ1のボスを撃破した!
ACHIEVEMENT_DESTROY_STAGE02_BOSS     =  2 #ステージ2のボスを撃破した!!
ACHIEVEMENT_DESTROY_STAGE03_BOSS     =  3 #ステージ3のボスを撃破した!!!
ACHIEVEMENT_DESTROY_STAGE04_BOSS     =  4 #ステージ4のボスを撃破した!!!!
ACHIEVEMENT_DESTROY_STAGE05_BOSS     =  5 #ステージ5のボスを撃破した!!!!!
ACHIEVEMENT_DESTROY_STAGE06_BOSS     =  6 #ステージ6のボスを撃破した!!!!!!
ACHIEVEMENT_DESTROY_STAGE07_BOSS     =  7 #ステージ7のボスを撃破した!!!!!!!
ACHIEVEMENT_DESTROY_STAGE08_BOSS     =  8 #ステージ8のボスを撃破した!!!!!!!!
ACHIEVEMENT_DESTROY_STAGE09_BOSS     =  9 #ステージ9のボスを撃破した!!!!!!!!!
ACHIEVEMENT_DESTROY_STAGE10_BOSS     =  10 #ステージ10のボスを撃破した!!!!!!!!!!
ACHIEVEMENT_FIRST_POW_UP             =  11 #はじめてのパワーカプセル回収成功！ 
ACHIEVEMENT_1STAGE_CLEAR             =  12 #初めてのステージクリア！
ACHIEVEMENT_DESTROY_BOSS_10TIME      =  13 #累計10体のボスを破壊した
ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS   =  14 #どのボスでも良いのでノーダメージでボスを撃破した
ACHIEVEMENT_SCORE_STAR_5CHAIN        =  15 #スコアスターをノーダメージで5連続ゲット
ACHIEVEMENT_FIRST_CLAW               =  16 #初めてクローカプセルを取得する

ACHIEVEMENT_10_SHOT_POW              =  17 #累計10個のショットアイテムを取得
ACHIEVEMENT_50_SHOT_POW              =  18 #累計50個のショットアイテムを取得
ACHIEVEMENT_100_SHOT_POW             =  19 #累計100個のショットアイテムを取得
ACHIEVEMENT_200_SHOT_POW             =  20 #累計200個のショットアイテムを取得
ACHIEVEMENT_500_SHOT_POW             =  21 #累計500個のショットアイテムを取得
ACHIEVEMENT_1000_SHOT_POW            =  22 #累計1000個のショットアイテムを取得
ACHIEVEMENT_2000_SHOT_POW            =  23 #累計2000個のショットアイテムを取得
ACHIEVEMENT_2465_SHOT_POW            =  24 #累計2465個のショットアイテムを取得

ACHIEVEMENT_10_MISSILE_POW              =  25 #累計10個のミサイルアイテムを取得
ACHIEVEMENT_50_MISSILE_POW              =  26 #累計50個のミサイルアイテムを取得
ACHIEVEMENT_100_MISSILE_POW             =  27 #累計100個のミサイルアイテムを取得
ACHIEVEMENT_200_MISSILE_POW             =  28 #累計200個のミサイルアイテムを取得
ACHIEVEMENT_400_MISSILE_POW             =  29 #累計400個のミサイルアイテムを取得
ACHIEVEMENT_765_MISSILE_POW             =  30 #累計765個のミサイルアイテムを取得
ACHIEVEMENT_1000_MISSILE_POW            =  31 #累計1000個のミサイルアイテムを取得
ACHIEVEMENT_2465_MISSILE_POW            =  32 #累計2465個のミサイルアイテムを取得

ACHIEVEMENT_10_SHIELD_POW              =  33 #累計10個のシールドアイテムを取得
ACHIEVEMENT_50_SHIELD_POW              =  34 #累計50個のシールドアイテムを取得
ACHIEVEMENT_100_SHIELD_POW             =  35 #累計100個のシールドアイテムを取得
ACHIEVEMENT_200_SHIELD_POW             =  36 #累計200個のシールドアイテムを取得
ACHIEVEMENT_400_SHIELD_POW             =  37 #累計400個のシールドアイテムを取得
ACHIEVEMENT_530_SHIELD_POW             =  38 #累計530個のシールドアイテムを取得

ACHIEVEMENT_10_CLAW_POW                =  39 #累計10個のクローアイテムを取得
ACHIEVEMENT_20_CLAW_POW                =  40 #累計20個のクローアイテムを取得
ACHIEVEMENT_50_CLAW_POW                =  41 #累計50個のクローアイテムを取得
ACHIEVEMENT_100_CLAW_POW               =  42 #累計100個のクローアイテムを取得


ACHIEVEMENT_FIRST_5WAY_SHOT            =  43 #初めて5WAYバルカンショットを体験
ACHIEVEMENT_FIRST_LASER                =  44 #初めてLASERを体験
ACHIEVEMENT_FIRST_TWIN_LASER           =  45 #初めてTWIN LASERを体験
ACHIEVEMENT_FIRST_SHOWER_LASER         =  46 #初めてSHOWER LASERを体験
ACHIEVEMENT_FIRST_WAVE                 =  47 #初めてWAVEを体験
ACHIEVEMENT_FIRST_MAX_WAVE             =  48 #初めて最大級のWAVEを体験

ACHIEVEMENT_FIRST_TWIN_MISSILE         =  49 #初めてTWIN MISSILEを体験
ACHIEVEMENT_FIRST_MULTI_MISSILE        =  50 #初めてMULTI MISSILEを体験

ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR          = 51 #ノーダメージでステージクリアした
ACHIEVEMENT_NO_SHOT_STAGE_CLEAR            = 52 #ノーショットでステージクリアした
ACHIEVEMENT_NO_DAMAGE_AND_SHOT_STAGE_CLEAR = 53 #ノーダメージ＆ノーショットでステージクリアした

ACHIEVEMENT_BOSS_INSTANK_KILL              = 54 #ボスを瞬殺した

ACHIEVEMENT_FIRST_REPLAY_PLAY_COMPLETE     = 55 #初めてリプレイ再生を最後まで再生出来た

ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM        = 56 #初めてトライアングルアイテムを取得できた！
ACHIEVEMENT_ENDURANCE_ONE_CLEARED          = 57 #のこりシールド値1でギリギリステージクリアした
ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS       = 58 #ボスのパーツをすべて破壊した

ACHIEVEMENT_FIRST_FAST_FORWARD             = 59 #初めて早回しを発生させた！
ACHIEVEMENT_8_FAST_FORWARD                 = 60 #累計8回、早回しを発生させた
ACHIEVEMENT_16_FAST_FORWARD                = 61 #累計16回、早回しを発生させた
ACHIEVEMENT_32_FAST_FORWARD                = 62 #累計32回、早回しを発生させた
ACHIEVEMENT_64_FAST_FORWARD                = 63 #累計64回、早回しを発生させた
ACHIEVEMENT_128_FAST_FORWARD               = 64 #累計128回、早回しを発生させた
ACHIEVEMENT_256_FAST_FORWARD               = 65 #累計256回、早回しを発生させた
ACHIEVEMENT_512_FAST_FORWARD               = 66 #累計512回、早回しを発生させた
ACHIEVEMENT_1024_FAST_FORWARD              = 67 #累計1024回、早回しを発生させた



#アチーブメント(実績)リストを参照するときに使用するインデックスナンバー定数定義 achievement_list[idナンバー例ACHIEVEMENT_1STAGE_CLEARなど][ここで定義した定数]
LIST_ACHIEVE_ID                           =  0 #アチーブメントのIDナンバーが入ります
LIST_ACHIEVE_FLAG                         =  1 #アチーブメント(実績)を取得したかどうかのフラグ
LIST_ACHIEVE_GRP_X                        =  2 #アチーブメントのグラフイックが収納されたx座標(u)
LIST_ACHIEVE_GRP_Y                        =  3 #アチーブメントのグラフイックが収納されたy座標(v)
LIST_ACHIEVE_IMGB                         =  4 #アチーブメントのグラフイックが収納されたイメージバンク値
LIST_ACHIEVE_COMMENT_ENG1                 =  5 #アチーブメントの英語コメント
LIST_ACHIEVE_COMMENT_ENG2                 =  6 #アチーブメントの英語コメント(詳細)
LIST_ACHIEVE_COMMENT_JPN1                 =  7 #アチーブメントの日本語コメント
LIST_ACHIEVE_COMMENT_JPN2                 =  8 #アチーブメントの日本語コメント(詳細)
LIST_ACHIEVE_GET_TIME                     =  9 #アチーブメント(実績)を取得した場合に取得した日時が入る
LIST_ACHIEVE_RANK                         =  10 #アチーブメントのレベル
LIST_ACHIEVE_COMMENT_COLOR                =  11 #コメントを表示するときに使用する色

#実績(アチーブメント)の取得フラグ用定数定義
RESULTS_NOT_OBTAINED            = 0 #実績未取得
RESULTS_ACQUISITION             = 1 #実績取得！！！！！

#勲章(メダル)自機のオプションスロットにはめ込むことが出来るメダルのIDナンバー    色々な効果を付加することが出来る
MEDAL_NO_SLOT                   = 0 #何もメダルがはめ込まれていない空のスロット
MEDAL_BEFOREHAND_1SHOT_ITEM     = 1 #ゲームスタート時点で事前にショットアイテムを1個入手した状態から始まる 1個目のショットアイテムは得点アイテムに変化する それ以降は通常となる         (トータルプレイタイム10分以上で取得)
MEDAL_BEFOREHAND_2SHOT_ITEM     = 2 #ゲームスタート時点で事前にショットアイテムを2個入手した状態から始まる 1~2個目までのショットアイテムは得点アイテムに変化する それ以降は通常となる    (1面のボス撃破で取得)
MEDAL_BEFOREHAND_3SHOT_ITEM     = 3 #ゲームスタート時点で事前にショットアイテムを3個入手した状態から始まる 1~3個目までのショットアイテムは得点アイテムに変化する それ以降は通常となる    (トータルスコア2000点で取得)
MEDAL_BEFOREHAND_4SHOT_ITEM     = 4 #ゲームスタート時点で事前にショットアイテムを4個入手した状態から始まる 1~4個目までのショットアイテムは得点アイテムに変化する それ以降は通常となる    (トータルプレイタイム180分、又はトータルスコア10000点で取得)
MEDAL_EQUIPMENT_LS_SHIELD       = 5 #L'sシールドが装備される (イベントで取得)
MEDAL_PLUS_MEDALLION            = 6 #はめ込むことで2つのオプションスロットが作られる(実質スロットが1増える) (スコアスター得点倍率7以上で取得)
MEDAL_CONCENTRATION             = 7 #攻撃を一転に集中させることが出来る(3面のボス撃破で取得)
MEDAL_FRAME_RESIST              = 8 #炎に対しての耐性が付く(プレイ回数20回以上で取得)
MEDAL_RECOVERY_OVER_TIME        = 9 #時間経過でシールドパワーが回復する
MEDAL_TWINKLE                   = 10 #暗闇状態で前方を明るく照らすことが出来る

MEDAL_GET                       =  1 #メダルを持ってるよ！っていうフラグ

#各機体の総スロット数の定数定義
ALL_SLOT1  = 1
ALL_SLOT2  = 2
ALL_SLOT3  = 3
ALL_SLOT4  = 4
ALL_SLOT5  = 5
ALL_SLOT6  = 6
ALL_SLOT7  = 7

#ショットレベル(というか種類？)の定数定義
SHOT_LV0_VULCAN_SHOT      =  0 #バルカンショット1連装
SHOT_LV1_TWIN_VULCAN_SHOT =  1 #ツインバルカンショット2連装
SHOT_LV2_3WAY_VULCAN_SHOT =  2 #3WAYバルカンショット
SHOT_LV3_5WAY_VULCAN_SHOT =  3 #5WAYバルカンショット
SHOT_LV4_LASER            =  4 #レーザー
SHOT_LV5_TWIN_LASER       =  5 #ツインレーザー
SHOT_LV6_3WAY_LASER       =  6 #3WAYレーザー
SHOT_LV7_WAVE_CUTTER_LV1  =  7 #ウェーブカッターLv1
SHOT_LV8_WAVE_CUTTER_LV2  =  8 #ウェーブカッターLv2
SHOT_LV9_WAVE_CUTTER_LV3  =  9 #ウェーブカッターLv3
SHOT_LV10_WAVE_CUTTER_LV4 = 10 #ウェーブカッターLv4

#ミサイルレベル(というか種類？)の定数定義
MISSILE_LV0_NORMAL_MISSILE = 0 #初期装備右下ミサイル
MISSILE_LV1_TWIN_MISSILE   = 1 #ツインミサイル(右下と右上方向)
MISSILE_LV2_MULTI_MISSILE  = 2 #マルチミサイル(右下右上左下左上4方向)

#!サブウェポン関連のIDナンバー定数定義 #############################################
TAIL_SHOT        = 0 #テイルショットＩＤナンバー
PENETRATE_ROCKET = 1 #ペネトレートロケットＩＤナンバー
SEARCH_LASER     = 2 #サーチレーザーＩＤナンバー
HOMING_MISSILE   = 3 #ホーミングミサイルＩＤナンバー
SHOCK_BUMPER     = 4 #ショックバンパーＩＤナンバー

#クロータイプのIDナンバー定数定義###################################################
ROLLING_CLAW     = 0      #ローリングクロー
TRACE_CLAW       = 1      #トレースクロー
FIX_CLAW         = 2      #フイックスクロー
REVERSE_CLAW     = 3      #リバースクロー

#難易度リストを参照するときに使用するインデックスナンバー定数定義 game_difficulty[ここで定義した定数]
LIST_DIFFICULTY                   = 0 #難易度(難しさ)
LIST_DIFFICULTY_TEXT              = 1 #難易度説明テキスト
LIST_START_BONUS_SHOT             = 2 #ゲーム開始時のショットボーナス
LIST_START_BONUS_MISSILE          = 3 #ゲーム開始時のミサイルボーナス
LIST_START_BONUS_SHIELD           = 4 #ゲーム開始時のシールドボーナス
LIST_START_CLAW                   = 5 #ゲーム開始時のクローの数
LIST_REPAIR_SHIELD                = 6 #ステージクリア後に回復するシールド値
LIST_RETURN_BULLET                = 7 #撃ち返し弾の有無と有の時の種類
LIST_SCORE_MAGNIFICATION          = 8 #スコア倍率
LIST_RANK_UP_FRAME                = 9 #ランク上昇フレーム数
LIST_START_RANK                   =10 #ゲームスタート時のランク数
LIST_DAMAGE_AFTER_INVINCIBLE_TIME =11 #被弾後の無敵時間
LIST_GET_ITEM_INVINCIBLE_TIME     =12 #アイテム取得後の無敵時間
LIST_ITEM_ERACE_BULLET            =13 #パワーアップアイテムが敵弾を消去するかどうか？のフラグ
LIST_RANK_LIMIT                   =14 #ランク数の上限値
LIST_RETURN_BULLET_START_LOOP     =15 #撃ち返しを始めてくるループ数
LIST_RETURN_BULLET_START_STAGE    =16 #撃ち返しを始めてくるステージ数
LIST_RANK_DOWN_NEED_DAMAGE        =17 #1ランクダウンに必要なダメージ数
LIST_LOOP_POWER_CONTROL           =18 #次のループに移る時のパワーアップ調整関連の動作の仕方とか
LIST_ITEM_RANGE_OF_ATTRACTION     =19 #アイテムを引き寄せる範囲
LIST_ITEM_BOUNCE_NUM              =20 #アイテムの跳ね返り回数(左端に当たったら何回まで跳ね返るかの数値)

#難易度名の定数定義
GAME_VERY_EASY = 0
GAME_EASY      = 1
GAME_NORMAL    = 2
GAME_HARD      = 3
GAME_VERY_HARD = 4
GAME_INSAME    = 5 #狂ってる・・・・・

#ランクリストを参照するときに使用するインデックスナンバー定数定義 game_rank_data_list[ここで定義した定数]
LIST_RANK                           = 0  #ランク数
LIST_RANK_E_SPEED_MAG               = 1  #敵スピード倍率
LIST_RANK_BULLET_SPEED_MAG          = 2  #敵狙い撃ち弾スピード倍率
LIST_RANK_RETURN_BULLET_PROBABILITY = 3  #敵撃ち返し弾発射確率
LIST_RANK_E_HP_MAG                  = 4  #敵耐久力倍率
LIST_RANK_E_BULLET_APPEND           = 5  #弾追加数
LIST_RANK_E_BULLET_INTERVAL         = 6  #弾発射間隔減少パーセント
LIST_RANK_NWAY_LEVEL                = 7  #nWAY弾のレベル(レベルが上がると扇状の幅が広がる)

#スコアリストを参照するときに使用するインデックスナンバー定数定義score_board[難易度][ここで定義した定数]
LIST_SCORE_BOARD_DIFFICULTY               =  0 #難易度
LIST_SCORE_BOARD_RANKING                  =  1 #順位
LIST_SCORE_BOARD_NAME                     =  2 #名前
LIST_SCORE_BOARD_SCORE                    =  3 #得点
LIST_SCORE_BOARD_LOOP                     =  4 #周回数
LIST_SCORE_BOARD_CLEAR_STAGE              =  5 #クリアしたステージ数
LIST_SCORE_BOARD_SHIP_USED                =  6 #使用した機体
LIST_SCORE_BOARD_SHIP_SLOT0               =  7 #スロット0に装備されたメダルID
LIST_SCORE_BOARD_SHIP_SLOT1               =  8 #スロット1に装備されたメダルID
LIST_SCORE_BOARD_SHIP_SLOT2               =  9 #スロット2に装備されたメダルID
LIST_SCORE_BOARD_SHIP_SLOT3               = 10 #スロット3に装備されたメダルID
LIST_SCORE_BOARD_SHIP_SLOT4               = 11 #スロット4に装備されたメダルID
LIST_SCORE_BOARD_SHIP_SLOT5               = 12 #スロット5に装備されたメダルID

#ゲーム開始時に追加されるクロー数の定数定義
NO_CLAW      = 0
ONE_CLAW     = 1
TWO_CLAW     = 2
THREE_CLAW   = 3

#ステージクリア時に回復するシールド値
REPAIR_SHIELD0 = 0
REPAIR_SHIELD1 = 1
REPAIR_SHIELD2 = 2
REPAIR_SHIELD3 = 3

#次の周回に移る時のパワーアップアイテム関連の動作
LOOP_POWER_CONTINUE            = 0    #全てのメインウェポンとミサイルの状態は次週にもそのまま引き継がれます
LOOP_ONE_LEVEL_DOWN            = 1    #メインウェポンが1レベルダウンします
LOOP_TWO_LEVEL_DOWN            = 2    #メインウェポンが2レベルダウンします
LOOP_THREE_LEVEL_DOWN          = 3    #メインウェポンが3レベルダウンします
LOOP_FOUR_LEVEL_DOWN           = 4    #メインウェポンが4レベルダウンします
LOOP_FIVE_LEVEL_DOWN           = 5    #メインウェポンが5レベルダウンします
LOOP_MAIN_WEAPON_TYPE_RESET    = 10   #メインウェポンのタイプのみ初期化されます 例 5WAYバルカンショット→初期バルカンショット  3WAYレーザー→通常のレーザー ウェーブカッターLV4→ウェーブカッターLV1
LOOP_MAIN_WEAPON_MISSILE_TYPE_RESET = 90   #メインウェポンとミサイルのタイプが初期化されます 例 5WAYバルカンショット→初期バルカンショット ツインミサイル4段階目→ツインミサイル1段階目
LOOP_ALL_RESET                 = 100  #メインウェポンもミサイルもゲーム開始時と同じ初期状態に戻ります

#!ステージの名称関連の定数定義################################################################
STAGE_MOUNTAIN_REGION         =  1 #ステージ1  山岳地帯          Mountain Region
STAGE_ADVANCE_BASE            =  2 #ステージ2  前線基地          Advance Base
STAGE_VOLCANIC_BELT           =  3 #ステージ3  火山地帯          Volcanic Belt
STAGE_NIGHT_SKYSCRAPER        =  4 #ステージ4  夜間超高層ビル地帯 Night Skyscraper
STAGE_AMPHIBIOUS_ASSAULT_SHIP =  5 #ステージ5  強襲揚陸艦襲撃     Amphibious Assault Ship
STAGE_DEEP_SEA_TRENCH         =  6 #ステージ6  深海海溝          Deep Sea Trench
STAGE_INTERMEDIATE_FORTRESS   =  7 #ステージ7  中間要塞          Intermediate Fortress
STAGE_ESCAPE_FORTRESS         =  8 #ステージ8  要塞脱出          Escape Fortress
STAGE_BOSS_RUSH               =  9 #ステージ9  連続強敵襲来       Boss Rush
STAGE_CHANCE_MEETING          = 10 #ステージ10 邂逅              Chance Meeting

#背景スクロールの種類
SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR               = 0 #横3重スクロール+星スクロール
SCROLL_TYPE_8WAY_SCROLL_AND_RASTER               = 1 #8方向スクロール+ラスタースクロール
SCROLL_TYPE_HEIGHT_FREE_SCROLL_AND_TRIPLE_SCROLL = 2 #縦2画面フリースクロール+横3重スクロール+(選択性の星スクロール)

#クロー関連の定数定義（主にトレースクロー）
TRACE_CLAW_COUNT       =  4 #トレースクローの数
TRACE_CLAW_INTERVAL    = 60 #トレースクローの間隔
TRACE_CLAW_BUFFER_SIZE = 60 #トレースクローのバッファーサイズ   1フレームは60分の1秒 60フレームで1秒分となります
CLAW_RAPID_FIRE_NUMBER =  2 #クローの最大連射数

SHIP_EXPLOSION_TIMER_LIMIT = 180 #自機が爆発した後、まだどれだけゲームが進行し続けるかのタイマー限界数
GAME_OVER_TIMER_LIMIT      = 180 #ゲームオーバーダイアログを表示した後まだどれだけゲームが進行し続けるのかのタイマー限界数

FADE_IN  = 0               #フェードインアウト用エフェクトスクリーン用の定数定義 0=in 1=out
FADE_OUT = 1

FLAG_OFF = 0               #フラグオフ・・・・・
FLAG_ON  = 1               #フラグオン！

DISP_OFF           =  0 #0=表示しない
DISP_ON            =  1 #1=表示する 

#イメージバンクの定数定義
IMG0 = 0 #イメージバンク0
IMG1 = 1 #イメージバンク1
IMG2 = 2 #イメージバンク2

#タイルマップナンバーの定数定義
TM0  = 0 #タイルマップ0
TM1  = 1 #タイルマップ1
TM2  = 2 #タイルマップ2
TM3  = 3 #タイルマップ3
TM4  = 4 #タイルマップ4
TM5  = 5 #タイルマップ5
TM6  = 6 #タイルマップ6
TM7  = 7 #タイルマップ7

#移動モードに入る定数定義 self.move_modeに入ります
MOVE_MANUAL = 0   #手動移動モード   パッドやキーボード入力によって移動
MOVE_AUTO   = 1   #自動移動モード   イベントによる自動移動モードとなり設定された位置まで自動で移動して行きます

#リプレイ機能のステータスです self.replay_statusに入ります
REPLAY_STOP   = 0 #何も作動してない状態です リプレイデータ記録無し,再生無し
REPLAY_RECORD = 1 #リプレイデータを記録中です
REPLAY_PLAY   = 2 #リプレイデータを再生中です

#パッド入力でのリプレイデータ記録に使用する定数定義
PAD_NONE    =    0 #0b 0000 0000 Low byte
PAD_UP      =    1 #0b 0000 0001
PAD_DOWN    =    2 #0b 0000 0010
PAD_LEFT    =    4 #0b 0000 0100
PAD_RIGHT   =    8 #0b 0000 1000
PAD_A       =   16 #0b 0001 0000
PAD_B       =   32 #0b 0010 0000
PAD_X       =   64 #0b 0100 0000
PAD_Y       =  128 #0b 1000 0000

PAD_SELECT  =    1 #0b 0000 0001 High byte
PAD_START   =    2 #0b 0000 0010 
PAD_LEFT_S  =    4 #0b 0000 0100 
PAD_RIGHT_S =    8 #0b 0000 1000 

#リプレイモードでの毎ステージ開始時の自機データの記録用で使用する定数(ST_はSTAGEの略称です)
ST_SCORE                       =  0   #毎ステージごとのスコア
ST_MY_SHIELD                   =  1   #自機のシールド耐久値
ST_MY_SPEED                    =  2   #自機のスピード
ST_SELECT_SHOT_ID              =  3   #現在使用しているショットのIDナンバー
ST_SHOT_EXP                    =  4   #自機ショットの経験値
ST_SHOT_LEVEL                  =  5   #自機ショットのレベル
ST_SHOT_SPEED_MAGNIFICATION    =  6   #自機ショットのスピードに掛ける倍率
ST_SHOT_RAPID_OF_FIRE          =  7   #自機ショットの連射数
ST_MISSILE_EXP                 =  8   #自機ミサイルの経験値
ST_MISSILE_LEVEL               =  9   #自機ミサイルのレベル
ST_MISSILE_SPEED_MAGNIFICATION = 10   #自機ミサイルのスピードに掛ける倍率
ST_MISSILE_RAPID_OF_FIRE       = 11   #自機ミサイルの連射数
ST_SELECT_SUB_WEAPON_ID        = 12   #現在使用しているサブウェポンのIDナンバー
ST_CLAW_TYPE                   = 13   #クローのタイプ
ST_CLAW_NUMBER                 = 14   #クローの装備数
ST_CLAW_DIFFERENCE             = 15   #クロ―同士の角度間隔
ST_TRACE_CLAW_INDEX            = 16   #トレースクロー（オプション）時のトレース用配列のインデックス値
ST_TRACE_CLAW_DISTANCE         = 17   #トレースクロー同士の間隔
ST_FIX_CLAW_MAGNIFICATION      = 18   #フイックスクロー同士の間隔の倍率
ST_REVERSE_CLAW_SVX            = 19   #リバースクロー用の攻撃方向ベクトル(x軸)
ST_REVERSE_CLAW_SVY            = 20   #リバースクロー用の攻撃方向ベクトル(y軸)
ST_CLAW_SHOT_SPEED             = 21   #クローショットのスピード
ST_LS_SHIELD_HP                = 22   #L'sシールドの耐久力

ST_SHIP_ID                     = 23   #使用している機体のIDナンバー
ST_SHIP_LEVEL                  = 24   #使用している機体のレベル
ST_SHIP_EXP                    = 25   #使用している機体の経験値

ST_SLOT1                       = 26   #スロット1にはめ込まれているメダルIDナンバーが入ります
ST_SLOT2                       = 27   #スロット2にはめ込まれているメダルIDナンバーが入ります
ST_SLOT3                       = 28   #スロット3にはめ込まれているメダルIDナンバーが入ります
ST_SLOT4                       = 29   #スロット4にはめ込まれているメダルIDナンバーが入ります
ST_SLOT5                       = 30   #スロット5にはめ込まれているメダルIDナンバーが入ります
ST_SLOT6                       = 31   #スロット6にはめ込まれているメダルIDナンバーが入ります
ST_SLOT7                       = 32   #スロット7にはめ込まれているメダルIDナンバーが入ります

ST_SCORE_STAR_MAG              = 33   #スコアスターの取得倍率が入ります

ST_SUB_WEAPON_TAIL_SHOT_LEV         = 34   #サブウェポンID0のテイルショットのレベル
ST_SUB_WEAPON_PENETRATE_ROCKET_LEV  = 35   #サブウェポンID1のペネトレートロケットのレベル
ST_SUB_WEAPON_SEARCH_LASER_LEV      = 36   #サブウェポンID2のサーチレーザーのレベル
ST_SUB_WEAPON_HOMING_MISSILE_LEV    = 37   #サブウェポンID3のホーミングミサイルのレベル
ST_SUB_WEAPON_SHOCK_BUMPER_LEV      = 38   #サブウェポンID4のショックバンバーのレベル
ST_SUB_WEAPON_ID5_LEV               = 39   #サブウェポンID5のレベル
ST_SUB_WEAPON_ID6_LEV               = 40   #サブウェポンID6のレベル
ST_SUB_WEAPON_ID7_LEV               = 41   #サブウェポンID7のレベル
ST_SUB_WEAPON_ID8_LEV               = 42   #サブウェポンID8のレベル
ST_SUB_WEAPON_ID9_LEV               = 43   #サブウェポンID9のレベル




#パーティクルの種類
PARTICLE_DOT            =  0 #パーティクルタイプ 1~2ドット描画タイプ(破壊後のエフェクト)
PARTICLE_CIRCLE         =  1 #パーティクルタイプ 円形パーティクル   (破壊後のエフェクト)
PARTICLE_LINE           =  2 #パーティクルタイプ ラインパーティクル (跳ね返りエフェクト)
PARTICLE_FIRE_SPARK     =  3 #パーティクルタイプ 大気圏突入時の火花 (火花が飛び散るエフェクト)

PARTICLE_SHOT_DEBRIS    =  4 #パーティクルタイプ 自機ショットの破片(デブリ)(障害物に当たったエフェクト)
PARTICLE_MISSILE_DEBRIS =  5 #パーティクルタイプ 自機ミサイルの破片(デブリ)(障害物に当たったエフェクト)

PARTICLE_BOSS_DEBRIS1   =  6 #パーティクルタイプ ボスの破片1 (破壊後のエフェクト)かなり大きい金属プレート
PARTICLE_BOSS_DEBRIS2   =  7 #パーティクルタイプ ボスの破片2 (破壊後のエフェクト)回転するブロック状な物
PARTICLE_BOSS_DEBRIS3   =  8 #パーティクルタイプ ボスの破片3 (破壊後のエフェクト)ホワイト系のスパーク 
PARTICLE_BOSS_DEBRIS4   =  9 #パーティクルタイプ ボスの破片4 (破壊後のエフェクト)橙色系の落下する火花
PARTICLE_BOSS_DEBRIS5   = 10 #パーティクルタイプ ボスの破片5 (破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS6   = 11 #パーティクルタイプ ボスの破片6 (破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS7   = 12 #パーティクルタイプ ボスの破片7 (破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS8   = 13 #パーティクルタイプ ボスの破片8 (破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS9   = 14 #パーティクルタイプ ボスの破片9 (破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS10  = 15 #パーティクルタイプ ボスの破片10(破壊後のエフェクト)

PARTICLE_BOSS_DEBRIS_FREE_IMAGE = 30 #パーティクルタイプ ボスの破片(自由に定義できる破片タイプ)


#背景オブジェクトの種類
BG_OBJ_CLOUD1,BG_OBJ_CLOUD2,BG_OBJ_CLOUD3,BG_OBJ_CLOUD4,BG_OBJ_CLOUD5      = 0,1,2,3,4     #雲小1~5
BG_OBJ_CLOUD6,BG_OBJ_CLOUD7,BG_OBJ_CLOUD8,BG_OBJ_CLOUD9,BG_OBJ_CLOUD10     = 5,6,7,8,9     #雲小6~10

BG_OBJ_CLOUD11,BG_OBJ_CLOUD12,BG_OBJ_CLOUD13,BG_OBJ_CLOUD14,BG_OBJ_CLOUD15   = 10,11,12,13,14  #雲中11~15
BG_OBJ_CLOUD16,BG_OBJ_CLOUD17,BG_OBJ_CLOUD18                                 = 15,16,17        #雲中16~18

BG_OBJ_CLOUD19,BG_OBJ_CLOUD20,BG_OBJ_CLOUD21                                 = 18,19,20        #雲大19~21

BG_OBJ_CLOUD22                                                               = 21              #雲特大22

#爆発パターンの種類
EXPLOSION_NORMAL           =  0 #標準サイズ(8x8サイズ)の敵を倒したときの爆発パターン
EXPLOSION_MIDDLE           =  1 #スクランブルハッチや重爆撃機系の敵を倒したときの中くらいの爆発パターン
EXPLOSION_BOSS_PARTS_SMOKE =  2 #ボスのパーツが爆発した後に跳んでいく煙のパターン
EXPLOSION_MY_SHIP          = 10 #自機の爆発パターン

#!メインメニューで使用する定数定義(0階層目) ###############################################################################################
MENU_GAME_START       =  0 #ゲームスタート！
MENU_DIFFICULTY       =  1 #難易度選択
MENU_SELECT_SHIP      =  2 #自機選択
MENU_MEDAL            =  3 #メダル装備
MENU_SCORE_BOARD      =  4 #スコアボード
MENU_STATUS           =  5 #ステータス表示
MENU_NAME_ENTRY       =  6 #ネームエントリー
MENU_CONFIG           =  7 #コンフィグ
MENU_REPLAY           =  8 #リプレイ再生
MENU_SELECT_STAGE     =  9 #セレクトステージ ステージ選択
MENU_SELECT_LOOP      = 10 #周回数選択
MENU_BOSS_MODE        = 11 #ボスモード選択
MENU_EXIT             = 12 #ゲーム終了(退出)

MENU_HITBOX           = 50 #ヒットボックス表示非表示選択

#サブメニューで使用する定数定義(1階層目)
MENU_SELECT_STAGE_1, MENU_SELECT_STAGE_2, MENU_SELECT_STAGE_3, MENU_SELECT_STAGE_4, MENU_SELECT_STAGE_5  =  0, 1, 2, 3, 4
MENU_SELECT_STAGE_6, MENU_SELECT_STAGE_7, MENU_SELECT_STAGE_8, MENU_SELECT_STAGE_9, MENU_SELECT_STAGE_10 =  5, 6, 7, 8, 9
MENU_SELECT_STAGE_11,MENU_SELECT_STAGE_12,MENU_SELECT_STAGE_13,MENU_SELECT_STAGE_14,MENU_SELECT_STAGE_15 = 10,11,12,13,14

MENU_SELECT_LOOP_1, MENU_SELECT_LOOP_2, MENU_SELECT_LOOP_3  = 0, 1, 2
MENU_SELECT_LOOP_4, MENU_SELECT_LOOP_5, MENU_SELECT_LOOP_6  = 3, 4, 5
MENU_SELECT_LOOP_7, MENU_SELECT_LOOP_8, MENU_SELECT_LOOP_9  = 6, 7, 8
MENU_SELECT_LOOP_10,MENU_SELECT_LOOP_11,MENU_SELECT_LOOP_12 = 9,10,11

MENU_BOSS_MODE_OFF,MENU_BOSS_MODE_ON = 0,1
MENU_HITBOX_OFF,MENU_HITBOX_ON = 0,1

MENU_NAME_ENTRY_OK = 8

MENU_CONFIG_SCREEN_MODE   =  0
MENU_CONFIG_JOYPAD_ASSIGN =  3
MENU_CONFIG_INITIALIZE    = 10

MENU_CONFIG_RETURN = 11

MENU_CONFIG_JOYPAD_ASSIGN_FIRE_AND_SUBWEAPON  =  0 
MENU_CONFIG_JOYPAD_ASSIGN_MISSILE             =  1
MENU_CONFIG_JOYPAD_ASSIGN_MAIN_WEAPON_CHANGE  =  2
MENU_CONFIG_JOYPAD_ASSIGN_SUB_WEAPON_CHANGE   =  3
MENU_CONFIG_JOYPAD_ASSIGN_SPEED               =  4

MENU_CONFIG_JOYPAD_ASSIGN_PAUSE               =  6
MENU_CONFIG_JOYPAD_ASSIGN_CLAW_STYLE          =  7
MENU_CONFIG_JOYPAD_ASSIGN_CLAW_DISTANCE       =  8

MENU_CONFIG_JOYPAD_ASSIGN_DEFAULT             = 10
MENU_CONFIG_JOYPAD_ASSIGN_CLEAR               = 11
MENU_CONFIG_JOYPAD_ASSIGN_SAVE_AND_RETURN     = 12

MENU_MEDAL_MYSHIP_MEDAL_AREA = 0

MENU_EXIT_NO = 0
MENU_EXIT_YES = 1

#サブメニューで使用する定数定義(2階層目)
MENU_CONFIG_INITIALIZE_SCORE       = 0
MENU_CONFIG_INITIALIZE_NAME        = 1
MENU_CONFIG_INITIALIZE_MEDAL       = 2
MENU_CONFIG_INITIALIZE_ACHIEVEMENT = 3
MENU_CONFIG_INITIALIZE_ALL         = 4
MENU_CONFIG_INITIALIZE_SHIP        = 5
MENU_CONFIG_INITIALIZE_RETURN      = 6

#セレクトカーソルのタイプ
CURSOR_TYPE_NO_DISP   = 0 #セレクトカーソルは表示しない
CURSOR_TYPE_NORMAL    = 1 #通常の横向きのクロー回転アニメーションカーソル
CURSOR_TYPE_UNDER_BAR = 2 #アンダーバータイプ
CURSOR_TYPE_BOX_FLASH = 3 #点滅囲み矩形タイプ

#セレクトカーソルのサイズ(セレクトカーソルのタイプが点滅囲み矩形タイプのみ機能します)
CURSOR_SIZE_NORMAL               = 0 #通常サイズです(縦10ドット横10ドット)
CURSOR_SIZE_RIGHT2_EXPAND        = 1 #点滅囲み矩形タイプのカーソルで右方向に2キャラ分拡張
CURSOR_SIZE_LEFT1_RIGHT1_EXPAND  = 2 #点滅囲み矩形タイプのカーソルで左右方向にそれぞれ1キャラ分拡張
CURSOR_SIZE_LEFT2_EXPAND         = 3 #点滅囲み矩形タイプのカーソルで左方向に2キャラ分拡張
CURSOR_SIZE_WINDOW_WIDTH_EXPAND  = 9 #ウィンドウの横幅一杯まで伸ばしたサイズの囲み矩形にします

#セレクトカーソルの移動音 pyxelのsndの番号を使って定義してね～～♪
CURSOR_MOVE_SE_NORMAL   = 16
CURSOR_MOVE_SE_TYPE1    = 1
CURSOR_MOVE_SE_TYPE2    = 2
CURSOR_MOVE_SE_TYPE3    = 3
CURSOR_MOVE_SE_TYPE4    = 4

CURSOR_PUSH_SE_NORMAL   = 19
CURSOR_PUSH_SE_TYPE1    = 1
CURSOR_PUSH_SE_TYPE2    = 2
CURSOR_PUSH_SE_TYPE3    = 3
CURSOR_PUSH_SE_TYPE4    = 4

CURSOR_OK_SE_NORMAL     = 17
CURSOR_OK_SE_TYPE1      = 1
CURSOR_OK_SE_TYPE2      = 2
CURSOR_OK_SE_TYPE3      = 3
CURSOR_OK_SE_TYPE4      = 4

CURSOR_CANCEL_SE_NORMAL   = 18
CURSOR_CANCEL_SE_TYPE1    = 1
CURSOR_CANCEL_SE_TYPE2    = 2
CURSOR_CANCEL_SE_TYPE3    = 3
CURSOR_CANCEL_SE_TYPE4    = 4

CURSOR_BOUNCE_SE_NORMAL     = 20
CURSOR_BOUNCE_SE_TYPE1      = 1
CURSOR_BOUNCE_SE_TYPE2      = 2
CURSOR_BOUNCE_SE_TYPE3      = 3
CURSOR_BOUNCE_SE_TYPE4      = 4

#カーソルが現在指し示しているアイテムの説明文を表示するかどうかのフラグ
COMMENT_FLAG_OFF            = 0 #表示しない
COMMENT_FLAG_ON             = 1 #表示する

#セレクトカーソルの動き方
CURSOR_MOVE_UD               =  0 #セレクトカーソルの動きは上下のみです 「UD」はUpDownの頭文字です
CURSOR_MOVE_UD_SLIDER        =  1 #セレクトカーソルは上下に動かすことができ、左右の入力でスライダーを動かせます(CONFIGで使用してます)
CURSOR_MOVE_UD_SLIDER_BUTTON =  2 #セレクトカーソルは上下に動かすことができ、左右の入力でスライダーを動かせます ON/OFF切り替えの項目ではボタンを押すことでも切り替えができます
CURSOR_MOVE_LR               =  3 #セレクトカーソルの動きは左右のみです LR=Left Right
CURSOR_MOVE_LR_SLIDER        =  4 #セレクトカーソルは左右に動かすことができ、上下の入力でスライダーを動かせます(NAME ENTRYで使用してます)
CURSOR_MOVE_LR_SLIDER_BUTTON =  5 #セレクトカーソルは左右に動かすことができ、上下の入力でスライダーを動かせます ON/OFF切り替えの項目ではボタンを押すことでも切り替えができます
CURSOR_MOVE_4WAY             =  6 #上下左右4方向に動かせます(MEDALで使用してます)
CURSOR_MOVE_4WAY_BUTTON      =  7 #上下左右4方向に動かせます(ボタンを押すと現在のカーソル位置のアイテムがアクティブとなります)
CURSOR_MOVE_8WAY             =  8 #斜め移動も含んだ8方向に動かせます
CURSOR_MOVE_8WAY_BUTTON      =  9 #斜め移動も含んだ8方向に動かせます(ボタンを押すと現在のカーソル位置のアイテムがアクティブとなります)
CURSOR_MOVE_SHOW_PAGE        = 10 #セレクトカーソルは表示せずLRキーもしくはLショルダーRショルダーで左右に頁をめくる動作です

#カーソルの移動量
STEP3,STEP4,STEP5,STEP6,STEP7,STEP8,STEP9,STEP10 = 3,4,5,6,7,8,9,10

#メニューのレイヤー数定数定義
MENU_LAYER0                  = 0 #レイヤー数0でメニュー階層は0
MENU_LAYER1                  = 1 #レイヤー数1でメニュー階層は1
MENU_LAYER2                  = 2 #レイヤー数2でメニュー階層は2
MENU_LAYER3                  = 3 #レイヤー数3でメニュー階層は3

#メニューで選ばれたアイテムの定数定義
UNSELECTED                   = -1  #まだ未選択なので-1

#背景BGスクロール面を表示するかしないかの定数定義
FRONT_BG_DISP_OFF   = 0   #BG背景(手前)表示オフ
FRONT_BG_DISP_ON    = 1   #               オン

CENTER_BG_DISP_OFF  = 0   #BG背景(中央)表示オフ
CENTER_BG_DISP_ON   = 1   #               オン

BACK_BG_DISP_OFF    = 0   #BG背景(奥)表示オフ
BACK_BG_DISP_ON     = 1   #             オン

#パワーアップアイテム類のtype定数の定義 obtain_itemクラスのitem_typeに代入されます
ITEM_SHOT_POWER_UP     = 1      #ショットアイテム
ITEM_MISSILE_POWER_UP  = 2      #ミサイルアイテム
ITEM_SHIELD_POWER_UP   = 3      #シールドアイテム

ITEM_CLAW_POWER_UP     = 4      #クローアイテム
ITEM_TRIANGLE_POWER_UP = 5      #トライアングルアイテム（ショット、ミサイル、シールド）

ITEM_TAIL_SHOT_POWER_UP        = 10    #テイルショットアイテム
ITEM_PENETRATE_ROCKET_POWER_UP = 11    #ペネトレートロケットアイテム
ITEM_SEARCH_LASER_POWER_UP     = 12    #サーチレーザーアイテム
ITEM_HOMING_MISSILE_POWER_UP   = 13    #ホーミングミサイルアイテム
ITEM_SHOCK_BUMPER_POWER_UP     = 14    #ショックバンパーアイテム 

ITEM_SCORE_STAR                = 20    #スコアスター(得点アイテム)

#!ステージのイベントリストで使う定数の定義
EVENT_ENEMY              = 0  #敵出現
EVENT_ADD_APPEAR_ENEMY   = 1  #敵出現（早回しによる敵の追加出現）
EVENT_FAST_FORWARD_NUM   = 2  #早回しに関する編隊群のパラメーターを設定するイベント

EVENT_SCROLL                      = 60 #スクロール制御
EVENT_DISPLAY_STAR                = 61 #星のスクロールのon/off
EVENT_CHANGE_BG_CLS_COLOR         = 62 #背景でまず最初に塗りつぶす色を指定する(初期状態は黒で塗り潰してます) CLSカラーの指定
EVENT_CHANGE_BG_TRANSPARENT_COLOR = 63 #背景マップを敷き詰める時の透明色を指定する(初期状態は黒)        TRANSPARENTカラーの指定
EVENT_CLOUD                       = 64 #背景雲の表示設定
EVENT_RASTER_SCROLL               = 65 #ラスタースクロールの制御
EVENT_BG_SCREEN_ON_OFF            = 66 #各BGスクリーンの表示のオンオフ
EVENT_ENTRY_SPARK_ON_OFF          = 67 #大気圏突入の火花エフェクト表示のオンオフ

EVENT_DISPLAY_CAUTION    = 70 #CAUTION.注意表示
EVENT_COMMANDER_MESSSAGE = 71 #司令からの通信メッセージ

EVENT_MIDDLE_BOSS   = 80 #中ボス出現
EVENT_WARNING       = 90 #WARNING.警告表示
EVENT_BOSS          = 100#ボスキャラ出現

#イベントリスト・スクロール制御関連の定数定義 EVENT_SCROLLの直後に記述されます 
SCROLL_NUM_SET               = 0  #スクロール関連のパラメーター設定
SCROLL_START                 = 1  #スクロール開始
SCROLL_STOP                  = 2  #スクロールストップ
SCROLL_SPEED_CHANGE          = 3  #スクロールスピードチェンジ
SCROLL_SPEED_CHANGE_VERTICAL = 4  #縦スクロールスピードチェンジ

SCROLL_SPEED            = 5  #スクロールスピード直接指定
SCROLL_REVERSE          = 6  #逆スクロール開始
SCROLL_UP               = 7  #上方向にスクロール開始
SCROLL_DOWN             = 8  #下方向にスクロール開始

#イベントリスト・雲のスクロール制御関連の定数定義 EVENT_CLOUDの直後に記述されます
CLOUD_NUM_SET          = 0  #雲のパラメータ設定
CLOUD_START            = 1  #雲を流すのを開始する
CLOUD_STOP             = 2  #雲を流すのを停止する

#イベントリスト BGスクロールオンオフの制御関連の定数定義 EVENT_BG_SCREEN_ON_OFFの直後に記述されます
BG_BACK   = 0 #BGスクリーン奥
BG_MIDDLE = 1 #BGスクリーン真ん中
BG_FRONT  = 2 #BGスクリーン手前

#背景の星のスクロールの有無
STAR_SCROLL_ON      = 1 #星スクロールあり
STAR_SCROLL_OFF     = 0 #           なし

#背景ラスタスクロールの有無 EVENT_RASTER_SCROLLの直後に記述されます
RASTER_SCROLL_ON    = 1 #ラスタースクロールあり
RASTER_SCROLL_OFF   = 0 #                なし

#背景ラスタスクロールの種類
RASTER_NORMAL      = 0 #奥と手前のラインごとのスクロールスピードの差で奥行き感を出すタイプ (流れるスピードはスクロールスピードに依存します)
RASTER_WAVE        = 1 #x軸にたいして波打つラスタースクロールタイプ(x座標オフセット値を加減算して波打つ感じを表現します)

#火花エフェクトの表示の仕方(大気圏突入シーンなどのエフェクトで使用) EVENT_ENTRY_SPARK_ON_OFFの直後に記述されます
RASTER_SCROLL_ON    = 1 #ラスタースクロールあり
SPARK_OFF = 0              #火花表示なし
SPARK_ON  = 1              #火花表示あり

# 敵キャラの名前(タイプナンバー)定数定義#################################### 敵の名称として連番で定数定義していましたが20231216より列挙型でautoを使用して自動で定数定義するようにしました(中に入る数字はどんな数値でも良い為です)
# CIR_COIN           =  1  #無人編隊戦闘機 サーコイン（サークルコイン）
# SAISEE_RO          =  2  #回転戦闘機サイシーロ(サインカーブを描く敵)
# HOUDA_UNDER        =  3  #固定砲台ホウダ 下
# HOUDA_UPPER        =  4  #固定砲台ホウダ 上
# HOPPER_CHAN2       =  5  #はねるホッパーチャンmk2
# MIST_M54           =  6  #謎の回転飛翔体M54
# TWIN_ARROW_SIN     =  7  #真！(SIN)ツインアロー
# TWIN_ARROW         =  8  #自機を追尾してくるツインアロー
# ROLBOARD           =  9  #ロルボードＹ軸を合わせた後突っ込んで来る怖い
# KURANBURU_UNDER    = 10  #クランブルアンダー(スクランブルハッチ)
# KURANBURU_UPPER    = 11  #クランブルアッパー(スクランブルハッチ)
# RAY_BLASTER        = 12  #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
# GREEN_LANCER       = 13  #3way弾を出してくるグリーンランサー・翠の硬い奴(ミサイルパワーアップアイテムを持っている！)
# TEMI               = 14  #テミー(アイテムキャリアー)
# MUU_ROBO           = 15  #ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
# CLAMPARION         = 16  #2機一体で挟みこみ攻撃をしてくるクランパリオン
# ROLL_BLITZ         = 17  #ロールブリッツ 画面内のあらかじめ決められた場所へスプライン曲線で移動,そこについたら狙い撃ち弾を出して画面外へ高速離脱
# VOLDAR             = 18  #ボルダー 硬めの弾バラマキ重爆撃機
# ROLL_BLITZ_POINTER = 19  #ロールブリッツポインター(最大5定点を滑らかに通過していくロールブリッツ)

#!敵キャラの名前(タイプナンバー)定数定義####################################
#2023 12/16より別クラスにて列挙型を使用し自動で任意の数値を定義するようにしました
class EnemyName(IntEnum):
    CIR_COIN           =  auto()  #無人編隊戦闘機 サーコイン（サークルコイン）
    SAISEE_RO          =  auto()  #回転戦闘機サイシーロ(サインカーブを描く敵)
    HOUDA_UNDER        =  auto()  #固定砲台ホウダ 下
    HOUDA_UPPER        =  auto()  #固定砲台ホウダ 上
    HOPPER_CHAN2       =  auto()  #はねるホッパーチャンmk2
    MIST_M54           =  auto()  #謎の回転飛翔体M54
    TWIN_ARROW_SIN     =  auto()  #真！(SIN)ツインアロー
    TWIN_ARROW         =  auto()  #自機を追尾してくるツインアロー
    ROLBOARD           =  auto()  #ロルボードＹ軸を合わせた後突っ込んで来る怖い
    KURANBURU_UNDER    =  auto()  #クランブルアンダー(スクランブルハッチ)
    KURANBURU_UPPER    =  auto()  #クランブルアッパー(スクランブルハッチ)
    RAY_BLASTER        =  auto()  #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
    GREEN_LANCER       =  auto()  #3way弾を出してくるグリーンランサー・翠の硬い奴(ミサイルパワーアップアイテムを持っている！)
    TEMI               =  auto()  #テミー(アイテムキャリアー)
    MUU_ROBO           =  auto()  #ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
    CLAMPARION         =  auto()  #2機一体で挟みこみ攻撃をしてくるクランパリオン
    ROLL_BLITZ         =  auto()  #ロールブリッツ 画面内のあらかじめ決められた場所へスプライン曲線で移動,そこについたら狙い撃ち弾を出して画面外へ高速離脱
    VOLDAR             =  auto()  #ボルダー 硬めの弾バラマキ重爆撃機
    ROLL_BLITZ_POINTER =  auto()  #ロールブリッツポインター(最大5定点を滑らかに通過していくロールブリッツ)

#マップチップで配置する敵キャラのBGナンバー 定数の定義式は(y/8)*32+(x/8)となります
BG_HOUDA_UNDER     = (64 /8) * 32 +(48 / 8) #固定砲台ホウダ 下
BG_HOUDA_UPPER     = (64 /8) * 32 +(56 / 8) #固定砲台ホウダ 上
BG_HOPPER_CHAN2    = (64 /8) * 32 +(64 / 8) #はねるホッパーチャンmk2
BG_SAISEE_RO       = (64 /8) * 32 +(72 / 8) #回転戦闘機サイシーロ(サインカーブを描く敵)
BG_KURANBURU_UNDER = (64 /8) * 32 +(80 / 8) #クランブルアンダー(スクランブルハッチ)
BG_KURANBURU_UPPER = (64 /8) * 32 +(88 / 8) #クランブルアッパー(スクランブルハッチ)
BG_TEMI            = (64 /8) * 32 +(96 / 8) #テミー(アイテムキャリアー)
BG_RAY_BLASTER     = (64 /8) * 32 +(104/ 8) #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
BG_MUU_ROBO        = (64 /8) * 32 +(112/ 8) #ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
BG_ROLL_BLITZ      = (64 /8) * 32 +(120/ 8) #ロールブリッツ 画面内のあらかじめ決められた場所へスプライン曲線で移動,そこについたら狙い撃ち弾を出して画面外へ高速離脱

#敵キャラの大きさの定数定義(この定数を見て敵を破壊した後に育成する爆発パターンの種類を決定しています)
E_SIZE_NORMAL         = 4  #敵サイズノーマル（8ドット）四方の当たり判定
E_SIZE_MIDDLE22       = 6  #敵サイズ2x2チップタイプ  中型16ドットx16ドットの当たり判定
E_SIZE_MIDDLE32       = 8  #敵サイズ3x2チップタイプ  中型24ドットx16ドットの当たり判定
E_SIZE_MIDDLE32_Y_REV = 9  #敵サイズ3x2チップタイプ  中型24ドットx16ドットの当たり判定(上下反転版)(天井に固定されてるハッチとかです)
E_SIZE_HI_MIDDLE53    =10  #敵サイズ5x3チップタイプ  準中型40ドットx24ドットの当たり判定（重爆撃機とか)
#敵キャラのIDナンバー定数定義
ID00,ID01,ID02,ID03,ID04,ID05,ID06,ID07,ID08,ID09,ID10 = 0,1,2,3,4,5,6,7,8,9,10
#敵キャラのステータス(状態)
ENEMY_STATUS_NORMAL    = 0 #通常 破壊時はscore_normalを加算
ENEMY_STATUS_ATTACK    = 1 #攻撃 破壊時はscore_attackを加算
ENEMY_STATUS_ESCAPE    = 2 #撤退 破壊時はscore_escapeを加算
ENEMY_STATUS_AWAITING  = 3 #待機 破壊時はscore_awaitingを加算
ENEMY_STATUS_DEFENSE   = 4 #防御 破壊時はscore_defenseを加算
ENEMY_STATUS_BERSERK   = 5 #怒り 破壊時はscore_berserkを加算

ENEMY_STATUS_MOVE_COORDINATE_INIT  = 10 #移動用座標初期化
ENEMY_STATUS_MOVE_BEZIER_CURVE     = 11 #ベジェ曲線で移動

#敵の攻撃方法(enemyクラスのattack_methodに入る)の定数定義
ENEMY_ATTCK_ANY                = 0  #任意攻撃(移動ルートで攻撃方法が変わるのではなく体力や自機の位置などによって攻撃方法が変化します)
ENEMY_ATTACK_NO_FIRE           = 1  #なにも攻撃しないよ
ENEMY_ATTACK_AIM_BULLET        = 2  #狙い撃ち弾
ENEMY_ATTACK_FRONT_5WAY        = 3  #前方に5way弾を撃ってきます
ENEMY_ATTACK_FRONT_GREEN_LASER = 4  #前方に細いグリーンレーザーを撃ってきます
#ヒットポイント(耐久力)の定数定義
HP00,HP01,HP02,HP03,HP04,HP05,HP06,HP07,HP08,HP09 =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
HP10,HP11,HP12,HP13,HP14,HP15,HP16,HP17,HP18,HP19 = 10,11,12,13,14,15,16,17,18,19
HP20,HP21,HP22,HP23,HP24,HP25,HP26,HP27,HP28,HP29 = 20,21,22,23,24,25,26,27,28,29
HP30,HP31,HP32,HP33,HP34,HP35,HP36,HP37,HP38,HP39 = 30,31,32,33,34,35,36,37,38,39
HP40,HP41,HP42,HP43,HP44,HP45,HP46,HP47,HP48,HP49 = 40,41,42,43,44,45,46,47,48,49
HP50,HP51,HP52,HP53,HP54,HP55,HP56,HP57,HP58,HP59 = 50,51,52,53,54,55,56,57,58,59
#ShotPower(ショットパワー)攻撃力の定数定義
SP00,SP01,SP02,SP03,SP04,SP05,SP06,SP07,SP08,SP09 =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
SP10,SP11,SP12,SP13,SP14,SP15,SP16,SP17,SP18,SP19 = 10,11,12,13,14,15,16,17,18,19
SP20,SP21,SP22,SP23,SP24,SP25,SP26,SP27,SP28,SP29 = 20,21,22,23,24,25,26,27,28,29
SP30,SP31,SP32,SP33,SP34,SP35,SP36,SP37,SP38,SP39 = 30,31,32,33,34,35,36,37,38,39
SP40,SP41,SP42,SP43,SP44,SP45,SP46,SP47,SP48,SP49 = 40,41,42,43,44,45,46,47,48,49
SP50,SP51,SP52,SP53,SP54,SP55,SP56,SP57,SP58,SP59 = 50,51,52,53,54,55,56,57,58,59
#得点の定数定義
PT01,PT02,PT03,PT04,PT05,PT06,PT07,PT08,PT09,PT10 =  1, 2, 3, 4, 5, 6, 7, 8, 9,10
PT11,PT12,PT13,PT14,PT15,PT16,PT17,PT18,PT19,PT20 = 11,12,13,14,15,16,17,18,19,20
PT21,PT22,PT23,PT24,PT25,PT26,PT27,PT28,PT29,PT30 = 21,22,23,24,25,26,27,28,29,30
PT31,PT32,PT33,PT34,PT35,PT36,PT37,PT38,PT39,PT40 = 31,32,33,34,35,36,37,38,39,40
PT41,PT42,PT43,PT44,PT45,PT46,PT47,PT48,PT49,PT50 = 41,42,43,44,45,46,47,48,49,50

PT1000 = 1000
#レベルの定数定義
LV00,LV01,LV02,LV03,LV04,LV05,LV06,LV07,LV08,LV09,LV10 = 0,1,2,3,4,5,6,7,8,9,10
#サイズ(大きさ)の定数定義 おもに画像表示用、当たり判定用としてwidthやheightに入ります
SIZE_1, SIZE_2, SIZE_3, SIZE_4, SIZE_5  =  1, 2, 3, 4, 5
SIZE_6, SIZE_7, SIZE_8, SIZE_9, SIZE_10 =  6, 7, 8, 9,10
SIZE_11,SIZE_12,SIZE_13,SIZE_14,SIZE_15 = 11,12,13,14,15
SIZE_16,SIZE_17,SIZE_18,SIZE_19,SIZE_20 = 16,17,18,19,20
SIZE_21,SIZE_22,SIZE_23,SIZE_24,SIZE_25 = 21,22,23,24,25
SIZE_26,SIZE_27,SIZE_28,SIZE_29,SIZE_30 = 26,27,28,29,30
SIZE_31,SIZE_32,SIZE_33,SIZE_34,SIZE_35 = 31,32,33,34,35
SIZE_36,SIZE_37,SIZE_38,SIZE_39,SIZE_40 = 36,37,38,39,40
SIZE_41,SIZE_42,SIZE_43,SIZE_44,SIZE_45 = 41,42,43,44,45
SIZE_46,SIZE_47,SIZE_48,SIZE_49,SIZE_50 = 46,47,48,49,50

#空中物か地上物かの判定用定数定義 enemyクラスのfloating_flagに入ります
AERIAL_OBJ = 0 #空中物(飛行物体)
GROUND_OBJ = 1 #地上物
MOVING_OBJ = 2 #地上を移動する物体(装甲車とか)

#敵弾のタイプ定数定義
# ENEMY_SHOT_NORMAL            =  0 #通常弾
# ENEMY_SHOT_SIN               =  1 #サインカーブ弾
# ENEMY_SHOT_COS               =  2 #コサインカーブ弾
# ENEMY_SHOT_LASER             =  3 #レーザービーム
# ENEMY_SHOT_GREEN_LASER       =  4 #ボスのグリーンレーザー
# ENEMY_SHOT_RED_LASER         =  5 #ボスのレッドレーザー
# ENEMY_SHOT_YELLOW_LASER      =  6 #ボスのイエローレーザー
# ENEMY_SHOT_BLUE_LASER        =  7 #ボスのブルーレーザー
# ENEMY_SHOT_RAINBOW_LASER     =  8 #ボスのレインボーレーザー
# ENEMY_SHOT_HOMING_LASER      =  9 #ホーミングレーザー(レイフォースみたいなの)
# ENEMY_SHOT_HOMING_LASER_TAIL = 10 #ホーミングレーザーの尻尾
# ENEMY_SHOT_LOCKON_LASER      = 11 #ロックオンレーザー(レイフォースみたいなの)
# ENEMY_SHOT_LOCKON_LASER_TAIL = 12 #ロックオンレーザーの尻尾
# ENEMY_SHOT_SEARCH_LASER      = 13 #サーチレーザー(イメージファイトみたいなの)
# ENEMY_SHOT_SEARCH_LASER_TAIL = 14 #サーチレーザーの尻尾
# ENEMY_SHOT_WAVE              = 15 #ウェーブカッター(ダライアスみたいなの)
# ENEMY_SHOT_RIPPLW_LASER      = 16 #リップルレーザー(グラディウスⅡみたいなの)
# ENEMY_SHOT_WAINDER_LASER     = 17 #ワインダーレーザー(グラディウスみたいなの)
# ENEMY_SHOT_CIRCLE_LASER      = 18 #サークルレーザー(イメージファイトみたいなの)
# ENEMY_SHOT_2TURN_LASER       = 19 #2回屈折サーチレーザー(ダライアスバーストみたいなの)
# ENEMY_SHOT_BOUND_LASER       = 20 #反射レーザー(R-TYPEみたいなの)
# ENEMY_SHOT_DROP_BULLET       = 21 #落下弾
# ENEMY_SHOT_CIRCLE_BULLET     = 22 #回転弾
# ENEMY_SHOT_SPLIT_BULLET      = 21 #分裂弾
# ENEMY_SHOT_HOMING_BULLET     = 23 #誘導弾
# ENEMY_SHOT_UP_LASER          = 24 #アップレーザー
# ENEMY_SHOT_DOWN_LASER        = 25 #ダウンレーザー
# ENEMY_SHOT_SPREAD_BOMB       = 26 #スプレッドボム
# ENEMY_SHOT_VECTOR_LASER      = 27 #ベクトルレーザー(グラ２みたいなの)
# ENEMY_SHOT_GREEN_CUTTER      = 28 #「ブリザーディア」が尾翼部から射出するグリーンカッター

#!敵弾のタイプ定数定義
#2023 12/16より別クラスにて列挙型を使用し自動で任意の数値を定義するようにしました
class EnemyShot(IntEnum):
    NORMAL            = auto() #通常弾
    SIN               = auto() #サインカーブ弾
    COS               = auto() #コサインカーブ弾
    LASER             = auto() #レーザービーム
    GREEN_LASER       = auto() #ボスのグリーンレーザー
    RED_LASER         = auto() #ボスのレッドレーザー
    YELLOW_LASER      = auto() #ボスのイエローレーザー
    BLUE_LASER        = auto() #ボスのブルーレーザー
    RAINBOW_LASER     = auto() #ボスのレインボーレーザー
    HOMING_LASER      = auto() #ホーミングレーザー(レイフォースみたいなの)
    HOMING_LASER_TAIL = auto() #ホーミングレーザーの尻尾
    LOCKON_LASER      = auto() #ロックオンレーザー(レイフォースみたいなの)
    LOCKON_LASER_TAIL = auto() #ロックオンレーザーの尻尾
    SEARCH_LASER      = auto() #サーチレーザー(イメージファイトみたいなの)
    SEARCH_LASER_TAIL = auto() #サーチレーザーの尻尾
    WAVE              = auto() #ウェーブカッター(ダライアスみたいなの)
    RIPPLW_LASER      = auto() #リップルレーザー(グラディウスⅡみたいなの)
    WAINDER_LASER     = auto() #ワインダーレーザー(グラディウスみたいなの)
    CIRCLE_LASER      = auto() #サークルレーザー(イメージファイトみたいなの)
    TURN_LASER        = auto() #2回屈折サーチレーザー(ダライアスバーストみたいなの)
    BOUND_LASER       = auto() #反射レーザー(R-TYPEみたいなの)
    DROP_BULLET       = auto() #落下弾
    CIRCLE_BULLET     = auto() #回転弾
    SPLIT_BULLET      = auto() #分裂弾
    HOMING_BULLET     = auto() #誘導弾
    UP_LASER          = auto() #アップレーザー
    DOWN_LASER        = auto() #ダウンレーザー
    SPREAD_BOMB       = auto() #スプレッドボム
    VECTOR_LASER      = auto() #ベクトルレーザー(グラ２みたいなの)
    GREEN_CUTTER      = auto() #「ブリザーディア」が尾翼部から射出するグリーンカッター

#!分裂弾の種類の定数定義
ENEMY_SHOT_DIVISION_3WAY    = 1 #3way分裂弾
ENEMY_SHOT_DIVISION_5WAY    = 2 #5way分裂弾
ENEMY_SHOT_DIVISION_7WAY    = 3 #7way分裂弾
ENEMY_SHOT_DIVISION_9WAY    = 4 #9way分裂弾

#育成する打ち返し弾の種類 Explosionクラスのreturn_bullet_typeに入る,難易度リスト(game_difficulty_list)でも使用してます
RETURN_BULLET_NONE      = 0 #撃ち返ししない
RETURN_BULLET_AIM       = 1 #自機狙い弾を1発撃ち返す
RETURN_BULLET_DELAY_AIM = 2 #自機狙い撃ち返し＆遅れて更に自機狙い弾を撃ち返す 2発
RETURN_BULLET_3WAY      = 3 #自機狙いの3way弾を撃ち返してくる


#敵弾クラスで使用する定数定義 主にcollision_typeやwidth,heightに入る
ESHOT_COL_MIN88 = 0 #最小の正方形8x8ドットでの当たり判定タイプ    collision_typeに入る
ESHOT_COL_BOX   = 1 #長方形での当たり判定タイプ                  collision_typeに入る 判定はwidth,heightを見て行います

ESHOT_SIZE1  =  1 #敵ショットのサイズ  1ドット width,heightに入ります
ESHOT_SIZE2  =  2 #敵ショットのサイズ  2ドット
ESHOT_SIZE3  =  3 #敵ショットのサイズ  3ドット
ESHOT_SIZE4  =  4 #敵ショットのサイズ  4ドット
ESHOT_SIZE5  =  5 #敵ショットのサイズ  5ドット
ESHOT_SIZE6  =  6 #敵ショットのサイズ  6ドット
ESHOT_SIZE7  =  7 #敵ショットのサイズ  7ドット
ESHOT_SIZE8  =  8 #敵ショットのサイズ  8ドット
ESHOT_SIZE9  =  9 #敵ショットのサイズ  9ドット
ESHOT_SIZE10 = 10 #敵ショットのサイズ 10ドット
ESHOT_SIZE11 = 11 #敵ショットのサイズ 11ドット
ESHOT_SIZE12 = 12 #敵ショットのサイズ 12ドット
ESHOT_SIZE13 = 13 #敵ショットのサイズ 13ドット
ESHOT_SIZE14 = 14 #敵ショットのサイズ 14ドット
ESHOT_SIZE15 = 15 #敵ショットのサイズ 15ドット
ESHOT_SIZE16 = 16 #敵ショットのサイズ 16ドット 

#敵や爆発関連の表示用のプライオリティレベルの定数定義
PRIORITY_SEND_TO_BACK  = 0  #最背面(スクロールしない背景が多いです)
PRIORITY_BACK          = 1  #背面
PRIORITY_MIDDLE        = 2  #中面
PRIORITY_BOSS_BACK     = 3  #ボスキャラの真後ろ
PRIORITY_BOSS          = 4  #ボスキャラと同面
PRIORITY_BOSS_FRONT    = 5  #ボスキャラの直ぐ手前
PRIORITY_FRONT_SCROLL  = 6  #前面スクロールのすぐ手前
PRIORITY_FRONT         = 7  #前面
PRIORITY_MORE_FRONT    = 8  #さらに前面
PRIORITY_TOP           = 9  #最前面(すべてにおいて最後に描画されるため最前面となる！)

#敵キャラが持っているアイテム類のID enemyクラスのitemに代入されます
E_NO_POW      = 0           #敵は何もパワーアップアイテムを持っていないです・・・涙
E_SHOT_POW    = 1           #敵が持っているショットアイテム定数定義
E_MISSILE_POW = 2           #敵が持っているミサイルアイテム定数定義
E_SHIELD_POW  = 3           #敵が持っているシールドアイテム定数定義

E_CLAW_POW        = 4        #敵が持っているクローアイテム定数定義

E_TRIANGLE_POW    = 5        #敵が持っている正三角形アイテム（ショット、ミサイル、シールド）アイテム定数定義

E_DESTRUCTION_POW = 6        #敵が持っている破壊アイテム定数定義（ザコ敵を殲滅させるアイテム）
E_SCORE_STAR_POW  = 7        #敵が持っているスコアスター(得点アイテム)の定数定義
E_INVINCIBLE_POW  = 8        #敵が持っている無敵アイテムの定数定義

E_TAIL_SHOT_POW        = 10     #敵が持っているテイルショットアイテム定数定義
E_PENETRATE_ROCKET_POW = 11     #敵が持っているペネトレートロケットアイテム定数定義
E_SEARCH_LASER_POW     = 12     #敵が持っているサーチレーザーアイテム定数定義
E_HOMING_MISSILE_POW   = 13     #敵が持っているホーミングミサイルアイテム定数定義
E_SHOCK_BUMPER_POW     = 14     #敵が持っているショックバンパーアイテム定数定義 

#!ボスキャラのboss_type定数定義
BOSS_BREEZARDIA        = 0 #MOUNTAIN_REGIONのボス「ブリザーディア」
BOSS_FATTY_VALGUARD    = 1 #ADVANCED_BASEのボス  「ファッティバルガード」
BOSS_MAD_CLUBUNGER     = 2 #VOLCANIC_BELTのボス  「マッドクラブンガー」

#!bossクラスのstatusに入る定数定義   (状態遷移フラグとして使用します)
BOSS_STATUS_MOVE_COORDINATE_INIT  =  0  #ボス用のステータス定数定義 移動用座標設定初期化
BOSS_STATUS_MOVE_BEZIER_CURVE     = 10  #ボス用のステータス定数定義 ベジェ曲線で移動
BOSS_STATUS_MOVE_LEMNISCATE_CURVE = 11  #ボス用のステータス定数定義 レムニスケート曲線で移動
BOSS_STATUS_MOVE_2POINT_INIT      = 12  #ボス用のステータス定数定義 移動元と移動先の2点間を移動するための座標位置設定初期化
BOSS_STATUS_MOVE_2POINT           = 13  #ボス用のステータス定数定義 2点間の移動にする

BOSS_STATUS_EXPLOSION_START    = 80  #ボス撃破！爆発開始！
BOSS_STATUS_EXPLOSION          = 81  #ボス爆発中！
BOSS_STATUS_BLAST_SPLIT_START  = 82  #ボス爆破分裂開始
BOSS_STATUS_BLAST_SPLIT        = 83  #ボス爆破分裂中
BOSS_STATUS_DISAPPEARANCE      = 89  #ボス消滅・・・・・

#bossクラスのreverseに入る定数定義(グラフイックの左右反転表示で使用します)
BOSS_GRP_NORMAL                =  1  #通常表示
BOSS_GRP_REVERSE               = -1  #反転表示

#bossクラスのattack_methodに入る定数定義 (ボスの攻撃方法)
BOSS_ATTACK_NO_FIRE               = 0 #なにも攻撃しないよ
BOSS_ATTACK_FRONT_5WAY            = 1 #前方に5way弾を撃ってきます
BOSS_ATTACK_RIGHT_GREEN_LASER     = 2 #後方に細いグリーンレーザーを撃ってきます
BOSS_ATTACK_FRONT_5WAY_AIM_BULLET = 3 #前方5way+狙い撃ち弾
BOSS_ATTACK_FRONT_5WAY_ARROW      = 4 #前方5way+ツインアロー
BOSS_ATTACK_HOMING_LASER          = 5 #ホーミングレーザー

BOSS_HP_BAR_DISPLAY_TIME = 32         #ボスの耐久力バーを表示する時間(弾が当たるたびにこの数値がカウンターに入る)

#bossクラスのweapon_statusに入る定数定義(ボスの持つ武器の状態)
WEAPON_READY          = 0    #何もしていない準備万端な状態
WEAPON_ROCK_ON        = 1    #目標を定めた状態（予兆エフェクトを表示)
WEAPON_FIRE           = 2    #武器発射中

#!SEの定数定義 ########################################################
SE_POWUP_GET      =  0
SE_VULCAN_SHOT    =  1
SE_MISSILE        =  1
SE_EXPLOSION      =  2
SE_SHIP_BROKEN    =  3
SE_LASER          =  4
SE_WAVE_CUTTER    =  5
SE_BOSS_EXPLOSION = 11
SE_SHIP_DAMAGE    = 15

#!ボタン割り当て(キーアサイン、キーコンフィグ)で使用する定数定義 アクションID 同時にCONFIG設定のPADアサイン項目のY座標(キャラ単位)としても使用します 連番にしちゃダメだよ(はぁと)
#!アクションID
ACT_SHOT_AND_SUB_WEAPON   =  0   #ショット＆サブウェポン同時発射アクションID
ACT_MISSILE               =  1   #ミサイルアクションID
ACT_MAIN_WEAPON_CHANGE    =  2   #メインウェポン切り替えアクションID
ACT_SUB_WEAPON_CHANGE     =  3   #サブウェポン切り替えアクションID
ACT_SPEED_CHANGE          =  4   #スピードチェンジアクションID

ACT_PAUSE                 =  6   #ポーズアクションID
ACT_CHANGE_CLAW_STYLE     =  7   #クロースタイルチェンジアクションID
ACT_CHANGE_CLAW_INTERVAL  =  8   #クローインターバルチェンジアクションID

ACT_DUMMY_1               =  50   #ダミーアクション用

ACT_SHOT                  =  60 #ショットアクションID
ACT_SUB_WEAPON            =  70 #サブウェポンアクションID

ACT_NO_ASSIGN             =  99 #未割当アクションID
#!ボタン割り当てリストを参照するときに使用するインデックス値ラベル self.pad_assign_list[ここに入る]
#!例 self.pad_assign_list[BTN_A]で Aボタンを押したらどのアクションIDが割り当てられているか判る、判るマン
#!初期状態はACT_SHOT_AND_SUB_WEAPONなのでショット＆サブウェポン同時発射アクションIDが割り当てられているのが判るのです
#!ボタンID
BTN_A             =  0
BTN_B             =  1
BTN_X             =  2
BTN_Y             =  3
BTN_BACK          =  4
BTN_GUIDE         =  5
BTN_START         =  6
BTN_LEFTSHOULDER  =  7
BTN_RIGHTSHOULDER =  8

BTN_KEYBOARD_SPACE = 100 #キーボードのスペースキーで決定されたときに使用

BTN_NONE          = -1 #何も割り当てられてない時用のダミーぃ

#!#########################################
#xbox-joypad vector graphics data (xboxコントローラー画像のベクター座標値データ群) XBJはX-Box-Joypadの略語です
XBJ_RATE = 0.05 #拡大率

XBJ_X001,XBJ_Y001 = 1651 * XBJ_RATE, 239 * XBJ_RATE
XBJ_X002,XBJ_Y002 = 1406 * XBJ_RATE, 239 * XBJ_RATE
XBJ_X003,XBJ_Y003 = 1150 * XBJ_RATE, 265 * XBJ_RATE
XBJ_X004,XBJ_Y004 = 1069 * XBJ_RATE, 194 * XBJ_RATE
XBJ_X005,XBJ_Y005 =  972 * XBJ_RATE, 220 * XBJ_RATE
XBJ_X006,XBJ_Y006 =  844 * XBJ_RATE, 277 * XBJ_RATE
XBJ_X007,XBJ_Y007 =  737 * XBJ_RATE, 355 * XBJ_RATE
XBJ_X008,XBJ_Y008 =  709 * XBJ_RATE, 476 * XBJ_RATE
XBJ_X009,XBJ_Y009 =  974 * XBJ_RATE, 341 * XBJ_RATE

XBJ_X010,XBJ_Y010 =  842 * XBJ_RATE, 400 * XBJ_RATE
XBJ_X011,XBJ_Y011 =  593 * XBJ_RATE, 631 * XBJ_RATE
XBJ_X012,XBJ_Y012 =  455 * XBJ_RATE, 896 * XBJ_RATE
XBJ_X013,XBJ_Y013 =  346 * XBJ_RATE,1148 * XBJ_RATE
XBJ_X014,XBJ_Y014 =  282 * XBJ_RATE,1392 * XBJ_RATE
XBJ_X015,XBJ_Y015 =  275 * XBJ_RATE,1532 * XBJ_RATE
XBJ_X016,XBJ_Y016 =  313 * XBJ_RATE,1646 * XBJ_RATE
XBJ_X017,XBJ_Y017 =  372 * XBJ_RATE,1762 * XBJ_RATE
XBJ_X018,XBJ_Y018 =  474 * XBJ_RATE,1893 * XBJ_RATE
XBJ_X019,XBJ_Y019 =  550 * XBJ_RATE,1949 * XBJ_RATE

XBJ_X020,XBJ_Y020 =  647 * XBJ_RATE,1928 * XBJ_RATE
XBJ_X021,XBJ_Y021 =  792 * XBJ_RATE,1779 * XBJ_RATE
XBJ_X022,XBJ_Y022 =  913 * XBJ_RATE,1646 * XBJ_RATE
XBJ_X023,XBJ_Y023 = 1034 * XBJ_RATE,1527 * XBJ_RATE
XBJ_X024,XBJ_Y024 = 1150 * XBJ_RATE,1442 * XBJ_RATE
XBJ_X025,XBJ_Y025 = 1290 * XBJ_RATE,1394 * XBJ_RATE
XBJ_X026,XBJ_Y026 = 1651 * XBJ_RATE,1373 * XBJ_RATE
XBJ_X027,XBJ_Y027 = 2002 * XBJ_RATE,1380 * XBJ_RATE
XBJ_X028,XBJ_Y028 = 2183 * XBJ_RATE,1424 * XBJ_RATE
XBJ_X029,XBJ_Y029 = 2246 * XBJ_RATE,1471 * XBJ_RATE

XBJ_X030,XBJ_Y030 = 2300 * XBJ_RATE,1543 * XBJ_RATE
XBJ_X031,XBJ_Y031 = 2381 * XBJ_RATE,1676 * XBJ_RATE
XBJ_X032,XBJ_Y032 = 2443 * XBJ_RATE,1790 * XBJ_RATE
XBJ_X033,XBJ_Y033 = 2497 * XBJ_RATE,1873 * XBJ_RATE
XBJ_X034,XBJ_Y034 = 2597 * XBJ_RATE,1937 * XBJ_RATE
XBJ_X035,XBJ_Y035 = 2689 * XBJ_RATE,1940 * XBJ_RATE
XBJ_X036,XBJ_Y036 = 2756 * XBJ_RATE,1949 * XBJ_RATE
XBJ_X037,XBJ_Y037 = 2839 * XBJ_RATE,1938 * XBJ_RATE
XBJ_X038,XBJ_Y038 = 2898 * XBJ_RATE,1876 * XBJ_RATE
XBJ_X039,XBJ_Y039 = 2963 * XBJ_RATE,1817 * XBJ_RATE

XBJ_X040,XBJ_Y040 = 3045 * XBJ_RATE,1712 * XBJ_RATE
XBJ_X041,XBJ_Y041 = 3089 * XBJ_RATE,1586 * XBJ_RATE
XBJ_X042,XBJ_Y042 = 3103 * XBJ_RATE,1457 * XBJ_RATE
XBJ_X043,XBJ_Y043 = 3051 * XBJ_RATE,1308 * XBJ_RATE
XBJ_X044,XBJ_Y044 = 3002 * XBJ_RATE,1164 * XBJ_RATE
XBJ_X045,XBJ_Y045 = 2955 * XBJ_RATE,1025 * XBJ_RATE
XBJ_X046,XBJ_Y046 = 2895 * XBJ_RATE, 882 * XBJ_RATE
XBJ_X047,XBJ_Y047 = 2821 * XBJ_RATE, 771 * XBJ_RATE
XBJ_X048,XBJ_Y048 = 2743 * XBJ_RATE, 642 * XBJ_RATE
XBJ_X049,XBJ_Y049 = 2680 * XBJ_RATE, 538 * XBJ_RATE

XBJ_X050,XBJ_Y050 = 2653 * XBJ_RATE, 439 * XBJ_RATE
XBJ_X051,XBJ_Y051 = 2626 * XBJ_RATE, 366 * XBJ_RATE
XBJ_X052,XBJ_Y052 = 2535 * XBJ_RATE, 289 * XBJ_RATE
XBJ_X053,XBJ_Y053 = 2431 * XBJ_RATE, 249 * XBJ_RATE
XBJ_X054,XBJ_Y054 = 2340 * XBJ_RATE, 230 * XBJ_RATE
XBJ_X055,XBJ_Y055 = 2272 * XBJ_RATE, 235 * XBJ_RATE
XBJ_X056,XBJ_Y056 = 2630 * XBJ_RATE, 492 * XBJ_RATE
XBJ_X057,XBJ_Y057 = 2573 * XBJ_RATE, 438 * XBJ_RATE
XBJ_X058,XBJ_Y058 = 2443 * XBJ_RATE, 370 * XBJ_RATE
XBJ_X059,XBJ_Y059 = 2321 * XBJ_RATE, 323 * XBJ_RATE

XBJ_X060,XBJ_Y060 = 2218 * XBJ_RATE, 286 * XBJ_RATE
XBJ_X061,XBJ_Y061 = 2121 * XBJ_RATE, 264 * XBJ_RATE
XBJ_X062,XBJ_Y062 = 1999 * XBJ_RATE, 245 * XBJ_RATE
XBJ_X063,XBJ_Y063 = 1874 * XBJ_RATE, 245 * XBJ_RATE
XBJ_X064,XBJ_Y064 = 1767 * XBJ_RATE, 241 * XBJ_RATE


XBJ_X100,XBJ_Y100 =  992 * XBJ_RATE,1004 * XBJ_RATE
XBJ_X101,XBJ_Y101 =  994 * XBJ_RATE,1108 * XBJ_RATE
XBJ_X102,XBJ_Y102 =  892 * XBJ_RATE,1112 * XBJ_RATE

XBJ_X103,XBJ_Y103 =  892 * XBJ_RATE,1234 * XBJ_RATE
XBJ_X104,XBJ_Y104 =  992 * XBJ_RATE,1234 * XBJ_RATE
XBJ_X105,XBJ_Y105 =  992 * XBJ_RATE,1316 * XBJ_RATE

XBJ_X106,XBJ_Y106 = 1114 * XBJ_RATE,1316 * XBJ_RATE
XBJ_X107,XBJ_Y107 = 1111 * XBJ_RATE,1234 * XBJ_RATE
XBJ_X108,XBJ_Y108 = 1199 * XBJ_RATE,1234 * XBJ_RATE

XBJ_X109,XBJ_Y109 = 1199 * XBJ_RATE,1108 * XBJ_RATE
XBJ_X110,XBJ_Y110 = 1111 * XBJ_RATE,1108 * XBJ_RATE
XBJ_X111,XBJ_Y111 = 1111 * XBJ_RATE,1004 * XBJ_RATE



#円座標
XBJ_XC00,XBJ_YC00 =  928 * XBJ_RATE,  722 * XBJ_RATE
XBJ_XC01,XBJ_YC01 = 1046 * XBJ_RATE, 1172 * XBJ_RATE
XBJ_XC02,XBJ_YC02 = 1651 * XBJ_RATE,  532 * XBJ_RATE
XBJ_XC03,XBJ_YC03 = 1336 * XBJ_RATE,  708 * XBJ_RATE

XBJ_XC04,XBJ_YC04 = 1958 * XBJ_RATE,  706 * XBJ_RATE
XBJ_XC05,XBJ_YC05 = 2003 * XBJ_RATE, 1140 * XBJ_RATE
XBJ_XC06,XBJ_YC06 = 2472 * XBJ_RATE, 1092 * XBJ_RATE
XBJ_XC07,XBJ_YC07 = 2660 * XBJ_RATE,  894 * XBJ_RATE
XBJ_XC08,XBJ_YC08 = 2291 * XBJ_RATE,  894 * XBJ_RATE
XBJ_XC09,XBJ_YC09 = 2472 * XBJ_RATE,  683 * XBJ_RATE

#円半径
XBJ_R0  = ( 928 -  838) * XBJ_RATE
XBJ_R0A = ( 928 -  770) * XBJ_RATE

XBJ_R1  = (1046 -  868) * XBJ_RATE
XBJ_R2  = (1651 - 1552) * XBJ_RATE
XBJ_R3  = (1336 - 1278) * XBJ_RATE

XBJ_R4  = (1958 - 1895) * XBJ_RATE
XBJ_R5  = (2003 - 1876) * XBJ_RATE
XBJ_R6  = 85 * XBJ_RATE
XBJ_R7  = 85 * XBJ_RATE
XBJ_R8  = 85 * XBJ_RATE
XBJ_R9  = 85 * XBJ_RATE