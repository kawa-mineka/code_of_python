#############################################
#主にウィンドウクラスで使用する定数定義です###
#############################################

#!ウィンドウのidの定数定義 windowクラスの window[i].window_idに入ります
WINDOW_ID_NO_MENU                        =  0 #ダミー用 ノーメニュー
WINDOW_ID_MAIN_MENU                      =  1 #タイトル画面からのメインメニュー
WINDOW_ID_SELECT_STAGE_MENU              =  2 #ステージ選択メニュー
WINDOW_ID_SELECT_LOOP_MENU               =  3 #ループ数選択メニュー
WINDOW_ID_BOSS_MODE_MENU                 =  4 #ボスモードオンオフメニュー
WINDOW_ID_HITBOX_MENU                    =  5 #ヒットボックス(当たり判定)表示オンオフメニュー(ボスのみ)
WINDOW_ID_SELECT_DIFFICULTY              =  6 #難易度選択メニュー
WINDOW_ID_SELECT_REPLAY_SLOT             =  7 #どのスロットのリプレイデータをロードするのかのメニュー
WINDOW_ID_GAME_OVER_RETURN               =  8 #ゲームオーバーから戻る時のメニュー
WINDOW_ID_GAME_OVER_RETURN_NO_SAVE       =  9 #ゲームオーバーから戻る時のメニュー(リプレイデータのセーブは無し)
WINDOW_ID_SELECT_FILE_SLOT               = 10 #リプレイデータをセーブするスロットを選択するメニュー
WINDOW_ID_SCORE_BOARD                    = 11 #スコアボードウィンドウ
WINDOW_ID_INPUT_YOUR_NAME                = 12 #名前入力ウィンドウ
WINDOW_ID_CONFIG                         = 13 #各種設定ウィンドウ(CONFIGウィンドウ)
WINDOW_ID_CONFIG_GRAPHICS                = 14 #グラフイック設定ウィンドウ
WINDOW_ID_CONFIG_SOUND                   = 15 #サウンド設定ウィンドウ
WINDOW_ID_CONFIG_CONTROL                 = 16 #コントロール設定ウィンドウ
WINDOW_ID_CONFIG_SETTING                 = 17 #ゲーム設定ウィンドウ
WINDOW_ID_STATUS                         = 18 #ステータスウィンドウ
WINDOW_ID_DUMMY_TEST                     = 19 #ダミーテスト用ウィンドウ
WINDOW_ID_ACHIEVEMENT_LIST               = 20 #実績(アチーブメント)リストウィンドウ
WINDOW_ID_MEDAL_LIST                     = 21 #メダルウィンドウリスト
WINDOW_ID_EQUIPMENT                      = 22 #装備ウィンドウ
WINDOW_ID_ITEM_LIST                      = 23 #アイテムリストウィンドウ
WINDOW_ID_EXIT                           = 24 #ゲーム終了(退出)ウィンドウ
WINDOW_ID_PAUSE_MENU                     = 25 #ポーズメニュー
WINDOW_ID_RETURN_TITLE                   = 26 #リターンタイトルウィンドウ
WINDOW_ID_SLOT                           = 27 #スロットウィンドウ
WINDOW_ID_SELECT_SHIP                    = 28 #自機選択ウィンドウ
WINDOW_ID_INITIALIZE                     = 29 #システムデータ初期化選択ウィンドウ
WINDOW_ID_SELECT_YES_NO                  = 30 #イエスノー選択ウィンドウ
WINDOW_ID_PRINT_INIT_SCORE               = 31 #スコアデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_PRINT_INIT_NAME                = 32 #ネームデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_PRINT_INIT_SHIP                = 33 #シップデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_PRINT_INIT_MEDAL               = 34 #メダルデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_PRINT_INIT_ACHIEVEMENT         = 35 #アチーブメントデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_PRINT_INIT_ALL                 = 36 #オールデータ初期化メッセージ表示ウィンドウ
WINDOW_ID_MEDAL_ACQUISITION_REPORT       = 37 #メダル取得報告ウィンドウ
WINDOW_ID_ACHIEVEMENT_ACQUISITION_REPORT = 38 #実績(アチーブメント)取得報告ウィンドウ
WINDOW_ID_JOYPAD_ASSIGN                  = 39 #ジョイパッドボタン割り当て設定ウィンドウ
WINDOW_ID_TITLE_TEXT                     = 40 #タイトルで表示されるテキスト群ウィンドウ(フレームレス)(外枠は表示しない)
WINDOW_ID_TITLE_STORY_TEXT               = 41 #タイトルで表示されるストーリー(フレームレス)(外枠は表示しない)(上方向に自動スクロールします)

