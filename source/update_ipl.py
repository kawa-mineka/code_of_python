################################################################
#  update_iplクラス                                             #      
################################################################
#  Appクラスのupdate関数から呼び出される関数群                    #
#  主にIPLメッセージ表示関連の更新を行う関数(メソッド？）ですよ～♪  #
# 2022 04/06からファイル分割してモジュールとして運用開始           #
###############################################################
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

class update_ipl:
    def __init__(self):
        None

    #IPLの更新#######################################
    def ipl(self):
        self.display_ipl_time -= 1    #IPLメッセージを表示する時間カウンターを1減らす
        if self.display_ipl_time <= 0: #カウンターが0以下になったら・・・
            self.game_status = SCENE_TITLE_INIT #ゲームステータスを「SCENE_TITLE_INIT(タイトル表示に必要な変数を初期化)」にする
        
        if (pyxel.frame_count % 10) == 0:
            if len(self.ipl_mes1) > self.ipl_mes_write_line_num: #まだ書き込むべき文字列があるのなら・・・
                text_mes = str(self.ipl_mes1[self.ipl_mes_write_line_num][0])
                text_col = str(self.ipl_mes1[self.ipl_mes_write_line_num][1])
                self.text_screen.append([text_mes,text_col]) #文字列群をテキストスクリーンのリストに追加する
                self.ipl_mes_write_line_num +=1  #スクリーンに表示したIPLメッセージデータの行数カウンタを1インクリメント
