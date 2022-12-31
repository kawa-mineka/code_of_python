#############################################
#主にVisualsceneクラスで使用する定数定義です###
#############################################

#!ビジュアルシーンのidの定数定義 visualsceneクラスの visualscene[i].idに入ります
VS_ID_DUMMY                              =  0 #ダミー用 (VSはVisualSceneの略語です VSCodeって意味じゃないですよぉ～♪)
VS_ID_OPENING_STORY1                     =  1 #オープニングのストーリーテキスト1

#ビジュアルシーンのid_subの定数定義 visualsceneクラスの visualscene[i].id_subに入ります
VS_ID_SUB_NORMAL                         = 0 #通常

#ビジュアルシーンのtypeの定数定義 visualsceneクラスのvisualscene[i].typeに入ります
VS_TYPE_NORMAL                           = 0 #通常

#ビジュアルシーンのstatusの定数定義 visualsceneクラスのvisualscene[i].statusに入ります
VS_STATUS_NORMAL                         = 0 #通常

#ビジュアルシーンのpriority(プライオリティ)(優先度)の定数定義 visualsceneクラスのvisualscene[i].priorityに入ります,行番号が小さいものほど前面に表示される
VS_PRIORITY_TOP        = 0 #最前面
VS_PRIORITY_1          = 1 #1番目
VS_PRIORITY_2          = 2
VS_PRIORITY_3          = 3
VS_PRIORITY_4          = 4
VS_PRIORITY_5          = 5 #5番目
VS_PRIORITY_NORMAL     = 6 #初期値(自機、敵、ボス背景より手前)

                            #このあたりの優先度でここでタイトルロゴが表示される

VS_PRIORITY_TITLE_BACK = 7 #タイトルロゴのすぐ後ろ

#ビジュアルシーンwaitの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].wait[ここで定義した定数]に入ります
LIST_VS_WAIT_0         = 0
LIST_VS_WAIT_1         = 1
LIST_VS_WAIT_2         = 2
LIST_VS_WAIT_3         = 3
LIST_VS_WAIT_4         = 4
LIST_VS_WAIT_5         = 5
#ビジュアルシーンflagの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].flag[ここで定義した定数]に入ります
LIST_VS_FLAG_0         = 0
LIST_VS_FLAG_1         = 1
LIST_VS_FLAG_2         = 2
LIST_VS_FLAG_3         = 3
LIST_VS_FLAG_4         = 4
LIST_VS_FLAG_5         = 5
#ビジュアルシーンgrpの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].grp[ここで定義した定数]に入ります
LIST_VS_GRP_0         = 0
LIST_VS_GRP_1         = 1
LIST_VS_GRP_2         = 2
LIST_VS_GRP_3         = 3
LIST_VS_GRP_4         = 4
LIST_VS_GRP_5         = 5
#ビジュアルシーンfaceの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].face[ここで定義した定数]に入ります
LIST_VS_FACE_0         = 0
LIST_VS_FACE_1         = 1
LIST_VS_FACE_2         = 2
LIST_VS_FACE_3         = 3
LIST_VS_FACE_4         = 4
LIST_VS_FACE_5         = 5
#ビジュアルシーンsoundの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].sound[ここで定義した定数]に入ります
LIST_VS_SOUND_0         = 0
LIST_VS_SOUND_1         = 1
LIST_VS_SOUND_2         = 2
LIST_VS_SOUND_3         = 3
LIST_VS_SOUND_4         = 4
LIST_VS_SOUND_5         = 5
#ビジュアルシーンbgmの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].bgm[ここで定義した定数]に入ります
LIST_VS_BGM_0         = 0
LIST_VS_BGM_1         = 1
LIST_VS_BGM_2         = 2
LIST_VS_BGM_3         = 3
LIST_VS_BGM_4         = 4
LIST_VS_BGM_5         = 5
#ビジュアルシーンeffectの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].effect[ここで定義した定数]に入ります
LIST_VS_EFFECT_0         = 0
LIST_VS_EFFECT_1         = 1
LIST_VS_EFFECT_2         = 2
LIST_VS_EFFECT_3         = 3
LIST_VS_EFFECT_4         = 4
LIST_VS_EFFECT_5         = 5
#ビジュアルシーンtextの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].text[ここで定義した定数]に入ります
LIST_VS_TEXT_0         = 0
LIST_VS_TEXT_1         = 1
LIST_VS_TEXT_2         = 2
LIST_VS_TEXT_3         = 3
LIST_VS_TEXT_4         = 4
LIST_VS_TEXT_5         = 5
#ビジュアルシーンscroll_textの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].scroll_text[ここで定義した定数]に入ります
LIST_VS_SCROLL_TEXT_X                    =  0  #スクロールテキストを表示する座標
LIST_VS_SCROLL_TEXT_Y                    =  1
LIST_VS_SCROLL_TEXT_WIDTH                =  2 #表示するエリアの横幅
LIST_VS_SCROLL_TEXT_HEIGHT               =  3 #表示するエリアの縦幅(
LIST_VS_SCROLL_TEXT_DATA_ENG             =  4 #実際に表示されるテキストデータ(英語)  (このリストの中に更にリストが入ります)
LIST_VS_SCROLL_TEXT_DATA_JPN             =  5 #実際に表示されるテキストデータ(日本語)(このリストの中に更にリストが入ります)
LIST_VS_SCROLL_TEXT_SUBTITLES_FLAG       =  6 #字幕表示するかどうかのフラグ
LIST_VS_SCROLL_TEXT_SUBTITLES_X          =  7 #字幕を表示するx座標
LIST_VS_SCROLL_TEXT_SUBTITLES_Y          =  8 #字幕を表示するy座標
LIST_VS_SCROLL_TEXT_SUBTITLES_WIDTH      =  9 #字幕の横幅
LIST_VS_SCROLL_TEXT_SUBTITLES_HEIGHT     = 10 #字幕の縦幅