#ウィンドウのid_subの定数定義 windowクラスの window[i].window_id_subに入ります
WINDOW_ID_SUB_NORMAL_MENU            = 0 #通常の選択メニュー
WINDOW_ID_SUB_YES_NO_MENU            = 1 #「はい」「いいえ」の2択式メニュー
WINDOW_ID_SUB_ON_OFF_MENU            = 2 #「ON」「OFF」の2択式メニュー        (フラグオン時は選択されている物がハイライトされた色となります)
WINDOW_ID_SUB_SELECT_NUM_MENU        = 3 #数値を横方向の操作で増減させて決めるメニュー
WINDOW_ID_SUB_TOGGLE_MENU            = 4 #押すことでオンオフを切り替えることが出来るトグルスイッチメニュー
WINDOW_ID_SUB_FULL_4WAY_MENU         = 5 #4方向入力による自由なデザインでのメニュー
WINDOW_ID_SUB_RIGHT_LEFT_PAGE_MENU   = 6 #左右の頁送りで切り替えるメニュー(スコアボードとかで使用)
WINDOW_ID_SUB_MULTI_SELECT_MENU      = 7 #通常の選択メニューと基本は同じだがあらかじめ選択された物がハイライトされた色で表示される
WINDOW_ID_SUB_SWITCH_TEXT_MENU       = 8 #上下操作でカーソルが上下し左右でそれぞれの項目に対応したテキストが切り替わり表示されるメニュータイプ

#ウィンドウの種類の定数定義 windowクラスのwindow[i].window_typeに入ります
WINDOW_TYPE_NORMAL                   = 0 #メッセージを表示し何かしらの入力を待つタイプ
WINDOW_TYPE_EDIT_TEXT                = 1 #メッセージを表示しさらにテキスト編集の入力待ちするタイプ
WINDOW_TYPE_SCROLL_TEXT              = 2 #カーソルキーで上下スクロールできる長文を読ませる時に使用するタイプ
WINDOW_TYPE_PRINT_TEXT               = 3 #テキストメッセージを表示するだけのタイプ
WINDOW_TYPE_BANNER                   = 4 #タイトルテキストをバナーとして表示するタイプ(テキストの圧縮あり)
WINDOW_TYPE_AUTO_SCROLL_TEXT         = 5 #テキストが自動で上方向下方向に流れていくデモなどで使用するタイプ

#ウィンドウの下地の定数定義 windowクラスの window[i].window_bgに入ります
WINDOW_BG_TRANSLUCENT     = 0 #半透明
WINDOW_BG_BLUE_BACK       = 1 #青地
WINDOW_BG_LOW_TRANSLUCENT = 2 #ちょっと半透明
WINDOW_BG_NONE            = 3 #下地無し

#ウィンドウ表示時に予め「黒矩形塗りつぶし」した後、表示するか、そのまま普通に重ね合わせて表示するか？どうか？
ORDINARY_SUPERPOSITION = 0 #そのまま普通に重ね合わせて表示
BLACK_RECTANGLE_FILL   = 1 #「黒矩形塗りつぶし」した後、表示する

#ウィンドウの表示プライオリティ(優先度) 数値が小さいものほど前面に表示されます
WINDOW_PRIORITY_TOP        = 0 #最前面
WINDOW_PRIORITY_1          = 1 #1番目
WINDOW_PRIORITY_2          = 2
WINDOW_PRIORITY_3          = 3
WINDOW_PRIORITY_4          = 4
WINDOW_PRIORITY_5          = 5 #5番目
WINDOW_PRIORITY_NORMAL     = 6 #初期値(自機、敵、ボス背景より手前)

                            #このあたりの優先度でここでタイトルロゴが表示される

WINDOW_PRIORITY_TITLE_BACK = 7 #タイトルロゴのすぐ後ろ


