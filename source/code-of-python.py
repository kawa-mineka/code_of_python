######################################
# -------   code of python    ------ #
######################################
#       program mineka.kawakami      #
#             2020 06/28             #
#      language python 3.8(64bit)    #
#                                    # 
#        OS windows10(64bit)         #
#          Editer VS Code            #
#         Game Engine Pyxel          #
# sub Game Engine pygame(sound onry) #
#                                    #
#         Development machine        #
#           CPU corei5-6500          #
#          base clock 3.2Ghz         #
#       turboboost clock 3.6Ghz      #
#           4Core 4thread            #
#         GPU GeForce GTX960         #
#             Memory 8GB             #
######################################
#todo1 MOUNTAIN_REGION 地下洞窟＆地底湖の実装
#todo4 MOUNTAIN_REGION ブリザーディア(ボス)の実装(かなり難しい.......)
#todo5 MOUNTAIN_REGION ブリザーディア(ボス)が大気圏離脱していくシーンの実装LOOP2
#todo6 MOUNTAIN_REGION ブリザーディア(ボス)が本体破壊後、分離して前部が地表へと逃げていく演出実装LOOP3
#todo10 MOUNTAIN_REGION 大気圏突入時のスタッフクレジット表示の実装

#todo12 MOUNTAIN_REGION 中ボスの実装
#todo13 ADVACE_BASE 中ボスの実装
#todo15 VOLCANIC_BELT スクロールシステムの構築(縦2画面フリースクロール＋横強制スクロール)+ラスタースクロールによる炎の演出+上下3キャララインほどの多ラインスクロール
#todo16 VOLCANIC_BELT メインスクロール面でのプロミネンスアニメーション(当たり判定アリ)
#todo17 VOLCANIC_BELT メインスクロール面に重ね合わせての岩盤(ＢＧ)の挟みこみアニメーション実装
#todo17A VOLCANIC_BELT 暗闇の中を突き進んでいくスポットライトエフェクトの実装

#todo19 汎用性のある中ボスの実装
#todo21 汎用母艦「アークウェスディ」からの自機射出演出
#todo23 狙い撃ちn-way弾を射出する関数で偶数弾の処理が微妙に奇数弾っぽくなってるのを治す(自機狙いの弾が出なくて奇数弾→偶数弾になってるポイ)
#todo29 敵の2回屈折サーチレーザーの実装
#todo30 敵のウェーブカッターの実装
#todo31 敵のリップルレーザーの実装
#todo32 敵のワインダーレーザーの実装
#todo33 敵のサークルレーザーの実装
#todo36 敵の反射レーザーの実装
#todo39 敵のスプレッドボムの実装
#todo40 敵のロックオンレーザーの実装（実際にロックオンされて当たる訳ではないので注意）
#todo42 大き目の爆発パターンは放物線上に破片を撒き散らすようにする

#todo50 NIGHT_SKYSCRAPER 夜間超高層ビル地帯の背景グラフイックとスクロールシステムの構築(縦2画面任意スクロール＋左右マップリピートによる3重スクロール)
#todo51 NIGHT_SKYSCRAPER 中ボスの実装
#todo52 NIGHT_SKYSCRAPER ボスの実装

#todo81 第2の機体ElegantPerlの実装
#todo82 ElegantPerl専用のPerlCrawの実装
#todo83 機体選択シーンの実装
#todo84 機体選択シーンにおける各機体のタイポモーションロゴのアニメーション作成(難しそう)

#todo90 MagiForceとJusticePythonの合体演出
#todo99 漢字フォント読み込み時に遅くなるので高速化する(案としては分割してローディング？)

#todo703 画面上の任意の位置＆画面下の任意の位置から降下、上昇してくる敵編隊の実装
#todo705 子世代まで分裂する隕石の実装(結構硬い感じで)
#todo706 画面後ろから出てきて画面前方まで移動しx軸合わせのサーチレーザーを撃ってくる敵（ちょっと硬め）の実装
#todo707 自機とx軸が一致したら上または下方向に発射されるロングロケットミサイル→ドット絵作成済み
#todo708 斜め前方にレーザー（少し長め）を等間隔で発射してくるレーザー固定砲台→ドット絵作成済み
#todo709 3way弾を撃ってくる固定砲台(近づくと反応してくる)→ドット絵作成済み
#todo710 自機とx軸が一致したら高速レーザーを発射する固定砲台→ドット作成済み
#todo711 前からゆっくりとやってきてある程度の距離まで進んだら下部に装備している高速ミサイルを発射して上方向か下方向に離脱していく中型機→ドット絵作成済み
#todo712 高速回転キリ揉み飛行で一撃離脱で大量の弾をばらまいていく高速機（最初自機のクローとして使おうとしてた物をドット絵として再利用する）→ドット絵作成済み

#todo800 メイン武器を高速で切り替えたときグラフイックパターンがおかしくなるバグ取り
#todo801 ボスを倒した瞬間、自機がほぼ同時にやられた場合、進行不可になるバグの処置(バグ取り難しいかも・・・)
#todo801 自機が爆発中にボスが出現すると、進行不可になるバグの処置  全然わからないどこにバグが潜んでいるのかそれは・・・謎
#todo803 ウィンドウシステムを改良する（滅茶苦茶難しそう・・・今は同じようなコードを羅列してるだけなのでシンプルに行きたいところですが・・）
#todo804 難易度選択によるスタート時のクロー追加ボーナスでローリングクローだけ上手く複数追加されない(1個だけなら追加される)(おそらく2~4個追加時に全く同じ座標で回転し続けて1個だけで回っているように見える？のかも？)要バグ取り
#todo805 ボスとの当たり判定関連の関数はショット、ミサイル、クローショットの3つの関数があるがほとんど同じようなコードの羅列なので共通化したい・・リファクタリングって奴なのかな？？
#todo806 ウィンドウシステムで背後のウィンドウを左右に移動させたときに２～３秒後に左側の枠が微妙にズレてしまい1ドットくらいの隙間が出るバグの修正
#todo807 1面クリア時の背景スクロールに問題あるのかわかんないけどボスを倒したあと自機が右へ自動で飛んでいく処理でpyxel error: access to outside tilemap in 'GetValue'が出てクラッシュするバグがある・・・全然わからない・・原因が・・・orz
#todo900 BGMの作成(無理そう.........)
#todo901 SE(効果音)のボリューム調整をCONFIGウィンドウで調整できるようにする BGMのほうはpygameで再生しているので簡単にできたけどSEはpyxelで鳴らしているのですが。。どうやってボリューム調整したらいいのかわかんない・・・

#実装完了済み！
import os
import sys

abs_path = os.path.abspath(__file__) #絶対パスを取得
print ("現在の実行ファイル")
print(abs_path) #このプログラム自体がどのフォルダーで起動してるのかコンソールに表示



# from random import randint   #random.randint(n,m) と呼ぶと、nからm(m自身を含む)までの間の整数が 等しい確率で、ランダムに返される
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import math #三角関数などを使用したいのでインポートぉぉおお！
import copy #スコアボードでデフォルトスコアボードを深い階層までのコピーを使いたいのでインポートします

import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
import pygame.mixer #MP3再生するためだけに使用する予定・・・予定は未定・・・そして未定は確定に！やったあぁ！ BGMだけで使用しているサブゲームエンジン

from const.const              import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？)
from const.const_window       import * #主にウィンドウクラスで使用する定数定義の読み込み
from const.const_visualscene  import * #主にビジュアルシーンで使用する定数定義の読み込み

from define.define_class       import * #クラス宣言モジュールの読み込み やっぱりimport *は不味いのかなぁ・・・よくわかんない
from define.define_data        import * #初期データリスト登録モジュールの読み込み
from define.define_ship_data   import * #各種機体(シップ)データ関連の登録モジュールの読み込み
from define.define_enemy_data  import * #敵のデータ関連の登録モジュールの読み込み
from define.define_boss_data   import * #ボスのデータ関連の登録モジュールの読み込み
from define.define_stage_data  import * #各ステージのイベントリスト登録モジュールの読み込み
from common.func               import * #汎用性のある関数群のモジュールの読み込み

from draw.graph                import * #Appクラスのdraw関数から呼び出される関数群のモジュールの読み込み 基本的に画像表示だけを行う関数(メソッド)群です

