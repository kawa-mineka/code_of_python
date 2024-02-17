=============================================================================================
プログラムファイルの詳細な説明です    2024 02/18更新
=============================================================================================
│  code-of-python.py                   メインプログラムです、このパイソンプログラムを実行してね
│  code-of-python.spec                 pyinstaller用specファイルです
│  readme.txt                          このファイルだよ～☆彡
│  
├─assets
│  │  readme.txt                       assetsフォルダーの説明テキストです
│  │
│  ├─fonts                             日本語用ドットフォントが入っているフォルダーです
│  │      k8x12.txt
│  │      k8x12S_jisx0208.png          美咲フォントpng画像ファイルです
│  │      k8x12s_jisx0208___001a.png
│  │      k8x12s_jisx0208___001b.png
│  │      k8x12s_jisx0208___001c.png
│  │      k8x12s_jisx0208___002a.png
│  │      k8x12s_jisx0208___002b.png
│  │      k8x12s_jisx0208___002c.png
│  │      k8x12s_jisx0208___003a.png
│  │      k8x12s_jisx0208___003b.png
│  │      k8x12s_jisx0208___003c.png
│  │      k8x12s_jisx0208___004a.png
│  │      k8x12s_jisx0208___004b.png
│  │      k8x12s_jisx0208___004c.png
│  │      misaki_font_k8x12s_001.pyxres  美咲フォントをpyxeresファイルに変換したものです
│  │      misaki_font_k8x12s_002.pyxres
│  │      misaki_font_k8x12s_003.pyxres
│  │      misaki_font_k8x12s_004.pyxres
│  │      misaki_font_triming_cutter.py  美咲フォントのpngファイルをpyxresファイルに変換するプログラムです
│  │      p8font.png
│  │      readme.txt
│  │      フォントデータ編集001.bat       フォントデータ編集用のバッチファイルです
│  │      フォントデータ編集002.bat
│  │      フォントデータ編集003.bat
│  │      フォントデータ編集004.bat
│  │
│  ├─graphic
│  │      canvas.jpg
│  │      face.pyxres
│  │      face2.pyxres
│  │      face_graphic.bat
│  │      face_graphic2.bat
│  │      min-sht2.pyxres                                       1面2面のリソースファイルです
│  │      min-sht3.pyxres                                       3面4面のリソースファイルです
│  │      tes.png
│  │      test_grp.bat
│  │      test_grp.pyxres
│  │      test_miku.jpg
│  │      ステージ1ステージ2グラフイックリソースデータ編集.bat      各ステージリソースデータ編集用のバッチファイルです
│  │      ステージ4ステージ5グラフイックリソースデータ編集.bat
│  │
│  ├─music
│  │       各面のBGMファイルです
│  │      
│  ├─replay               リプレイデータが入っている各フォルダーです
│  │  ├─slot_0
│  │  ├─slot_1
│  │  ├─slot_2
│  │  ├─slot_3
│  │  ├─slot_4
│  │  ├─slot_5
│  │  ├─slot_6
│  │  ├─slot_7
│  │  ├─slot_8
│  │  ├─slot_9
│  │  └─slot_master       リプレイデータのコピー元となるマスターデータです
│  │
│  ├─sound                サウンドファイル置き場です(未使用)
│  └─system
│          master-system-data.pyxres   システムデータの原本です
│          システムデータ原本編集.bat    システムデータの原本編集用のバッチファイルです
│
├─common
│  └─ func.py                          ある程度の汎用性のある関数群です update_* の各メソッドから呼ばれる場合が多いですねぇ
│
├─const
│  └─ const.py                         定数定義です ほとんどのプログラムで使われてるのでimportしないと動かないよ
│     const_visualscene.py             ビジュアルシーンで主に使用する定数定義です
│     const_window.py                  ウィンドウクラスで主に使用する定数定義です
│
├─define
│  └─ boss_data.py    ボス関連のデータ
│     class_data.py   各クラスのメンバ変数とか宣言してます、あとコンストラクタの処理とか
│     data.py         色んなデータのリスト登録です
│     enemy_data.py   敵データ関連のリスト登録
│     ship_data.py    自機関連のデータリスト登録
│     stage_data.py   各ステージのイベントデータとか、ゲーム全体のステージ配列などのリスト登録です
│  
├─draw
│  └─ graph.py        drawクラスから呼ばれるメソッドが詰まっております 座標が入ったメンバ変数の数値を読んでそれに従ってグラフイックを表示するだけの処理です
│
├─update
│  └─ bg.py
│     boss.py          ボス関連の更新処理
│     btn.py           入力関連の更新処理(キーパッドが押されたとかボタンが押されたとか～そんなの)
│     btn_assign.py    パッドコントロールボタン設定です,各ボタンにどの機能を割り当てるかの処理です
│     collision.py     当たり判定を行ってます  
│     debug.py         デバッグモードで使用されるプログラムです、通常では使ったダメだよ☆彡
│     enemy.py         敵関連の処理です
│     event.py         ステージのイベントデータリストを解析して敵を出す処理です、あとBGマップのチップデータをみて敵の地上砲台を出現させたりも
│     init.py          ゲーム開始直後の初期処理やステージ開始直後の初期化処理を行います
│     ipl.py           ゲーム起動直後に出るIPLメッセージの表示とか
│     item.py          アイテム関連の更新
│     medal.py         主にメダルスロット関連の処理を行います
│     obj.py           背景に表示される色んなオブジェクト(雲とかスパークとかパーティクルとか)の更新処理です
│     pause.py         ゲーム中ポーズを掛けたときの処理
│     replay.py        リプレイ関連の更新です
│     score.py         スコア加算の計算とかです
│     ship.py          自機関連の更新、自機が出すショット、ミサイル、クロー関連も更新しております
│     sound.py         サウンドエフェクト(効果音)関連の処理を行います
│     status.py        メニューから表示される「STATUS」関連の計算を行います
│     system.py        システムデータのセーブ＆ロードの処理
│     title.py         タイトルメニューでの選択メニューをすべて行ってます
│     visualscene.py   ビジュアルシーンの作製や更新を行います
│     window.py        メインメニューなどで表示されるウィンドウの更新処理です セレクトカーソルの更新も行います
