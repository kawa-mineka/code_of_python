=============================================================================================
プログラムファイルの詳細な説明です    2022 05/07更新
=============================================================================================
code-of-python.py       メインプログラムです、このパイソンプログラムを実行してね

code-of-python.spec     pyinstaller用specファイルです

const.py                定数定義です ほとんどのプログラムで使われてるのでimportしないと動かないよ

define_boss_data.py     ボス関連のデータ
define_class.py         各クラスのメンバ変数とか宣言してます、あとコンストラクタの処理とか
define_data.py          色んなデータのリスト登録です
define_enemy_data.py    敵データ関連のリスト登録
define_ship_data.py     自機関連のデータリスト登録
define_sound            BGMファイルを事前に読み込み、リストに登録する処理
define_stage_data.py    各ステージのイベントデータとか、ゲーム全体のステージ配列などのリスト登録です

func.py                 ある程度の汎用性のある関数群です update_* の各メソッドから呼ばれる場合が多いですねぇ
graph.py                drawクラスから呼ばれるメソッドが詰まっております 座標が入ったメンバ変数の数値を読んでそれに従ってグラフイックを表示するだけの処理です

readme.txt              このファイルだよ～☆彡

update_boss.py          ボス関連の更新処理
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
update_ship.py          自機関連の更新、自機が出すショット、ミサイル、クロー関連も更新しております
update_status.py        メニューから表示される「STATUS」関連の計算を行います
update_system.py        システムデータのセーブ＆ロードの処理
update_title.py         タイトルメニューでの選択メニューをすべて行ってます
update_window.py        メインメニューなどで表示されるウィンドウの更新処理です