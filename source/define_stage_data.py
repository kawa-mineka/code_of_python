from const import *         #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class define_stage_data:
    def __init__(self):
        None

    def game_event_list(self):     #ゲーム全体のイベントリストの定義
        #ゲーム全体のイベントリスト(ステージ、ループ数も考慮されてます)
        #フォーマット(このリストの書き方）は
        # game_event_list[
        #[ステージ1周回1、ステージ1周回2、ステージ1周回3],
        #[ステージ2周回1、ステージ2周回2、ステージ2周回3],
        #[ステージ3周回1、ステージ3周回2、ステージ3周回3],
        #[ステージ4周回1、ステージ4周回2、ステージ4周回3],
        #[ステージ5周回1、ステージ5周回2、ステージ5周回3],
        #[ステージ6周回1、ステージ6周回2、ステージ6周回3]
        #]
        #みたいな感じで書きます
        #self.game_event_list = [self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode]
        self.game_event_list = [
                            [self.event_list_stage_mountain_region_l1,
                            self.event_list_stage_mountain_region_l1,
                            self.event_list_stage_mountain_region_l1],
                            
                            [self.event_list_stage_advance_base_l1,
                            self.event_list_stage_advance_base_l2,
                            self.event_list_stage_advance_base_l3],
                            
                            [self.event_list_stage_volcanic_belt_l1,
                            self.event_list_stage_volcanic_belt_l1,
                            self.event_list_stage_volcanic_belt_l1]
                            ]

    def stage_data_list(self):     #ステージデータリストの定義
        #各ステージで使用する設定データのリストです
        #[ステージ名,
        # 障害物とみなす背景画像(BG)のY座標位置(例88だとキャラチップのＹ座標が88以上のマップチップは障害物とみなされます),
        # BG(背景スクロール)で使用するタイルマップの番号,
        #
        # 背景スクロールの種類,星スクロールのon/off 
        # ラスタスクロールのon/off,
        # BG背景(手前)を表示するかどうかのフラグ,BG背景(中央)を表示するかどうかのフラグ,BG背景(奥)を表示するかどうかのフラグ
        # 大気圏突入時の火花を表示するかどうかのフラグ
        # 背景マップチップを消去するときに使うチップ番号(主にマップスクロールで出来を出現させた後、その敵がいたマップチップをnull(消去)するときに使われます)]
        # 背景の縦幅(通常ステージは120で2画面分自由スクロールするステージなどは240になったりする)
        self.stage_data_list = [
            [STAGE_MOUNTAIN_REGION,256,TM1,
            SCROLL_TYPE_8FREEWAY_SCROLL_AND_RASTER ,STAR_SCROLL_ON,
            RASTER_SCROLL_ON,
            FRONT_BG_DISP_ON,CENTER_BG_DISP_ON,BACK_BG_DISP_ON,
            SPARK_ON,
            0,
            WINDOW_H],
            
            [STAGE_ADVANCE_BASE,   88 ,TM0,
            SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR    ,STAR_SCROLL_ON,
            RASTER_SCROLL_OFF,
            FRONT_BG_DISP_ON,CENTER_BG_DISP_ON,BACK_BG_DISP_ON,
            SPARK_OFF,
            0,
            WINDOW_H],
            
            [STAGE_VOLCANIC_BELT,   88 ,TM2,
            SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR    ,STAR_SCROLL_OFF,
            RASTER_SCROLL_OFF,
            FRONT_BG_DISP_ON,CENTER_BG_DISP_ON,BACK_BG_DISP_ON,
            SPARK_OFF,
            32*3,
            WINDOW_H * 2],
            
            
            
            
            ]

    def event_list(self):          #各ステージのイベントリストの定義
        #各ステージのイベントリストだよ
        #イベントリストは早回しで「イベントが実行されるステージカウント数タイマー」が書き換えられるので関数「update_stage_start_init」内でリスタートごとに再読み込みする
        #
        #データリスト形式
        #[イベントが実行されるステージカウント数タイマー,イベントの内容,敵キャラのIDナンバー,x座標,y座標,編隊の場合は編隊数,通常or早回し発生の判別,編隊殲滅後カウントを減少させる数,実際に減らすカウント数]
        #スクロールカウント数が99999999の場合は実質エンドコードみたいな～☆彡
        #
        #各イベントのフォーマット
        #EVENT_FAST_FORWARD_NUM   早回しする編隊群数と時間の設定[この時点から早回しする編隊群の数(例 3だとこのイベントからあと3イベント早回しが発生します),早回しするタイマー数(例 30だとこれ以降カウントタイマーが編隊を全滅させる事で30早まります)]
        #EVENT_ENEMY            敵の出現                [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊群の場合は編隊数の指定]
        #EVENT_WARNING          ワーニングダイアログ表示     [警告表示時間,グラフイックロゴ表示に掛ける時間,テキスト表示に掛ける時間](単位は全てフレームです)
        #EVENT_BOSS            各ステージに対応したボスを出現させる
        #EVENT_ADD_APPEAR_ENEMY   早回しの条件が成立したとき敵を出現させる [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊数]
        #EVENT_SCROLL           スクロール制御
        #   SCROLL_NUM_SET        スクロール関連のパラメーター設定 [横スクロールスピード設定値,横スクロールスピードの変化量,縦スクロールスピード設定値,縦スクロールスピードの変化量]
        #   SCROLL_START          スクロールの開始（横スクロールでスピードは通常の1)
        #   SCROLL_STOP           スクロールの停止
        #   SCROLL_SPEED_CHANGE    スクロールスピードを変化させる[スクロールスピードの設定値(-ならバックスクロール),スクロールスピードの変化量(-なら減速,+なら加速)]
        #   VERTICAL_SCROLL_START   縦スクロールの開始
        #   VERTICAL_SCROLL_STOP    縦スクロールのスタート
        #EVENT_DISPLAY_STAR      背景星スクロールのon/off [0=off/1=on]
        #EVENT_CHANGE_BG_CLS_COLOR 背景でまず最初に塗りつぶす色の指定 0~15 pyxelのカラーコード
        #EVENT_CHANGE_BG_TRANSPARENT_COLOR 背景マップチップを敷き詰める時に使用する透明色の指定 0~15 pyxelのカラーコード
        #EVENT_CLOUD            背景の雲の制御
        #   CLOUD_NUM_SET          雲のパラメータ設定[発生させる間隔(単位はフレーム),
        #                                    雲の量(0=比較的小さい雲だけ,1=小中サイズの雲を流す,2=小中大すべての種類の雲を流す),
        #                                    流れ方(0=そのまま左に素直に流れていく-0.25=上方向に流されていく0.25=下方向に流されていく),
        #                                    流れるスピード(倍率となります,通常は1,少数も使用可です)
        #                                    ]            
        #   CLOUD_START            雲を流すのを開始する
        #   CLOUS_STOP            雲を流すのを停止する
        #EVENT_RASTER_SCROLL        ラスタースクロールの制御
        #   RASTER_SCROLL_OFF         ラスタースクロールの表示をoffにする[表示オフにするラスタスクロールのid]
        #   RASTER_SCROLL_ON          ラスタースクロールの表示をonにする [表示オンにするラスタスクロールのid]
        #EVENT_BG_SCREEN_ON_OFF    背景BGの表示のon/off
        #   BG_BACK or BG_MIDDLE or BG_FRONT  BGの種類を選択
        #   DISP_OFF or DISP_ON            表示オフ/表示オン
        #EVENT_ENTRY_SPARK_ON_OFF  大気圏突入の火花表示のon/off
        #   SPARK_OFF or SPARK_ON           火花表示on/off
        
        #ボステストモード専用のボスだけを出現させるイベントリスト
        self.event_list_boss_test_mode = [
            [   50,EVENT_WARNING,500,120,240],
            [  100,EVENT_BOSS],
            [99999999],]
        self.event_list_no_enemy_mode = [
            [200000,EVENT_WARNING,500,120,240],
            [200200,EVENT_BOSS],
            [99999999],]
        
        self.event_list_stage_mountain_region_l1= [
            [ 100,EVENT_BG_SCREEN_ON_OFF,BG_BACK,DISP_OFF],
            [ 110,EVENT_ENTRY_SPARK_ON_OFF,SPARK_OFF],
            
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 40   ,6],
            [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,        0.5,0.01],
            [ 303,EVENT_ENTRY_SPARK_ON_OFF,SPARK_ON],
            [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,        0.5,0.01],
            [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,        0.5,0.01],
            [ 403,EVENT_ENEMY,CIR_COIN    ,160, 70   ,6],
            [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,        0.5,0.01],
            [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,        0.5,0.01],
            [ 550,EVENT_ENEMY,CIR_COIN    ,160, 40   ,6],
            [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,        0.5,0.01],
            [ 690,EVENT_ENEMY,CIR_COIN    ,160, 70   ,6],
            [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,        0.5,0.01],
            [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,        0.5,0.01],
            [ 891,EVENT_ENEMY,SAISEE_RO,170, 50-10],
            [ 892,EVENT_ENEMY,SAISEE_RO,169, 50   ],
            [ 893,EVENT_ENEMY,SAISEE_RO,168, 50+10],
            [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,        0.5,0.01],
            
            [ 910,EVENT_BG_SCREEN_ON_OFF,BG_BACK,DISP_ON],
            
            [ 951,EVENT_ENEMY,SAISEE_RO,170, 50-20],
            [ 952,EVENT_ENEMY,SAISEE_RO,169, 50   ],
            [ 953,EVENT_ENEMY,SAISEE_RO,168, 50+20],
            
            [1000,EVENT_CLOUD,CLOUD_NUM_SET,6,1,-0.25,1],
            [1010,EVENT_CLOUD,CLOUD_START],
            
            [1051,EVENT_ENEMY,SAISEE_RO,170, 50-30],
            [1052,EVENT_ENEMY,SAISEE_RO,169, 50-20],
            [1053,EVENT_ENEMY,SAISEE_RO,168, 50   ],
            [1054,EVENT_ENEMY,SAISEE_RO,167, 50+20],
            [1055,EVENT_ENEMY,SAISEE_RO,166, 50+30],
            
            [1100,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1110,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1120,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1130,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1140,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1150,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1160,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1170,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            [1180,EVENT_ENEMY,SAISEE_RO,170, 30   ],
            
            [1300,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1310,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1320,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1330,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1340,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1350,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1360,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1370,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            [1380,EVENT_ENEMY,SAISEE_RO,170, 70   ],
            
            [1451,EVENT_ENEMY,SAISEE_RO,170, 10   ],
            [1452,EVENT_ENEMY,SAISEE_RO,169, 20   ],
            [1453,EVENT_ENEMY,SAISEE_RO,168, 30   ],
            [1454,EVENT_ENEMY,SAISEE_RO,167, 40   ],
            [1455,EVENT_ENEMY,SAISEE_RO,166, 50   ],
            [1456,EVENT_ENEMY,SAISEE_RO,165, 60   ],
            [1457,EVENT_ENEMY,SAISEE_RO,164, 70   ],
            [1458,EVENT_ENEMY,SAISEE_RO,163, 80   ],
            [1459,EVENT_ENEMY,SAISEE_RO,162, 90   ],
            
            [1500,EVENT_DISPLAY_STAR,           DISP_OFF],
            [1510,EVENT_CHANGE_BG_CLS_COLOR,        12],
            [1560,EVENT_CHANGE_BG_TRANSPARENT_COLOR,  12],
            
            [1561,EVENT_ENEMY,SAISEE_RO,170, 10   ],
            [1562,EVENT_ENEMY,SAISEE_RO,169, 20   ],
            [1563,EVENT_ENEMY,SAISEE_RO,168, 30   ],
            [1564,EVENT_ENEMY,SAISEE_RO,167, 40   ],
            [1565,EVENT_ENEMY,SAISEE_RO,166, 50   ],
            [1566,EVENT_ENEMY,SAISEE_RO,165, 60   ],
            [1567,EVENT_ENEMY,SAISEE_RO,164, 70   ],
            [1568,EVENT_ENEMY,SAISEE_RO,163, 80   ],
            [1569,EVENT_ENEMY,SAISEE_RO,162, 90   ],
            
            [1600,EVENT_CLOUD,CLOUD_NUM_SET,6,2,-0.4,1],
            
            [1610,EVENT_ENEMY,VOLDAR,168, 0],
            
            
            [1710,EVENT_ENEMY,RAY_BLASTER,168, 40-20],
            [1720,EVENT_ENEMY,RAY_BLASTER,168, 40   ],
            [1730,EVENT_ENEMY,RAY_BLASTER,168, 40+20],
            
            [1810,EVENT_ENEMY,RAY_BLASTER,168, 60-20],
            [1850,EVENT_ENEMY,RAY_BLASTER,168, 60   ],
            [1890,EVENT_ENEMY,RAY_BLASTER,168, 60+20],
            
            
            
            [2300,EVENT_SCROLL,SCROLL_SPEED_CHANGE,0.5,-0.01],
            
            [2310,EVENT_RASTER_SCROLL,RASTER_SCROLL_OFF,1],
            
            [2340,EVENT_ENEMY,TWIN_ARROW,160,  20],
            [2341,EVENT_ENEMY,TWIN_ARROW,160,  60],
            [2342,EVENT_ENEMY,TWIN_ARROW,160, 100],
            
            [2600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
            [2601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
            [2602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
            [2603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
            [2604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],
            
            [2740,EVENT_ENEMY,TWIN_ARROW,120,  -8],
            [2741,EVENT_ENEMY,TWIN_ARROW,160, 60],
            [2742,EVENT_ENEMY,TWIN_ARROW,120,  130],
            
            [2840,EVENT_ENEMY,TWIN_ARROW,120,  -8],
            [2841,EVENT_ENEMY,TWIN_ARROW,80,  -8],
            [2842,EVENT_ENEMY,TWIN_ARROW,160, 60],
            [2843,EVENT_ENEMY,TWIN_ARROW,80,  130],
            [2844,EVENT_ENEMY,TWIN_ARROW,120,  130],
            
            [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0,-0.004],
            [3100,EVENT_CLOUD,CLOUD_STOP],
            [3110,EVENT_ENTRY_SPARK_ON_OFF,SPARK_OFF],
            
            [3200,EVENT_WARNING,500,120,240],
            
            
            [3320,EVENT_SCROLL,SCROLL_SPEED_CHANGE,3.0,0.0001],
            [3340,EVENT_BOSS],
            
            [3420,EVENT_SCROLL,SCROLL_SPEED_CHANGE,4.0,0.001],
            
            
            
            [99999999],]
        self.event_list_stage_mountain_region_l2= [
            
            [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,        0.5,0.01],
            [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,        0.5,0.01],
            [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,        0.5,0.01],
            [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,        0.5,0.01],
            [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,        0.5,0.01],
            [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,        0.5,0.01],
            [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,        0.5,0.01],
            [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,        0.5,0.01],
            [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,        0.5,0.01],
            
            [1000,EVENT_CLOUD,CLOUD_NUM_SET,6,1,-0.25,1],
            
            [1010,EVENT_CLOUD,CLOUD_START],
            
            [1500,EVENT_DISPLAY_STAR,           0],
            [1510,EVENT_CHANGE_BG_CLS_COLOR,        12],
            [1560,EVENT_CHANGE_BG_TRANSPARENT_COLOR,  12],
            
            
            [1600,EVENT_CLOUD,CLOUD_NUM_SET,6,2,-0.4,1],
            
            [2300,EVENT_SCROLL,SCROLL_SPEED_CHANGE,0.5,-0.01],
            
            [2310,EVENT_RASTER_SCROLL,RASTER_SCROLL_OFF,1],
            
            [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0,-0.004],
            [3100,EVENT_CLOUD,CLOUD_STOP],
            [3200,EVENT_SCROLL,SCROLL_SPEED_CHANGE,3.0,0.0001],
            [4000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
            [5000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
            [6000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
            [7000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
            [8000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
            [9000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
            [11000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
            [14000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
            
            
            
            [99999999],]
        
        self.event_list_stage_mountain_region_dummy= [
            [99999999],]
            
        self.event_list_stage_advance_base_l1= [
            
            [  10,EVENT_FAST_FORWARD_NUM,4,30],
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
            [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
            
            [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
            [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
            [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],
            
            [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
            [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
            [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
            
            [1095,EVENT_ENEMY,GREEN_LANCER,180,10],
            
            [1100,EVENT_ENEMY,CIR_COIN,    160,20    ,7],
            [1300,EVENT_ENEMY,CIR_COIN,    160,80    ,7],
            
            [1400,EVENT_ENEMY,TWIN_ARROW,160, 40],
            [1401,EVENT_ENEMY,TWIN_ARROW,160, 60],
            [1402,EVENT_ENEMY,TWIN_ARROW,160, 80],
            
            [1500,EVENT_ENEMY,TWIN_ARROW,160,  20],
            [1501,EVENT_ENEMY,TWIN_ARROW,160,  60],
            [1502,EVENT_ENEMY,TWIN_ARROW,160, 100],
            
            [1600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
            [1601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
            [1602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
            [1603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
            [1604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],
            
            [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE,-4,-0.001],
            [4800,EVENT_SCROLL,SCROLL_STOP],
            [5010,EVENT_SCROLL,SCROLL_SPEED_CHANGE,1, 0.002],
            [6000,EVENT_SCROLL,SCROLL_SPEED_CHANGE,5, 0.002],
            
            [7000,EVENT_WARNING,500,120,240],
            [7300,EVENT_BOSS],
            [99999999],]
        self.event_list_stage_advance_base_l2= [
            [  10,EVENT_FAST_FORWARD_NUM,4,30],
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
            [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
            
            [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
            [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
            [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],
            
            [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
            [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
            [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
            
            [1095,EVENT_ENEMY,GREEN_LANCER,180,10],
            
            [6000,EVENT_WARNING,500,120,240],
            [6300,EVENT_BOSS],
            [99999999],]
        self.event_list_stage_advance_base_l3= [    
            [  10,EVENT_FAST_FORWARD_NUM,4,30],
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
            [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
            
            [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
            [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
            [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],
            
            [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
            [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
            [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
            
            [1095,EVENT_ENEMY,GREEN_LANCER,180,10],
            
            [1100,EVENT_ENEMY,CIR_COIN,    160,20    ,7],
            [1300,EVENT_ENEMY,CIR_COIN,    160,80    ,7],
            
            [1400,EVENT_ENEMY,TWIN_ARROW,160, 40],
            [1401,EVENT_ENEMY,TWIN_ARROW,160, 60],
            [1402,EVENT_ENEMY,TWIN_ARROW,160, 80],
            
            [1500,EVENT_ENEMY,TWIN_ARROW,160,  20],
            [1501,EVENT_ENEMY,TWIN_ARROW,160,  60],
            [1502,EVENT_ENEMY,TWIN_ARROW,160, 100],
            
            [1600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
            [1601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
            [1602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
            [1603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
            [1604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],
            
            [6000,EVENT_WARNING,500,120,240],
            [6300,EVENT_BOSS],
            [99999999],] 
        
        
        self.event_list_stage_volcanic_belt_l1= [
            
            [   5,EVENT_CHANGE_BG_TRANSPARENT_COLOR,  15],
            [  10,EVENT_FAST_FORWARD_NUM,4,30],
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
            [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
            
            [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
            [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
            [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],
            
            [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
            [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
            [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
            
            [1095,EVENT_ENEMY,GREEN_LANCER,180,10],
            
            [1100,EVENT_ENEMY,CIR_COIN,    160,20    ,7],
            [1300,EVENT_ENEMY,CIR_COIN,    160,80    ,7],
            
            [1400,EVENT_ENEMY,TWIN_ARROW,160, 40],
            [1401,EVENT_ENEMY,TWIN_ARROW,160, 60],
            [1402,EVENT_ENEMY,TWIN_ARROW,160, 80],
            
            [1500,EVENT_ENEMY,TWIN_ARROW,160,  20],
            [1501,EVENT_ENEMY,TWIN_ARROW,160,  60],
            [1502,EVENT_ENEMY,TWIN_ARROW,160, 100],
            
            [1600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
            [1601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
            [1602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
            [1603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
            [1604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],
            
            [4000,EVENT_WARNING,500,120,240],
            [4300,EVENT_BOSS],
            [99999999],]

    def bg_animation_list(self):   #各ステージのＢＧ書き換えによるアニメーションの為のデータリスト群の定義
        #フォーマットの説明
        #[アニメーションさせたいマップチップのx座標(0~255(8の倍数にしてね)),
        #                            y座標(0~255(8の倍数にしてね)),
        #                           アニメスピード(1なら1フレーム毎 2だと2フレーム毎って感じ),
        #                           アニメ枚数(横一列に並べてください)]
        self.bg_animation_list_mountain_region = [
                            [192,192,6,8],                          
                            [144, 64,6,8],
                            ]