from update.update_obj         import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主に背景オブジェクトの更新を行う関数(メソッド？）です

from update.update_ipl         import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にIPL表示関連の更新を行う関数(メソッド？）です
from update.update_init        import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にゲームスタート時の初期化,ステージスタート時の初期化の更新を行うメソッドです  
from update.update_title       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にタイトルメニューの更新を行う関数(メソッド？）です
from update.update_pause       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み ゲーム中のポーズ更新のメソッド群です
from update.update_score       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み スコア加算やハイスコアのチェック、登録などの更新メソッド
from update.update_sound       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み BGNやSEの読み込み、再生など
from update.update_status      import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にステータス表示ウィンドウで使われる項目を更新するメソッドです
from update.update_bg          import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にBGアクセス(タイルマップにアクセスするときに使用,タイルマップ書き換えとか読み出しとか)更新メソッドです

from update.update_system      import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にシステムデータのセーブロードを行う関数(メソッド？）です
from update.update_window      import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にウィンドウやセレクトカーソルの更新を行う関数(メソッド？）です
from update.update_visualscene import * #ppクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にビジュアルシーンの作製や更新を行うのです
from update.update_replay      import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み リプレイ記録再生の更新を行う関数(メソッド？）です
from update.update_debug       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み デバッグ用パラメーターの更新やキー入力による直接デバッグを行うメソッドです
from update.update_btn         import * #Appクラスのupdate関数から呼び出されるモジュール 主にショット＆ミサイル関連のボタンが押されたかを調べるメソッドです
from update.update_btn_assign  import * #Appクラスのupdate関数から呼び出されるモジュール パッドのボタンの機能変更（ボタンアサインコンフィグ)メソッドです

from update.update_ship        import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主に自機関連のメソッドです
from update.update_enemy       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主に敵の更新や敵弾の更新を行います
from update.update_boss        import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み ボスの更新を行います
from update.update_collision   import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主に衝突当たり判定を行います
from update.update_item        import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にパワーアップアイテム関連の更新を行います

from update.update_event       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み 主にイベントリストでの敵発生やマップスクロール時に敵を出す処理を行います

class App:
    ##########################################################################################################################################
    #関数を定義沢山定義するところだよ############################################################################################################
    #なんかpythonではこのあたり（Appクラスの __init__関数定義が終わったあたり）で定義しないとエラーが出るらしい
    #確かに関数定義をしないで関数呼び出したらエラーになるよなぁ・・・最初は関数定義はどこでも定義できると思って最後の方で定義してエラー出て悩んでたよ
    def __init__(self):
        if getattr(sys, 'frozen', False): #Pyinstallerでビルドしたかしていないかを判定しています hasattr(sys, "frozen")でも確認可能なようです(exeになっているときはTrue)
            self.program_directory = os.path.dirname(os.path.abspath(sys.executable))#Pyinstallerでビルドした時(実行ファイルかどうか)に実行されます
                                                                                #sys.executableがビルドしたEXEのパスを返します
                                                                                #osモジュールでディレクトリのパスに変換。
            print(" ")
            print("USE build  .EXE file")
            self.exe_mode = FLAG_ON  #pyinstallerでexe化したファイルを実行しているフラグを立てる
        else:
            self.program_directory = os.path.dirname(os.path.abspath(__file__))       #Pyinstallerでビルドしていない時に実行されます。
            print(" ")
            print("USE normal .py file")
            self.exe_mode = FLAG_OFF  #pyinstallerでexe化したファイルを実行しているフラグは立てない pyファイルで実行中
        
        print(" ")
        print("現在実行中のフォルダー")
        print(self.program_directory)
        print(" ")
        
        self.user_profile = os.path.join(os.path.expanduser("~"))
        print(" ")
        print("ユーザープロファイル")
        print(self.user_profile)
        print(" ")
        
        print("AppData/Local/code_of_python exist?")
        print(self.user_profile + "/AppData/Local/code_of_python")
        print(os.path.exists(self.user_profile + "/AppData/Local/code_of_python"))
        print(" ")
        
        if os.path.exists(self.user_profile + "/AppData/Local/code_of_python") == False: #もしAppData/Local/code_of_pythonフォルダーが存在しないのなら
            os.makedirs(self.user_profile + "/AppData/Local/code_of_python/system")      #systemフォルダーを作製する
            os.makedirs(self.user_profile + "/AppData/Local/code_of_python/replay")      #replayフォルダーを作製する
            print("AppData/Local/code_of_pythonフォルダーを作製しました")
            print(" ")
            
        update_system.check_exist_sysytem_file(self) #ユーザープロファイルのcode-of-pythonフォルダにシステムファイルがあるかどうか調べなかったらデフォルトのシステムデータをコピーする
        
        print(" ")
        # print("PYXEL VERSION " + pyxel.PYXEL_VERSION)         #pyxel 1.8.15まで使えていたけどpyxel 1.9.10以降は使えなくなった模様
        # print("PYXEL WORKING DIR " + pyxel.PYXEL_WORKING_DIR) #pyxel 1.8.15まで使えていたけどpyxel 1.9.10以降は使えなくなった模様
        
        print("PYXEL VERSION "             + pyxel.VERSION)         #pyxel 1.9.10以降はこれでいける模様
        print("PYXEL WORKING DIR "         + pyxel.WORKING_DIR)     #pyxel 1.9.10以降はこれでいける模様
        
        print("APP FILE EXTENSION "        + pyxel.APP_FILE_EXTENSION)
        print("APP STARTUP SCRIPT FILE "   + pyxel.APP_STARTUP_SCRIPT_FILE)
        print("RESOURCE_FILE_EXTENSION "   + pyxel.RESOURCE_FILE_EXTENSION)
        
        # print("RESOURCE_ARCHIVE_DIRNAME "  + pyxel.RESOURCE_ARCHIVE_DIRNAME) pyxel 2.0.0だとサポートされていないのでコメントアウト
        
        print(" ")
        print("NUM_COLORS "     + str(pyxel.NUM_COLORS))
        print("NUM_IMAGES "     + str(pyxel.NUM_IMAGES))
        print("IMAGE_SIZE "     + str(pyxel.IMAGE_SIZE))
        print("NUM_TILEMAPS "   + str(pyxel.NUM_TILEMAPS))
        print("TILEMAP_SIZE "   + str(pyxel.TILEMAP_SIZE))
        print("TILE_SIZE "      + str(pyxel.TILE_SIZE))
        
        # pyxel.screen_mode(scr = 2) #将来的にはスクリーンフィルターエフェクト(ブラウン管再現フィルターとかドットスムースフィルター)が変えられるかもしれないので記述しておくです
        
        pygame.mixer.init()  #pygameミキサー関連の初期化 pyxel.initよりも先にpygameをinitしないと上手く動かないみたい・・・
        
        pyxel.init(WINDOW_W,WINDOW_H,title="CODE OF PYTHON",fps = 60,quit_key=pyxel.KEY_NONE) #ゲームウィンドウのタイトルバーの表示とfpsの設定(60fpsにした),キーボード入力による強制終了は無しとする pyxel.init(caption=)がpyxel.init(title=)に変更されたっぽい？？？
        # pyxel.init(640,400,title="CODE OF PYTHON",fps = 60,quit_key=pyxel.KEY_NONE)   #デバッグ確認用高解像度用イニシャライズ
        
        self.ship_equip_slot_list = [[0] * 6 for i in range(LOOK_AT_LOGO)]  #(横6,縦LOOK_AT_LOGO(15))までint(0)が入ったリストを作製し初期化します
        
        self.temp_my_ship_medal = [0] * 6 #(横6個分 int(0)が入ったメダルID一時退避保存用リストを初期化作製する(リプレイ再生前と後で一時退避的に使われます)
        
        define_data.default_score_board(self) #スコアボードの初期データ(デフォルトデータ)を登録する関数の呼び出し        
        
        self.attrib_chr_col    = [[0] * int(WINDOW_W // 8)  for i in range (int(WINDOW_H // 8)) ] #キャラ表示単位でのアトリビュートリスト(色情報)初期化
        self.attrib_screen_col = [[0] * WINDOW_W for i in range (WINDOW_H) ]                      #ドット表示単位でのアトリビュートリスト(色情報)初期化
        self.attrib_line_col   = [[0] * 2  for i in range(WINDOW_H)]                              #横ライン単位でのアトリビュートリスト(色情報)初期化 横2ドット単位でのタイリングパターンに対応するので[0,0]の色指定整数値2項目にしてますの
        
        # print(self.attrib_chr_col)
        # print(self.attrib_screen_col)
        # print(self.attrib_line_col)
        
        #self.score_board = self.default_score_b11oard この方法でのリストコピーだとリストの「参照元id」がコピーされるだけなのでscore_boardリストの要素を変更するとdefault_score_boardリストの要素も変更されたように見えるので使えないので注意
        self.score_board = copy.deepcopy(self.default_score_board)  #ですのでdeepcopyを使います、そうすれば深い階層までコピーされ、コピー前後でidが変更されて全くの別リストになります 
                                                                    #他の方法としてはスライスを使ったself.score_board = self.default_score_board[:]とかあるみたいだけど浅い階層しかコピーされないみたい
        self.header                          = "code-of-python system-data ver 1.00"#システムファイルに書き込むヘッダ文字列
        self.default_my_name                 = "AAA     "                           #プレイヤーの名前(ネームエントリーの関係上半角8文字でお願いします)
        self.default_medal_list = [0,0,0,0,0,  0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]     #取得メダルリストを作製初期化
                                                                                    #0=未入手 1=入手 メダルのIDナンバーがリストのインデックス値となります
        
        #パッドボタン割り当て初期データのリスト [Aボタン,Bボタン,
        #                                     Xボタン,Yボタン,
        #                                     BACKボタン,GUIDEボタン,STARTボタン
        #                                     LEFTSHOULDERボタン,RIGHTSHOULDERボタン]
        # self.default_pad_assign_list = [ACT_SHOT_AND_SUB_WEAPON,ACT_MISSILE,
        #                                 ACT_MAIN_WEAPON_CHANGE,ACT_SUB_WEAPON_CHANGE,
                                        
        #                                 ACT_SPEED_CHANGE,ACT_NO_ASSIGN,ACT_PAUSE,
                                        
        #                                 ACT_CHANGE_CLAW_STYLE,ACT_CHANGE_CLAW_INTERVAL]
        self.default_pad_assign_list = [ACT_SHOT_AND_SUB_WEAPON,ACT_MISSILE,
                                        ACT_MAIN_WEAPON_CHANGE,ACT_SUB_WEAPON_CHANGE,
                                        
                                        ACT_SPEED_CHANGE,ACT_NO_ASSIGN,ACT_PAUSE,
                                        
                                        ACT_CHANGE_CLAW_STYLE,ACT_CHANGE_CLAW_INTERVAL]
        #何も設定されてないパッドアサインリストを作製
        self.empty_pad_assign_list =    [ACT_NO_ASSIGN,ACT_NO_ASSIGN,
                                        ACT_NO_ASSIGN,ACT_NO_ASSIGN,
                                        
                                        ACT_NO_ASSIGN,ACT_NO_ASSIGN,ACT_NO_ASSIGN,
                                        
                                        ACT_NO_ASSIGN,ACT_NO_ASSIGN]
        
        define_data.default_achievement_list(self) #実績のIDナンバーとそれに対するグラフイックチップの位置や英語コメント、日本語コメントのデータリストの定義関数の呼び出し
        
        self.default_boss_number_of_defeat = [0] * 50                                  #ボス撃破数デフォルトリストを作製します
        
        self.my_name               = copy.deepcopy(self.default_my_name)               #自分の名前の初期データを深い階層でコピーする
        self.medal_list            = copy.deepcopy(self.default_medal_list)            #メダルリストの初期データを深い階層でコピーする
        self.achievement_list      = copy.deepcopy(self.default_achievement_list)      #実績リストの初期データを深い階層でコピーする
        self.boss_number_of_defeat = copy.deepcopy(self.default_boss_number_of_defeat) #ボスを倒した総数の初期データを深い階層でコピーする
        self.pad_assign_list       = copy.deepcopy(self.default_pad_assign_list)       #パッド割り当て情報の初期データを深い階層でコピーする
        
        
        self.development_testtime            = 0  #ゲーム開発時の総テスト時間
        self.one_game_playtime_seconds       = 0  #1プレイでのゲームプレイ時間(秒単位)
        
        self.total_game_playtime_seconds     = 0  #初めてこのゲームをプレイしてからの合計プレイ時間(単位は秒となります)
        self.tatal_score                     = 0  #累計得点数
        self.number_of_play                  = 0  #遊んだ回数
        self.number_of_times_destroyed       = 0  #自機が破壊された回数
        
        self.title_startup_count             = 0  #タイトルロゴの起動表示回数カウンタ(初回起動なのか？2回目以降のタイトル表示なのかを判別します)
        
        self.storyboard_index                = 0 #ストーリーボードのインデックス値を初期化
        
        update_system.load_data(self)        #システムデータをロードする関数の呼び出し
        if self.fullscreen_mode == FLAG_ON:  #フルスクリーン起動モードフラグが立っていたのなら
            #pyxel.init(WINDOW_W,WINDOW_H,title="CODE OF PYTHON",fps = 60,fullscreen = True,quit_key=pyxel.KEY_NONE) #フルスクリーンでpyxelを再起動する ver1.5以降からfullscreen = Trueは使えなくなったらしいです
            pyxel.fullscreen(True)           #pyxel Ver1.5からfullscreen命令が追加されたらしい 裏技ッポイけど！？使っても良いのん？？
        pyxel.mouse(False)                   #マウスカーソルを非表示にする
        
        update_window.refresh_pad_assign_graph_list(self)#パッドアサイングラフイックリストを新規に作成する(self.pad_assign_listに依存しているためself.pad_assign_listを作製した直後この場所で作製するべし！)
        
        self.bg_cls_color         = pyxel.COLOR_BLACK  #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=pyxel.COLOR_BLACK=黒色です)
        self.bg_transparent_color = pyxel.COLOR_BLACK  #BGタイルマップを敷き詰めるときに指定する透明色です
        
        self.game_quit_timer    = 0  #ゲーム終了時に使用する終了カウントタイマーです(終了工程開始時に数値設定し1フレームごと減算し0になったらゲーム終了！)
        self.game_quit_from_playing = 0 #タイトルからの終了工程なのか？それともゲーム中からの終了工程なのかどうかのフラグ 0=タイトルから 1=ゲーム中から
        
        self.rnd_seed           = 0  #線形合同法で使用する乱数の種を初期化します(r_randintが呼ばれるごとにrnd_seedの中身が変化するので注意！)
        self.master_rnd_seed    = 0  #線形合同法で使用する乱数の種(ゲームスタート時のrnd_seedを保存してリプレイファイル再生時の最初の乱数の種として使用します初期化します
        
        self.start_stage_number = STAGE_MOUNTAIN_REGION    #スタート時のステージ数を保存する変数をまず初期化
        self.start_stage_loop   = LOOP01                   #スタート時のループ数を保存する変数をまず初期化
        self.start_stage_age    = 0                        #スタート時の年代数を保存する変数をまず初期化
        
        self.replay_slot_num    = 0  #リプレイファイルをセーブしたりロードするスロットナンバーが入ります(0~9)
        
        define_data.stage_asset_list(self)             #ステージごとのアセットファイル名(pyxresファイル)が登録されたリストを作成する関数の呼び出し
        define_data.medal_graph_and_comment_list(self) #メダルのIDナンバーとそれに対するグラフイックチップの位置や英語コメントなどの定義関数の呼び出し
        
        #ゲーム中で絶対に変化することのないリスト群はここで作成します#######################################
        define_data.ipl_mes(self)               #IPLメッセージテキストの定義関数の呼び出し
        define_data.flash_color_list(self)      #点滅用カラーリスト群の定義 サブウェポンセレクターカーソルなどで使用する点滅用カラーリスト群(pyxelのカラーナンバーだよ)
        define_data.expansion_shrink(self)      #サブウェポンアイテムの外を回っている四角形描画用のデータリスト定義関数の呼び出し
        define_data.font_code_table(self)       #美咲フォントコードテーブルの定義関数の呼び出し
        define_data.game_difficulty_list(self)  #難易度ごとの各種設定数値のリストの定義関数の呼び出し
        define_data.game_rank_data_list(self)   #ランク値による各種設定数値のリストの定義関数の呼び出し
        define_data.storyboard(self)            #タイトルデモ、ミドルデモなどのビジュアルシーンの絵コンテ(ストーリーボード）の定義関数の呼び出し
        
        define_enemy_data.anime_ptn(self)       #敵キャラのアニメパターンのキャラチップ番号の定義関数の呼び出し
        define_enemy_data.move_data(self)       #敵の移動データリストの定義関数の呼び出し
        
        define_boss_data.move_data(self)        #ボスの移動データリストの定義関数の呼び出し
        
        define_stage_data.stage_data_list(self) #ステージデータリストの定数定義関数の呼び出し
        
        define_ship_data.default_ship_list(self)          #各機体リスト(初期状態)の定義関数の呼び出し
        define_ship_data.sub_weapon_level_data_list(self) #サブウェポンのレベルデータリストの定義関数の呼び出し
        define_ship_data.shot_table_list(self)            #ショットパワーアップテーブルリストの定義関数の呼び出し
        define_ship_data.missile_table_list(self)         #ミサイルパワーアップテーブルリストの定義関数の呼び出し
        
        self.game_status = Scene.IPL                #ゲームステータスを「IPL表示」にする
        #self.game_status = Scene.GAME_START_INIT   #ゲームの状況ステータスを表してます（ゲームそのもの自体の状態遷移フラグとして使用します）
                                                    #まず最初はゲームステータスは「ゲームスタート時の初期化」にします
                                                    #将来的には「起動処理中」とか「タイトル表示中」にする予定
        
        #再スタートで初期化してはいけない変数はここ(appクラスの__init__関数)で定義します###################################
        self.hi_score =  100                    #ハイスコア
        # self.total_game_playtime_seconds = 0  #トータルゲームプレイ時間 (秒)
        
        #self.replay_data = [[]]*50              #リプレイデータ用に使用する横無限大,縦50ステージ分の空っぽのリプレイデータリストを作成します
        #上の方法で空リストを作成すると1つのリストに数値を入れると他の全てのリストに数値が代入されちゃう・・・・・なんでや！
        #なんか上の方法だと要素のリストがすべて同じオブジェクトになるらしい・・・聞いてないよそんなの・・・
        #内包表記って言うのを使えば良いらしい！？
        self.replay_data          = [[] for i in range(50)] #これでいいのかな？？？うまくいったぜ！
        self.replay_stage_my_data = [[] for i in range(50)] #リプレイ録画時、ステージスタート時に記録される自機関連のデータが入るリスト横無限大,縦50ステージ分
        
        self.replay_mode_stage_data        =[[0] * 80 for i in range(50)] #リプレイモードでの毎ステージスタート時の自機データ収納リストを初期化します                 (横30,縦50ステージ分の空リスト)
        self.replay_mode_stage_data_backup =[[0] * 80 for i in range(50)] #リプレイモードでの毎ステージスタート時の自機データ収納リスト(バックアップ用)を初期化します  (横30,縦50ステージ分の空リスト)
        self.temp_graph_list = []               #スコアデータウィンドウを育成するときに使用する一時的なメダルリストグラフイック座標値などが入ったリスト群を初期化宣言
        self.master_se_vol_list = [[] for i in range(62)] #SE用のマスターボリュームリストを保存しておくためのリストです
        self.adjustable_se_vol_list =[[] for i in range(62)]
        
        self.replay_control_data_size = []      #リプレイファイルのステージ毎のコントロールデータのファイルサイズリストです
        self.master_flag_list = [[] for i in range(128)] #ウィンドウ表示時に使用するフラグ＆データ関連の元リストを初期化
        self.replay_stage_num = 0               #リプレイ再生、録画時のステージ数を0で初期化します(1ステージ目=0→2ステージ目=1→3ステージ目=2って感じ)
        self.move_mode = MOVE_MANUAL            #移動モードの状態です
                                                #MOVE_MANUAL = パッドやキーボード入力によって移動
                                                #MOVE_AUTO = イベントによる自動移動モードとなり設定された位置まで自動で移動して行きます
        
        self.replay_status= REPLAY_RECORD       #リプレイ記録のステータスです
                                                #REPLAY_STOP = 0   #何も作動してない状態です リプレイデータ記録無し,再生無し
                                                #REPLAY_RECORD = 1 #リプレイデータを記録中です
                                                #REPLAY_PLAY   = 2 #リプレイデータを再生中です
        
        #####IPL関連の変数を初期化#####################################################################################
        self.display_ipl_time = 200            #IPLメッセージを表示する時間 200
        self.text_console_scroll_counter = 0   #テキストコンソールでスクロールして画面上に消えて行った行数
        self.ipl_mes_write_line_num = 0        #スクリーンに表示したIPLメッセージデータの行数
        self.text_screen = []                  #テキストスクリーン用のリストを初期化して使えるようにします
        
        self.scroll_type = 0                   #スクロールの種類が入る変数を初期化
        self.game_playing_flag  = FLAG_OFF     #ゲーム中なのか？それ以外の状態なのか？を示すフラグです 0=プレイ以外 1=プレイ中
        self.star_scroll_flag   = FLAG_OFF     #背景のスクロールする星々を表示するかのフラグを初期化
        self.raster_scroll_flag = FLAG_OFF     #背景ラスタスクロールを表示するかのフラグを初期化
        self.reference_tilemap  = 0            #BGタイルマップを調べたり書き換えたりする時、どのタイルマップナンバーを使用するのかの変数の初期化です
        
        func.load_kanji_font_data(self)        #漢字フォントデータをロードする関数の呼び出し
        self.select_cursor_flag = FLAG_OFF     #セレクトカーソルを動かすかどうかのフラグはOFFにして初期化しておく
        
        self.playing_ship_list = copy.deepcopy(self.default_ship_list) #シップ関連のリストはシステムデータロード関連はまだ未実装なのでとりあえずデフォルトのリストをコピーして仮状態でいきますっ！(システムデータリセットの事も考えてディープコピーします)
        
        self.my_ship_id = J_PYTHON             #自機選択のシステムデータロード関連はまだ未実装なのでとりあえずJ_PYTHONにしておきます
        self.my_ship_level = 1                 #レベルや経験値システムもまだ未実装なので初期化だけしておきます
        self.my_ship_exp = 0
        
        func.read_ship_equip_medal_data(self)  #プレイ中の自機リスト群にメダルスロット装備関連のデータを読み込んで行く関数の呼び出し
        func.medal_effect_plus_medallion(self) #装備されたメダルを調べ、メダルスロットを増やすメダルがはめ込まれていたらスロット数を増やす関数の呼び出し
        
        update_sound.pre_load_bgm(self)           #事前にバッファーに読み込むタイプのBGMファイルをローディングする
        
        #毎フレームごとにupdateとdrawを呼び出す
        #近年のゲームエンジンはみんなこんな感じらしい？？？unityやUEもこんな感じなのかな？？使ったことないけど
        pyxel.run(self.update,self.draw)#この命令でこれ以降は１フレームごとに自動でupdate関数とdraw関数が交互に実行されることとなります

    ##############################################################################
    ###############################################################################
    ###############################################################################
    #     ゲームで扱う情報を更新したり、キー入力（コントロ―ラー入力）を行う             # 
    #                あっぷで～～と☆彡    KANSUU                                   #
    ###############################################################################
    ###############################################################################
    #          ウィンドウズアップデートはあってはならない文明                         #
    #                      滅ぶべし・・・                                           #
    ################################################################################
    #パイソンはどうして関数を呼び出すだけなのにselfを付けないといけないのか              #
    #謎である                                                                        #
    #良く判らないけどプログラムコードを分割して複数のファイルにして                      #
    #別のクラスとして管理し始めたんだけど・・・・・・・・・・・                          #
    #  update_ipl.ipl()         →エラーになる                                        #
    #  update_ipl.ipl(self)     →selfを付けて引数を1個多くすると何故かokになる         # 
    #クラスのメソッド(そもそもメソッドというのが良く判らない。。。)呼び出す時も           #
    #  update_score.score_board_bubble_sort(self.game_difficulty)      →エラーになる #
    #  updade_score.score_board_bubble_sort(self,self.game_difficulty) →上手くいく   #
    #良く判らない・・・・判らない・・・判らない・・・・・・・・                          #
    #だからセルフってなんですのん？？？                                                #
    #それと関数とメソッドの違いってなんですのん？良く判らない、同じじゃないの？？          #
    ##################################################################################
    def update(self):
        ################################起動処理中 IPL ###################################################################
        if self.game_status == Scene.IPL:         #ゲームステータスが「IPL」の場合IPLメッセージの更新を行う
            update_ipl.ipl(self)                  #IPLの更新
        
        ################################ タイトル関連の変数を初期化 ###################################################################
        if self.game_status == Scene.TITLE_INIT:  #ゲームステータスが「TITLE_INIT」の場合タイトル関連の変数を初期化する関数を呼び出す
            update_title.title_init(self)         #タイトル関連の変数の初期化関数を呼び出す
        
        ################################ タイトルロゴの初回表示 ###################################################################
        if self.game_status == Scene.TITLE_FIRST:       #ゲームステータスが「TITLE_FIRST」の場合タイトルの更新を行う
            update_title.title(self)                    #タイトルの更新
            update_obj.append_star(self)                #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)                       #背景の星の更新（移動）関数呼び出し
            update_window.window(self)                  #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)             #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self)           #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
            update_visualscene.visualscene(self)        #ビジュアルシーンの更新関数の呼び出し
        ################################ タイトルでのボタン入力待ち###################################################################
        if self.game_status == Scene.TITLE_HIT_ANY_BTN: #ゲームステータスが「TITLE_HIT_ANY_BTN」場合は何かしらのボタン入力待ちをする
            update_title.title_hit_any_btn(self)        #タイトルメニューを表示した後,何かしらのボタンの入力待ち状態
            update_obj.append_star(self)                #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)                       #背景の星の更新（移動）関数呼び出し
            update_window.window(self)                  #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)             #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self)           #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
            update_visualscene.visualscene(self)        #ビジュアルシーンの更新関数の呼び出し
        ################################ タイトルロゴの2回目以降の表示 ###################################################################
        if self.game_status == Scene.TITLE_SECOND: #ゲームステータスが「TITLE_SECOND」の場合タイトルの更新を行う
            update_title.title(self)               #タイトルの更新
            update_obj.append_star(self)           #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)                  #背景の星の更新（移動）関数呼び出し
            update_window.window(self)             #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)        #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self)      #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
        
        ################################ タイトルでメニュー選択中 ###################################################################
        if self.game_status == Scene.TITLE_MENU_SELECT:
            update_title.title_menu_select(self)        #タイトルでのメニュー選択処理をする関数の呼び出し
            update_obj.append_star(self)                #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)                       #背景の星の更新（移動）関数呼び出し
            update_window.window(self)                  #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)             #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self)           #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
            update_window.select_cursor(self)           #セレクトカーソルでメニューを選択する関数を呼び出す
            update_window.judge_medal_acquisition(self) #メダルの取得判定を行う関数を呼び出す
        
        ############################### ロード用リプレイデータスロットの選択中 #######################################################
        if self.game_status == Scene.SELECT_LOAD_SLOT:#「SELECT_LOAD_SLOT」の時は
            update_obj.append_star(self)                #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)                       #背景の星の更新（移動）関数呼び出し
            update_window.window(self)                  #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)             #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self)           #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
            update_window.select_cursor(self)           #セレクトカーソルでメニューを選択する関数を呼び出す
            if self.cursor_decision_item_y != UNSELECTED:#決定ボタンが押されてアイテムが決まったのなら
                self.replay_slot_num = self.cursor_decision_item_y #リプレイ番号は決定ボタンを押した時点での決定アイテムのy座標数とする
                self.cursor_type = CURSOR_TYPE_NO_DISP        #セレクトカーソルの表示をoffにする
                self.move_mode = MOVE_MANUAL                  #移動モードを「手動移動」にする
                self.replay_status = REPLAY_PLAY              #リプレイ機能の状態を「再生中」にします
                self.replay_stage_num = 0                     #リプレイデータを最初のステージから再生できるように0初期化
                func.backup_status_data_for_replay_mode(self) #リプレイ再生前に現在のステータスを一時保存する関数の呼び出し
                update_replay.data_file_load(self)            #リプレイデータファイルのロードを行います
                update_replay.load_stage_data(self)           #リプレイ再生時は,ステージスタート時のパラメーターをロードする関数を呼び出します
                self.active_window_id = WINDOW_ID_MAIN_MENU   #メインメニューウィンドウIDを最前列でアクティブなものとする
                self.game_status = Scene.GAME_START_INIT      #ゲームステータスを「SCENE_GAME_START_INIT」にしてゲームスタート時の初期化にする
        
        ################################ ゲームスタート時の初期化 #################################################################
        if self.game_status == Scene.GAME_START_INIT: #ゲームステータスが「START_INIT」の場合（ゲームスタート時の状態遷移）は以下を実行する
            update_init.game_start(self)              #ゲーム開始前の初期化    スコアやシールド値、ショットレベルやミサイルレベルなどの初期化
            update_replay.push_status_data(self)      #リプレイデータ(ステータス関連)をバックアップする(プッシュする感じみたいな？？？)関数の呼び出し
            self.game_status = Scene.STAGE_START_INIT #ゲームステータスを「STAGE_START_INIT」にする
        
        ################################ステージスタート時の初期化 #################################################################
        if self.game_status == Scene.STAGE_START_INIT: #ゲームステータスが「START_INIT」の場合（ゲームスタート時の状態遷移）は以下を実行する
            update_init.stage_start(self)              #ステージ開始前の初期化   自機の座標や各リストの初期化、カウンター類の初期化
            self.game_status = Scene.PLAY              #ゲームステータスを「STAGE_START_INIT」にする
        
        ################################ ゲームプレイ中！！！！！！ ###############################################################
        if     self.game_status == Scene.PLAY\
            or self.game_status == Scene.EXPLOSION\
            or self.game_status == Scene.STAGE_CLEAR\
            or self.game_status == Scene.GAME_OVER\
            or self.game_status == Scene.BOSS_APPEAR\
            or self.game_status == Scene.BOSS_BATTLE\
            or self.game_status == Scene.BOSS_EXPLOSION\
            or self.game_status == Scene.STAGE_CLEAR\
            or self.game_status == Scene.STAGE_CLEAR_MOVE_MY_SHIP\
            or self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status == Scene.STAGE_CLEAR_FADE_OUT:
            #自機関連の処理######################################################################################
            # ##################################################################################################
            update_ship.ship(self)                 #自機の更新処理（移動処理）関数を呼び出す
            update_ship.record_coordinate(self)    #自機の座標を過去履歴リストに書き込んでいく関数（トレースクローの座標として使用します）を呼び出す
            update_ship.clip(self)                 #自機をはみ出さないようにする関数を呼び出す
            #パワーアップ関連の処理################################################
            update_btn.powerup_shot(self)          #ショットのパワーアップ処理関数を呼び出し
            update_btn.powerup_missile(self)       #ミサイルのパワーアップ処理関数の呼び出し
            #自機スピードチェンジ###################################################
            update_btn.change_speed(self)          #自機スピードチェンジボタンが押されたか調べる関数呼び出し
            #自機ショット関連の処理#################################################
            update_ship.shot(self)                  #自機弾の更新関数を呼び出す
            update_ship.clip_shot(self)             #自機弾をはみ出さないようにする関数を呼び出す
            update_collision.my_shot_to_bg(self)    #自機弾と背景との当たり判定を行う関数を呼び出す
            update_collision.my_shot_to_enemy(self) #自機弾と敵の当たり判定を行う関数を呼び出す
            update_collision.my_shot_to_boss(self)  #自機弾とボスの当たり判定を行う関数を呼び出す
            #ミサイル関連の処理###################################################################
            update_ship.missile(self)               #自機ミサイルの更新（移動処理）関数を呼び出す
            update_ship.clip_missile(self)          #自機ミサイルをはみ出さないようにする関数を呼び出す
            update_collision.missile_to_enemy(self) #自機ミサイルと敵との当たり判定を行う関数の呼び出す
            update_collision.missile_to_boss(self)  #自機ミサイルとボスとの当たり判定を行う関数を呼び出す
            #クロー関連の処理 ####################################################################
            update_ship.claw(self)                    #クローの更新（移動処理）関数を呼び出す
            update_ship.claw_shot(self)               #クローの弾の更新（移動処理）を呼び出す
            update_collision.claw_shot_to_enemy(self) #クローの弾と敵との当たり判定関数を呼び出す
            update_collision.claw_shot_to_boss(self)  #クローの弾とボスとの当たり判定関数を呼び出す
            update_collision.claw_shot_to_bg(self)    #クローの弾と背景との当たり判定関数を呼び出す
            
            #敵の弾関連の処理 ###################################################################################
            ####################################################################################################
            update_enemy.shot(self)                       #敵の弾の更新（移動処理とか）＆自機と敵弾と自機との当たり判定の関数の呼び出し
            update_enemy.clip_shot(self)                  #敵の弾が画面からはみ出したら消去する関数の呼び出し
            update_collision.enemy_shot_to_bg(self)       #敵の弾と背景との当たり判定を行う関数の呼び出し
            
            #クロー関連の処理###########################################################################################################
            update_btn.delete_claw_btn(self)              #クローを消滅させるキーが押されたか調べる関数の呼び出し
            update_btn.change_fix_claw_interval_btn(self) #フイックスクロー間隔変化ボタンが押されたか調べる関数を呼び出す
            update_btn.change_claw_style_btn(self)        #クロースタイル変更ボタンが押されたか調べる関数を呼び出す    
            
            #イベントリスト関連の処理###############################################################################################################
            update_event.list_execution(self)             #イベントリスト解析による敵の発生関数を呼び出す
            update_event.enemy_born_map_scroll(self)      #マップスクロールによる敵の発生関数を呼び出す
            update_event.building_born_timeline_map(self) #タイムラインマップによる建物の追加発生を行う
            update_event.append_request(self)             #アペンドイベントリクエストによる敵の追加発生関数を呼び出す（早回しなどの追加注文発生とかの処理）(イベント追加依頼）
            
            #敵関連の処理###############################################################################################################
            update_enemy.enemy(self)                      #敵の更新（移動とか）関数を呼び出す
            update_enemy.clip(self)                       #画面からはみ出た敵を消去する関数を呼び出し
            #ボス関連の処理#############################################################################################################
            update_boss.boss(self)                        #ボスの更新移動とかを行う関数を呼び出す
            if self.game_status == Scene.BOSS_APPEAR or self.game_status == Scene.BOSS_BATTLE:
                self.boss_battle_time += 1                #状態遷移が「ボス出現中」と「ボスと戦闘中」の時だけボス戦闘時間を1増加させていきます
            
            #パワーアップアイテム類の処理################################################################################################
            update_item.obtain_item(self)                    #パワーアップアイテム類の更新（移動とか）する関数を呼び出します
            update_collision.obtain_item_to_enemy_shot(self) #パワーアップアイテムと敵弾の当たり判定を行う関数を呼び出します
            update_item.clip_obtain_item(self)               #画面からはみ出したパワーアップアイテム類を消去する関数を呼び出します
            self.stage_count += 1                            #ステージ開始から経過したフレームカウント数を1増加させる
            #ランクアップ処理#############################################################################################################
            update_status.rank_up_look_at_playtime(self)   #時間経過によるランクアップ関数を呼び出します
            #スクロール関連の処理#########################################################################################################
            if self.boss_test_mode == MENU_BOSS_MODE_OFF:                #ボス戦テストモードオフの時だけ
                self.scroll_count += self.side_scroll_speed              #スクロールカウント数をスクロールスピード分(通常は1)増加させていく
                self.vertical_scroll_count += self.vertical_scroll_speed #縦スクロールカウント数を縦スクロールスピード分(大抵のステージは縦スクロールしないので0)増加させていく
            
            #縦横スクロールのスピード調整#################################################################################################
            func.adjust_scroll_speed(self)           #縦横スクロールのスピードを設定値までに近づけていく関数を呼び出します
            
            #ラスタスクロールの更新#######################################################################################################
            update_obj.raster_scroll(self)            #ラスタースクロールの更新関数の呼び出し
            #マップチップナンバー書き換えによるアニメーション関連の更新######################################################################
            update_obj.bg_rewrite_animation(self)     #BG書き換えによるアニメーション関数の呼び出し
            # update_obj.dummy_bg_animation(self)     #BG 座標直接指定による書き換えダミーテスト
            #リプレイデータの記録と再生###################################################################################################
            update_replay.record_data(self)           #パッド＆キーボード入力によるリプレイデータの記録を行う関数を呼び出します
            update_replay.increace_frame_index(self)  #リプレイ用のフレームインデックス値を1進めていく関数を呼びますぅ
            #乱数ルーレットの更新########################################################################################################
            update_status.rnd0_9(self)                    #乱数ルーレット( 0~9)の更新
            update_status.rnd0_99(self)                   #乱数ルーレット(0~99)の更新
            #実績(アチーブメント)の取得判定###############################################################################################
            if self.replay_status == REPLAY_RECORD:               #リプレイデータを保存している時(ゲームプレイ中)だけは実績取得の判定を行う(リプレイ再生時に実績取得すると不味いからね～～♪)
                update_window.judge_achievement_acquisition(self) #実績(アチーブメント)を取得したかどうかを調べる関数の呼び出し
        
        if     self.game_status == Scene.PLAY\
            or self.game_status == Scene.BOSS_APPEAR\
            or self.game_status == Scene.BOSS_BATTLE\
            or self.game_status == Scene.BOSS_EXPLOSION :#「プレイ中」とボス関連の時だけ自機の当たり判定関連とシールド値のチェック&ボタンを押したら何かをする処理を実行する
            #自機と色んなオブジェクトとの当たり判定処理#############################
            update_collision.ship_to_enemy(self)       #自機と敵との当たり判定関数を呼び出す             
            update_collision.ship_to_bg(self)          #自機と背景障害物との当たり判定関数を呼び出す
            update_collision.ship_to_obtain_item(self) #自機とパワーアップアイテム類の当たり判定（パワーアップゲットしたかな？どうかな？）
            update_collision.ship_to_boss(self)        #自機とボスとの当たり判定を行う関数を呼び出す
            #自機シールドのチェック###############################################
            update_ship.check_shield(self)             #自機のシールドが残っているのかチェックする関数を呼び出す
            #武器発射関連の処理###################################################
            update_btn.shot_btn(self)                  #ショット発射ボタンが押されたかどうか？を調べる関数を呼び出す
            update_btn.missile_btn(self)               #ミサイル発射ボタンが押されたかどうか？を調べる関数を呼び出す
            update_btn.claw_shot_btn(self)             #クローが弾を発射するボタンが押された？かどうかを調べる関数を呼び出す
            update_btn.change_sub_weapon_btn(self)     #サブウェポンの切り替えボタンが押されたか？どうかを調べる関数を呼び出す
            #デバッグモードによる敵や敵弾の追加発生（ボタンを押したら敵が出てくる！？）###################################################
            update_debug.enemy_append(self)          #デバッグモードによる敵＆敵弾追加発生
            #プレイ時間の計算#####################################################
            update_status.calc_playtime(self)          #プレイ時間を計算する関数を呼び出す
            #バックグラウンド(BG)を表示するときのカメラオフセット座標値を計算する#####
            func.screen_camera_offset(self)            #カメラオフセット座標値を計算する関数を呼び出す
            #ハイスコアの更新チェック##############################################
            update_score.check_hi_score(self)          #ハイスコアが更新されているか調べる関数を呼び出す
            #タイマーフレア放出###################################################
            update_obj.timer_flare(self)               #タイマーフレア放出の更新処理関数を呼び出す
            #大気圏突入時の火花の発生##########################################################
            update_obj.atmospheric_entry_spark(self)   #大気圏突入時の火花を発せさせる関数の呼び出し
        
        if self.game_status == Scene.BOSS_EXPLOSION:         #「BOSS_EXPLOSION」の時は
            update_item.present_repair_item(self)            #リペアアイテムを出現させる関数の呼び出し
        
        if self.game_status == Scene.EXPLOSION:              #「EXPLOSION」の時は
            self.my_ship_explosion_timer += 1                # my_ship_explosionタイマーを加算していき
            if self.my_ship_explosion_timer >= SHIP_EXPLOSION_TIMER_LIMIT:#リミット値まで行ったのなら
                self.game_status = Scene.GAME_OVER         #「GAME_OVER」にする
                pygame.mixer.music.fadeout(6000)           #BGMフェードアウト開始
        
        ############################### ゲーム一時中断中(PAUSE) ###################################################################
        if self.game_status == Scene.PAUSE:                  #「PAUSE」の時は
            update_pause.pause_menu(self)                    #ポーズ時のメニューセレクト処理を行う関数を呼び出す
        
        #######ゲームオーバー後の処理#############################################################
        if self.game_status == Scene.GAME_OVER:              #「GAME_OVER」の時は
            self.game_over_timer += 1                         # ゲームオーバータイマーを加算していき
            if self.game_over_timer >= GAME_OVER_TIMER_LIMIT: #リミット値まで行ったのなら
                if self.replay_status == REPLAY_RECORD:      #リプレイデータを記録している場合(ゲームプレイ中)は・・・・
                    self.number_of_play += 1                      #1ゲームプレイしたので「プレイ回数」を1増やす
                    self.total_score += self.score                #累計スコアに現在のスコアを加算する
                
                # pygame.mixer.music.load("assets/music/facton Morning Dreams 3727468_0_1.mp3") #GAME OVER BGMファイルの読み込み
                # pygame.mixer.music.set_volume(self.master_bgm_vol / 100)                      #ボリューム値設定
                # pygame.mixer.music.play(-1)                                                   #GAME OVER BGMをループ再生
                
                self.game_status = Scene.GAME_OVER_FADE_OUT   #「ゲームオーバーフェードアウト開始」にする
        
        if self.game_status == Scene.GAME_OVER_FADE_OUT:     #「GAME_OVER_FADE_OUT」の時は
            if self.fade_complete_flag == FLAG_ON:           #フェードアウト完了のフラグが建ったのなら
                self.bg_cls_color = 0                        #クリアスクリーン時の塗りつぶし色を初期値の0(黒)に戻す（イベントとかで変化する場合があるため） 
                self.star_scroll_flag = FLAG_ON              #背景星のスクロール表示をonにする（イベントとかで変化する場合があるため） 
                self.game_status = Scene.GAME_OVER_SHADOW_IN #「GAME_OVER_SHADOW_IN」状態にする
        
        if self.game_status == Scene.GAME_OVER_SHADOW_IN:    #「GAME_OVER_SHADOW_IN」の時は
            if self.shadow_in_out_complete_flag == FLAG_ON:  #シャドウイン完了のフラグが建ったのなら
                
                self.game_over_bgm.set_volume(self.master_bgm_vol / 100)      #ボリューム値設定
                self.game_over_bgm.play()                                     #ゲームオーバーBGM再生開始
                
                self.game_status = Scene.GAME_OVER_STOP      #「GAME_OVER_STOP」状態にする
        
        if self.game_status == Scene.GAME_OVER_STOP:         #「GAME_OVER_STOP」の時は
            if self.replay_status == REPLAY_RECORD: #リプレイ録画中の時のリターンタイトルウィンドウ表示
                update_window.create(self,WINDOW_ID_GAME_OVER_RETURN,43,68)    #RETRN? SAVE&RETURNウィンドウの作成
                self.cursor_type = CURSOR_TYPE_NORMAL             #選択カーソル表示をonにする
                self.select_cursor_flag = FLAG_ON                 #セレクトカーソルの移動更新フラグをオン
                self.cursor_move_direction = CURSOR_MOVE_UD       #カーソルは上下移動のみ
                self.cursor_x = 46                                #セレクトカーソルの座標を設定します
                self.cursor_y = 80
                self.cursor_item_y = 0                            #いま指示しているアイテムナンバーは0の「RETURN」
                self.cursor_decision_item_y = UNSELECTED          #まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
                self.cursor_max_item_y = 1                        #最大項目数は「RETURN」「SAVE & RETURN」の2項目なので 2-1=1を代入
                self.active_window_id = WINDOW_ID_GAME_OVER_RETURN#このウィンドウIDを最前列でアクティブなものとする
                self.game_status = Scene.RETURN_TITLE             #ゲームステータスを「RETURN_TITLE」にする
            elif self.replay_status == REPLAY_PLAY: #リプレイ再生中の時のリターンタイトルウィンドウ表示(SAVE&RETURN項目は表示しない)  
                update_window.create(self,WINDOW_ID_GAME_OVER_RETURN_NO_SAVE,43,68)     #RETRN?ウィンドウの作成
                func.restore_status_data_for_replay_mode(self)             #リプレイ再生が終了したので記録しておいたステータスを復帰させる
                self.cursor_type = CURSOR_TYPE_NORMAL                      #選択カーソル表示をonにする
                self.select_cursor_flag = FLAG_ON                          #セレクトカーソルの移動更新フラグをオン
                self.cursor_move_direction = CURSOR_MOVE_UD                #カーソルは上下移動のみ
                self.cursor_x = 46                                         #セレクトカーソルの座標を設定します
                self.cursor_y = 80
                self.cursor_item_y = 0                                     #いま指示しているアイテムナンバーは0の「RETURN」
                self.cursor_decision_item_y = UNSELECTED                   #まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
                self.cursor_max_item_y = 0                                 #最大項目数は「RETURN」の1項目なので 1-1=0を代入
                self.active_window_id = WINDOW_ID_GAME_OVER_RETURN_NO_SAVE #このウィンドウIDを最前列でアクティブなものとする
                self.game_status = Scene.RETURN_TITLE                      #ゲームステータスを「RETURN_TITLE」にする
        
        if self.game_status == Scene.RETURN_TITLE:           #「RETURN_TITLE」の時は        
            if   self.cursor_decision_item_y == 0:           #メニューでアイテムナンバー0の「RETURN」が押されたら
                self.game_playing_flag = FLAG_OFF            #ゲームプレイ中のフラグを降ろす
                self.select_cursor_flag = FLAG_OFF           #セレクトカーソルの移動更新は行わないのでフラグを降ろす
                
                if self.replay_status == REPLAY_RECORD:      #リプレイデータ記録中(ゲームプレイ)中の時は
                    func.write_ship_equip_medal_data(self)                          #機体メダルスロット装備リストに現在プレイ中のシップリストのメダル情報を書き込む関数の呼び出し
                    update_system.save_data(self)                                   #システムデータをセーブする関数の呼び出し
                    update_score.recoard_score_board(self)                          #スコアボードに点数書き込み
                    update_score.score_board_bubble_sort(self,self.game_difficulty) #現在選択している難易度を引数として書き込んだスコアデータをソートする関数の呼び出し
                
                self.game_over_bgm.fadeout(1200)                     #GAME OVER BGMフェードアウト開始
                self.game_status = Scene.TITLE_INIT            #ゲームステータスを「SCENE_TITLE_INIT」にしてタイトルの初期化工程にする
                
            elif self.cursor_decision_item_y == 1:             #メニューでアイテムナンバー1の「SAVE & RETURN」が押されたら
                update_window.create_replay_data_slot_select(self)           #リプレイデータファイルスロット選択ウィンドウの表示
                self.cursor_type = CURSOR_TYPE_NORMAL               #選択カーソル表示をonにする
                self.cursor_move_direction = CURSOR_MOVE_UD         #カーソルは上下移動のみ
                self.cursor_x = 67                                  #セレクトカーソルの座標を設定します
                self.cursor_y = 55
                self.cursor_step_x = 4                              #横方向の移動ドット数は4ドット
                self.cursor_step_y = 7                              #縦方向の移動ドット数は7ドット
                self.cursor_item_y = 0                              #いま指示しているアイテムナンバーは0の「1」
                self.cursor_decision_item_y = UNSELECTED            #まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
                self.cursor_max_item_y = 6                          #最大項目数は「1」「2」「3」「4」「5」「6」「7」の7項目なので 7-1=6を代入
                self.cursor_menu_layer = 0                          #メニューの階層は最初は0にします
                self.active_window_id = WINDOW_ID_SELECT_FILE_SLOT  #このウィンドウIDを最前列でアクティブなものとする
                self.game_status = Scene.SELECT_SAVE_SLOT    #ゲームステータスを「SCENE_SELECT_SAVE_SLOT」にしてセーブスロット選択にする
                
                self.game_over_bgm.fadeout(3000)                    #GAME OVER BGMフェードアウト開始
        
        if self.game_status == Scene.SELECT_SAVE_SLOT:       #「SCENE_SELECT_SAVE_SLOT」の時
            if self.cursor_decision_item_y != UNSELECTED:          #決定ボタンが押されたら
                self.replay_slot_num = self.cursor_decision_item_y #スロット番号は決定ボタンを押した時点でのアイテムy座標値とする
                self.game_playing_flag = FLAG_OFF                  #ゲームプレイ中のフラグを降ろす
                self.select_cursor_flag = FLAG_OFF                 #セレクトカーソルの移動更新は行わないのでフラグを降ろす
                
                func.write_ship_equip_medal_data(self)                          #機体メダルスロット装備リストに現在プレイ中のシップリストのメダル情報を書き込む関数の呼び出し
                update_system.save_data(self)                                   #システムデータをセーブする関数の呼び出し
                update_score.recoard_score_board(self)                          #スコアボードに点数書き込み
                update_score.score_board_bubble_sort(self,self.game_difficulty) #現在選択している難易度を引数として書き込んだスコアデータをソートする関数の呼び出し
                
                update_replay.push_list_data(self)          #録画したリプレイデータを登録します
                
                update_replay.data_file_save(self)          #リプレイデータファイルのセーブ
                
                self.replay_recording_data = []            #録画したリプレイデータは登録したので元のデータは消去します
                self.replay_mode_stage_data_backup = self.replay_mode_stage_data #各ステージ開始時のデータ履歴をバックアップ
                self.game_status = Scene.TITLE_INIT        #ゲームステータスを「SCENE_TITLE_INIT」にしてタイトルの初期化工程にする
        
        #########ステージクリア後の処理#############################################################
        if self.game_status == Scene.STAGE_CLEAR_FADE_OUT:   #「SCENE_STAGE_CLEAR_FADE_OUT」の時は
            if self.fade_complete_flag == FLAG_ON:           #フェードアウト完了のフラグが建ったのなら
                self.stage_number += 1    #ステージ数を1増やす
                self.replay_stage_num += 1#リプレイ再生記録用のステージ数も1増やします
                if self.replay_stage_num > 50:            #リプレイ記録用のファイルは50ステージ分しか今の所用意していないので
                    self.replay_status = REPLAY_STOP      #リプレイの記録はストップさせるようにします
                    self.replay_stage_num = 50            #念のため記録ステージ数は最高の50で丸めておきます
                
                if self.stage_number > STAGE_NIGHT_SKYSCRAPER: #ステージ4 夜間超高層ビル地帯以降のステージはまだ未完成なので・・・
                    self.stage_number = STAGE_MOUNTAIN_REGION   #ステージ1 山岳地帯に戻してやります
                    self.stage_loop += 1     #ループ数を1増やします
                    if self.stage_loop >= 4: #4周目以降は作っていないので\\\
                        self.stage_loop = 1  #1周目に戻ります
                
                self.game_status = Scene.STAGE_START_INIT    #ゲームステータスを「STAGE_START_INIT」にして次のステージへ・・・・
        
        #########ゲーム終了工程開始#################################################################
        if self.game_status == Scene.GAME_QUIT_START:    #「GAME QUIT START」の時は
            self.star_scroll_speed = 1                   #星のスクロールスピードを倍率1に戻す
            self.select_cursor_flag = FLAG_OFF           #セレクトカーソル移動フラグを降ろす
            self.cursor_type = CURSOR_TYPE_NO_DISP       #セレクトカーソルの表示をoffにする
            pygame.mixer.music.fadeout(4000)
            pyxel.playm(4)                               #ゲーム終了音楽再生
            self.game_quit_timer = 420                   #終了タイマーセット(420フレーム=7秒)
            self.game_status = Scene.GAME_QUIT_WAIT
            
        elif self.game_status == Scene.GAME_QUIT_WAIT:   #「GAME QUIT WAIT」の時は
            self.star_scroll_speed -= 0.003              #ゲーム終了時は星のスクロールスピードの倍率を毎フレームごと0.003減らしていく
            if self.star_scroll_speed < 0:
                self.star_scroll_speed = 0               #0以下になったら強制的に0を代入
            
            self.game_quit_timer -= 1                    #終了タイマーデクリメント
            if self.game_quit_timer <=0:                 #タイマーが0以下になったら
                self.game_status = Scene.GAME_QUIT       #「GAME QUIT」にする
            
        elif self.game_status == Scene.GAME_QUIT:        #「GAME QUIT」の時は
            func.write_ship_equip_medal_data(self)       #機体メダルスロット装備リストに現在プレイ中のシップリストのメダル情報を書き込む関数の呼び出し
            update_system.save_data(self)                #システムデータをセーブします
            pyxel.quit()                                 #ゲーム終了！！！！！！！！！！！！！！！！！！！！！！！！！！
        
        ################################ ゲーム終了工程時の処理 ###################################################################
        if self.game_status == Scene.GAME_QUIT_START or self.game_status == Scene.GAME_QUIT_WAIT:
            update_obj.append_star(self)      #背景の星の追加＆発生育成関数呼び出し
            update_obj.star(self)             #背景の星の更新（移動）関数呼び出し
            update_window.window(self)        #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)   #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self) #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
        
        ####################ゲームプレイ中のフラグが立っていたのなら以下の処理を行う(主にゲーム進行に関与しない映像処理関連)################
        if self.game_playing_flag  == FLAG_ON: #ゲームプレイ中のフラグが立っていたのならば
            update_debug.debug_status(self)    #デバッグステータス表示＆非表示の切り替え
            #映像オブジェクト関連の処理################################################################################################
            update_obj.append_star(self)       #背景の星の追加＆発生育成関数呼び出し
            update_obj.append_cloud(self)      #背景の雲の追加＆発生育成関数呼び出し
            update_obj.star(self)              #背景の星の更新（移動）関数呼び出し
            update_obj.particle(self)          #パーティクルの更新関数呼び出し
            update_obj.background_object(self) #背景オブジェクトの更新関数の呼び出し
            update_obj.building_object(self)   #建物オブジェクトの更新関数の呼び出し
            update_obj.explosion(self)         #爆発パターンの更新関数呼び出し 
            #一時停止(pause)の処理###################################################################################################
            update_btn.pause_btn(self)         #ポーズボタンが押されたらポーズをかける関数を呼び出し
            #ウィンドウ＆メニューカーソル関連の処理###############################################################################################
            update_window.window(self)        #ウィンドウの更新（ウィンドウの開き閉じ画面外に消え去っていくとか）関数を呼び出し
            update_window.clip_window(self)   #画面外にはみ出たウィンドウを消去する関数の呼び出し
            update_window.active_window(self) #現在アクティブ(最前面)になっているウィンドウのインデックス値(i)を求める関数の呼び出し
        
        if self.select_cursor_flag == FLAG_ON: #セレクトカーソルを動かすフラグが立っているのならカーソルの移動更新を行う
            update_window.select_cursor(self)  #セレクトカーソルでメニューを選択する関数を呼び出す

    ###########################################################
    ###########################################################
    ###########################################################
    # ゲーム内での描画処理を行う            どろ～～☆彡       #
    ###########################################################
    ###########################################################
    ###########################################################
    def draw(self):
        pyxel.cls(self.bg_cls_color)                #背景を指定色で消去する(初期値は0なので真っ黒になります)
        if self.game_status == Scene.IPL:
            graph.draw_ipl(self)                    #IPLメッセージを表示する関数の呼び出し
        
        if     self.game_status == Scene.TITLE_FIRST\
            or self.game_status == Scene.TITLE_HIT_ANY_BTN\
            or self.game_status == Scene.TITLE_SECOND\
            or self.game_status == Scene.TITLE_MENU_SELECT\
            or self.game_status == Scene.SELECT_LOAD_SLOT\
            or self.game_status == Scene.GAME_QUIT_START\
            or self.game_status == Scene.GAME_QUIT_WAIT\
            or self.game_status == Scene.GAME_QUIT:
            
            graph.draw_star(self)                          #背景の星を表示する関数の呼び出し
            graph.draw_visualscene(self,WINDOW_PRIORITY_TITLE_BACK)                     #タイトルより奥にあるビジュアルシーンを表示する
            graph.draw_window(self,WINDOW_PRIORITY_TITLE_BACK,   ORDINARY_SUPERPOSITION)#タイトルより奥にあるウィンドウをそのまま重ね合わせて表示する
            
            #ゲームプレイ中からの終了工程の場合はタイトルロゴを表示しない
            if  self.game_quit_from_playing == FLAG_OFF:
                graph.draw_title(self)                     #タイトルロゴの表示関数の呼び出し
            
            graph.draw_window(self,WINDOW_PRIORITY_NORMAL,BLACK_RECTANGLE_FILL)  #透明のウィンドウの場合は黒矩形塗りつぶししたあと表示
            graph.redraw_star(self)                                              #透明または半透明のウィンドウが存在する範囲内だけ星を再描画する
            graph.draw_window(self,WINDOW_PRIORITY_NORMAL,ORDINARY_SUPERPOSITION)#そのまま普通に重ね合わせてウィンドウを表示
            
            graph.draw_window(self,WINDOW_PRIORITY_TOP,   BLACK_RECTANGLE_FILL)  #最前面ウィンドウの黒抜き部分を表示する
            graph.redraw_star_priority_top(self)                                 #最前面のウィンドウ背後の部分に星を描画する
            graph.draw_window(self,WINDOW_PRIORITY_TOP,   ORDINARY_SUPERPOSITION)#最前面ウィンドウをそのまま重ね合わせて表示する
            
            graph.draw_select_cursor(self)                             #セレクトカーソルの表示関数の呼び出し
        
        if self.game_playing_flag == FLAG_ON and self.star_scroll_flag == FLAG_ON:#ゲームプレイ中フラグon,星スクロールフラグonの時は背景の星を表示する
            graph.draw_star(self)                  #背景の星を表示する関数の呼び出し 
        
        if     self.game_status == Scene.PLAY\
            or self.game_status == Scene.BOSS_APPEAR\
            or self.game_status == Scene.BOSS_BATTLE\
            or self.game_status == Scene.BOSS_EXPLOSION\
            or self.game_status == Scene.EXPLOSION\
            or self.game_status == Scene.STAGE_CLEAR\
            or self.game_status == Scene.STAGE_CLEAR_MOVE_MY_SHIP\
            or self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status == Scene.STAGE_CLEAR_FADE_OUT\
            or self.game_status == Scene.GAME_OVER\
            or self.game_status == Scene.GAME_OVER_FADE_OUT\
            or self.game_status == Scene.PAUSE:
            
            #一番奥の背景の表示
            if   self.stage_number == STAGE_MOUNTAIN_REGION:
                ####################背景表示
                ###################pyxel.bltm(-(pyxel.frame_count // 8),0,0,((pyxel.frame_count / 2) - 160) ,0,160,120,0)最初はこれで上手くいかなかった・・・・なぜ？
                ###################奥の背景表示
                ###################pyxel.bltm(-(pyxel.frame_count // 4) + 400,0,0,0,16,256,120,0)
                
                #雲ウェーブラスタースクロールの表示
                graph.draw_raster_scroll(self,PRIORITY_SEND_TO_BACK)  #ラスタースクロール描画関数呼び出し 山より奥で描画します
                
                #奥の雲スクロールの表示
                if self.disp_flag_bg_back == DISP_ON:
                    # pyxel.bltm(-int(self.scroll_count  // 10 % (256*8 - 160)),-(self.vertical_scroll_count // 28) + 97,  1,    0,235,    256,7,    1)
                    pyxel.bltm(-int(self.scroll_count  // 10 % (256*8 - 160)),-(self.vertical_scroll_count // 28) + 97,  TM1,    0*8,235*8,    256*8,7*8,    1)
                #影が強めの奥の山を描画
                if self.disp_flag_bg_middle == DISP_ON:
                    # pyxel.bltm(-int(self.scroll_count  // 8  % (256*8 - 160)),-(self.vertical_scroll_count // 24) + 116,  1,    0,243,    256,5,    self.bg_transparent_color)
                    pyxel.bltm(-int(self.scroll_count  // 8  % (256*8 - 160)),-(self.vertical_scroll_count // 24) + 116,  TM1,    0*8,243*8,    256*8,5*8,    self.bg_transparent_color)
                #手前の小さめの山を描画
                if self.disp_flag_bg_front == DISP_ON:
                    # pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  1,    0,248,    256,5,    self.bg_transparent_color)
                    pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  TM1,    0*8,248*8,    256*8,5*8,    self.bg_transparent_color)
                
                #湖面のラスタースクロールの表示、成層圏と大気圏の境目のラスタースクロールの表示
                graph.draw_raster_scroll(self,PRIORITY_BACK)  #ラスタースクロール描画関数呼び出し 山より手前で描画しますっ！
            elif self.stage_number == STAGE_ADVANCE_BASE:
                # pyxel.bltm(-(self.scroll_count // 8) + 250,0,0,0,240,256,120,self.bg_transparent_color)
                pyxel.bltm(-(self.scroll_count // 8) + 250,0,TM0,  0*8,240*8,  256*8,120*8,self.bg_transparent_color)
            elif self.stage_number == STAGE_VOLCANIC_BELT:
                #火山湖面ウェーブラスタースクロールの表示
                graph.draw_raster_scroll(self,PRIORITY_SEND_TO_BACK)  #ラスタースクロール描画関数呼び出し背景一番奥の火山の真下で描画します
                #火山上
                pyxel.bltm(-(self.scroll_count // 16) + 50,0                         ,TM2,  0*8,216*8   ,  256*8, 15*8,0)
                #火山下
                pyxel.bltm(-(self.scroll_count // 8) + 100,-self.camera_offset_y // 8,TM2,  0*8,239*8 -2,  256*8,120*8,0)
                
                #カメラオフセット値を計算する
                self.camera_offset_y = (self.bg_height - WINDOW_H) * self.my_y / (self.bg_height - SHIP_H) #SHIP_Hは自機の縦幅8ドット
                #最上部積層雲の描画
                pyxel.bltm(-((self.scroll_count // 6) % 256),14 ,TM2,  0*8,208*8   + self.camera_offset_y // 5,  256*8, 1*8 + 12,pyxel.COLOR_BLACK) #上の方
                pyxel.bltm(-((self.scroll_count // 4) % 256),8  ,TM2,  0*8,208*8   + self.camera_offset_y // 4,  256*8, 1*8 + 8 ,pyxel.COLOR_BLACK)
                pyxel.bltm(-((self.scroll_count // 3) % 256),4  ,TM2,  0*8,208*8   + self.camera_offset_y // 3,  256*8, 1*8 + 4 ,pyxel.COLOR_BLACK)
                pyxel.bltm(-((self.scroll_count // 2) % 256),2  ,TM2,  0*8,208*8   + self.camera_offset_y // 3,  256*8, 1*8 + 3 ,pyxel.COLOR_BLACK)
                pyxel.bltm(-((self.scroll_count )     % 256),0  ,TM2,  0*8,208*8   + self.camera_offset_y // 2,  256*8, 1*8     ,pyxel.COLOR_BLACK) #下の方
            elif self.stage_number == STAGE_NIGHT_SKYSCRAPER:
                # pyxel.bltm(-int(self.scroll_count %(256*8) -160) // 1,0,TM0,  0*8,48*8,  256*8,120*8,self.bg_transparent_color)
                
                #MAPチップx座標(0~19)と(236~255)は同じパターンのマップチップを敷き詰めて背景ループスクロール時不自然にならないようにしてください(横幅20キャラ縦幅15キャラ分)
                # pyxel.bltm(-int(pyxel.frame_count % (256*8 - 160)),-self.vertical_scroll_count,TM0,  0*8,20*8,  256*8,120*8,self.bg_transparent_color)
                pyxel.bltm(-int(self.scroll_count % (256*8 - 160)),-self.vertical_scroll_count,TM0,  0*8,20*8,  256*8,120*8,self.bg_transparent_color)
            
            #真ん中の背景の表示
            if   self.stage_number == STAGE_MOUNTAIN_REGION:
                if self.disp_flag_bg_front == DISP_ON:
                    #pyxel.bltm(-int(self.scroll_count % (256*8 - 160)),     -self.vertical_scroll_count,  1,    0,0,    256,256,    self.bg_transparent_color)
                    pyxel.bltm(-int(self.scroll_count % (256*8 - 160)),     -self.vertical_scroll_count,  TM1,    0*8,0*8,    256 * 8,256 * 8,    self.bg_transparent_color)
            elif self.stage_number == STAGE_ADVANCE_BASE:
                # pyxel.bltm(-(self.scroll_count // 4) + 400,0,0,0,224,256,120,self.bg_transparent_color)
                pyxel.bltm(-(self.scroll_count // 4) + 400,0,TM0,   0*8,224*8, 256*8,120*8,self.bg_transparent_color)
            elif self.stage_number == STAGE_VOLCANIC_BELT:
                pyxel.bltm(-(self.scroll_count // 4) + 400,-self.camera_offset_y // 4,TM2,   0*8, 76*8, 256*8,120*8,    self.bg_transparent_color)
            
            graph.draw_background_object(self)               #背景オブジェクトの描画関数の呼び出し
            
            #建物の表示 奥ビル----------------------------------------------------------------------------
            graph.draw_building_object_individual(self,3)    #建物オブジェクトの描画関数の呼び出し   奥ビル
            #建物の表示 中ビル------------------------------------------------------------------------------
            graph.draw_building_object_individual(self,2)    #建物オブジェクトの描画関数の呼び出し   中ビル
            #建物の表示 前ビル------------------------------------------------------------------------------
            graph.draw_building_object_individual(self,1)    #建物オブジェクトの描画関数の呼び出し   前ビル
            
            graph.draw_enemy_shot(self,PRIORITY_BOSS_BACK)   #敵の弾を表示する関数を呼び出す(ボスキャラの真後ろ)---------------------------
            graph.draw_boss(self)                            #ボスを表示する関数を呼び出す
            graph.draw_boss_hp(self)                         #ボスの耐久力を表示する関数を呼び出す
            graph.draw_enemy_shot(self,PRIORITY_BOSS_FRONT)  #敵の弾を表示する関数を呼び出す(ボスキャラのすぐ手前)-------------------------
            
            graph.draw_obtain_item(self)                     #パワーアップアイテム類の表示
            
            graph.draw_enemy(self)                           #敵を表示する関数を呼び出す
            graph.draw_enemy_shot(self,PRIORITY_FRONT)       #敵の弾を表示する関数を呼び出す (前面)---------------------------------------
            graph.draw_enemy_shot(self,PRIORITY_MORE_FRONT)  #敵の弾を表示する関数を呼び出す (敵弾の中でもさらに前面)-----------------------
            
            graph.draw_particle(self,PRIORITY_FRONT)         #パーティクルを表示する関数の呼び出し(前面)
            
            graph.draw_my_shot(self)      #自機弾の表示
            graph.draw_missile(self)      #ミサイルの表示
            graph.draw_claw_shot(self)    #クローショットの表示
            
            #手前の背景表示
            if   self.stage_number == STAGE_ADVANCE_BASE:
                #結局なんでこれでキチンとスクロール表示されたのか謎・・・結局はじめは-1024ドットのx座標位置からスクロール開始していくことに・・
                #pyxel.bltm(-(pyxel.frame_count // 2) + 1024,0,0,0,0,256,120,0)
                if   self.stage_loop == 1:
                    # pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,    0,0,    256,120,    self.bg_transparent_color) #1周目マップ
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM0,    0*8,0*8,    256*8,120*8,    self.bg_transparent_color) #1周目マップ
                elif self.stage_loop == 2:
                    # pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,    0,16,   256,120,    self.bg_transparent_color) #2周目マップ
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM0,    0*8,16*8,   256*8,120*8,    self.bg_transparent_color) #2周目マップ
                elif self.stage_loop == 3:
                    # pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,    0,32,   256,120,    self.bg_transparent_color) #3周目マップ
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM0,    0*8,32*8,   256*8,120*8,    self.bg_transparent_color) #3周目マップ
            elif self.stage_number == STAGE_VOLCANIC_BELT:
                #カメラオフセット値を計算する
                self.camera_offset_y = (self.bg_height - WINDOW_H) * self.my_y / (self.bg_height - SHIP_H) #SHIP_Hは自機の縦幅8ドット
                #当たり判定アリの実地形を描画する
                if   self.stage_loop == 1:
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM2,    0*8,0*8  + self.camera_offset_y,   256*8,120*8,    self.bg_transparent_color) #1周目マップ
                elif self.stage_loop == 2:
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM2,    0*8,32*8 + self.camera_offset_y,   256*8,120*8,    self.bg_transparent_color) #2周目マップ
                elif self.stage_loop == 3:
                    pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  TM2,    0*8,64*8 + self.camera_offset_y,   256*8,120*8,    self.bg_transparent_color) #3周目マップ
            
            graph.draw_enemy_shot(self,PRIORITY_TOP)        #敵の弾を表示する関数を呼び出す (最前面)-------------------------------------
        
        #自機、クロー、シールドの表示###############################################
        if     self.game_status == Scene.PLAY\
            or self.game_status == Scene.BOSS_APPEAR\
            or self.game_status == Scene.BOSS_BATTLE\
            or self.game_status == Scene.BOSS_EXPLOSION\
            or self.game_status == Scene.STAGE_CLEAR\
            or self.game_status == Scene.STAGE_CLEAR_MOVE_MY_SHIP\
            or self.game_status == Scene.STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status == Scene.STAGE_CLEAR_FADE_OUT\
            or self.game_status == Scene.PAUSE:
            
            graph.draw_my_ship(self)     #自機の表示
            graph.draw_claw(self)        #クローの表示
            graph.draw_ls_shield(self)   #Ｌ'sシールドシステムの表示
        
        #「ゲームプレイ中」フラグが立っている時は爆発パターンを表示する################################
        if self.game_playing_flag == FLAG_ON:              #「ゲームプレイ中」の時は爆発パターン表示
            graph.draw_explosion(self,PRIORITY_FRONT)      #爆発パターン(前面)の表示
            graph.draw_explosion(self,PRIORITY_MORE_FRONT) #爆発パターン(さらに前面)の表示
            graph.draw_particle(self,PRIORITY_MORE_FRONT)  #パーティクルを表示する関数の呼び出し(パーティクルの中でも更に前面)
            
            #建物の表示 すべてのオブジェクトよりも前に表示される建物を表示----------------------------------------------------
            graph.draw_building_object_individual(self,0)               #建物オブジェクトの描画関数の呼び出し  めっちゃ手前ビル
        
        #フェードアウトスクリーンの表示###############################################
        if    self.game_status == Scene.GAME_OVER_FADE_OUT\
            or self.game_status == Scene.STAGE_CLEAR_FADE_OUT:
            
            # self.draw_fade_in_out_screen(FADE_OUT,0)        #フェードイン＆フェードアウト用のエフェクトスクリーンの描画表示
            graph.draw_vertical_fade_in_screen(self)        #フェードイン＆フェードアウト用のエフェクトスクリーンの描画表示
        
        #画面中央80ドットだけ表示する処理###########################################
        if    self.game_status == Scene.GAME_OVER_SHADOW_IN\
            or self.game_status == Scene.GAME_OVER_STOP\
            or self.game_status == Scene.RETURN_TITLE:
            
            graph.draw_shadow_out_screen(self,40,0)  #中央付近80ドット分だけ残してシャドウアウトする
        
        if self.game_playing_flag == FLAG_ON:              #「ゲームプレイ中」の時は以下の処理も行う
            graph.draw_sub_weapon_select_guidebox(self)    #選択中のサブウェポンのカーソルガイドボックスの表示
            graph.draw_sub_weapon_select_gauge(self)       #サブウェポン一覧表示graph
            graph.draw_status(self)                        #スコアやスピード、自機耐久力などの表示関数の呼び出し （通常ステータス表示）
            graph.draw_debug_status(self)                  #デバッグ用ステータスの表示関数の呼び出し          （デバック用ステータス表示）
            
            #1回目「黒矩形塗りつぶし」したあとウィンドウ表示
            graph.draw_window(self,WINDOW_PRIORITY_NORMAL,BLACK_RECTANGLE_FILL) #ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_5,     BLACK_RECTANGLE_FILL) #前面から6番目のウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_4,     BLACK_RECTANGLE_FILL) #前面から5番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_3,     BLACK_RECTANGLE_FILL) #前面から4番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_2,     BLACK_RECTANGLE_FILL) #前面から3番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_1,     BLACK_RECTANGLE_FILL) #前面から2番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_TOP,   BLACK_RECTANGLE_FILL) #最前面1番目ウィンドウの表示
            
            graph.redraw_star(self)                                   #透明または半透明のウィンドウが存在する範囲内だけ星を再描画する
            #2回目 そのまま普通に重ね合わせてウィンドウ表示
            graph.draw_window(self,WINDOW_PRIORITY_NORMAL,ORDINARY_SUPERPOSITION) #前面ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_5,     ORDINARY_SUPERPOSITION) #前面から6番目のウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_4,     ORDINARY_SUPERPOSITION) #前面から5番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_3,     ORDINARY_SUPERPOSITION) #前面から4番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_2,     ORDINARY_SUPERPOSITION) #前面から3番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_1,     ORDINARY_SUPERPOSITION) #前面から2番目ウィンドウの表示
            graph.draw_window(self,WINDOW_PRIORITY_TOP,   ORDINARY_SUPERPOSITION) #最前面1番目ウィンドウの表示
            
            graph.draw_select_cursor(self)                 #セレクトカーソルの表示graph
            graph.draw_warning_dialog(self)                #WARNINGダイアログの表示
            graph.draw_stage_clear_dialog(self)            #STAGE CLEARダイアログの表示
            
            # self.draw_dummy_put_bg_xy()  #BG Get&Put dummy test
        
        #一時停止・ポーズメッセージの表示#########################################
        if self.game_status == Scene.PAUSE:
            graph.draw_pause_message(self)            #一時停止・ポーズメッセージの表示
        
        # #タイトルメッセージテキストの表示#########################################
        # if self.game_status == Scene.TITLE_HIT_ANY_BTN:
        #     graph.draw_title_message(self)            #タイトルメッセージテキストの表示
        
        #ゲームオーバーダイアログの表示##################################################
        if     self.game_status == Scene.GAME_OVER\
            or self.game_status == Scene.GAME_OVER_FADE_OUT\
            or self.game_status == Scene.GAME_OVER_SHADOW_IN\
            or self.game_status == Scene.GAME_OVER_STOP\
            or self.game_status == Scene.RETURN_TITLE:
            graph.draw_gameover_dialog(self)          #ゲームオーバーダイアログを表示をする関数呼び出し
App()