#ウィンドウの枠の種類の定数定義 windowクラスの window[i].window_frameに入ります
WINDOW_FRAME_NORMAL       = 0 #通常のフレーム
WINDOW_FRAME_NONE         = 1 #フレーム無し BGだけのタイプ 外枠無しのウィンドウ

#ウィンドウの開閉していく方向 windowクラスの window[i].open_direction または window[i].close_directionに入ります
#スクロールするテキストをどの様な方向にスクロールさせるのか？を指定するためにwindow[i].scroll_text[LIST_WINDOW_TEXT_SLIDE_IN_WAY]に入ります
DIR_RIGHT_DOWN            = 3 #右下方向
DIR_LEFT_UP               = 7 #左上方向
DIR_RIGHT_UP              = 9 #右上方向
DIR_LEFT_DOWN             = 1 #左下方向
DIR_UP                    = 8 #上方向
DIR_DOWN                  = 2 #下方向
DIR_RIGHT                 = 6 #右方向
DIR_LEFT                  = 4 #左方向

#メッセージウィンドウ関連の定数定義 windowクラスの window[i].window_statusに入ります
WINDOW_OPEN            =  0    #ウィンドウ開き進行中
WINDOW_WRITE_TITLE_BAR =  4    #ウィンドウのタイトルバー表示中
WINDOW_WRITE_MESSAGE   =  5    #メッセージの表示中
WINDOW_SELECT_YES_NO   =  8    #「はい」「いいえ」の2択表示中
WINDOW_OPEN_COMPLETED  =  9    #ウィンドウ開き完了！
WINDOW_CLOSE           = 10    #ウィンドウ閉め進行中
WINDOW_CLOSE_COMPLETED = 11    #ウィンドウ閉め完了！
WINDOW_MOVE            = 12    #ウィンドウ移動中

#ウィンドウのテキスト行間ドット数 windowクラスのbetween_lineに入ります
WINDOW_BETWEEN_LINE_7   =  7     #行間 7ドット
WINDOW_BETWEEN_LINE_8   =  8     #行間 8ドット
WINDOW_BETWEEN_LINE_9   =  9     #行間 9ドット
WINDOW_BETWEEN_LINE_10  = 10     #行間10ドット
#ウィンドウで表示されるボタンのサイズ
WINDOW_BUTTON_SIZE_1X1    = 0      #1x1キャラ分(8x8ドット)
WINDOW_BUTTON_SIZE_1TEXT  = 1      #半角文字サイズ4*6ドット
WINDOW_BUTTON_SIZE_1X2    = 2      #1x2キャラ分(8x16ドット)

#ウィンドウのメニューでその項目を変化させる時クリック音を出すか出さないかのフラグ
CLICK_SOUND_OFF = 0 #クリック音を出さない
CLICK_SOUND_ON  = 1 #出す

#メッセージ,ボタンの表示の仕方 windowクラスのwindow[i].title_text[LIST_WINDOW_TEXT_ALIGN],またはwindow[i].item_text[j][LIST_WINDOW_TEXT_ALIGN]に入ります
BUTTON_DISP_OFF    =  0 #0=表示しない
BUTTON_DISP_ON     =  1 #1=表示する

DISP_CENTER        =  2 #2=中央表示
DISP_LEFT_ALIGN    =  3 #3=左揃え
DISP_RIGHT_ALIGN   =  4 #4=右揃え

SKIP_CURSOR_AREA   = 10 #メッセージもコメントも表示せず、カーソルはこのアイテム位置を飛び越えて移動する(スキップして移動する)

WIDE_SIZE_BUTTON   = 11 #横幅一杯を使用する横長のボタン

SIZE3_BUTTON_1     = 12 #横3x縦1キャラサイズのボタンの1番左端 (1**)
SIZE3_BUTTON_2     = 13 #横3x縦1キャラサイズのボタンの真ん中  (*2*)
SIZE3_BUTTON_3     = 14 #横3x縦1キャラサイズのボタンの1番右端 (**3)

SIZE5_BUTTON_1     = 15 #横5x縦1キャラサイズのボタンの左端       (1****)
SIZE5_BUTTON_2     = 16 #横5x縦1キャラサイズのボタンの左から2番目 (*2***)
SIZE5_BUTTON_3     = 17 #横5x縦1キャラサイズのボタンの真ん中     (**3**)
SIZE5_BUTTON_4     = 18 #横5x縦1キャラサイズのボタンの右から2番目 (***4*)
SIZE5_BUTTON_5     = 19 #横5x縦1キャラサイズのボタンの右端       (****5)

