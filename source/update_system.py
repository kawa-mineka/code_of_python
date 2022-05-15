###########################################################
#  update_systemクラス                                    #
###########################################################
# Appクラスのupdate関数から呼び出される関数群                #
# 主にシステムファイルのセーブやロードを行うメソッド          #
#     #
#                         #
# 2022 05/07からファイル分割してモジュールとして運用開始      #
###########################################################
import shutil #高水準のファイル操作を行いたいのでインポート

from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

class update_system:
    def __init__(self):
        None

    #ユーザープロファイルのcode-of-pythonフォルダにシステムファイルがあるかどうか調べなかったらデフォルトのシステムデータをコピーする
    def check_exist_sysytem_file(self):
        if os.path.isfile(self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres") == False: #システムファイルが存在しないのなら
            if self.exe_mode == FLAG_OFF: #pyファイルで実行時
                source_folder = self.program_directory + "/assets/system/master-system-data.pyxres"
            else:                         #exeファイルで実行時
                source_folder = os.path.dirname(os.path.abspath(__file__)) + "/assets/system/master-system-data.pyxres"
                
            print("ユーザープロファイルにシステムファイルが存在しないので初期システムデータをコピーします")
            print("コピー元")
            print(source_folder)
            print("コピー先")
            print(self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres")
            
            shutil.copyfile(source_folder,self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres")
            print("システムファイルをコピーしました")

    #システムデータからの数値読み込み
    def read_data_num(self,x,y,tm,digit):      #x,yは1の位の座標です,tmはtilemapの数値,digitは桁数です
        global num   #なんやようわからんが・・・global命令で 「numはグローバル変数やで～」って宣言したら上手くいくようになった、なんでや・・・？？謎
        num = 0
        a = 1
        for i in range(digit):
            num += (func.get_chrcode_tilemap(self,tm,x-i,y) - 16) * a
            a = a * 10
        return(num)

    #システムデータへの数値書き込み
    def write_data_num(self,x,y,tm,digit,num): #x,yは1の位の座標です,tmはtilemapの数値,digitは桁数 numは書き込む数値です(整数を推奨)
        a = 10
        for i in range(digit):
            n = num % a * 10 // a
            func.set_chrcode_tilemap(self,tm,x-i,y,n + 16)
            a = a * 10                      #めっちゃ判りにくいなぁ・・・試行錯誤で上手くいった？かも？です！？
                                            #書き込みテストで段々ステップアップしていくと上手くいくね☆彡
        
        #書き込みテストその１ 0からdigit桁数まで数値と桁数が増えてく digit=1なら0 digit=3なら210 digit=7なら6543210 digit=10なら9876543210
        # n = 0 
        # for i in range(digit):
            # pyxel.tilemap(0).set(x-i,y,n + 16)
            # n += 1
        
        #書き込みテストその２
        # for i in range(digit):
            # pyxel.tilemap(0).set(x-i,y,(digit - i) + 16)

    #システムデータのロード
    def load_data(self):
        pyxel.load(self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres") #システムデータを読み込む
        # pyxel.load(os.path.abspath("./assets/system/system-data.pyxres")) #システムデータを読み込む
        # pyxel.load("./assets/system/system-data.pyxres") #システムデータを読み込む
        
        self.game_difficulty = func.get_chrcode_tilemap(self,0,0,120) - 16 #数字の[0]はアスキーコード16番なので16引いて数値としての0にしてやります
        print(self.game_difficulty)
        self.stage_number    = func.get_chrcode_tilemap(self,0,0,121) - 16
        print(self.stage_number)
        self.stage_loop      = func.get_chrcode_tilemap(self,0,0,122) - 16
        print(self.stage_loop)
        self.stage_age       = 0
        #プレイした回数を読み込む
        self.number_of_play = update_system.read_data_num(self,6,6,0,7)
        print(self.number_of_play)
        #累計得点数を読み込む
        self.total_score    = update_system.read_data_num(self,15,8,0,16)
        print(self.total_score)
        
        #総ゲームプレイ時間(秒)を計算する
        sec_1  = func.get_chrcode_tilemap(self,0,9,5) - 16 #秒の  1の位取得
        sec_10 = func.get_chrcode_tilemap(self,0,8,5) - 16 #秒の  10の位取得
        min_1  = func.get_chrcode_tilemap(self,0,6,5) - 16 #分の  1の位取得
        min_10 = func.get_chrcode_tilemap(self,0,5,5) - 16 #分の  10の位取得
        hour_1 = func.get_chrcode_tilemap(self,0,3,5) - 16 #時の   1の位取得
        hour_10 = func.get_chrcode_tilemap(self,0,2,5) - 16 #時の   10の位取得
        hour_100 = func.get_chrcode_tilemap(self,0,1,5) - 16 #時の   100の位取得
        hour_1000 = func.get_chrcode_tilemap(self,0,0,5) - 16 #時の   1000の位取得
        
        s = sec_10 * 10 + sec_1
        m = min_10 * 10 + min_1
        h = hour_1000 * 1000 + hour_100 * 100 + hour_10 * 10 + hour_1
        t_sec = h * 3600 + m * 60 + s
        self.total_game_playtime_seconds = t_sec
        print(self.total_game_playtime_seconds)
        #総開発テスト時間(分)を計算する
        min_1  = func.get_chrcode_tilemap(self,0,7,3) - 16 #分の  1の位取得
        min_10 = func.get_chrcode_tilemap(self,0,6,3) - 16 #分の  10の位取得
        hour_1 = func.get_chrcode_tilemap(self,0,4,3) - 16 #時の   1の位取得
        hour_10 = func.get_chrcode_tilemap(self,0,3,3) - 16 #時の   10の位取得
        hour_100 = func.get_chrcode_tilemap(self,0,2,3) - 16 #時の   100の位取得
        hour_1000 = func.get_chrcode_tilemap(self,0,1,3) - 16 #時の   1000の位取得
        hour_10000 = func.get_chrcode_tilemap(self,0,0,3) - 16 #時の   10000の位取得
        m = min_10 * 10 + min_1
        h = hour_10000 * 10000 + hour_1000 * 1000 + hour_100 * 100 + hour_10 * 10 + hour_1
        t_min = h * 60 + m
        self.total_development_testtime_min = t_min
        print(self.total_development_testtime_min)
        
        #デバッグモード＆ゴッドモード用のフラグやパラメーターの初期化とか宣言はこちらで行うようにします
        #debug_menu_status                  #デバッグパラメータの表示ステータス
                                            #0=表示しない 1=フル表示タイプ 2=簡易表示タイプ
        self.debug_menu_status             = func.get_chrcode_tilemap(self,0,0,126) - 16 #数字の[0]はアスキーコード16番なので16引いて数値としての0にしてやります
        
        #boss_collision_rect_display_flag        ボス用の当たり判定確認の為の矩形表示フラグ(デバッグ時に1にします)
        self.boss_collision_rect_display_flag = func.get_chrcode_tilemap(self,0,0,127) - 16
        #bg_collision_Judgment_flag            背景の障害物との衝突判定を行うかどうかのフラグ
                                            #0=背景の障害物との当たり判定をしない 1=行う
        self.bg_collision_Judgment_flag      = func.get_chrcode_tilemap(self,0,0,128) - 16
        #boss_test_mode                      ボス戦闘のみのテストモード 
                                            #0=オフ 1=オン scroll_countを増やさない→マップスクロールしないので敵が発生しません
                                            #イベントリストもボス専用の物が読み込まれます
        self.boss_test_mode                = func.get_chrcode_tilemap(self,0,0,129) - 16
        #no_enemy_mode                       マップチップによる敵の発生を行わないモードのフラグですです(地上の敵が出ない！)2021 03/07現在機能してない模様
                                            #0=マップスクロールによって敵が発生します
                                            #1=                    発生しません        
        self.no_enemy_mode                 = func.get_chrcode_tilemap(self,0,0,130) - 16
        #god_mode_status                    #ゴッドモードのステータス
                                            #0=ゴッドモードオフ 1=ゴッドモードオン
        self.god_mode_status               = func.get_chrcode_tilemap(self,0,0,131) - 16
        #fullscreen_mode                    #フルスクリーンでの起動モード
                                            #0=ウィンドウモードでの起動 1=フルスクリーンモードでの起動
        self.fullscreen_mode               = func.get_chrcode_tilemap(self,0,0,132) - 16
        #ctrl_type                          #コントロールパッドのタイプ
                                            #0~5
        self.ctrl_type                     = func.get_chrcode_tilemap(self,0,0,133) - 16
        #master_bgm_vol                     #BGMのマスターボリューム
                                            #0~100
        self.master_bgm_vol                = update_system.read_data_num(self,2,134,0,3)
        #master_se_vol                      #SEのマスターボリューム
                                            #0~7
        self.master_se_vol                 = update_system.read_data_num(self,2,135,0,3)
        #language                           #選択言語
                                            #0=英語 1=日本語
        self.language                      = func.get_chrcode_tilemap(self,0,0,136) - 16
        
        #メダル所有フラグの読み込み
        for i in range(10):
            self.medal_list[i] = func.get_chrcode_tilemap(self,0,0,210 + i) - 16
        
        #各機体のスロット装備済みメダルデータの読み込み
        for i in range(LOOK_AT_LOGO): #iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):        #jはスロット0からスロット6まで変化
                self.ship_equip_slot_list[i][j] = func.get_chrcode_tilemap(self,0,23 + j,11 + i) - 16
        
        #スコアボードデータの読み込み
        for i in range(GAME_INSAME+1): #iは0からGAME_INSAME+1(6)まで変化する(難易度)
            tm = 4
            for j in range(11):      #jは0から11まで変化する(順位)
                self.score_board[i][j][LIST_SCORE_BOARD_DIFFICULTY]  = i                                        #難易度ID読み込み 
                self.score_board[i][j][LIST_SCORE_BOARD_RANKING]     = update_system.read_data_num(self,1,5 + j + (i * 16),tm, 2) #順位読み込み
                
                namestr = ""
                for k in range(8):   #kは0から8まで変化する(8文字だよ)
                    st = chr(func.get_chrcode_tilemap(self,tm,3 + k,5 + j + (i * 16))+32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)
                    namestr = namestr + st
                
                # namestr = chr(pyxel.tilemap(tm).pget(3,5 + j + (i * 16))+32) 
                self.score_board[i][j][LIST_SCORE_BOARD_NAME]    = str(namestr) #アスキーコード8文字分の名前を読み込み
                
                self.score_board[i][j][LIST_SCORE_BOARD_SCORE]       = update_system.read_data_num(self,23,5 + j + (i * 16),tm, 12) #得点読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_LOOP]        = update_system.read_data_num(self,28,5 + j + (i * 16),tm, 2) #周回数読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_CLEAR_STAGE] = update_system.read_data_num(self,34,5 + j + (i * 16),tm, 2) #クリアしたステージ数読み込み
                self.score_board[i][j][LIST_SCORE_BOARD_SHIP_USED]   = update_system.read_data_num(self,39,5 + j + (i * 16),tm, 2) #使用した機体読み込み
                
                for l in range(6): #機体に装着されたメダル装備IDの読み込み
                    self.score_board[i][j][LIST_SCORE_BOARD_SHIP_SLOT0 + l] = func.get_chrcode_tilemap(self,tm,41 + l,5 + j + (i * 16)) - 16
        
        #名前の読み込み
        namestr = ""
        for i in range(8):   #kは0から8まで変化する(8文字だよ)
            st = chr(func.get_chrcode_tilemap(self,0,0 + i,1) + 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)
            namestr = namestr + st
        self.my_name = str(namestr)
        
        #各ステージボス撃破数の読み込み
        for i in range(14):
            self.boss_number_of_defeat[i] = update_system.read_data_num(self,27,210 + i,0,4)
        
        #実績(アチーブメント)の読み込み
        for i in range(len(self.achievement_list)):
            self.achievement_list[i][LIST_ACHIEVE_FLAG] = func.get_chrcode_tilemap(self,0,0,41 + i) - 16
        
        #スコアスター最大得点倍率の読み込み
        self.max_score_star_magnification = update_system.read_data_num(self,2,137,0,3)
        
        #パワーカプセル類の累計取得数の読み込み
        self.get_shot_pow_num     = update_system.read_data_num(self,7,138,0,8) #ショットカプセル累計取得数の読み込み
        self.get_missile_pow_num  = update_system.read_data_num(self,7,139,0,8) #ミサイルカプセル累計取得数の読み込み
        self.get_shield_pow_num   = update_system.read_data_num(self,7,140,0,8) #シールドカプセル累計取得数の読み込み
        self.get_claw_num         = update_system.read_data_num(self,7,141,0,8) #クロー累計取得数の読み込み
        self.get_score_star_num   = update_system.read_data_num(self,7,142,0,8) #スコアスター累計取得数の読み込み
        self.get_triangle_pow_num = update_system.read_data_num(self,7,144,0,8) #トライアングルアイテム累計取得数の読み込み
        self.fast_forward_num     = update_system.read_data_num(self,7,145,0,8) #累計早回し発生数の読み込み
        
        # self.test_read_num = update_system.read_data_num(self,15,156,0,16) #数値の読み取りテストです

    #システムデータのセーブ
    def save_data(self):
        pyxel.load(self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres") #システムデータにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        # pyxel.load(os.path.abspath("./assets/system/system-data.pyxres")) #システムデータにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        # pyxel.load("./assets/system/system-data.pyxres") #システムデータにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        #各種設定値書き込み 数字の[0]はアスキーコード16番なので16足してアスキーコードとしての0にしてやります
        func.set_chrcode_tilemap(self,0, 0,120,self.game_difficulty + 16)                 #難易度書き込み
        func.set_chrcode_tilemap(self,0, 0,121,self.stage_number + 16)                    #スタートステージ数書き込み
        func.set_chrcode_tilemap(self,0, 0,122,self.stage_loop + 16)                      #スタート周回数書き込み
        func.set_chrcode_tilemap(self,0, 0,126,self.debug_menu_status + 16)               #デバッグメニュー表示フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,127,self.boss_collision_rect_display_flag + 16)#ボス当たり判定矩形表示フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,128,self.bg_collision_Judgment_flag + 16)      #BGとの当たり判定フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,129,self.boss_test_mode + 16)                  #ボステストモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,130,self.no_enemy_mode + 16)                   #敵が出ないモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,131,self.god_mode_status + 16)                 #ゴッドモードフラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,132,self.fullscreen_mode + 16)                 #フルスクリーン起動フラグ書き込み
        func.set_chrcode_tilemap(self,0, 0,133,self.ctrl_type + 16)                       #パッドコントロールタイプ書き込み
        update_system.write_data_num(self,2,134,0,3,self.master_bgm_vol)             #マスターBGMボリューム値書き込み
        update_system.write_data_num(self,2,135,0,3,self.master_se_vol)              #マスターSEボリューム値書き込み
        func.set_chrcode_tilemap(self,0 ,0,136,self.language + 16)                        #選択言語書き込み
        
        #プレイした回数を書き込む
        update_system.write_data_num(self,6,6,0,7,self.number_of_play)
        #累計得点数を書き込む
        update_system.write_data_num(self,15,8,0,16,self.total_score)
        #メダル所有フラグの書き込み
        for i in range(10):
            func.set_chrcode_tilemap(self,0, 0,210 + i,self.medal_list[i] + 16)
        
        #各機体のスロット装備済みメダルデータの書き込み
        for i in range(LOOK_AT_LOGO): #iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):        #jはスロット0からスロット6まで変化
                func.set_chrcode_tilemap(self,0, 23 + j,11 + i,self.ship_equip_slot_list[i][j] + 16)
        
        #スコアボードデータの書き込み
        for i in range(GAME_INSAME+1): #iは0からGAME_INSAME+1(6)まで変化する(難易度)
            tm = 4
            for j in range(11):      #jは0から11まで変化する(順位)
                update_system.write_data_num(self,1,5 + j + (i * 16),tm, 2,self.score_board[i][j][LIST_SCORE_BOARD_RANKING]) #順位書き込み
                
                namestr = self.score_board[i][j][LIST_SCORE_BOARD_NAME]                 #スコアボードからアスキーコード8文字分の名前を取り出す
                for k in range(8):   #kは0から8まで変化する(8文字だよ)
                    func.set_chrcode_tilemap(self,tm, 3 + k,5 + j + (i * 16),ord(namestr[k]) - 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)数字は16の差が出る
                
                update_system.write_data_num(self,23,5 + j + (i * 16),tm, 12,self.score_board[i][j][LIST_SCORE_BOARD_SCORE])       #得点書き込み
                update_system.write_data_num(self,28,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_LOOP])        #周回数書き込み
                update_system.write_data_num(self,34,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_CLEAR_STAGE]) #クリアしたステージ数書き込み
                update_system.write_data_num(self,39,5 + j + (i * 16),tm,  2,self.score_board[i][j][LIST_SCORE_BOARD_SHIP_USED])   #使用した機体書き込み
                
                for l in range(6): #機体に装着されたメダル装備IDの書き込み
                    func.set_chrcode_tilemap(self,tm, 41 + l,5 + j + (i * 16),self.score_board[i][j][LIST_SCORE_BOARD_SHIP_SLOT0 + l] + 16)
        
        #名前の書き込み
        for i in range(8):   #kは0から8まで変化する(8文字だよ)
            func.set_chrcode_tilemap(self,0, 0 + i,1,ord(self.my_name[i]) - 32)  #sysytemデータで使用しているフォントはアスキーコードと実際の文字列に32の差が出るので注意(フォントマップの横幅が32キャラだから)数字は16の差が出る
        
        #各ステージボス撃破数の書き込み
        for i in range(14):
            update_system.write_data_num(self,27,210 + i,0,4,self.boss_number_of_defeat[i])
        
        #実績(アチーブメント)の書き込み
        for i in range(len(self.achievement_list)):
            func.set_chrcode_tilemap(self,0, 0,41 + i,self.achievement_list[i][LIST_ACHIEVE_FLAG] + 16)
        
        #スコアスター最大得点倍率の書き込み
        update_system.write_data_num(self,2,137,0,3,self.max_score_star_magnification)
        
        #パワーカプセル類の累計取得数の書き込み
        update_system.write_data_num(self,7,138,0,8,self.get_shot_pow_num   )  #ショットカプセル累計取得数の書き込み
        update_system.write_data_num(self,7,139,0,8,self.get_missile_pow_num)  #ミサイルカプセル累計取得数の書き込み
        update_system.write_data_num(self,7,140,0,8,self.get_shield_pow_num )  #シールドカプセル累計取得数の書き込み
        update_system.write_data_num(self,7,141,0,8,self.get_claw_num       )  #クロー累計取得数の書き込み
        update_system.write_data_num(self,7,142,0,8,self.get_score_star_num )  #スコアスター累計取得数の書き込み
        update_system.write_data_num(self,7,144,0,8,self.get_triangle_pow_num) #トライアングルアイテム累計取得数の書き込み
        update_system.write_data_num(self,7,145,0,8,self.fast_forward_num)     #累計早回し発生数の書き込み
        
        #総ゲームプレイ時間(秒)のそれぞれの桁の数値を計算する (自分でも訳が分からないよ・・・)------------------------------
        t_sec = self.total_game_playtime_seconds
        se = t_sec % 60        #se 秒は 総秒数を60で割った余り
        mi = t_sec // 60 % 60  #mi 分は 総秒数を60で割った数(切り捨て)を更に60で割った余り
        ho = t_sec // 3600     #ho 時は 総秒数を3600で割った数(切り捨て)
        #それぞれの桁の数値(0~9)を計算して求めていく
        sec_1  = se  % 10
        sec_10 = se // 10
        min_1  = mi  % 10
        min_10 = mi // 10
        hour_1 = ho % 10
        hour_10 = ho % 100 // 10
        hour_100 = ho % 1000 // 100
        hour_1000 = ho % 10000 // 1000
        #総ゲームプレイ時間(秒)を書き込んでいく
        func.set_chrcode_tilemap(self,0, 9,5,sec_1 + 16) #秒の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 8,5,sec_10 + 16) #秒の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 6,5,min_1 + 16) #分の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 5,5,min_10 + 16) #分の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 3,5,hour_1  + 16) #時の   1の位を書き込む
        func.set_chrcode_tilemap(self,0, 2,5,hour_10 + 16) #時の   10の位を書き込む
        func.set_chrcode_tilemap(self,0, 1,5,hour_100 + 16) #時の   100の位を書き込む
        func.set_chrcode_tilemap(self,0, 0,5,hour_1000 + 16) #時の   1000の位を書き込む
        
        #総開発テストプレイ時間(分)を計算します------------------------------------------------------
        self.total_development_testtime_min += self.one_game_playtime_seconds // 60 #今プレイしているゲームの時間(分)を総ゲームテスト時間に加算
        t_dev_min = self.total_development_testtime_min
        mi = t_dev_min % 60    #mi 分は 総分数を60で割った余り
        ho = t_dev_min // 60      #ho 時は 総秒数を60で割った数(切り捨て)
        #それぞれの桁の数値(0~9)を計算して求めていく
        min_1  = mi  % 10
        min_10 = mi // 10
        hour_1 = ho % 10
        hour_10 = ho % 100 // 10
        hour_100 = ho % 1000 // 100
        hour_1000 = ho % 10000 // 1000
        hour_10000 = ho % 100000 // 10000
        #総開発テストプレイ時間を書き込んでいく
        func.set_chrcode_tilemap(self,0, 7,3,min_1 + 16) #分の  1の位を書き込む
        func.set_chrcode_tilemap(self,0, 6,3,min_10 + 16) #分の  10の位を書き込む
        func.set_chrcode_tilemap(self,0, 4,3,hour_1  + 16) #時の   1の位を書き込む
        func.set_chrcode_tilemap(self,0, 3,3,hour_10 + 16) #時の   10の位を書き込む
        func.set_chrcode_tilemap(self,0, 2,3,hour_100 + 16) #時の   100の位を書き込む
        func.set_chrcode_tilemap(self,0, 1,3,hour_1000 + 16) #時の   1000の位を書き込む
        func.set_chrcode_tilemap(self,0, 0,3,hour_10000 + 16) #時の   10000の位を書き込む
        
        update_system.write_data_num(self,16,152,0,16,8777992360588341) #!############################ test write
        
        test_num = -0.123
        test_num = test_num * 1000
        test_num = test_num + 1000                             #この式と逆の方法で計算してやれば符号の付いた実数値を取り出せる
        update_system.write_data_num(self,10,162,0,10,int(test_num))    #!############################ test write マイナス符号付き実数値の数値が書き込めるかのテスト
        
        pyxel.save(self.user_profile + "/AppData/Local/code_of_python/system/system-data.pyxres") #システムデータを書き込み
        # pyxel.save(os.path.abspath("./assets/system/system-data.pyxres")) #システムデータを書き込み
        # pyxel.save("./assets/system/system-data.pyxres") #システムデータを書き込み

