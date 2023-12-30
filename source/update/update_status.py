###########################################################
#  update_statusクラス                                     #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にメインメニューのステータスで表示される項目関連の        #
#  数値を更新する関数(メソッド？？？？？)                    #
#                                                         #
# 2022 04/07からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func  import * #汎用性のある関数群のモジュールの読み込み

class update_status:
    #プレイ時間の計算処理を行う
    def calc_playtime(self):
        self.playtime_frame_counter += 1         #フレームカウンターをインクリメント
        if self.playtime_frame_counter >= 60:     #フレームカウンターが60以上になったら
            self.playtime_frame_counter = 0      #フレームカウンターをリセットして
            self.one_game_playtime_seconds   += 1 #1プレイタイムを1秒増加させる
            if self.replay_status != REPLAY_PLAY: #リプレイ再生している時は総ゲームプレイ時間は加算しない
                self.total_game_playtime_seconds += 1 #総ゲームプレイ時間も1秒増加させる

    #1プレイタイムを見てランクを上昇させる
    def rank_up_look_at_playtime(self):
        if (pyxel.frame_count % self.rank_up_frame) == 0:
            if self.rank < self.rank_limit: #ランク数がランク上限限界値より小さいのなら
                self.rank += 1      #ランク数をインクリメント
                func.get_rank_data(self) #ランク数が変化したのでランク数をもとにしたデータをリストから各変数に代入する関数の呼び出し

    #乱数0_9関数(0~9)の更新
    def rnd0_9(self):
        self.rnd0_9_num  = pyxel.frame_count %  10 #フレームカウント数を 10で割った余りが変数rnd0_9_numに入ります(0~9の数値が1フレームごとに変化する)

    #乱数099関数(0~999)の更新
    def rnd0_99(self):
        self.rnd0_99_num = pyxel.frame_count % 100 #フレームカウント数を100で割った余りが変数rnd0_99_numに入ります(0~99の数値が1フレームごとに変化する)
