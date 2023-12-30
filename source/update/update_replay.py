###########################################################
#  update_replayクラス                                    #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にリプレイ記録に関する更新を行う関数(メソッド？）ですよ～♪#
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
#import math         #三角関数などを使用したいのでインポートぉぉおお！
#from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func  import * #汎用性のある関数群のモジュールの読み込み
from update.update_system import * #リプレイファイルの読み書きで使用します

class update_replay:
    #リプレイデータ・ファイルロード
    def data_file_load(self):
        self.replay_data          = [[] for i in range(50)] #リプレイデータが入るリスト(50ステージ分)を初期化
        self.replay_control_data_size = []                  #ステージ毎のコントロールデータのサイズが入るリストを初期化
        slot_num = "slot_" + str(self.replay_slot_num)      #これからアクセスするスロットナンバーを取得
        pyxel.load(os.path.abspath("./assets/replay/" + slot_num + "/replay_status.pyxres")) #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        # pyxel.load("./assets/replay/" + slot_num + "/replay_status.pyxres") #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        
        #各種設定値読み込み 数字の[0]はアスキーコード16番なので16引いて文字から数字としての0にしてやります
        self.master_rnd_seed  = func.get_chrcode_tilemap(self,0,  0,0)       #乱数の種(ゲームスタート時)を読み込み(そのまま取得します)
        self.game_difficulty  = func.get_chrcode_tilemap(self,0,  0,1) - 16  #難易度読み込み
        self.stage_number     = func.get_chrcode_tilemap(self,0,  0,2) - 16  #ステージ数読み込み
        self.stage_loop       = func.get_chrcode_tilemap(self,0,  0,3) - 16  #ループ数読み込み
        self.replay_stage_num = func.get_chrcode_tilemap(self,0,  0,4) - 16  #リプレイファイルとして記録する総ステージ数を読み込み
        self.boss_test_mode   = func.get_chrcode_tilemap(self,0,  0,5) - 16  ##ボステストモードのフラグを読み込み
        
        #ステージ毎ごとの自機関連パラメーターのロード---------------------------------------------------------------------------
        for i in range(self.replay_stage_num + 1):
            self.replay_mode_stage_data[i][ST_SCORE]           = update_system.read_data_num(self,5   -1+10,10+i,0, 10)        #座標(5,10+i)から10ケタのスコア(整数)を読み込みます
            self.replay_mode_stage_data[i][ST_MY_SHIELD]       = update_system.read_data_num(self,16  -1 +5,10+i,0,  5)        #座標(16,10+i)から5ケタのシールド値を読み込みます
            self.replay_mode_stage_data[i][ST_MY_SPEED]        = update_system.read_data_num(self,22  -1 +3,10+i,0,  3) // 100 #座標(22,10+i)から3ケタの自機スピード(0.75とか1.25とか小数点第2位まで行くので100でわった値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_SELECT_SHOT_ID]  = update_system.read_data_num(self,27  -1 +2,10+i,0,  2)    #座標(27,10+i)から2ケタのショットIDを読み込みます
            
            self.replay_mode_stage_data[i][ST_SHOT_EXP]                 = update_system.read_data_num(self,31  -1 +4,10+i,0,  4)         #座標(31,10+i)から4ケタのショットの経験値を読み込みます
            self.replay_mode_stage_data[i][ST_SHOT_LEVEL]               = update_system.read_data_num(self,36  -1 +2,10+i,0,  2)         #座標(36,10+i)から2ケタのショットのレベルを読み込みます
            self.replay_mode_stage_data[i][ST_SHOT_SPEED_MAGNIFICATION] = update_system.read_data_num(self,39  -1 +5,10+i,0,  5) // 1000 #座標(39,10+i)から5ケタのショットのスピードに掛ける倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_SHOT_RAPID_OF_FIRE]       = update_system.read_data_num(self,45  -1 +2,10+i,0,  2)         #座標(45,10+i)から2ケタのショットの連射数を読み込みます
            
            self.replay_mode_stage_data[i][ST_MISSILE_EXP]                 = update_system.read_data_num(self,49  -1 +4,10+i,0,  4)         #座標(49,10+i)から4ケタのミサイルの経験値を読み込みます
            self.replay_mode_stage_data[i][ST_MISSILE_LEVEL]               = update_system.read_data_num(self,54  -1 +2,10+i,0,  2)         #座標(54,10+i)から2ケタのミサイルのレベルを読み込みます
            self.replay_mode_stage_data[i][ST_MISSILE_SPEED_MAGNIFICATION] = update_system.read_data_num(self,57  -1 +5,10+i,0,  5) // 1000 #座標(57,10+i)から5ケタのミサイルのスピードに掛ける倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_MISSILE_RAPID_OF_FIRE]       = update_system.read_data_num(self,63  -1 +2,10+i,0,  2)         #座標(63,10+i)から2ケタのミサイルの連射数を読み込みます
            
            self.replay_mode_stage_data[i][ST_SELECT_SUB_WEAPON_ID] = update_system.read_data_num(self,68  -1 +2,10+i,0,  2)   #座標(68,10+i)から2ケタの現在使用しているサブウェポンのIDナンバーを読み込みます
            
            self.replay_mode_stage_data[i][ST_CLAW_NUMBER]          = update_system.read_data_num(self,74  -1 +2,10+i,0,  2)   #座標(74,10+i)から2ケタのクローの装備数を読み込みます
            self.replay_mode_stage_data[i][ST_CLAW_TYPE]            = update_system.read_data_num(self,71  -1 +2,10+i,0,  2)   #座標(71,10+i)から2ケタのクローのタイプを読み込みます
            self.replay_mode_stage_data[i][ST_CLAW_DIFFERENCE]      = update_system.read_data_num(self,77  -1 +4,10+i,0,  4)   #座標(77,10+i)から4ケタのクロ―同士の角度間隔を読み込みます
            
            self.replay_mode_stage_data[i][ST_TRACE_CLAW_INDEX]        = update_system.read_data_num(self,82  -1 +2,10+i,0,  2)          #座標(82,10+i)から2ケタのトレースクロー（オプション）時のトレース用配列のインデックス値を読み込みます
            self.replay_mode_stage_data[i][ST_TRACE_CLAW_DISTANCE]     = update_system.read_data_num(self,85  -1 +5,10+i,0,  5) // 1000  #座標(85,10+i)から5ケタのトレースクロー同士の間隔を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_FIX_CLAW_MAGNIFICATION]  =  update_system.read_data_num(self,91  -1 +5,10+i,0,  5) // 1000 #座標(91,10+i)から5ケタのフイックスクロー同士の間隔の倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVX]        = update_system.read_data_num(self,97  -1 +5,10+i,0,  5) // 1000  #座標(97,10+i)から5ケタのリバースクロー用の攻撃方向ベクトル(x軸)を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVY]        = update_system.read_data_num(self,103 -1 +5,10+i,0,  5) // 1000  #座標(103,10+i)から5ケタのリバースクロー用の攻撃方向ベクトル(y軸)を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_CLAW_SHOT_SPEED]         = update_system.read_data_num(self,109 -1 +5,10+i,0,  5) // 1000  #座標(109,10+i)から5ケタのクローショットのスピードを読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_LS_SHIELD_HP]            = update_system.read_data_num(self,115 -1 +4,10+i,0,  4)          #座標(115,10+i)から4ケタのL'sシールドの耐久力を読み込みます
            
            self.replay_mode_stage_data[i][ST_SHIP_ID]                 = update_system.read_data_num(self,144 -1 +3,10+i,0,  3)          #座標(144,10+i)から3ケタの使用している機体のIDナンバーを読み込みます
            self.replay_mode_stage_data[i][ST_SHIP_LEVEL]              = update_system.read_data_num(self,148 -1 +3,10+i,0,  3)          #座標(148,10+i)から3ケタの使用している機体のレベルを読み込みます
            self.replay_mode_stage_data[i][ST_SHIP_EXP]                = update_system.read_data_num(self,152 -1 +4,10+i,0,  4)          #座標(152,10+i)から4ケタの使用している機体の経験値を読み込みます
            
            self.replay_mode_stage_data[i][ST_SLOT1]                   = update_system.read_data_num(self,160 -1 +2,10+i,0,  2) #座標(160,10+i)から2ケタの使用している機体のメダルスロット1のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT2]                   = update_system.read_data_num(self,162 -1 +2,10+i,0,  2) #座標(162,10+i)から2ケタの使用している機体のメダルスロット2のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT3]                   = update_system.read_data_num(self,164 -1 +2,10+i,0,  2) #座標(164,10+i)から2ケタの使用している機体のメダルスロット3のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT4]                   = update_system.read_data_num(self,166 -1 +2,10+i,0,  2) #座標(166,10+i)から2ケタの使用している機体のメダルスロット4のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT5]                   = update_system.read_data_num(self,168 -1 +2,10+i,0,  2) #座標(168,10+i)から2ケタの使用している機体のメダルスロット5のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT6]                   = update_system.read_data_num(self,170 -1 +2,10+i,0,  2) #座標(170,10+i)から2ケタの使用している機体のメダルスロット6のメダルIDを読み込みます
            self.replay_mode_stage_data[i][ST_SLOT7]                   = update_system.read_data_num(self,172 -1 +2,10+i,0,  2) #座標(172,10+i)から2ケタの使用している機体のメダルスロット7のメダルIDを読み込みます
            
            self.replay_mode_stage_data[i][ST_SCORE_STAR_MAG]          = update_system.read_data_num(self,176 -1 +3,10+i,0,  3) #座標(176,10+i)から3ケタのスコアスター得点倍率を読み込みます
            
            pad_data_size = update_system.read_data_num(self,128 -1 +8,10+i,0,  8) #座標(128,10+i)からの8ケタのコントロールパッド入力データが記録されたファイルのデータサイズを読み込みます
            self.replay_control_data_size.append(pad_data_size)           #コントロールデータのファイルサイズリストにサイズを追加していきます
        
        #各ステージのパッド入力データのロード---------------------------------------------------------------------------------------
        for st in range(self.replay_stage_num + 1): #st(ステージ指定用に作った変数は0始まりなので注意)
            file_number = "{:>03}".format(st + 1)
            file_name = "./assets/replay/" + slot_num + "/" + file_number + ".pyxres"
            pyxel.load(os.path.abspath(file_name)) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            # pyxel.load(file_name) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            replay_control_data_count = self.replay_control_data_size[st] #stステージ目のreplay_dataのリスト長(要素数)を代入
            
            for i in range (replay_control_data_count):
                x = int(i % 256)                      #x座標は現在のカウント値iを256で割った余り
                y = int(i // 256) % 256               #y座標は現在のカウント値iを256で割った数(切り捨て)を更に256で割った余り
                z = int(i // 65536)                   #z座標(この場合はタイルマップナンバーになります)は65536で割った数(切り捨て)
                num = func.get_chrcode_tilemap(self,z, x,y)       #numにタイルマップ(z),座標(x,y)から読み取ったコントロールパッド入力データを代入
                self.replay_data[st].append(int(num))    #リストにパッド入力データ記録！getで読み取ったのは文字(str)なので数値(int)に変換してリストにアペンドします

    #リプレイデータ・ファイルセーブ
    def data_file_save(self):
        self.replay_control_data_size = [] #まず最初にステージ毎のコントロールデータのサイズが入るリストを初期化
        slot_num = "slot_" + str(self.replay_slot_num) #これからアクセスするスロットナンバーを取得
        
        #各ステージのパッド入力データのセーブ---------------------------------------------------------------------------------------
        for st in range(self.replay_stage_num + 1): #st(ステージ指定用に作った変数は0始まりなので注意)
            file_number = "{:>03}".format(st + 1)
            file_name = "./assets/replay/" + slot_num + "/" + file_number + ".pyxres"
            pyxel.load(os.path.abspath(file_name)) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            # pyxel.load(file_name) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            replay_control_data_count = len(self.replay_data[st])        #stステージ目のreplay_dataのリスト長(要素数)を代入
            self.replay_control_data_size.append(replay_control_data_count) #ステージ毎のコントロールデータのサイズをリストに追加していきます
            for z in range(8): #データクリア処理-------------------------------------
                for y in range(256):
                    for x in range(256):
                        # pyxel.tilemap(z).set(x,y,128-16+6-16)
                        func.set_chrcode_tilemap(self,z,x,y,0)
            
            #カウント65536でタイルマップを1枚埋め尽くす事になります
            #カウント65537だとタイルマップ1枚と次のタイルマップ1マス分必要となります
            #タイルマップ1ページ分はカウントが0~65536間の場合書き込み開始 65537だとエラーになります(なんか書き込む(SET)時は座標が256越えてもエラーが出ないみたい)
            #う～ん上手く行ってるのか謎・・・・
            for i in range (replay_control_data_count):
                num = int(self.replay_data[st][i])    #リストからパッド入力データ取得
                x = int(i % 256)                   #x座標は現在のカウント値iを256で割った余り
                y = int(i // 256) % 256            #y座標は現在のカウント値iを256で割った数(切り捨て)を更に256で割った余り
                z = int(i // 65536)                #z座標(この場合はタイルマップナンバーになります)は65536で割った数(切り捨て)
                func.set_chrcode_tilemap(self,z,x,y,num) #numをタイルマップ(z),座標(x,y)に書き込む
            
            pyxel.save(os.path.abspath(file_name)) #リプレイパッド入力データファイルをセーブ！
            # pyxel.save(file_name) #リプレイパッド入力データファイルをセーブ！
        
        #リプレイファイル本体のデータをセーブする---------------------------------------------------------------------------------------
        pyxel.load(os.path.abspath("./assets/replay/" + slot_num + "/replay_status.pyxres")) #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        # pyxel.load("./assets/replay/" + slot_num + "/replay_status.pyxres") #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        #各種設定値書き込み 数字の[0]はアスキーコード16番なので16足してアスキーコードとしての0にしてやります
        func.set_chrcode_tilemap(self,0, 0,0,self.master_rnd_seed)          #乱数の種(ゲームスタート時)を書き込み(数文字には変換しない)
        func.set_chrcode_tilemap(self,0, 0,1,self.game_difficulty + 16)     #難易度書き込み
        func.set_chrcode_tilemap(self,0, 0,2,self.start_stage_number + 16)  #ゲーム開始時のステージ数書き込み
        func.set_chrcode_tilemap(self,0, 0,3,self.start_stage_loop + 16)    #ゲーム開始時のループ数書き込み
        func.set_chrcode_tilemap(self,0, 0,4,self.replay_stage_num + 16)    #リプレイファイルとして記録する総ステージ数を書き込み
        func.set_chrcode_tilemap(self,0, 0,5,self.boss_test_mode   + 16)    #ボステストモードのフラグを書き込み
        
        #ステージ毎ごとの自機関連パラメーターのセーブ--------------------------------------------------------------------------------
        for i in range(self.replay_stage_num + 1):
            update_system.write_data_num(self,5   -1+10,10+i,0, 10,int(self.replay_mode_stage_data[i][ST_SCORE]))           #座標(5,10+i)に10ケタのスコア(整数)を書き込みます
            update_system.write_data_num(self,16  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_MY_SHIELD]))       #座標(16,10+i)に5ケタのシールド値を書き込みます
            update_system.write_data_num(self,22  -1 +3,10+i,0,  3,int(self.replay_mode_stage_data[i][ST_MY_SPEED]*100))    #座標(22,10+i)に3ケタの自機スピード(0.75とか1.25とか小数点第2位まで行くので100倍した値を書き込みます)
            
            update_system.write_data_num(self,27  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SELECT_SHOT_ID]))  #座標(27,10+i)に2ケタのショットIDを書き込みます
            
            update_system.write_data_num(self,31  -1 +4,10+i,0,  4,int(self.replay_mode_stage_data[i][ST_SHOT_EXP]))              #座標(31,10+i)に4ケタのショットの経験値を書き込みます
            update_system.write_data_num(self,36  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SHOT_LEVEL]))            #座標(36,10+i)に2ケタのショットのレベルを書き込みます
            update_system.write_data_num(self,39  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_SHOT_SPEED_MAGNIFICATION] * 1000)) #座標(39,10+i)に5ケタのショットのスピードに掛ける倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            update_system.write_data_num(self,45  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SHOT_RAPID_OF_FIRE]))    #座標(45,10+i)に2ケタのショットの連射数を書き込みます
            
            update_system.write_data_num(self,49  -1 +4,10+i,0,  4,int(self.replay_mode_stage_data[i][ST_MISSILE_EXP]))                  #座標(49,10+i)に4ケタのミサイルの経験値を書き込みます
            update_system.write_data_num(self,54  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_MISSILE_LEVEL]))                #座標(54,10+i)に2ケタのミサイルのレベルを書き込みます
            update_system.write_data_num(self,57  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_MISSILE_SPEED_MAGNIFICATION]* 1000))  #座標(57,10+i)に5ケタのミサイルのスピードに掛ける倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            update_system.write_data_num(self,63  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_MISSILE_RAPID_OF_FIRE]))        #座標(63,10+i)に2ケタのミサイルの連射数を書き込みます
            
            update_system.write_data_num(self,68  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SELECT_SUB_WEAPON_ID]))   #座標(68,10+i)に2ケタの現在使用しているサブウェポンのIDナンバーを書き込みます
            
            update_system.write_data_num(self,74  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_CLAW_NUMBER]))            #座標(74,10+i)に2ケタのクローの装備数を書き込みます
            update_system.write_data_num(self,71  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_CLAW_TYPE]))              #座標(71,10+i)に2ケタのクローのタイプを書き込みます
            update_system.write_data_num(self,77  -1 +4,10+i,0,  4,int(self.replay_mode_stage_data[i][ST_CLAW_DIFFERENCE]))        #座標(77,10+i)に4ケタのクロ―同士の角度間隔を書き込みます
            
            update_system.write_data_num(self,82  -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_TRACE_CLAW_INDEX]))       #座標(82,10+i)に2ケタのトレースクロー（オプション）時のトレース用配列のインデックス値を書き込みます
            update_system.write_data_num(self,85  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_TRACE_CLAW_DISTANCE] * 1000))    #座標(85,10+i)に5ケタのトレースクロー同士の間隔を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            update_system.write_data_num(self,91  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_FIX_CLAW_MAGNIFICATION] * 1000)) #座標(91,10+i)に5ケタのフイックスクロー同士の間隔の倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            update_system.write_data_num(self,97  -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVX] * 1000))       #座標(97,10+i)に5ケタのリバースクロー用の攻撃方向ベクトル(x軸)を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            update_system.write_data_num(self,103 -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVY] * 1000))       #座標(103,10+i)に5ケタのリバースクロー用の攻撃方向ベクトル(y軸)を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            update_system.write_data_num(self,109 -1 +5,10+i,0,  5,int(self.replay_mode_stage_data[i][ST_CLAW_SHOT_SPEED] * 1000))        #座標(109,10+i)に5ケタのクローショットのスピードを書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            update_system.write_data_num(self,115 -1 +4,10+i,0,  4,int(self.replay_mode_stage_data[i][ST_LS_SHIELD_HP]))           #座標(115,10+i)に4ケタのL'sシールドの耐久力を書き込みます
            
            update_system.write_data_num(self,144 -1 +3,10+i,0,  3,int(self.replay_mode_stage_data[i][ST_SHIP_ID]   ))          #座標(144,10+i)から3ケタの使用している機体のIDナンバーを書き込みます
            update_system.write_data_num(self,148 -1 +3,10+i,0,  3,int(self.replay_mode_stage_data[i][ST_SHIP_LEVEL]))          #座標(148,10+i)から3ケタの使用している機体のレベルを書き込みます
            update_system.write_data_num(self,152 -1 +4,10+i,0,  4,int(self.replay_mode_stage_data[i][ST_SHIP_EXP]  ))          #座標(152,10+i)から4ケタの使用している機体の経験値を書き込みます
            
            update_system.write_data_num(self,160 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT1])) #座標(160,10+i)から2ケタの使用している機体のメダルスロット1のメダルIDを書き込みます
            update_system.write_data_num(self,162 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT2])) #座標(162,10+i)から2ケタの使用している機体のメダルスロット2のメダルIDを書き込みます
            update_system.write_data_num(self,164 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT3])) #座標(164,10+i)から2ケタの使用している機体のメダルスロット3のメダルIDを書き込みます
            update_system.write_data_num(self,166 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT4])) #座標(166,10+i)から2ケタの使用している機体のメダルスロット4のメダルIDを書き込みます
            update_system.write_data_num(self,168 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT5])) #座標(168,10+i)から2ケタの使用している機体のメダルスロット5のメダルIDを書き込みます
            update_system.write_data_num(self,170 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT6])) #座標(170,10+i)から2ケタの使用している機体のメダルスロット6のメダルIDを書き込みます
            update_system.write_data_num(self,172 -1 +2,10+i,0,  2,int(self.replay_mode_stage_data[i][ST_SLOT7])) #座標(172,10+i)から2ケタの使用している機体のメダルスロット7のメダルIDを書き込みます
            
            update_system.write_data_num(self,176 -1 +3,10+i,0,  3,int(self.replay_mode_stage_data[i][ST_SCORE_STAR_MAG]))  #座標(176,10+i)から3ケタのスコアスター得点倍率を書き込み
            
            update_system.write_data_num(self,128 -1 +8,10+i,0,  8,int(self.replay_control_data_size[i])) #座標(128,10+i)に8ケタのコントロールパッド入力データが記録されたファイルのデータサイズを書き込みます
        pyxel.save(os.path.abspath("./assets/replay/" + slot_num + "/replay_status.pyxres")) #リプレイステータスファイルをセーブ！
        # pyxel.save("./assets/replay/" + slot_num + "/replay_status.pyxres") #リプレイステータスファイルをセーブ！

    #リプレイデータの記録   自動移動モードの時とステージクリアのブーストの時とリプレイ再生中の時はリプレイデータを記録しません
    def record_data(self):
        if     self.move_mode     == MOVE_AUTO\
            or self.game_status   == Scene.STAGE_CLEAR_MOVE_MY_SHIP\
            or self.game_status   == Scene.STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status   == Scene.STAGE_CLEAR_FADE_OUT\
            or self.replay_status == REPLAY_PLAY:
            self.pad_data_h = 0b00000000             #次のフレーム時の記録のためにデータを初期化してあげます
            self.pad_data_l = 0b00000000
            return
        else:
            self.replay_recording_data[self.replay_stage_num].append(self.pad_data_h)   #リプレイデータリストにパッド入力データを記録追加します
            self.replay_recording_data[self.replay_stage_num].append(self.pad_data_l)
            self.pad_data_h = 0b00000000             #次のフレーム時の記録のためにデータを初期化してあげます
            self.pad_data_l = 0b00000000

    #リプレイデータ再生用のインデックス値を1増やしていく関数(リプレイフレームインデックス値の更新)
    def increace_frame_index(self):
        if self.replay_frame_index < len(self.replay_data[self.replay_stage_num]) - 2:
            self.replay_frame_index += 2  #インデックス値がリストの大きさを超えていなかったら2(PADデータは2バイト長(16ビット長)なので次のデータに移行するには2増やす)増やして次のデータを取り込めるようにしてやります

    #リプレイデータ(ステータス関連)をバックアップする(プッシュする感じみたいな？？？)
    def push_status_data(self):
        self.backup_rnd_seed         = self.master_rnd_seed  #乱数の種(ゲームスタート時)をバックアップ
        self.backup_game_difficulty  = self.game_difficulty  #難易度をバックアップ
        self.backup_stage_number     = self.stage_number     #ステージ数をバックアップ
        self.backup_stage_loop       = self.stage_loop       #ループ数をバックアップ

    #リプレイデータ(リスト本体)をバックアップする(プッシュする感じみたいな？？？)
    def push_list_data(self):
        self.replay_data      = self.replay_recording_data    #録画されたリプレイデータをデータリストを登録

    #リプレイデータ(ステータス関連)をリストアする(ポップする感じみたいな？？？)
    #未使用メソッド・・・・・・・orz
    def restore_data(self):
        self.master_rnd_seed   = self.backup_rnd_seed         #乱数の種(ゲームスタート時)をリストア
        self.game_difficulty   = self.backup_game_difficulty  #難易度をリストア
        self.stage_number      = self.backup_stage_number     #ステージ数をリストア
        self.stage_loop        = self.backup_stage_loop       #ループ数をリストア

    #リプレイデータ記録中に使用するステージスタート時のパラメータのセーブ
    def save_stage_data(self):
        self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE]                       = self.score          #リプレイファイルに記録されたスコアをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SHIELD]                   = self.my_shield      #リプレイファイルに記録されたシールド値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SPEED]                    = self.my_speed       #リプレイファイルに記録された自機移動スピードをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SHOT_ID]              = self.select_shot_id #リプレイファイルに記録されたショットIDをセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_EXP]                    = self.shot_exp       #リプレイファイルに記録された自機ショットの経験値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_LEVEL]                  = self.shot_level     #リプレイファイルに記録された自機ショットのレベルをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_SPEED_MAGNIFICATION]    = self.shot_speed_magnification #リプレイファイルに記録された自機ショットのスピードに掛ける倍率をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_RAPID_OF_FIRE]          = self.shot_rapid_of_fire       #リプレイファイルに記録された自機ショットの連射数をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_EXP]                 = self.missile_exp              #リプレイファイルに記録された自機ミサイルの経験値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_LEVEL]               = self.missile_level            #リプレイファイルに記録された自機ミサイルのレベルをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_SPEED_MAGNIFICATION] = self.missile_speed_magnification #リプレイファイルに記録された自機ミサイルのスピードに掛ける倍率をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_RAPID_OF_FIRE]       = self.missile_rapid_of_fire   #リプレイファイルに記録された自機ミサイルの連射数をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SUB_WEAPON_ID]        = self.select_sub_weapon_id    #リプレイファイルに記録された現在使用しているサブウェポンのIDナンバーをセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_TYPE]                   = self.claw_type               #リプレイファイルに記録されたクローのタイプをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_NUMBER]                 = self.claw_number             #リプレイファイルに記録されたクローの装備数をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_DIFFERENCE]             = self.claw_difference         #リプレイファイルに記録されたクロ―同士の角度間隔をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_INDEX]            = self.trace_claw_index        #リプレイファイルに記録されたトレースクロー（オプション）時のトレース用配列のインデックス値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_DISTANCE]         = self.trace_claw_distance     #リプレイファイルに記録されたトレースクロー同士の間隔をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_FIX_CLAW_MAGNIFICATION]      = self.fix_claw_magnification  #リプレイファイルに記録されたフイックスクロー同士の間隔の倍率をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVX]            = self.reverse_claw_svx        #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(x軸)をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVY]            = self.reverse_claw_svy        #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(y軸)をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_SHOT_SPEED]             = self.claw_shot_speed         #リプレイファイルに記録されたクローショットのスピードをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_LS_SHIELD_HP]                = self.ls_shield_hp            #リプレイファイルに記録されたL'sシールドの耐久力をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_ID]                     = self.my_ship_id     #リプレイファイルに記録された使用している機体のIDナンバーをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_LEVEL]                  = self.my_ship_level  #リプレイファイルに記録された使用している機体のレベルをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_EXP]                    = self.my_ship_exp    #リプレイファイルに記録された使用している機体の経験値をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT1]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0] #リプレイファイルに記録された使用している機体のスロット1に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT2]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT1] #リプレイファイルに記録された使用している機体のスロット2に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT3]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT2] #リプレイファイルに記録された使用している機体のスロット3に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT4]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT3] #リプレイファイルに記録された使用している機体のスロット4に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT5]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT4] #リプレイファイルに記録された使用している機体のスロット5に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT6]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT5] #リプレイファイルに記録された使用している機体のスロット6に装備されているメダルIDをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT7]                       = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT6] #リプレイファイルに記録された使用している機体のスロット7に装備されているメダルIDをセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE_STAR_MAG]              = self.score_star_magnification #リプレイファイルに記録されたスコアスター取得得点倍率をセーブ

    #リプレイデータ記録中に使用するステージスタート時のパラメータのロード
    def load_stage_data(self):
        self.score     = self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE]                #リプレイファイルに記録されたスコアをロード
        self.my_shield = self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SHIELD]            #リプレイファイルに記録されたシールド値をロード
        self.my_speed  = self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SPEED]             #リプレイファイルに記録された自機移動スピードをロード
        
        self.select_shot_id  = self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SHOT_ID] #リプレイファイルに記録されたショットIDをロード
        
        self.shot_exp                 = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_EXP]                 #リプレイファイルに記録された自機ショットの経験値をロード
        self.shot_level               = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_LEVEL]               #リプレイファイルに記録された自機ショットのレベルをロード
        self.shot_speed_magnification = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_SPEED_MAGNIFICATION] #リプレイファイルに記録された自機ショットのスピードに掛ける倍率をロード
        self.shot_rapid_of_fire       = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_RAPID_OF_FIRE]       #リプレイファイルに記録された自機ショットの連射数をロード
        
        self.missile_exp                 = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_EXP]                 #リプレイファイルに記録された自機ミサイルの経験値をロード
        self.missile_level               = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_LEVEL]               #リプレイファイルに記録された自機ミサイルのレベルをロード
        self.missile_speed_magnification = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_SPEED_MAGNIFICATION] #リプレイファイルに記録された自機ミサイルのスピードに掛ける倍率をロード
        self.missile_rapid_of_fire       = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_RAPID_OF_FIRE]       #リプレイファイルに記録された自機ミサイルの連射数をロード
        
        self.select_sub_weapon_id        = self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SUB_WEAPON_ID] #リプレイファイルに記録された現在使用しているサブウェポンのIDナンバーをロード
        
        self.claw_type                   = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_TYPE]       #リプレイファイルに記録されたクローのタイプをロード
        self.claw_number                 = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_NUMBER]     #リプレイファイルに記録されたクローの装備数をロード
        self.claw_difference             = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_DIFFERENCE] #リプレイファイルに記録されたクロ―同士の角度間隔をロード
        
        self.trace_claw_index            = self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_INDEX]     #リプレイファイルに記録されたトレースクロー（オプション）時のトレース用配列のインデックス値をロード
        self.trace_claw_distance         = self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_DISTANCE]  #リプレイファイルに記録されたトレースクロー同士の間隔をロード
        
        self.fix_claw_magnification      = self.replay_mode_stage_data[self.replay_stage_num][ST_FIX_CLAW_MAGNIFICATION] #リプレイファイルに記録されたフイックスクロー同士の間隔の倍率をロード
        
        self.reverse_claw_svx            = self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVX]  #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(x軸)をロード
        self.reverse_claw_svy            = self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVY]  #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(y軸)をロード
        
        self.claw_shot_speed             = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_SHOT_SPEED]  #リプレイファイルに記録されたクローショットのスピードをロード
        self.ls_shield_hp                = self.replay_mode_stage_data[self.replay_stage_num][ST_LS_SHIELD_HP]     #リプレイファイルに記録されたL'sシールドの耐久力をロード
        
        self.my_ship_id                  = self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_ID]     #リプレイファイルに記録された使用している機体のIDナンバーをロード
        self.my_ship_level               = self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_LEVEL]  #リプレイファイルに記録された使用している機体のレベルをロード
        self.my_ship_exp                 = self.replay_mode_stage_data[self.replay_stage_num][ST_SHIP_EXP]    #リプレイファイルに記録された使用している機体の経験値をロード
        
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT1] #リプレイファイルに記録された使用している機体のスロット1に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT1] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT2] #リプレイファイルに記録された使用している機体のスロット2に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT2] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT3] #リプレイファイルに記録された使用している機体のスロット3に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT3] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT4] #リプレイファイルに記録された使用している機体のスロット4に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT4] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT5] #リプレイファイルに記録された使用している機体のスロット5に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT5] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT6] #リプレイファイルに記録された使用している機体のスロット6に装備されているメダルIDをロード
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT6] = self.replay_mode_stage_data[self.replay_stage_num][ST_SLOT7] #リプレイファイルに記録された使用している機体のスロット7に装備されているメダルIDをロード
        
        self.score_star_magnification    = self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE_STAR_MAG]    #リプレイファイルに記録されたスコアスター取得得点倍率をロード

