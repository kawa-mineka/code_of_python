###########################################################
#  scoreクラス                                             #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  スコア加算の更新を行うメソッド                            #
#                                                         #
# 2022 04/07からファイル分割してモジュールとして運用開始      #
###########################################################
# import math                  #三角関数などを使用したいのでインポートぉぉおお！
# from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
# import pyxel                 #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
# from common.func  import *   #汎用性のある関数群のモジュールの読み込み
from const.const import *      #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class score:
    #スコア加算処理
    def add_score(self,point):
        """
        スコア加算処理
        
        point=取得得点
        """
        self.score += int(point * self.score_magnification) #スコアをpoint*スコア倍率分加算する(整数値で)

    #ハイスコアのチェックを行う関数
    def check_hi_score(self):
        """
        ハイスコアのチェックを行う関数
        """
        if self.score > self.hi_score: #スコアがハイスコアより大きければ
            self.hi_score = self.score #ハイスコアにスコアを代入する

    #スコアボードへの書き込み ランク外である11位にスコアを書き込む関数(スコアボードは10位までしか表示されないのでこの状態では表示されませんバブルソートしてね)
    def recoard_score_board(self):
        """
        スコアボードへの書き込み ランク外である11位にスコアを書き込む関数(スコアボードは10位までしか表示されないのでこの状態では表示されませんバブルソートしてね)
        """
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_NAME]        = self.my_name
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SCORE]       = self.score
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_LOOP]        = self.stage_loop
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_CLEAR_STAGE] = self.stage_number
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_USED]   = self.my_ship_id
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT0]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT1]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT1]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT2]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT2]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT3]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT3]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT4]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT4]
        self.score_board[self.game_difficulty][11-1][LIST_SCORE_BOARD_SHIP_SLOT5]  = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT5]

    #スコアボードの点数によるバブルソート 11位に今プレイしたゲームの得点を書き込みその後この関数を呼び出し→順位の11がどの位置に移動したかチェック→その位置にカーソル移動させてネームエントリー→そしてリストに書き込む
    def score_board_bubble_sort(self,diff): #diffは難易度です
        """
        スコアボードの点数によるバブルソート 11位に今プレイしたゲームの得点を書き込みその後この関数を呼び出し→順位の11がどの位置に移動したかチェック→その位置にカーソル移動させてネームエントリー→そしてリストに書き込む
        """
        for i in range(len(self.score_board[diff])): #ランキングデータは11位までなのでiは0~11まで変化する
            for j in range(len(self.score_board[diff])-1,i,-1):
                if self.score_board[diff][j][LIST_SCORE_BOARD_SCORE] > self.score_board[diff][j-1][LIST_SCORE_BOARD_SCORE]: #位置jの得点より前の位置j-1の得点が大きいのなら要素を入れ替える
                    for k in range(LIST_SCORE_BOARD_SHIP_SLOT5): #難易度からスロット5に装備されたメダルIDまでの12種類の要素をループしてコピー
                        self.score_board[diff][j][k],self.score_board[diff][j-1][k] = self.score_board[diff][j-1][k],self.score_board[diff][j][k]