#ウィンドウテキストのリストの2次元配列のインデックスナンバーとして使用する定数定義
#windowクラスのwindow[i].title_text[ここで定義した定数]
#        またはwindow[i].item_text[j][ここで定義した定数]
#        またはwindow[i].item_kanji_text[j][ここで定義した定数]
#        またはwindow[i].scroll_text[ここで定義した定数]に入ります
LIST_WINDOW_TEXT                    =  0 #ウィンドウテキスト
LIST_WINDOW_TEXT_CLICK_SE_FLAG      =  1 #カーソル移動音を出すかどうかのフラグ
LIST_WINDOW_TEXT_ALIGN              =  2 #ウィンドウテキストの揃え方(アライメント)(整列の仕方)
LIST_WINDOW_TEXT_OX                 =  3 #ウィンドウテキスト表示x軸のオフセット値
LIST_WINDOW_TEXT_OY                 =  4 #ウィンドウテキスト表示y軸のオフセット値
LIST_WINDOW_TEXT_COLOR              =  5 #ウィンドウテキストの表示色

LIST_WINDOW_TEXT_FLASH              =  6 #ウィンドウテキストの点滅のしかた
LIST_WINDOW_TEXT_TYPE               =  7 #ウィンドウテキストのタイプ
LIST_WINDOW_TEXT_STATUS             =  8 #ウィンドウテキストのステータス(状態)
LIST_WINDOW_TEXT_LENGTH             =  9 #ウィンドウテキストの長さ
LIST_WINDOW_TEXT_LINEFEED_WIDTH     = 10 #ウィンドウテキストの折り返し改行幅

LIST_WINDOW_TEXT_LINEFEED_HEIGHT    = 11 #ウィンドウテキストの折り返し改行幅(縦書きモードの時)
LIST_WINDOW_TEXT_DISP_TYPE          = 12 #ウィンドウテキストの文字の表示のしかた
LIST_WINDOW_TEXT_DISP_SPEED         = 13 #ウィンドウテキストの文字の表示スピード(一文字ずつ表示する場合のみ)
LIST_WINDOW_TEXT_SCROLL_SPEED       = 14 #ウィンドウテキストのスクロールスピード値
LIST_WINDOW_TEXT_SLIDE_IN_WAY       = 15 #ウィンドウテキストがスライドインしてくる方向

LIST_WINDOW_TEXT_SLIDE_OUT_WAY      = 16 #ウィンドウテキストをスライドアウトさせる方向
LIST_WINDOW_TEXT_SLIDE_NOW_SPEED    = 17 #ウィンドウテキストをスライドインアウトさせる時の現在のスピード値
LIST_WINDOW_TEXT_SLIDE_START_SPEED  = 18 #ウィンドウテキストをスライドインアウトさせる時の初期スピード値
LIST_WINDOW_TEXT_SLIDE_END_SPEED    = 19 #ウィンドウテキストをスライドインアウトさせる時の最後のスピード値(目標となるスピード値ですの)
LIST_WINDOW_TEXT_SLIDE_MAG_SPEED    = 20 #ウィンドウテキストをスライドインアウトさせる時のスピード値に掛ける加速度

LIST_WINDOW_TEXT_OPE_OBJ            = 21 #ウィンドウテキストで編集対象となるオブジェクトを指示します(windowクラスのflag_list[i][対象オブジェクト]の対象オブジェクトとなります)
LIST_WINDOW_TEXT_OPE_OBJ_TYPE       = 22 #ウィンドウテキストで編集対象となるオブジェクトの種類分類
LIST_WINDOW_TEXT_OPE_OBJ_TEXT       = 23 #ウィンドウテキストで編集対象となるオブジェクトのタイトルテキスト「ON」とか「OFF」とか
LIST_WINDOW_TEXT_OPE_OBJ_TEXT_ALIGN = 24 #ウィンドウテキストで編集対象となるオブジェクトのタイトルテキストの揃え方(アライメント)(整列の仕方)アラ～イイアラ～～イイ
LIST_WINDOW_TEXT_OPE_OBJ_COMPARE    = 25 #対象オブジェクトと比較するパラメータ数値(この数値とOPE_OBJの数値を比較してTrueかFalseか判定します)

LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OX    = 26 #ウィンドウテキストで編集対象となるオブジェクトのタイトルテキスト x軸のオフセット値
LIST_WINDOW_TEXT_OPE_OBJ_TEXT_OY    = 27 #ウィンドウテキストで編集対象となるオブジェクトのタイトルテキスト y軸のオフセット値
LIST_WINDOW_TEXT_OPE_OBJ_OFF_COLOR  = 28 #対象オブジェクトがFalse(OFF)になった時の文字色
LIST_WINDOW_TEXT_OPE_OBJ_ON_COLOR   = 29 #対象オブジェクトがTrue(ON)になった時の文字色
LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM    = 30 #ウィンドウテキストで編集対象となるオブジェクトの最小値(数値の場合)

LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM        = 31 #ウィンドウテキストで編集対象となるオブジェクトの最大値(数値の場合)
LIST_WINDOW_TEXT_OPE_OBJ_SWITCH_TEXT    = 32 #ウィンドウテキストで編集対象となるオブジェクトテキスト(切り替え表示タイプ「VERYEASY」「EASY」「NORMAL」「HARD」とか表示テキストがボタンまたは左右カーソルセレクトで切り替わる
LIST_WINDOW_TEXT_OPE_OBJ_MARKER_TYPE    = 33 #ウィンドウテキストで編集対象となるオブジェクトが増減できる数値とかの場合増加減出来るかどうかの矢印マーカーの種別（矢印マーカを表示するしないの判断はLIST_WINDOW_TEXT_OPE_OBJ_TYPEをみて行う,LIST_WINDOW_TEXT_OPE_OBJ_MARKER_TYPEは複数の表示パターンを持てるようにするためのリザーブ）

LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_FLAG    = 34 #増減表示（上矢印）を表示するかのフラグ
LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_FLAG  = 35 #増減表示（下矢印）を表示するかのフラグ
LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG = 36 #増減表示（右矢印）を表示するかのフラグ
LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG  = 37 #増減表示（左矢印）を表示するかのフラグ

LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_X    = 38 #対象が数値とかで増加減出来るかどうかの、上矢印の座標(x,y)
LIST_WINDOW_TEXT_OPE_OBJ_UP_MARKER_Y    = 39
LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_X  = 40 #対象が数値とかで増加減出来るかどうかの、下矢印の座標(x,y)
LIST_WINDOW_TEXT_OPE_OBJ_DOWN_MARKER_Y  = 41
LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_X = 42 #対象が数値とかで増加減出来るかどうかの、右矢印の座標(x,y)
LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_Y = 43
LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_X  = 44 #対象が数値とかで増加減出来るかどうかの、左矢印の座標(x,y)
LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_Y  = 45

