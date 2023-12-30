###########################################################
#  update_titleクラス                                       #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にタイトルメニューの更新を行う関数(メソッド？）ですよ～♪  #
# 2022 04/03からファイル分割してモジュールとして運用開始      #
###########################################################
import copy #スコアボードでデフォルトスコアボードを深い階層までのコピーを使いたいのでインポートします

import pyxel                     #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const              import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func               import * #汎用性のある関数群のモジュールの読み込み
from update.update_system      import * #システムデータをセーブするときに使用します
from update.update_window      import * #各種ウィンドウ作成時に使用するのでインポート
from update.update_visualscene import * #ビジュアルシーン作成時に使用するのでインポートします
# from update.update_sound       import * #SEのVOLリスト原本を取得しバックアップするために必要なのでインポート
from update.update_btn_assign  import * #パッドボタン割り当てのリスト更新で使用するのでインポートします

class update_title:
    def __init__(self):
        None

    #タイトル表示に必要な変数を設定＆初期化する##############
    def title_init(self):
        """
        タイトル表示に必要な変数を設定＆初期化する
        """
        pyxel.load(os.path.abspath("./assets/graphic/min-sht2.pyxres")) #タイトル＆ステージ1＆2のリソースファイルを読み込む
        # pyxel.load("./assets/graphic/min-sht2.pyxres") #タイトル＆ステージ1＆2のリソースファイルを読み込む
        #タイトル関連の変数を初期化
        
        # dat = pyxel.sound(5).volumes #ボリューム調整用にテスト表示
        # print("LEN" + str(len(dat)))
        # for i in range(len(dat)):
        #     print(str(dat[i]))
        
        update_sound.backup_se_vol_list(self)            #各効果音のVOLのリストを原本として保存しておくメソッドの呼び出し
        update_sound.create_adjustable_se_vol_list(self) #マスターSEボリュームリストを参考にボリューム調整を施したリストを作り上げるメソッドの呼び出し
        
        if self.title_startup_count == 0:
            #初回起動
            self.display_title_time      = 204      #タイトルを表示する時間
            self.title_oscillation_count = 200      #タイトルグラフイックの振れ幅カウンター
            self.title_slash_in_count    = 100      #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
        else:#2回目以降の起動
            self.display_title_time      = 104      #タイトルを表示する時間
            self.title_oscillation_count = 100      #タイトルグラフイックの振れ幅カウンター
            self.title_slash_in_count =    50       #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
        
        self.push_any_btn_flag    = FLAG_OFF        #何かしらかのボタンが押されたかどうかのフラグを降ろしておく
        self.release_the_btn_flag = FLAG_OFF        #すべての決定ボタンが離された？かどうかのフラグを降ろしておく
        
        self.stars             = []  #タイトル表示時も背景の星を流したいのでリストをここで初期化してやります
        self.star_scroll_speed = 1   #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
        self.window            = []  #タイトル表示時もメッセージウィンドウを使いたいのでリストをここで初期化してあげます
        self.visualscene       = []  #タイトル表示時もビジュアルシーンを使いたいのでリストをここで初期化してあげます
        self.redraw_star_area  = []  #タイトル表示時も半透明ウィンドウ表示でのスターリドロー処理も行いたいのでここで初期化してあげます
        self.cursor            = []  #タイトル表示時もウィンドウカーソルを使いたいのでリストをここで初期化してあげます
        
        #リプレイ記録用に使用する横無限大,縦50ステージ分の空っぽのリプレイデータリストを作成します
        self.replay_recording_data =[[] for i in range(50)]
        
        self.bg_cls_color = 0         #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)ゲーム時に初期値から変更されることがあるのでここで初期化する
        
        # セレクトカーソル関連の変数宣言   タイトル画面でセレクトカーソルを使いたいのでここで変数などを宣言＆初期化します
        self.cursor_type = CURSOR_TYPE_NO_DISP #セレクトカーソルの種類
        self.cursor_x = 0                      #セレクトカーソルのx座標
        self.cursor_y = 0                      #セレクトカーソルのy座標
        self.cursor_step_x = STEP4             #横方向の移動ドット数(初期値は4ドット)
        self.cursor_step_y = STEP7             #縦方向の移動ドット数(初期値は7ドット)
        self.cursor_page = 0                   #いま指し示しているページナンバー
        self.cursor_pre_page = 0               #前フレームで表示していたページ数 pre_pageとpageが同じなら新規ウィンドウは育成しない
        self.cursor_page_max = 0               #セレクトカーソルで捲ることが出来る最多ページ数
        self.cursor_item_x = 0                 #いま指し示しているアイテムナンバーx軸方向
        self.cursor_item_y = 0                 #いま指し示しているアイテムナンバーy軸方向
        self.cursor_decision_item_x = UNSELECTED #ボタンが押されて「決定」されたアイテムのナンバーx軸方向 UNSELECTEDは未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.cursor_decision_item_y = UNSELECTED #ボタンが押されて「決定」されたアイテムのナンバーy軸方向 UNSELECTEDは未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.cursor_max_item_x = 0             #x軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.cursor_max_item_y = 0             #y軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.cursor_color = 0                  #セレクトカーソルの色
        self.cursor_menu_layer = MENU_LAYER0   #現在選択中のメニューの階層の数値が入ります
        self.cursor_pre_decision_item_y = 0    #前の階層で選択したアイテムのナンバーを入れます
                                            #選択してcursor_decision_item_yに入ったアイテムナンバーをcursor_pre_decision_item_yに入れて次の階層に潜るって手法かな？
        self.cursor_move_direction = 0         #セレクトカーソルがどう動かせることが出来るのか？の状態変数です
        self.cursor_move_data = 0              #カーソルが実際に動いた方向のデータが入ります
        self.cursor_button_data =   BTN_NONE   #カーソル決定時に押されたボタンのIDが入ります
        self.cursor_size      = 0              #セレクトカーソルの大きさです(囲み矩形タイプで使用します)
        self.cursor_repeat_flag = FLAG_OFF     #セレクトカーソルの移動リピートを行うかどうかのフラグです OFF=リピートは掛けないpyxelのbtnpでカーソル移動を判断する ON=キーリピートオン
        self.cursor_repeat_time_count = 10     #セレクトカーソルの方向キーを押し続けた状態(キーリピート)のタイムカウントです(キーリピートカウンター) 初期値は10フレーム=(60分の1秒)x10なので6ぶんの1秒ごとにカーソルが動くという事です
        self.keypad_repeat_num = 3             #キーパッドのリピートが掛ったとき何フレームごとにボタンをONにするかの数値(リピートが掛ると減少していくようにする)
        self.cursor_pad_assign_mode = FLAG_OFF #パッドボタンアサインモードのフラグをOFFにします FLAG_OFF=ABXYボタンとLRショルダーボタンのみ機能します(パッドアサインモード以外はこちらの状態での使用となります)
                                                #                                               FLAG_ON=ABXY,BACK,STARTボタンとLRショルダーボタンすべてが「決定」ボタンとなりパッドアサイン機能として使用できるようになるです            
        self.active_window_id = 0              #アクティブになっているウィンドウのIDが入ります
        self.active_window_index = 0           #アクティブになっているウィンドウのインデックスナンバー(i)が入ります(ウィンドウIDを元にして全ウィンドウデータから検索しインデックス値を求めるのです！)
        #system-data.pyxresリソースファイルからこれらの設定値を読み込むようにしたのでコメントアウトしています
        # self.game_difficulty = GAME_NORMAL         #難易度                  タイトルメニューで難易度を選択して変化させるのでここで初期化します
        
        # self.stage_number = STAGE_MOUNTAIN_REGION  #最初に出撃するステージ   タイトルメニューでステージを選択して変化させるのでここで初期化します
        # self.stage_loop   = 1                      #ループ数(ステージ周回数) タイトルメニューで周回数を選択して変化させるのでここで初期化します
        
        pygame.mixer.init(frequency = 44100)     #pygameミキサー関連の初期化
        pygame.mixer.music.set_volume(0.7)       #音量設定(0~1の範囲内)
        pygame.mixer.music.load('assets/music/BGM200-171031-konotenitsukame-intro.wav') #タイトルイントロ部分のwavファイルを読み込み
        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        pygame.mixer.music.play(1)               #イントロを1回だけ再生
        
        func.read_ship_equip_medal_data(self)    #プレイ中の自機リスト群にメダルスロット装備関連のデータを読み込んで行く関数の呼び出し
        func.zero_clear_out_of_range_slot(self)  #総スロット以上の場所のスロットを空にする関数の呼び出し
        
        if self.title_startup_count == 0:
            update_window.create(self,WINDOW_ID_TITLE_TEXT,0,0)  #タイトルで表示されるテキスト群ウィンドウ(フレームレス)(外枠は表示しない)を作製
            #選択カーソル表示はoff,カーソルは上下移動のみ,いま指示しているアイテムナンバーは0,まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
            #選択できる項目数は13項目なので 13-1=12を代入,メニューの階層は最初は0にします,カーソル移動ステップはx4,y7
            func.set_cursor_data(self,CURSOR_TYPE_NO_DISP,CURSOR_MOVE_UD,0,0,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER0)
            self.active_window_id = WINDOW_ID_TITLE_TEXT  #このウィンドウIDを最前列アクティブなものとする
            self.push_any_btn_flag    = FLAG_OFF          #決定ボタンを押した,離したフラグをオフにする
            self.release_the_btn_flag = FLAG_OFF
            update_visualscene.create(self,VS_ID_OPENING_STORY1)             #オープニングのストーリーテキストその1のビジュアルシーンを作製する
            update_visualscene.init_storyboard(self)                         #ストーリーボードの初期化
            self.game_status = Scene.TITLE_FIRST   #初回起動の場合は,       ゲームステータスを「TITLE_FIRST」 にしてタイトル表示を開始する
        else:
            self.game_status = Scene.TITLE_SECOND  #2回目以降の起動の場合は,ゲームステータスを「TITLE_SECOND」にしてタイトル表示を開始する

    #タイトルの更新############################################################
    def title(self):
        """
        タイトルの更新
        """
        self.display_title_time -= 1          #タイトルを表示する時間カウンターを1減らす
        if self.display_title_time <= 0:      #カウンターが0以下になったら・・・
            self.display_title_time = 0       #強制的に0の状態にする
        
        self.title_oscillation_count -= 1     #タイトルグラフイックの振れ幅カウンターを1減らす
        if self.title_oscillation_count < 0:  #カウンターが0以下になったら・・・
            self.title_oscillation_count = 0  #強制的に0の状態にする
        
        self.title_slash_in_count -= 1        #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンターを1減らす
        if self.title_slash_in_count < 0:     #カウンターが0以下になったら・・・
            self.title_slash_in_count = 0     #強制的に0の状態にする
        
        #BGMイントロ再生が終了したらBGMループ部分を再生し始める
        if pygame.mixer.music.get_pos() == -1:      #pygame.mixer.music.get_posはBGM再生が終了すると-1を返してきます
            pygame.mixer.init(frequency = 44100)    #pygameミキサー関連の初期化
            pygame.mixer.music.set_volume(0.7)      #音量設定(0~1の範囲内)
            pygame.mixer.music.load('assets/music/BGM200-171031-konotenitsukame-loop.wav') #タイトルBGMループ部分のwavファイルを読み込み
            pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
            pygame.mixer.music.play(-1)             #タイトルBGMをループ再生
        
        #全てのカウンター類が0になったらゲームメニューウィンドウを育成する
        if self.title_oscillation_count == 0 and self.title_slash_in_count == 0 and self.display_title_time == 0:
            if self.title_startup_count == 0:
                self.game_status = Scene.TITLE_HIT_ANY_BTN  #初回起動の場合はゲームステータスを「TITLE_HIT_ANY_BTN」(タイトルを表示した後、何かしらのボタンの入力待ち状態)」にする
            else:
                update_window.create(self,WINDOW_ID_MAIN_MENU,0,0)         #メニューウィンドウを作製
                #選択カーソル表示をon,カーソルは上下移動のみ,いま指示しているアイテムナンバーは0,まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
                #選択できる項目数は13項目なので 13-1=12を代入,メニューの階層は最初は0にします,カーソル移動ステップはx4,y7
                func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,MAIN_MENU_X+5,MAIN_MENU_Y+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER0)
                self.active_window_id = WINDOW_ID_MAIN_MENU         #このウィンドウIDを最前列アクティブなものとする
                self.push_any_btn_flag    = FLAG_OFF                #決定ボタンを押した,離したフラグをオフにする
                self.release_the_btn_flag = FLAG_OFF
                self.game_status = Scene.TITLE_MENU_SELECT  #2回目以降の起動の場合は,ゲームステータスを「SCENE_TITLE_MENU_SELECT」にして直ぐにメニューセレクトに入る

    #タイトルメニューを表示した後,何かしらのボタンの入力待ち状態##########################
    def title_hit_any_btn(self):
        print (self.push_any_btn_flag)
        print(self.release_the_btn_flag)
        if self.push_any_btn_flag == FLAG_ON and self.release_the_btn_flag == FLAG_ON:
            pyxel.play(0,CURSOR_OK_SE_NORMAL)                   #カーソルOK音を鳴らす
            i = func.search_window_id(self,WINDOW_ID_TITLE_TEXT)
            self.window[i].vy = 0.3                             #WINDOW_ID_TITLE_TEXTウィンドウを下にフッ飛ばしていく
            self.window[i].vy_accel = 1.2
            self.window[i].window_status = WINDOW_CLOSE
            
            self.visualscene = []                                              #ビジュアルシーンを全て初期化する
            func.set_attrib_line_col(self,pyxel.COLOR_WHITE,pyxel.COLOR_WHITE) #タイトルデモのビジュアルシーンでは日本語テキストスクロールにグラデを掛けていたので白色に初期化する
            
            update_window.create(self,WINDOW_ID_MAIN_MENU,0,0)  #メニューウィンドウを作製
            #選択カーソル表示をon,カーソルは上下移動のみ,いま指示しているアイテムナンバーは0,まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
            #選択できる項目数は13項目なので 13-1=12を代入,メニューの階層は最初は0にします,カーソル移動ステップはx4,y7
            func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,MAIN_MENU_X+5,MAIN_MENU_Y+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER0)
            self.active_window_id = WINDOW_ID_MAIN_MENU         #このウィンドウIDを最前列アクティブなものとする
            self.push_any_btn_flag    = FLAG_OFF                #決定ボタンを押した,離したフラグをオフにする
            self.release_the_btn_flag = FLAG_OFF
            self.title_startup_count = 1                        #初回起動は終わったのでスタートアップカウントを2回目以降の起動カウント(とりあえず整数の1)にする
            self.game_status = Scene.TITLE_MENU_SELECT          #ゲームステータスを「TITLE_MENU_SELECT」(タイトルでメニューを選択中)」にする
            
        elif self.push_any_btn_flag == FLAG_ON and self.release_the_btn_flag == FLAG_OFF:
            if      pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) == False\
                and  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) == False\
                and  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) == False\
                and  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) == False:
                
                self.release_the_btn_flag = FLAG_ON #全てのボタンが離されたフラグをON
            
        elif self.push_any_btn_flag == FLAG_OFF and self.release_the_btn_flag == FLAG_OFF:
            if     pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) == True\
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) == True\
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) == True\
                or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) == True:
                
                self.push_any_btn_flag = FLAG_ON #何かしらかのボタンが押されたかどうかのフラグをON

    #タイトルメニューの選択中の更新#####################################
    def title_menu_select(self):
        """
        タイトルメニューの選択中の更新
        """
        if   self.cursor_menu_layer == MENU_LAYER0: #メニューが0階層目の選択分岐
            if   self.cursor_decision_item_y == MENU_GAME_START:        #GAME STARTが押されたら
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                self.move_mode = MOVE_MANUAL                #移動モードを「手動移動」にする
                self.replay_status = REPLAY_RECORD          #リプレイデータを「記録中」にする
                self.start_stage_number = self.stage_number #リプレイファイル保存用にゲーム開始時のステージナンバーとループ数を保管しておきます（リプレイデータはゲーム終了後にセーブされるのでstage_numberなどの値が変化するのでstart_stage_numberって変数を作ってリプレイ記録時にはこれを使うのです)
                self.start_stage_loop   = self.stage_loop
                self.game_status = Scene.GAME_START_INIT    #ゲームステータスを「GAME_START_INIT」にしてゲーム全体を初期化＆リスタートする
                self.active_window_id = WINDOW_ID_MAIN_MENU #メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_decision_item_y == MENU_SELECT_STAGE:      #SELECT STAGEが押されて
                if func.search_window_id(self,WINDOW_ID_SELECT_STAGE_MENU) == -1: #SELECT_STAGE_MENUウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SELECT STAGE」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)       #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_SELECT_STAGE_MENU,90,60)  #ステージセレクトウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は4項目なので 4-1=3を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,92,71,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,4-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_STAGE_MENU #このウィンドウIDを最前列アクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_SELECT_LOOP:       #SELECT LOOPが押されて
                if func.search_window_id(self,WINDOW_ID_SELECT_LOOP_MENU) == -1: #SELECT_LOOP_MENUウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SELECT LOOP」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_SELECT_LOOP_MENU,112,66)      #ループセレクトウィンドウの作成
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は3項目なので 3-1=2を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,90+24,72+5,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,3-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_LOOP_MENU  #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_BOSS_MODE:         #BOSS MODEが押されて
                if func.search_window_id(self,WINDOW_ID_BOSS_MODE_MENU) == -1: #BOSS MODEウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「BOSS MODE」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_BOSS_MODE_MENU,99,59)        #ボスモードon/offウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「ON」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96+5,69+self.boss_test_mode * STEP7,STEP4,STEP7,0,0,0,self.boss_test_mode,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_BOSS_MODE_MENU    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_HITBOX:            #HITBOXが押されて....
                if func.search_window_id(self,WINDOW_ID_HITBOX_MENU) == -1: #HITBOXウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「HITBOX」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_HITBOX_MENU,99,59)           #ヒットボックスon/offウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「OFF」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96+5,69+self.boss_collision_rect_display_flag * STEP7,STEP4,STEP7,0,0,0,self.boss_collision_rect_display_flag,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_HITBOX_MENU       #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_DIFFICULTY:        #DIFFICULTYが押されて
                if func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY) == -1: #SELECT_DIFFICULTYウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「DIFFICULTY」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_SELECT_DIFFICULTY,93,52)     #「SELECT DIFFICULTY」ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは2の「NORMAL」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は6項目なので 6-1=5を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96,63 + self.game_difficulty * STEP7,STEP4,STEP7,0,0,0,self.game_difficulty,UNSELECTED,UNSELECTED,0,6-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_DIFFICULTY #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_SELECT_SHIP:       #SELECT SHIPが押されて・・・
                if func.search_window_id(self,WINDOW_ID_SELECT_SHIP) == -1: #SELECT_SHIPウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SELECT SHIP」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_SELECT_SHIP,0,0)     #「SELECT SHIP」ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「JUSTICE PYTHON」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は13項目なので 13-1=12を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,7,10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_SHIP #このウィンドウIDを最前列でアクティブなものとする
                    #!check##############################################################################################
                    update_window.change_window_priority_top(self,WINDOW_ID_SELECT_SHIP) #ウィンドウ「SELECT SHIP」のプライオリティを最前面にする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_SCORE_BOARD:       #SCORE BOARDが押されて...
                if func.search_window_id(self,WINDOW_ID_SCORE_BOARD) == -1: #SCORE_BOARDウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SCORE BOARD」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create_score_board(self,GAME_NORMAL)                #スコアボードウィンドウを育成=============
                    #選択カーソル表示をoff,カーソルは表示せずLRキーもしくはLショルダーRショルダーで左右に頁をめくる動作,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は1項目なので 1-1=0を代入,いま指し示しているページナンバー 0=very easy,#最大ページ数 難易度は0~5の範囲 なのでMAX5,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NO_DISP,CURSOR_MOVE_SHOW_PAGE,92,71,STEP4,STEP7,0,5,0,0,UNSELECTED,UNSELECTED,0,0,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SCORE_BOARD       #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_NAME_ENTRY:        #NAME ENTRYが押されて...
                if func.search_window_id(self,WINDOW_ID_INPUT_YOUR_NAME) == -1: #INPUT_YOUR_NAMEウィンドウが存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_x = self.cursor_decision_item_x #現時点で選択されたアイテム「NAME ENTRY」を前のレイヤー選択アイテムとしてコピーする
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「NAME ENTRY」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_INPUT_YOUR_NAME,80,52)       #「ENTER YOUR NAME」ウィンドウの作製
                    #選択カーソルのタイプはアンダーバーの点滅にします,カーソルは左右でスライダー入力,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーx軸は0,y軸は0(縦には動かないので常に0となります)
                    #まだボタンも押されておらず未決定状態なのでdecision_item_x,decision_item_yはUNSELECTED,最大項目数x軸方向は(8文字+OKボタンなので)合計9項目 9-1=8を代入,最大項目数y軸方向は0,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_UNDER_BAR,CURSOR_MOVE_LR_SLIDER,100,66,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,9-1,0,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_INPUT_YOUR_NAME   #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_CONFIG:            #CONFIGが押されて
                if func.search_window_id(self,WINDOW_ID_CONFIG) == -1: #SELECT_CONFIGウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「CONFIG」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_CONFIG,4,4)                #「CONFIG」ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動+左右によるパラメーターの変更,カーソル移動ステップはx4,y9,いま指示しているアイテムナンバーは0の
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は12項目なので12-1=11を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD_SLIDER,10,16,STEP4,STEP8,0,0,0,0,UNSELECTED,UNSELECTED,0,12-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_CONFIG #このウィンドウIDを最前列でアクティブなものとする
                    update_window.change_window_priority_top(self,WINDOW_ID_CONFIG) #ウィンドウ「CONFIG」のプライオリティを最前面にする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_REPLAY:            #REPLAYが押されたら
                self.game_status = Scene.SELECT_LOAD_SLOT           #ゲームステータスを「SCENE_SELECT_LOAD_SLOT」にしてロードデータスロットの選択に移る
                update_window.create_replay_data_slot_select(self)               #リプレイデータファイルスロット選択ウィンドウの表示
                #選択カーソル表示をonにする,カーソルは上下移動のみ,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                #まだボタンも押されておらず未決定状態なのでdecision_item_yは-1最大項目数は「1」「2」「3」「4」「5」「6」「7」の7項目なので 7-1=6を代入,メニューの階層が増えたので,MENU_LAYER0からMENU_LAYER1にします
                func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,67,55,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,6,0,MENU_LAYER1)
                self.active_window_id = WINDOW_ID_SELECT_FILE_SLOT  #このウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_push_se) #カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_MEDAL:             #MEDALが押されて
                if func.search_window_id(self,WINDOW_ID_MEDAL_LIST) == -1 and func.search_window_id(self,WINDOW_ID_EQUIPMENT) == -1: #MEDAL_LISTウィンドウとEQUIPMENTウィンドウが同時に存在しないのなら・・
                    update_window.move_left_main_menu_window(self) #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「MEDAL_LIST」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)   #メインメニューのカーソルデータをPUSH
                    
                    update_window.create(self,WINDOW_ID_MEDAL_LIST,17,48) #「MEDAL_LIST」ウィンドウの作製
                    update_window.create(self,WINDOW_ID_EQUIPMENT,17,17)  #「EQUIPMENT」 ウィンドウの作製
                    #カーソルは点滅囲み矩形タイプ,カーソルは4方向,カーソル移動ステップはx10y10,いま指し示しているitem_x,item_yは(0,2)
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,x最大項目数は9項目なので9-1=8を代入,y最大項目数は5項目なので5-1=4を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_BOX_FLASH,CURSOR_MOVE_4WAY,46,60,STEP10,STEP10,0,0,0,2,UNSELECTED,UNSELECTED,9-1,5-1,0,MENU_LAYER1)
                    
                    self.active_window_id = WINDOW_ID_MEDAL_LIST #MEDAL_LISTウィンドウを最前列でアクティブなものとする
                    func.make_medal_list_window_comment_disp_flag_table(self) #メダルリストウィンドウで「存在するアイテム」を調べ上げコメント表示フラグテーブルを作製する関数の呼び出す
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_STATUS:            #STATUSが押されたら・・・
                if func.search_window_id(self,WINDOW_ID_STATUS) == -1: #STATUSウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「STATUS」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)         #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_STATUS,4,0)           #STATUSウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は11項目なので 13-1=12を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,9,10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_STATUS       #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_EXIT:              #EXITが押されたら・・・
                if func.search_window_id(self,WINDOW_ID_EXIT) == -1: #ゲーム終了(退出)ウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「EXIT」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    update_window.create(self,WINDOW_ID_EXIT,50,59)                  #ゲーム終了(退出)ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_EXIT    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
            
        elif self.cursor_menu_layer == MENU_LAYER1: #メニューが1階層目の選択分岐
            if  self.cursor_pre_decision_item_y  == MENU_SELECT_STAGE:
                if   self.cursor_decision_item_y == MENU_SELECT_STAGE_1:
                    #「SELECT STAGE」→「1」
                    self.stage_number   = 1                          #ステージナンバー1
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    
                    i = func.search_window_id(self,WINDOW_ID_SELECT_STAGE_MENU)
                    self.window[i].vx = 0.6            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.1
                    self.window[i].vy = 0.1 * self.stage_number
                    self.window[i].vy_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_SELECT_STAGE_2:
                    #「SELECT STAGE」→「2」
                    self.stage_number   = 2                         #ステージナンバー2
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    
                    i = func.search_window_id(self,WINDOW_ID_SELECT_STAGE_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.1
                    self.window[i].vy = 0.1 * self.stage_number
                    self.window[i].vy_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_SELECT_STAGE_3:
                    #「SELECT STAGE」→「3」
                    self.stage_number   = 3                        #ステージナンバー3
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    
                    i = func.search_window_id(self,WINDOW_ID_SELECT_STAGE_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.1
                    self.window[i].vy = 0.1 * self.stage_number
                    self.window[i].vy_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_SELECT_STAGE_4:
                    #「SELECT STAGE」→「4」
                    self.stage_number   = 4                        #ステージナンバー4
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    
                    i = func.search_window_id(self,WINDOW_ID_SELECT_STAGE_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.1
                    self.window[i].vy = 0.1 * self.stage_number
                    self.window[i].vy_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                

            elif self.cursor_pre_decision_item_y == MENU_SELECT_LOOP:
                if   self.cursor_decision_item_y == MENU_SELECT_LOOP_1:
                    #「SELECT LOOP NUMBER」→「1」
                    self.stage_loop = 1                           #ループ数に1週目を代入
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    i = func.search_window_id(self,WINDOW_ID_SELECT_LOOP_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_SELECT_LOOP_2:
                    #「SELECT LOOP NUMBER」→「2」
                    self.stage_loop = 2                           #ループ数に2週目を代入
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    i = func.search_window_id(self,WINDOW_ID_SELECT_LOOP_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_SELECT_LOOP_3:
                    #「SELECT LOOP NUMBER」→「3」
                    self.stage_loop = 3                          #ループ数に3週目を代入
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    i = func.search_window_id(self,WINDOW_ID_SELECT_LOOP_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_BOSS_MODE:
                if   self.cursor_decision_item_y == MENU_BOSS_MODE_OFF:
                    #「BOSS MODE」→「OFF」
                    self.boss_test_mode = MENU_BOSS_MODE_OFF        #ボステストモードをoff
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_BOSS_MODE_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_BOSS_MODE_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_BOSS_MODE_ON:
                    #「BOSS MODE」→「ON」
                    self.boss_test_mode = MENU_BOSS_MODE_ON  #ボステストモードをon
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_BOSS_MODE_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_BOSS_MODE_MENUウィンドウを右下にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.2
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_HITBOX:
                if   self.cursor_decision_item_y == MENU_HITBOX_OFF:
                    #「HITBOX」→「OFF」
                    self.boss_collision_rect_display_flag = 0            #ボス当たり判定表示をoff
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_HITBOX_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_HITBOX_MENUウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_HITBOX_ON:
                    #「HITBOX」→「ON」
                    self.boss_collision_rect_display_flag = 1            #ボス当たり判定表示をON
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_HITBOX_MENU)
                    self.window[i].vx = 0.3            #WINDOW_ID_HITBOX_MENUウィンドウを右下にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.2
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list   #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU                     #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY:
                if   self.cursor_decision_item_y == GAME_VERY_EASY:
                    #「DIFFICULTY」→「VERY_EASY」
                    self.game_difficulty = GAME_VERY_EASY
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = -0.1
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == GAME_EASY:
                    #「DIFFICULTY」→「EASY」
                    self.game_difficulty = GAME_EASY
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = -0.05
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == GAME_NORMAL:
                    #「DIFFICULTY」→「NORMAL」
                    self.game_difficulty = GAME_NORMAL
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == GAME_HARD:
                    #「DIFFICULTY」→「HARD」
                    self.game_difficulty = GAME_HARD
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.1
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == GAME_VERY_HARD:
                    #「DIFFICULTY」→「VERY_HARD」
                    self.game_difficulty = GAME_VERY_HARD
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.2
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == GAME_INSAME:
                    #「DIFFICULTY」→「INSAME」
                    self.game_difficulty = GAME_INSAME
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_SELECT_DIFFICULTY)
                    self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.3
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD:
                if   self.cursor_page == GAME_VERY_EASY and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_VERY_EASY)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_page == GAME_EASY      and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_EASY)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_page == GAME_NORMAL    and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_NORMAL)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_page == GAME_HARD      and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_HARD)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_page == GAME_VERY_HARD and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_VERY_HARD)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_page == GAME_INSAME    and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                    if self.cursor_move_data == PAD_RIGHT:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                    else:
                        func.all_move_window(self,WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                    
                    update_window.create_score_board(self,GAME_INSAME)                           #スコアボードウィンドウ育成
                    self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
                elif self.cursor_decision_item_y != -1: #何かしらのアイテムの所でボタンが押されたのなら
                    #SCORE BOARDはキー入力のタイミングで同じウィンドウIDを持つウィンドウが複数存在してしまう可能性があるので
                    #ウィンドウIDナンバーを元にすべての同一IDウィンドウを調べ上げ画面外にフッ飛ばすようにする
                    func.all_move_window(self,WINDOW_ID_SCORE_BOARD,0,0.3,0,1.2) #すべてのSCORE_BOARDウィンドウを下方向にフッ飛ばしていく
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)               #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED                    #前回選択したアイテムも未決定に
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_NAME_ENTRY and self.cursor_decision_item_x == MENU_NAME_ENTRY_OK:
                update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                #「ENTER YOUR NAME」→「OK」ボタンを押した
                text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                self.my_name = text[:8] #文字列textの先頭から8文字までをmy_nameとします
                func.all_move_window(self,WINDOW_ID_INPUT_YOUR_NAME,0.2,0.3,1.2,1.2) #すべてのINPUT_YOUR_NAMEウィンドウを右下方向にフッ飛ばしていく
                func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_CONFIG:
                if   self.cursor_decision_item_y == MENU_CONFIG_SCREEN_MODE:
                    flag_index = self.window[self.active_window_index].item_text[MENU_CONFIG_SCREEN_MODE][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexにMENU_CONFIG_SCREEN_MODEが入ったリストインデックス値が入ります
                    num = self.window[self.active_window_index].flag_list[flag_index] #numにフルスクリーン起動モードフラグが代入されます
                    if num == FLAG_ON:  #フルスクリーン起動モードフラグが立っていたのなら
                        pyxel.fullscreen(True)           #pyxel Ver1.5からfullscreen命令が追加されたらしい 裏技ッポイけど！？使っても良いのん？？
                    else:
                        pyxel.fullscreen(False)          #フルスクリーンフラグが立っていなかったらノーフルスクリーンモード(ウィンドウ表示)にする
                elif self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN:
                    update_window.change_window_priority_normal(self,WINDOW_ID_CONFIG) #CONFIGウィンドウの表示優先度を「normal」にする
                    if func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN) == -1: #「JOYPAD_ASSIGN」ウィンドウが存在しないのなら・・
                        self.cursor_pre_pre_decision_item_y = self.cursor_pre_decision_item_y #前のレイヤー選択アイテム「CONFIG」を前の前のレイヤー選択アイテムとして保存する
                        self.cursor_pre_decision_item_y     = self.cursor_decision_item_y     #今選択されたアイテム「JOYPAD ASSIGN」を前のレイヤー選択アイテムとして保存する
                        func.push_cursor_data(self,WINDOW_ID_CONFIG)             #「CONFIG」ウィンドウのカーソルデータをPUSH
                        update_window.create(self,WINDOW_ID_JOYPAD_ASSIGN,0,0) #「JOYPAD ASSIGN」ウィンドウの作製
                        #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは2の「NORMAL」
                        #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は13項目なので 13-1=12を代入,メニューの階層が増えたのでMENU_LAYER1からMENU_LAYER2にします
                        func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,7,10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER2)
                        self.active_window_id = WINDOW_ID_JOYPAD_ASSIGN #このウィンドウIDを最前列でアクティブなものとする
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                        self.cursor_pad_assign_mode = FLAG_ON                             #カーソル移動を「パッドボタン割り当てモードON」にします(BACK,STARTボタンも使用したい為です)
                elif self.cursor_decision_item_y == MENU_CONFIG_INITIALIZE:
                    update_window.change_window_priority_normal(self,WINDOW_ID_CONFIG) #CONFIGウィンドウの表示優先度を「normal」にする
                    if func.search_window_id(self,WINDOW_ID_INITIALIZE) == -1: #「INITIALIZE」ウィンドウが存在しないのなら・・
                        self.cursor_pre_pre_decision_item_y = self.cursor_pre_decision_item_y #前のレイヤー選択アイテム「CONFIG」を前の前のレイヤー選択アイテムとして保存する
                        self.cursor_pre_decision_item_y     = self.cursor_decision_item_y     #今選択されたアイテム「INITIALIZE」を前のレイヤー選択アイテムとして保存する
                        func.push_cursor_data(self,WINDOW_ID_CONFIG)           #「CONFIG」ウィンドウのカーソルデータをPUSH
                        ox,oy = (WINDOW_W - 48) // 2,(WINDOW_H - 58) // 2 #「INITIALIZE」ウィンドウの座標指定
                        update_window.create(self,WINDOW_ID_INITIALIZE,ox,oy)    #「INITIALIZE」ウィンドウの作製
                        #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは2の「NORMAL」
                        #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は7項目なので 7-1=6を代入,メニューの階層が増えたのでMENU_LAYER1からMENU_LAYER2にします
                        func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,ox + 3,oy + 11,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,7-1,0,MENU_LAYER2)
                        self.active_window_id = WINDOW_ID_INITIALIZE #このウィンドウIDを最前列でアクティブなものとする
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                elif self.cursor_decision_item_y == MENU_CONFIG_RETURN:
                    func.restore_master_flag_list(self) #フラグ＆データ関連のマスターリストを参照して個別のフラグ変数へリストアする
                    update_window.change_window_priority_normal(self,WINDOW_ID_CONFIG) #CONFIGウィンドウの表示優先度を「normal」にする
                    i = func.search_window_id(self,WINDOW_ID_CONFIG)
                    self.window[i].vx = -0.5            #WINDOW_ID_CONFIGウィンドウを左下にフッ飛ばしていく
                    self.window[i].vx_accel = 1.1
                    self.window[i].vy = 0.1
                    self.window[i].vy_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    
                    func.write_ship_equip_medal_data(self)                 #機体メダルスロット装備リストに現在プレイ中のシップリストのメダル情報を書き込む関数の呼び出し
                    update_system.save_data(self)                            #システムデータをセーブします
                    pyxel.load(os.path.abspath("./assets/graphic/min-sht2.pyxres")) #タイトル＆ステージ1＆2のリソースファイルを読み込む
                    # pyxel.load("./assets/graphic/min-sht2.pyxres") #タイトル＆ステージ1＆2のリソースファイルを読み込む
                    
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_MEDAL:
                if self.cursor_decision_item_y == 4 and 6 <= self.cursor_decision_item_x <= 8: #OKボタンが押されたときの処理
                    update_window.move_right_main_menu_window(self) #メインメニューウィンドウを右にずらす関数の呼び出し
                    func.create_master_flag_list(self) #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_MEDAL_LIST)
                    self.window[i].vx = 0.3            #MEDAL_LISTウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.1
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    
                    i = func.search_window_id(self,WINDOW_ID_EQUIPMENT)
                    self.window[i].vx = -0.3           #EQUIPMENTウィンドウを左にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.1
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                    self.cursor_size = CURSOR_SIZE_NORMAL       #矩形囲みタイプのセレクトカーソルのサイズを通常サイズに戻す
                elif 2 <= self.cursor_decision_item_y <= 4:                                    #所持メダルリスト欄内でボタンが押されたときの処理
                    i = func.search_window_id(self,WINDOW_ID_MEDAL_LIST) #メダルリストウィンドウのインデックス値取得
                    if self.window[i].comment_disp_flag[self.cursor_decision_item_y][self.cursor_decision_item_x] == DISP_ON: #決定ボタンが押された位置のコメント表示フラグが立っている時はそこの部分のアイテムは所持しているので....
                        num = self.window[i].item_id[self.cursor_decision_item_y][self.cursor_decision_item_x]                #決定ボタンが押された位置のアイテムIDを取得する
                        if num != MEDAL_NO_SLOT:               #MEDAL_NO_SLOT(メダルは何もない)以外の場合は
                            func.equip_medal_playing_ship(self,num) #アイテムID(この場合はメダルID)を書き込んで更新する
                    
                    i = func.search_window_id(self,WINDOW_ID_EQUIPMENT)    #メダル装備ウィンドウのインデックス値取得
                    self.window[i].ship_list = self.playing_ship_list #ウィンドウクラスのシップリストも更新してやります
                    func.medal_effect_plus_medallion(self)                #装備メダルに「スロット数を拡張するメダル」があればスロット数を増やし,無ければスロット数を初期状態にする関数の呼び出し
                    func.zero_clear_out_of_range_slot(self)               #現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする関数の呼び出し
                    
                    self.cursor_decision_item_x = UNSELECTED
                    self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_decision_item_y == MENU_MEDAL_MYSHIP_MEDAL_AREA:              #自機装備メダル欄内でボタンが押されたときの処理
                    i = func.search_window_id(self,WINDOW_ID_EQUIPMENT)             #メダル装備ウィンドウのインデックス値取得
                    func.purge_medal_playing_ship(self,self.cursor_decision_item_x) #決定ボタンが押された位置のスロットを空にする関数の呼び出し
                    func.zero_clear_out_of_range_slot(self)               #現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする関数の呼び出し
                    func.playing_ship_medal_left_justified(self)          #装備スロットに空が出来たので左に詰めていく関数を呼び出す              
                    
                    i = func.search_window_id(self,WINDOW_ID_EQUIPMENT)    #メダル装備ウィンドウのインデックス値取得
                    self.window[i].ship_list = self.playing_ship_list #ウィンドウクラスのシップリストも更新してやります
                    func.medal_effect_plus_medallion(self)                #装備メダルに「スロット数を拡張するメダル」があればスロット数を増やし,無ければスロット数を初期状態にする関数の呼び出し
                    
                    self.cursor_decision_item_x = UNSELECTED
                    self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                
            elif self.cursor_pre_decision_item_y == MENU_STATUS and 0 <= self.cursor_decision_item_y <= 12:
                i = func.search_window_id(self,WINDOW_ID_STATUS)
                self.window[i].vx = 0.3            #STATUSウィンドウを右下にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_x = UNSELECTED
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_SELECT_SHIP and self.cursor_decision_item_y == 12:
                update_window.change_window_priority_normal(self,WINDOW_ID_SELECT_SHIP) #SELECT_SHIPウィンドウの表示優先度を「normal」にする
                i = func.search_window_id(self,WINDOW_ID_SELECT_SHIP)
                self.window[i].vx = -0.3            #SELECT_SHIPウィンドウを左下にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_x = UNSELECTED
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_EXIT:
                if   self.cursor_decision_item_y == MENU_EXIT_NO:
                    i = func.search_window_id(self,WINDOW_ID_EXIT)
                    self.window[i].vy = -0.3            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    func.pop_cursor_data(self,WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                elif self.cursor_decision_item_y == MENU_EXIT_YES:
                    self.star_scroll_flag  = 1
                    i = func.search_window_id(self,WINDOW_ID_EXIT)
                    self.window[i].vy = -0.1            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.05
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.09
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    
                    i = func.search_window_id(self,WINDOW_ID_MAIN_MENU)
                    self.window[i].vy = -0.1            #メインメニューウィンドウを左上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.1
                    self.window[i].vx = -0.1
                    self.window[i].vx_accel = 1.1
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.game_quit_from_playing = 0                  #タイトルメニューからの終了
                    self.game_status = Scene.GAME_QUIT_START         #ステータスを「GAME QUIT START」ゲーム終了工程開始にする
            
        elif self.cursor_menu_layer == MENU_LAYER2: #メニューが2階層目の選択分岐
            if   self.cursor_pre_pre_decision_item_y == MENU_CONFIG:
                if   self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_decision_item_y == MENU_CONFIG_INITIALIZE_RETURN:
                    update_window.change_window_priority_normal(self,WINDOW_ID_INITIALIZE) #INITIALIZEウィンドウの表示優先度を「normal」にする
                    func.create_master_flag_list(self)                    #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,WINDOW_ID_INITIALIZE)
                    self.window[i].vx = 0.3                           #WINDOW_ID_INITIALIZEウィンドウを右上にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = -0.2
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list                #マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_CONFIG)                          #「CONFIG」ウィンドウのカーソルデータをPOP
                    self.cursor_pre_pre_decision_item_y = UNSELECTED                #前々回選択されたアイテムは未選択にして初期化
                    self.cursor_pre_decision_item_y = MENU_CONFIG                   #前回選択されたアイテムを「CONFIG」にする 
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_CONFIG                        #1階層前の「CONFIG」ウィンドウIDを最前列でアクティブなものとする
                    update_window.change_window_priority_top(self,WINDOW_ID_CONFIG) #CONFIGウィンドウの表示優先度を「TOP」にする
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_decision_item_y == MENU_CONFIG_INITIALIZE_SCORE:
                    if func.search_window_id(self,WINDOW_ID_PRINT_INIT_SCORE) == -1 and func.search_window_id(self,WINDOW_ID_SELECT_YES_NO) == -1: #PRINT_INIT_SCOREウィンドウとSELECT_YES_NOウィンドウが同時に存在しないのなら・・
                        self.cursor_pre_pre_pre_decision_item_y = self.cursor_pre_pre_decision_item_y #2回前に選択されたアイテムを3回前に選択されたアイテムにコピー 
                        self.cursor_pre_pre_decision_item_y = self.cursor_pre_decision_item_y #1回前に選択されたアイテムを2回前に選択されたアイテムにコピー
                        self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「INITIALIZE_SCORE」を前のレイヤー選択アイテムとしてコピーする
                        func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)           #メインメニューのカーソルデータをPUSH
                        update_window.create(self,WINDOW_ID_SELECT_YES_NO,34,25)    #「SELECT_YES_NO」 ウィンドウの作製
                        update_window.create(self,WINDOW_ID_PRINT_INIT_SCORE,20,10) #「PRINT_INIT_SCORE」ウィンドウの作製
                        #カーソルは点滅囲み矩形タイプ,カーソルは4方向,カーソル移動ステップはx4y7,いま指し示しているitem_x,item_yは(0,0)
                        #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,x最大項目数は1項目なので1-1=0を代入,y最大項目数は2項目なので2-1=1を代入,メニューの階層が増えたのでMENU_LAYER2からMENU_LAYER3にします
                        func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,38,35,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER3)
                        
                        self.active_window_id = WINDOW_ID_SELECT_YES_NO #SELECT_YES_NOウィンドウを最前列でアクティブなものとする
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_decision_item_y == MENU_CONFIG_INITIALIZE_NAME:
                    if func.search_window_id(self,WINDOW_ID_PRINT_INIT_NAME) == -1 and func.search_window_id(self,WINDOW_ID_SELECT_YES_NO) == -1: #PRINT_INIT_NAMEウィンドウとSELECT_YES_NOウィンドウが同時に存在しないのなら・・
                        self.cursor_pre_pre_pre_decision_item_y = self.cursor_pre_pre_decision_item_y #2回前に選択されたアイテムを3回前に選択されたアイテムにコピー 
                        self.cursor_pre_pre_decision_item_y = self.cursor_pre_decision_item_y #1回前に選択されたアイテムを2回前に選択されたアイテムにコピー
                        self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「INITIALIZE_NAME」を前のレイヤー選択アイテムとしてコピーする
                        func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)           #メインメニューのカーソルデータをPUSH
                        update_window.create(self,WINDOW_ID_SELECT_YES_NO,34,25)    #「SELECT_YES_NO」 ウィンドウの作製
                        update_window.create(self,WINDOW_ID_PRINT_INIT_NAME,20,10) #「PRINT_INIT_NAME」ウィンドウの作製
                        #カーソルは点滅囲み矩形タイプ,カーソルは4方向,カーソル移動ステップはx4y7,いま指し示しているitem_x,item_yは(0,0)
                        #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,x最大項目数は1項目なので1-1=0を代入,y最大項目数は2項目なので2-1=1を代入,メニューの階層が増えたのでMENU_LAYER2からMENU_LAYER3にします
                        func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,38,35,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER3)
                        
                        self.active_window_id = WINDOW_ID_SELECT_YES_NO #SELECT_YES_NOウィンドウを最前列でアクティブなものとする
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_decision_item_y == MENU_CONFIG_INITIALIZE_ALL:
                    if func.search_window_id(self,WINDOW_ID_PRINT_INIT_ALL) == -1 and func.search_window_id(self,WINDOW_ID_SELECT_YES_NO) == -1: #PRINT_INIT_ALLウィンドウとSELECT_YES_NOウィンドウが同時に存在しないのなら・・
                        self.cursor_pre_pre_pre_decision_item_y = self.cursor_pre_pre_decision_item_y #2回前に選択されたアイテムを3回前に選択されたアイテムにコピー 
                        self.cursor_pre_pre_decision_item_y = self.cursor_pre_decision_item_y #1回前に選択されたアイテムを2回前に選択されたアイテムにコピー
                        self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「INITIALIZE_NAME」を前のレイヤー選択アイテムとしてコピーする
                        func.push_cursor_data(self,WINDOW_ID_MAIN_MENU)           #メインメニューのカーソルデータをPUSH
                        update_window.create(self,WINDOW_ID_SELECT_YES_NO,34,25)    #「SELECT_YES_NO」 ウィンドウの作製
                        update_window.create(self,WINDOW_ID_PRINT_INIT_ALL,20,10) #「PRINT_INIT_ALL」ウィンドウの作製
                        #カーソルは点滅囲み矩形タイプ,カーソルは4方向,カーソル移動ステップはx4y7,いま指し示しているitem_x,item_yは(0,0)
                        #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,x最大項目数は1項目なので1-1=0を代入,y最大項目数は2項目なので2-1=1を代入,メニューの階層が増えたのでMENU_LAYER2からMENU_LAYER3にします
                        func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,38,35,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER3)
                        
                        self.active_window_id = WINDOW_ID_SELECT_YES_NO #SELECT_YES_NOウィンドウを最前列でアクティブなものとする
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                    
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_FIRE_AND_SUBWEAPON:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定の場合は何もしない
                        
                        #! self.pad_assign_list[self.cursor_button_data] = ACT_SHOT_AND_SUB_WEAPON
                        update_btn_assign.list(self,self.cursor_button_data,ACT_SHOT_AND_SUB_WEAPON)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)  #カーソルOK音を鳴らす
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)           #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list             #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)                 #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)           #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED                          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_MISSILE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #! self.pad_assign_list[self.cursor_button_data] = ACT_MISSILE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_MISSILE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_MAIN_WEAPON_CHANGE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #! self.pad_assign_list[self.cursor_button_data] = ACT_MAIN_WEAPON_CHANGE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_MAIN_WEAPON_CHANGE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_SUB_WEAPON_CHANGE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #! self.pad_assign_list[self.cursor_button_data] = ACT_SUB_WEAPON_CHANGE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_SUB_WEAPON_CHANGE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_SPEED:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #!self.pad_assign_list[self.cursor_button_data] = ACT_SPEED_CHANGE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_SPEED_CHANGE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_PAUSE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #!self.pad_assign_list[self.cursor_button_data] = ACT_PAUSE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_PAUSE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_CLAW_STYLE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #!self.pad_assign_list[self.cursor_button_data] = ACT_CHANGE_CLAW_STYLE
                        update_btn_assign.list(self,self.cursor_button_data,ACT_CHANGE_CLAW_STYLE)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_CLAW_DISTANCE:
                    if self.cursor_button_data != BTN_KEYBOARD_SPACE: #スペースキーで決定は除く
                        
                        #!self.pad_assign_list[self.cursor_button_data] = ACT_CHANGE_CLAW_INTERVAL
                        update_btn_assign.list(self,self.cursor_button_data,ACT_CHANGE_CLAW_INTERVAL)
                        
                        pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                        # self.cursor_button_data = BTN_NONE #押されたボタンIDを初期化
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_list = self.pad_assign_list    #ウィンドウクラスのパッドアサインリストも更新してやります
                        update_window.refresh_pad_assign_graph_list(self)        #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                        i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)  #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                        self.window[i].pad_assign_graph_list = self.pad_assign_graph_list    #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                        self.cursor_decision_item_x = UNSELECTED
                        self.cursor_decision_item_y = UNSELECTED          #選択アイテムをすべて「未選択」にします
                    
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_DEFAULT:
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)   #カーソルOK音を鳴らす
                    
                    self.pad_assign_list = copy.deepcopy(self.default_pad_assign_list) #パッド割り当て情報の初期データを深い階層でコピーする
                    i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)            #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                    self.window[i].pad_assign_list = self.pad_assign_list              #ウィンドウクラスのパッドアサインリストも更新してやります
                    update_window.refresh_pad_assign_graph_list(self)                  #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                    i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)            #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                    self.window[i].pad_assign_graph_list = self.pad_assign_graph_list  #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                    self.cursor_decision_item_x = UNSELECTED
                    self.cursor_decision_item_y = UNSELECTED                           #選択アイテムをすべて「未選択」にします
                    
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_CLEAR:
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)   #カーソルOK音を鳴らす
                    
                    self.pad_assign_list = copy.deepcopy(self.empty_pad_assign_list)   #パッド割り当て情報の空データを深い階層でコピーする
                    i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)            #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                    self.window[i].pad_assign_list = self.pad_assign_list              #ウィンドウクラスのパッドアサインリストも更新してやります
                    update_window.refresh_pad_assign_graph_list(self)                  #パッドアサイングラフイックリストを更新して新しいものにします(self.pad_assign_listに依存しているため)
                    i = func.search_window_id(self,WINDOW_ID_JOYPAD_ASSIGN)            #ジョイパッドボタン割り当て設定ウィンドウのインデックス値を取得
                    self.window[i].pad_assign_graph_list = self.pad_assign_graph_list  #ウィンドウクラスのパッドアサイングラフイックリストも更新してやります
                    self.cursor_decision_item_x = UNSELECTED
                    self.cursor_decision_item_y = UNSELECTED                           #選択アイテムをすべて「未選択」にします
                    
                elif self.cursor_pre_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN and self.cursor_decision_item_y == MENU_CONFIG_JOYPAD_ASSIGN_SAVE_AND_RETURN:
                    update_window.change_window_priority_normal(self,MENU_CONFIG_JOYPAD_ASSIGN) #MENU_CONFIG_JOYPAD_ASSIGNウィンドウの表示優先度を「normal」にする
                    func.create_master_flag_list(self)                              #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = func.search_window_id(self,MENU_CONFIG_JOYPAD_ASSIGN)
                    self.window[i].vx = 0.3                                         #MENU_CONFIG_JOYPAD_ASSIGNウィンドウを右上にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = -0.2
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.window[i].flag_list = self.master_flag_list                #マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                    func.pop_cursor_data(self,WINDOW_ID_CONFIG)                     #「CONFIG」ウィンドウのカーソルデータをPOP
                    self.cursor_pre_pre_decision_item_y = UNSELECTED                #前々回選択されたアイテムは未選択にして初期化
                    self.cursor_pre_decision_item_y = MENU_CONFIG                   #前回選択されたアイテムを「CONFIG」にする 
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                    self.active_window_id = WINDOW_ID_CONFIG                        #1階層前の「CONFIG」ウィンドウIDを最前列でアクティブなものとする
                    update_window.change_window_priority_top(self,WINDOW_ID_CONFIG) #CONFIGウィンドウの表示優先度を「TOP」にする
                    self.cursor_pad_assign_mode = FLAG_OFF                          #カーソル移動を「パッドボタン割り当てモードOFF」にします(パッドアサインは終了したのでBACK,STARTボタンは「決定」ボタンとして使用できないようにしたい為です)
                
        elif self.cursor_menu_layer == MENU_LAYER3: #メニューが3階層目の選択分岐
            if   self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_SCORE and self.cursor_decision_item_y == 0:
                #CONFIG→INITIALIZE→SCORE→NO
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_SCORE)
                self.window[i].vx = -0.6            #PRINT_INIT_SCOREウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
            elif self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_SCORE and self.cursor_decision_item_y == 1:
                #CONFIG→INITIALIZE→SCORE→YES
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_SCORE)
                self.window[i].vx = -0.6            #PRINT_INIT_SCOREウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE                    #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.score_board = copy.deepcopy(self.default_score_board)      #現在のスコアボードをデフォルトの物からコピーして初期化する
                update_system.save_data(self)                                         #システムデータをセーブします
                pyxel.load(os.path.abspath("./assets/graphic/min-sht2.pyxres"))                   #タイトル＆ステージ1＆2のリソースファイルを読みます
                
            elif self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_NAME and self.cursor_decision_item_y == 0:
                #CONFIG→INITIALIZE→NAME→NO
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_NAME)
                self.window[i].vx = -0.6            #PRINT_INIT_NAMEウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
            elif self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_NAME and self.cursor_decision_item_y == 1:
                #CONFIG→INITIALIZE→NAME→YES
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_NAME)
                self.window[i].vx = -0.6            #PRINT_INIT_NAMEウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE                    #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.my_name = copy.deepcopy(self.default_my_name)              #現在のマイネームリストをデフォルトの物からディープコピーして初期化する
                update_system.save_data(self)                                         #システムデータをセーブします
                pyxel.load(os.path.abspath("./assets/graphic/min-sht2.pyxres"))                   #タイトル＆ステージ1＆2のリソースファイルを読みます
                
            elif self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_ALL and self.cursor_decision_item_y == 0:
                #CONFIG→INITIALIZE→ALL→NO
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_ALL)
                self.window[i].vx = -0.6            #PRINT_INIT_ALLウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
            elif self.cursor_pre_pre_pre_decision_item_y == MENU_CONFIG and self.cursor_pre_pre_decision_item_y == MENU_CONFIG_INITIALIZE and self.cursor_pre_decision_item_y == MENU_CONFIG_INITIALIZE_ALL and self.cursor_decision_item_y == 1:
                #CONFIG→INITIALIZE→ALL→YES
                i = func.search_window_id(self,WINDOW_ID_PRINT_INIT_ALL)
                self.window[i].vx = -0.6            #PRINT_INIT_ALLウィンドウを左にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                i = func.search_window_id(self,WINDOW_ID_SELECT_YES_NO)
                self.window[i].vx = 0.6            #SELECT_YES_NOウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,WINDOW_ID_INITIALIZE)   #1階層前のカーソルデータをPOP
                self.cursor_pre_decision_item_y = self.cursor_pre_pre_decision_item_y         #preにMENU_CONFIG_INITIALIZEが入る
                self.cursor_pre_pre_decision_item_y = self.cursor_pre_pre_pre_decision_item_y #pre_preにMENU_CONFIGが入る
                self.cursor_decision_item_y = UNSELECTED                                      #選択アイテムは強制的に未選択にする
                self.active_window_id = WINDOW_ID_INITIALIZE                    #1階層前のイニシャライズウィンドウIDを最前列でアクティブなものとする
                pyxel.playm(5) #ビャカビャカビャビャカ～♪ボンボンボンボン・・・・・・
                
                self.my_name     = copy.deepcopy(self.default_my_name)                         #現在のマイネームリストをデフォルトの物からディープコピーして初期化する
                self.medal_list  = copy.deepcopy(self.default_medal_list)                      #現在のメダル所有リストをデフォルトの物からディープコピーして初期化する
                self.achievement_list      = copy.deepcopy(self.default_achievement_list)      #現在の実績(アチーブメント)リストをデフォルトの物からディープコピーして初期化する
                self.boss_number_of_defeat = copy.deepcopy(self.default_boss_number_of_defeat) #現在プレイ中のボス撃破数リストをデフォルトの物からディープコピーして初期化する
                self.achievement_list      = copy.deepcopy(self.default_achievement_list)      #現在の実績(アチーブメント)リストをデフォルトの物からディープコピーして初期化する
                
                self.score_board = copy.deepcopy(self.default_score_board)      #現在のスコアボードをデフォルトの物からコピーして初期化する
                self.playing_ship_list = copy.deepcopy(self.default_ship_list)  #現在プレイ中のシップデータリストをデフォルトの物からディープコピーして初期化する
                
                self.game_difficulty = GAME_NORMAL
                self.stage_number    = STAGE_MOUNTAIN_REGION
                self.stage_loop      = LOOP01
                self.start_stage_age = 0
                self.debug_menu_status = 0
                self.boss_collision_rect_display_flag = FLAG_OFF
                self.bg_collision_Judgment_flag       = FLAG_ON
                self.boss_test_mode  = FLAG_OFF
                self.no_enemy_mode   = FLAG_OFF
                self.god_mode_status = FLAG_OFF
                self.fullscreen_mode = FLAG_OFF
                
                self.ctrl_type = 1
                self.master_bgm_vol = 50
                self.master_se_vol  = 7
                
                self.number_of_play = 0                   #遊んだ回数初期化
                self.number_of_times_destroyed       = 0  #自機が破壊された回数初期化
                self.total_score    = 0                   #累計得点数初期化
                self.total_game_playtime         = 0      #初めてこのゲームをプレイしてからの合計プレイ時間初期化
                self.total_game_playtime_seconds = 0      #初めてこのゲームをプレイしてからの合計プレイ時間(単位は秒となります)初期化
                self.number_of_times_destroyed   = 0      #自機が破壊された回数初期化
                self.max_score_star_magnification = 1     #スコアスター連続取得倍率初期化
                self.get_shot_pow_num     = 0             #ショットカプセル累計取得数を初期化
                self.get_missile_pow_num  = 0             #ミサイルカプセル累計取得数を初期化
                self.get_shield_pow_num   = 0             #シールドカプセル累計取得数を初期化
                self.get_triangle_pow_num = 0             #トライアングルアイテム累計取得数を初期化
                self.fast_forward_num    = 0              #累計早回し発生数を初期化
                self.get_claw_num        = 0              #クロー累計取得数を初期化
                self.get_score_star_num  = 0              #スコアスター累計取得数を初期化
                
                update_system.save_data(self)                                   #システムデータをセーブします
                pyxel.load(os.path.abspath("./assets/graphic/min-sht2.pyxres"))                    #タイトル＆ステージ1＆2のリソースファイルを読みます
