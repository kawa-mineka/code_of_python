=============================================================================================
プログラムファイルの詳細な説明です    2022 10/30更新
=============================================================================================
code-of-python.py       メインプログラムです、このパイソンプログラムを実行してね

code-of-python.spec     pyinstaller用specファイルです

const.py                定数定義です ほとんどのプログラムで使われてるのでimportしないと動かないよ

define_boss_data.py     ボス関連のデータ
define_class.py         各クラスのメンバ変数とか宣言してます、あとコンストラクタの処理とか
define_data.py          色んなデータのリスト登録です
define_enemy_data.py    敵データ関連のリスト登録
define_ship_data.py     自機関連のデータリスト登録
define_sound.py         BGMファイルを事前に読み込み、リストに登録する処理
define_stage_data.py    各ステージのイベントデータとか、ゲーム全体のステージ配列などのリスト登録です

func.py                 ある程度の汎用性のある関数群です update_* の各メソッドから呼ばれる場合が多いですねぇ
graph.py                drawクラスから呼ばれるメソッドが詰まっております 座標が入ったメンバ変数の数値を読んでそれに従ってグラフイックを表示するだけの処理です

readme.txt              このファイルだよ～☆彡

update_boss.py          ボス関連の更新処理
update_btn_assign.py    パッドコントロールボタン設定です,各ボタンにどの機能を割り当てるかの処理です
update_btn.py           入力関連の更新処理(キーパッドが押されたとかボタンが押されたとか～そんなの)
update_collision.py     当たり判定を行ってます     
update_debug.py         デバッグモードで使用されるプログラムです、通常では使ったダメだよ☆彡
update_enemy.py         敵関連の処理です
update_event.py         ステージのイベントデータリストを解析して敵を出すしょりです、あとBGマップのチップデータをみて敵の地上砲台を出現させたりも
update_init.py          ゲーム開始直後の初期処理やステージ開始直後の初期化処理を行います
update_ipl.py           ゲーム起動直後に出るIPLメッセージの表示とか
update_item.py          アイテム関連の更新
update_obj.py           背景に表示される色んなオブジェクト(雲とかスパークとかパーティクルとか)の更新処理です
update_pause.py         ゲーム中ポーズを掛けたときの処理         
update_replay.py        リプレイ関連の更新です
update_score.py         スコア加算の計算とかです
update_se.py            サウンドエフェクト(効果音)関連の処理を行います
update_ship.py          自機関連の更新、自機が出すショット、ミサイル、クロー関連も更新しております
update_status.py        メニューから表示される「STATUS」関連の計算を行います
update_system.py        システムデータのセーブ＆ロードの処理
update_title.py         タイトルメニューでの選択メニューをすべて行ってます
update_window.py        メインメニューなどで表示されるウィンドウの更新処理です セレクトカーソルの更新も行います

=============================================================================================
This is a detailed description of the program file 2022 Updated 10/30/2010
=============================================================================================
code-of-python.py       The main program, run this python program

code-of-python.spec     Spec file for pyinstaller

const.py                constants definitions, used by most programs, so import them or they won't work!

define_boss_data.py     Boss related data
define_class.py         Declaration of member variables of each class, and constructor processing.
define_data.py          List of various data
define_enemy_data.py    Enemy data related list
define_ship_data.py     Register the list of ship data.
define_sound.py         The process of loading BGM files in advance and registering them in the list.
define_stage_data.py    Register a list of event data for each stage and the stage array for the whole game.

func.py                 A group of functions with a certain degree of versatility, often called from update_* methods.
graph.py                This is a collection of methods called from the draw class. It is just a process to read the numerical value of a member variable containing coordinates and display a graphical representation accordingly.

readme.txt              This is the file.

update_boss.py          update boss-related processes
update_btn_assign.py    Pad control button settings, process which function to assign to each button
update_btn.py           Input related update process (keypad pressed, button pressed - that kind of thing)
update_collision.py     Performs collision detection     
update_debug.py         This program is used in debug mode.
update_enemy.py         Enemy-related processing
update_event.py         Analyzes the event data list of the stage and creates enemies.
update_init.py          Performs initialization processing immediately after the game starts and immediately after the stage starts.
update_ipl.py           Display IPL messages immediately after game startup
update_item.py          Updates item-related information.
update_obj.py           Updates various objects displayed in the background (clouds, sparks, particles, etc.)
update_pause.py         Processes when the game is paused         
update_replay.py        Replay related updates
update_score.py         Calculation of score addition
update_se.py            Processing of sound effects
update_ship.py          Updates to the ship's engine, shots, missiles, and claws.
update_status.py        Performs calculations related to the "STATUS" displayed from the menu
update_system.py        Handling of system data save and load
update_title.py         All menu selections in the title menu
update_window.py        Updates the window displayed in the main menu, etc. It also updates the select cursor