#ウィンドウフラグリストの２次元配列のインデックスナンバーとして使用する定数定義 windowクラスのwindow[i].flag_list[ここで定義した定数]に入ります
LIST_WINDOW_FLAG_DEBUG_MODE        =  0 #デバッグモードのon/offフラグ
LIST_WINDOW_FLAG_GOD_MODE          =  1 #ゴッドモードのon/offフラグ
LIST_WINDOW_FLAG_HIT_BOX           =  2 #ヒットボックス(当たり判定)のon/offフラグ
LIST_WINDOW_FLAG_BOSS_MODE         =  3 #ボスモード(ボス戦闘のみのモード)のon/offフラグ
LIST_WINDOW_FLAG_START_STAGE       =  4 #開始ステージ数
LIST_WINDOW_FLAG_START_LOOP        =  5 #開始ループ数
LIST_WINDOW_FLAG_START_AGE         =  6 #開始時代数
LIST_WINDOW_FLAG_DIFFICULTY        =  7 #難易度
LIST_WINDOW_FLAG_SCREEN_MODE       =  8 #画面スクリーンモード(ウィンドウ表示、全画面表示切替)
LIST_WINDOW_FLAG_BGM_VOL           =  9 #BGMボリューム値
LIST_WINDOW_FLAG_SE_VOL            = 10 #SE(サウンドエフェクト)ボリューム値
LIST_WINDOW_FLAG_CTRL_TYPE         = 11 #パッド入力パターン
LIST_WINDOW_FLAG_LANGUAGE          = 12 #選択言語
LIST_WINDOW_FLAG_                  = 13 #
LIST_WINDOW_FLAG_                  = 14 #
LIST_WINDOW_FLAG_                  = 15 #
LIST_WINDOW_FLAG_                  = 16 #
LIST_WINDOW_FLAG_                  = 17 #
LIST_WINDOW_FLAG_                  = 18 #
LIST_WINDOW_FLAG_                  = 19 #
LIST_WINDOW_FLAG_                  = 20 #
LIST_WINDOW_FLAG_                  = 21 #
LIST_WINDOW_FLAG_                  = 22 #
LIST_WINDOW_FLAG_                  = 23 #
LIST_WINDOW_FLAG_                  = 24 #
#ウィンドウグラフイック群リストの２次元配列のインデックスナンバーとして使用する定数定義 windowクラスのwindow[i].graph_list[ここで定義した定数]に入ります
LIST_WINDOW_GRAPH_OX               =  0 #グラフイックキャラを表示する座標(ox,oy)ウィンドウ表示座標からのオフセット値となります
LIST_WINDOW_GRAPH_OY               =  1 #
LIST_WINDOW_GRAPH_IMGB             =  2 #表示するグラフイックキャラが入っているイメージバンクの数値
LIST_WINDOW_GRAPH_U                =  3 #表示するグラフイックキャラが入っている場所を示した座標(u,v)
LIST_WINDOW_GRAPH_V                =  4 #
LIST_WINDOW_GRAPH_W                =  5 #表示するグラフイックキャラの縦幅、横幅(width,height)マイナス値の場合は反転します
LIST_WINDOW_GRAPH_H                =  6 #
LIST_WINDOW_GRAPH_COLKEY           =  7 #透明色の指定
LIST_WINDOW_GRAPH_ANIME_FRAME_NUM  =  8 #アニメーションパターンの枚数(1の場合はアニメーション無し)
LIST_WINDOW_GRAPH_ANIME_SPEED      =  9 #アニメーションのスピード(1が速く数値が増えるにつれて遅くなる4位が良いかも？)
LIST_WINDOW_GRAPH_ITEM_X           = 10 #このグラフイックキャラはアイテムとしてどこに位置するのかを指定する(x座標)
LIST_WINDOW_GRAPH_ITEM_Y           = 11 #このグラフイックキャラはアイテムとしてどこに位置するのかを指定する(y座標)(0,0)だったらdecision_item_x=0,decision_item_y=0
                                        #                                                                   (2,1)だったらdecision_item_x=2,decision_item_y=1って事になります

