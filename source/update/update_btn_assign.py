###########################################################
#  update_btn_assignクラス                                 #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  パッド割り当ての更新を行うメソッド                        #
#  各ボタンに色々な機能を割り当てる処理を行うボタン           #
#  つまりキーコンフィグって事です、ハイ                      #
#                                                         #
# 2022 10/22からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func  import * #汎用性のある関数群のモジュールの読み込み

from update.update_obj  import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update.update_ship import * #自機関連更新関数モジュール読み込み

class update_btn_assign:
    def __init__(self):
        None

    #パッドアサインリストを更新する
    #btn_id    = ボタンID     = 機能を割り当てるボタンのIDナンバー
    #action_id = アクションID = 割り当てる機能(アクション)のIDナンバー
    def list(self,btn_id,action_id):
        """
        パッドアサインリストを更新する
        btn_id    = ボタンID     = 機能を割り当てるボタンのIDナンバー
        action_id = アクションID = 割り当てる機能(アクション)のIDナンバー
        """
        # print("ボタンID "     + str(btn_id))
        # print("アクションID " + str(action_id))
        # print("")
        # print("同じアクションを持つボタンID は " + str(update_btn_assign.check_action_id(self,action_id)))
        # print("")
        btn_id1 = btn_id
        btn_id2 = update_btn_assign.check_action_id(self,action_id) #同じアクションを持つボタンIDを調べそのボタンIDをbtn_id2に入れる
        if btn_id2 == -1: #同じアクションIDを持つボタンが存在しない場合は
            #そのまま登録する
            self.pad_assign_list[btn_id] = action_id #ボタンIDの所にアクションIDを書き込む
        else:
            #それぞれのボタンIDに登録されているアクションIDを読み出す
            action_id1 = self.pad_assign_list[btn_id1]
            action_id2 = self.pad_assign_list[btn_id2]
            #アクションIDを入れ替える
            self.pad_assign_list[btn_id1] = action_id2 #ボタンID1の所にアクションID2を書き込む
            self.pad_assign_list[btn_id2] = action_id1 #ボタンID2の所にアクションID2を書き込む これでアクションIDが入れ替わる

    #パッドアサインリストにアクションIDが既に存在するか調べる関数
    #action_id = アクションID = 割り当てる機能(アクション)のIDナンバー
    #返り値は=存在したbtn_idを返します 存在しなかった場合は -1を返します
    def check_action_id(self,action_id):
        """
        パッドアサインリストにアクションIDが既に存在するか調べる関数
        action_id = アクションID = 割り当てる機能(アクション)のIDナンバー
        返り値は=存在したbtn_idを返します 存在しなかった場合は -1を返します
        """
        list_count = len(self.pad_assign_list) #list_countにpad_assign_listの長さが入る
        for i in range (list_count): #pad_assign_listの長さの回数だけループして調べ上げる
            dat = self.pad_assign_list[i] #どの様なボタンIDが割り当てられているか取り出す
            if dat == action_id: #同じアクションIDを見つけたのなら
                return(i) #iであるインデックス値がbtn_idとなるので iの値を返す
        
        return(-1) #ループをすべて周って調べ上げても見つからなかった時は-1を返します