LIST_VS_SCROLL_TEXT_SHADOW_FLAG          = 11 #スクロールテキストの上下端に影を付けるかどうかのフラグ
LIST_VS_SCROLL_TEXT_SHADOW_COL           = 12 #スクロールテキストの上下端に影を付ける際、どの様な色にするかの指定
LIST_VS_SCROLL_TEXT_SHADOW_UP_LINE_NUM   = 13 #スクロールテキストの上下に影を付ける際の上部分のラインドット数
LIST_VS_SCROLL_TEXT_SHADOW_DOWN_LINE_NUM = 14 #スクロールテキストの上下に影を付ける際の下部分のラインドット数

LIST_VS_SCROLL_TEXT_BETWEEN_LINE_ENG     = 15 #実際に表示されるテキストデータ(英語)表示時の行間ドット数
LIST_VS_SCROLL_TEXT_BETWEEN_LINE_JPN     = 16 #実際に表示されるテキストデータ(日本語)表示時の行間ドット数
LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG     = 17 #スクロールしたドット数(最初は0で変化していきます)(英語)
LIST_VS_SCROLL_TEXT_SCROLLED_DOT_JPN     = 18 #スクロールしたドット数(最初は0で変化していきます)(日本語)
LIST_VS_SCROLL_TEXT_SCROLLED_DOT_MAX_ENG = 19 #スクロールしたドット数の最大値(この数値までスクロールさせたら終了とする)(英語)
LIST_VS_SCROLL_TEXT_SCROLLED_DOT_MAX_JPN = 20 #スクロールしたドット数の最大値(この数値までスクロールさせたら終了とする)(日本語)
LIST_VS_SCROLL_TEXT_SPEED_ENG            = 21 #スクロールするスピード(英語)
LIST_VS_SCROLL_TEXT_SPEED_JPN            = 22 #スクロールするスピード(日本語)
LIST_VS_SCROLL_TEXT_END_FLAG             = 23 #テキストが最後までスクロール完了したかどうかのフラグ
LIST_VS_SCROLL_TEXT_END_ACTION           = 24 #テキストが最後までスクロール完了した後どうするか？の指定

#ビジュアルシーンscriptの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].script[ここで定義した定数]に入ります
LIST_VS_SCRIPT_0         = 0
LIST_VS_SCRIPT_1         = 1
LIST_VS_SCRIPT_2         = 2
LIST_VS_SCRIPT_3         = 3
LIST_VS_SCRIPT_4         = 4
LIST_VS_SCRIPT_5         = 5
#ビジュアルシーンvector_grpの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].vector_grp[ここで定義した定数]に入ります
LIST_VS_VECTOR_GRP_0         = 0
LIST_VS_VECTOR_GRP_1         = 1
LIST_VS_VECTOR_GRP_2         = 2
LIST_VS_VECTOR_GRP_3         = 3
LIST_VS_VECTOR_GRP_4         = 4
LIST_VS_VECTOR_GRP_5         = 5
#ビジュアルシーンtimelineの２次元配列のインデックスナンバーとして使用する定数定義 visualsceneクラスのvisualscene[i].timeline[ここで定義した定数]に入ります
LIST_VS_TIMELINE_0         = 0
LIST_VS_TIMELINE_1         = 1
LIST_VS_TIMELINE_2         = 2
LIST_VS_TIMELINE_3         = 3
LIST_VS_TIMELINE_4         = 4
LIST_VS_TIMELINE_5         = 5