#ウィンドウスクリプトリストのリストの2次元配列のインデックスナンバーとして使用する定数定義 windowクラスのwindow[i].script[ここで定義した定数]に入ります(一つだけだよ=1個だけ)(リスト表記=複数の数値が入ります)
LIST_WINDOW_SCRIPT_TEXT            =  0 #スクリプト文本文が入ります(文字列型)
LIST_WINDOW_SCRIPT_OX              =  1 #スクリプト内のテキストの表示オフセット座標(OX,OY)
LIST_WINDOW_SCRIPT_OY              =  2 #
LIST_WINDOW_SCRIPT_DISP_TYPE       =  3 #スクリプトテキストの表示タイプ
LIST_WINDOW_SCRIPT_DISP_SPEED      =  4 #スクリプトテキストの表示スピード
LIST_WINDOW_SCRIPT_TEXT_WIDTH      =  5 #現在のスクリプトテキストの最大表示幅(はみ出したとき折り返すかどうかは〇〇の値で判断する)
LIST_WINDOW_SCRIPT_TEXT_HEIGHT     =  6 #現在のスクリプトテキストの最大表示行数
LIST_WINDOW_SCRIPT_ALIGN           =  7 #現在のスクリプトテキストの表示揃えの仕方
LIST_WINDOW_SCRIPT_COLOR           =  8 #現在のスクリプトテキストの表示色
LIST_WINDOW_SCRIPT_SCROLL_TYPE     =  9 #現在のスクリプトテキストのスクロールタイプ
LIST_WINDOW_SCRIPT_SCROLL_SPEED    = 10 #現在のスクリプトテキストのスクロールスピード
LIST_WINDOW_SCRIPT_WAIT            = 11 #スクリプトテキスト用のウェイトタイマー wait**
LIST_WINDOW_SCRIPT_COUNT           = 12 #スクリプトテキスト用のカウンター      count**
LIST_WINDOW_SCRIPT_FLAG            = 13 #スクリプトテキスト用のフラグ          FLAG** 
LIST_WINDOW_SCRIPT_VAR             = 14 #スクリプトテキスト用の変数リスト群(整数)[["@変数名",整数],[@EGG,123],[@HUM,456667],.........[@PULIN,467890]]
LIST_WINDOW_SCRIPT_STR             = 15 #スクリプトテキスト用の変数リスト群(文字列型)[["$変数名","文字列"],["$STR1","AAA"],["$STR_A3","BBB"],["$STR_3456","CDE"]....["$STR_3414","ZZzzz"]]
LIST_WINDOW_SCRIPT_LABEL           = 16 #スクリプトテキスト用のラベル定義リスト群(文字列型)[["#ラベル名",プログラムカウント数],["#HYOUZI_KAISI",34],.......["#HOGEHOGE",46]]
LIST_WINDOW_SCRIPT_PROGRAM_COUNTER = 17 #スクリプトテキスト用の処理用実行位置カウンター(一つだけだよ)プログラムカウンターPC
LIST_WINDOW_SCRIPT_STACK_MEMORY    = 18 #スクリプトテキスト用スタックメモリー(リスト表記)スタックメモリエリア
LIST_WINDOW_SCRIPT_STACK_POINTER   = 19 #スクリプトテキスト用スタックポインタ(一つだけだよ)SP
LIST_WINDOW_SCRIPT_RETURN_MEMORY   = 20 #スクリプトテキスト用リターンメモリー(リスト表記)RETURN文で戻るべきプログラムカウンターがスタックされる
LIST_WINDOW_SCRIPT_RETURN_POINTER  = 21 #スクリプトテキスト用リターンポインタ(一つだけだよ)RP
LIST_WINDOW_SCRIPT_FOR_START_NUM   = 22 #スクリプトテキスト用FOR文での開始値(リスト表記)
LIST_WINDOW_SCRIPT_FOR_END_NUM     = 23 #スクリプトテキスト用FOR文での終了値(リスト表記)
LIST_WINDOW_SCRIPT_FOR_STEP_NUM    = 24 #スクリプトテキスト用FOR文での増分値(リスト表記) 

#ウィンドウベクターグラフイックス群リストの2次元配列のインデックスナンバーとして使用する定数定義 windowクラスのwindow[i].vector_grp[ここで定義した定数]に入ります
LIST_WINDOW_VECTOR_GRP_PSET        =  0 #ベクターグラフイック 点描画命令
LIST_WINDOW_VECTOR_GRP_LINE        =  1 #ベクターグラフイック 線描画命令[LIST_WINDOW_VECTOR_GRP_LINE,始点座標x0,始点座標y0,終点座標x1,終点座標y1,色]
LIST_WINDOW_VECTOR_GRP_BOX         =  2 #ベクターグラフイック 矩形描画命令
LIST_WINDOW_VECTOR_GRP_BOXF        =  3 #ベクターグラフイック 塗りつぶし矩形描画命令
LIST_WINDOW_VECTOR_GRP_CIRCLE      =  4 #ベクターグラフイック 円描画命令
LIST_WINDOW_VECTOR_GRP_CIRCLEF     =  5 #ベクターグラフイック 塗りつぶし円描画命令
LIST_WINDOW_VECTOR_GRP_ELLIE       =  6 #ベクターグラフイック 楕円描画命令
LIST_WINDOW_VECTOR_GRP_ELLIEF      =  7 #ベクターグラフイック 塗りつぶし楕円描画命令
LIST_WINDOW_VECTOR_GRP_TRI         =  8 #ベクターグラフイック 三角形描画命令
LIST_WINDOW_VECTOR_GRP_TRIF        =  9 #ベクターグラフイック 塗りつぶし三角形描画命令
LIST_WINDOW_VECTOR_GRP_FILL        = 10 #ベクターグラフイック ペイント命令
LIST_WINDOW_VECTOR_GRP_CHR         = 11 #ベクターグラフイック 1文字表示命令

#ウィンドウタイム＆カウンター群リストの２次元配列のインデックスナンバーとして使用する定数定義 windowクラスのwindow[i].time_counter_list[j][ここで定義した定数]に入ります
LIST_WINDOW_TIME_COUNTER_TYPE      =  0  #ウィンドウに表示するタイムカウンターの種類
LIST_WINDOW_TIME_COUNTER_OX        =  1  #表示座標(ox,oy)ウィンドウ原点からのオフセット値
LIST_WINDOW_TIME_COUNTER_OY        =  2
LIST_WINDOW_TIME_COUNTER_COLOR     =  3  #色
LIST_WINDOW_TIME_COUNTER_ALIGN     =  4  #揃え方(アライメント)(整列の仕方)

#ウィンドウタイムカウンターリストのLIST_WINDOW_TIME_COUNTER_TYPEに入るカウンタタイプ windowクラスのwindow[i].time_counter_list[j][LIST_WINDOW_TIME_COUNTER_TYPE]に入ります
TIME_COUNTER_TYPE_TOTAL_PLAYTIME         =  0  #総プレイ時間
TIME_COUNTER_TYPE_NUMBER_OF_PLAY         =  1  #プレイした回数
TIME_COUNTER_TYPE_NUMBER_TIMES_DESTROYED =  2  #自機が破壊された回数
TIME_COUNTER_TYPE_TOTAL_SCORE            =  3  #累計得点数

#ウィンドウクラスのリスト関連で何もない時に使用する定数定義
NO_TITLE_TEXT      = []
NO_ITEM_TEXT       = []
NO_ITEM_KANJI_TEXT = []
NO_EDIT_TEXT       = []
NO_ANIMATION_TEXT  = []
NO_SCROLL_TEXT     = []
NO_SCRIPT          = []
NO_VECTOR_GRP      = []

NO_SHIP_LIST             = []
NO_SHIP_MEDAL_LIST       = []
NO_WEAPON_LIST           = []
NO_WEAPON_GRAPH_LIST     = []
NO_SUB_WEAPON_LIST       = []
NO_SUB_WEAPON_GRAPH_LIST = []
NO_MISSILE_LIST          = []
NO_MISSILE_GRAPH_LIST    = []
NO_MEDAL_LIST            = []
NO_MEDAL_GRAPH_LIST      = []
NO_PAD_ASSIGN_LIST       = []
NO_PAD_ASSIGN_GRAPH_LIST = []
NO_ITEM_LIST             = []
NO_ITEM_GRAPH_LIST       = []
NO_FLAG_LIST             = []
NO_GRAPH_LIST            = []
NO_TIME_COUNTER_LIST     = []

NO_EQUIP_MEDAL_GRAPH_LIST   = []
NO_EQUIP_MEDAL_COMMENT_LIST = []

NO_COMMENT_DISP_FLAG      = []
NO_COMMENT_LIST_ENG       = []
NO_COMMENT_LIST_JPN       = []
NO_ITEM_ID                = []

#メッセージを点滅させるかのフラグ windowクラスのwindow[i].item_text[j][LIST_WINDOW_TEXT_FLASH]に入ります
MES_NO_FLASH         = 0 #点滅しない
MES_BLINKING_FLASH   = 1 #点滅
MES_RED_FLASH        = 2 #赤い点滅
MES_GREEN_FLASH      = 3 #緑で点滅
MES_YELLOW_FLASH     = 4 #黄色で点滅
MES_MONOCHROME_FLASH = 5 #白黒で点滅
MES_RAINBOW_FLASH    = 6 #虹色に点滅

#ウィンドウテキストで編集対象となるオブジェクトの種類分類ですwindowクラスのwindow[i].item_text[j][LIST_WINDOW_TEXT_OPE_OBJ_TYPE]に入ります
OPE_OBJ_TYPE_NONE    = 0 #操作テキストオブジェクトの指定は無し
OPE_OBJ_TYPE_ON_OFF  = 1 #操作テキストオブジェクトは「ON」「OFF」の二つから選ぶシンプルなタイプです
OPE_OBJ_TYPE_NUM     = 2 #操作テキストオブジェクトは数値を増減させて選択するタイプ
OPE_OBJ_MULTI_ITEM   = 3 #操作テキストオブジェクトは多項目から選択するタイプ