#!ビジュアルシーンテキストの2次元配列のインデックスナンバーとして使用する定数定義
#visualsceneクラスのvisualscene[i].text[LIST_VS_SCROLL_TEXT_DATA_ENG][ここで定義した定数]
#                   visualscene[i].text[LIST_VS_SCROLL_TEXT_DATA_JPN][ここで定義した定数]
#
#             またはvisualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_ENG][ここで定義した定数]
#                   visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_DATA_JPN][ここで定義した定数]に入ります
LIST_VS_TEXT                    =  0 #VSテキスト
LIST_VS_TEXT_COLOR              =  1 #VSテキストの表示色
LIST_VS_TEXT_ALIGN              =  2 #VSテキストの揃え方(アライメント)(整列の仕方)
LIST_VS_TEXT_FLASH              =  3 #VSテキストの点滅の仕方
LIST_VS_TEXT_BTN_SE_FLAG        =  4 #パッドボタン音を出すかどうかのフラグ
LIST_VS_TEXT_OX                 =  5 #VSテキスト表示x軸のオフセット値

LIST_VS_TEXT_OY                 =  6 #VSテキスト表示y軸のオフセット値
LIST_VS_TEXT_TYPE               =  7 #VSテキストのタイプ
LIST_VS_TEXT_STATUS             =  8 #VSテキストのステータス(状態)
LIST_VS_TEXT_LENGTH             =  9 #VSテキストの長さ
LIST_VS_TEXT_LINEFEED_WIDTH     = 10 #VSテキストの折り返し改行幅

LIST_VS_TEXT_LINEFEED_HEIGHT    = 11 #VSテキストの折り返し改行幅(縦書きモードの時)
LIST_VS_TEXT_DISP_TYPE          = 12 #VSテキストの文字の表示のしかた
LIST_VS_TEXT_DISP_SPEED         = 13 #VSテキストの文字の表示スピード(一文字ずつ表示する場合のみ)
LIST_VS_TEXT_SCROLL_SPEED       = 14 #VSテキストのスクロールスピード値
LIST_VS_TEXT_SLIDE_IN_WAY       = 15 #VSテキストがスライドインしてくる方向

LIST_VS_TEXT_SLIDE_OUT_WAY      = 16 #VSテキストをスライドアウトさせる方向
LIST_VS_TEXT_SLIDE_NOW_SPEED    = 17 #VSテキストをスライドインアウトさせる時の現在のスピード値
LIST_VS_TEXT_SLIDE_START_SPEED  = 18 #VSテキストをスライドインアウトさせる時の初期スピード値
LIST_VS_TEXT_SLIDE_END_SPEED    = 19 #VSテキストをスライドインアウトさせる時の最後のスピード値(目標となるスピード値ですの)
LIST_VS_TEXT_SLIDE_MAG_SPEED    = 20 #VSテキストをスライドインアウトさせる時のスピード値に掛ける加速度

#ビジュアルシーンクラスのリスト関連で何も入ってない空リスト作成時に使用する定数定義
NO_VS_WAIT_LIST          = []
NO_VS_FLAG_LIST          = []
NO_VS_GRP_LIST           = []
NO_VS_FACE_LIST          = []
NO_VS_SOUND_LIST         = []
NO_VS_BGM_LIST           = []
NO_VS_EFFECT_LIST        = []
NO_VS_TEXT_LIST          = []
NO_VS_SCROLL_TEXT_LIST   = []
NO_VS_SCRIPT_LIST        = []
NO_VS_VECTOR_GRP_LIST    = []
NO_VS_TIMELINE_LIST      = []

NO_VS_TEXT_ENG = []
NO_VS_TEXT_JPN = []

SUBTITLES_OFF = 0 #字幕表示のオンオフ
SUBTITLES_ON  = 1

EDGE_SHADOW_OFF = 0 #テキストの端に影を付けるかのオンオフ
EDGE_SHADOW_ON  = 1

END_ACTION_NONE = 0 #終了後は何もしない
END_ACTION_DEL  = 1 #終了したらビジュアルシーン自体を消去する