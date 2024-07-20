###########################################################
#  medalクラス                                             #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にメダルスロット関連の処理をする関数(メソッド？？？？？)  #
#                                                         #
# 2024 02/11からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const        import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class medal:
    #プレイ中の自機リスト(playing_ship_list)を参照して自機にメダルをはめ込む（装着？）する関数 (num=メダルIDナンバー)
    def equip_medal_playing_ship(self,num):
        """
        プレイ中の自機リスト(playing_ship_list)を参照して自機にメダルをはめ込む（装着？）する
        
        num=メダルIDナンバー
        """
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #既にスロットに同じメダルがはめ込まれていないか調べ上げる
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == num: #これからはめ込むメダルがすでにはめ込まれていたら・・・
                pyxel.play(CH0,20)#カーソル衝突を鳴らしてはめ込まずそのままリターンする
                return          #リターンする
        
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #空きスロットを探す
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_NO_SLOT: #スロットを小さいナンバーの方から調べていって空スロットがあったのなら
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] = num #空きスロットにメダルIDナンバーを書き込みしてはめ込む！
                pyxel.play(CH0,17)#カーソルOK音を鳴らす
                return
        
        pyxel.play(CH0,20)#カーソル衝突音を鳴らす
        return

    #プレイ中の自機リスト(playing_ship_list)を参照して自機からメダルを外す(パージ)する関数(slot_num=自機のスロットナンバー)
    def purge_medal_playing_ship(self,slot_num):
        """
        プレイ中の自機リスト(playing_ship_list)を参照して自機からメダルを外す(パージ)する
        
        slot_num=自機のスロットナンバー
        """
        self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + slot_num] = MEDAL_NO_SLOT #決定ボタンが押された位置のスロットナンバーを空にする
        pyxel.play(CH0,18)#カーソルキャンセル音を鳴らす

    #自機に装備され,はめ込まれたメダルを左詰めにする関数(空きスロットの隙間を詰めて、空きスロットがどれだけあるのか見やすくする関数)
    def playing_ship_medal_left_justified(self):
        """
        自機に装備され,はめ込まれたメダルを左詰めにする(空きスロットの隙間を詰めて、空きスロットがどれだけあるのか見やすくする)
        """
        # start_slot = 0
        for i in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]): #iは0から所持スロットの最大値まで変化していきます
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_NO_SLOT: #これからはめ込む場所が空スロットの場合は・・・一つ右のスロットのメダルと現在のメダルスロットに移動させていく
                for j in range(self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] - i): #jは0から(スロット最大値-i)まで変化していく
                    self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + j + 1] #現在のスロットに一つ右横のスロットのメダルIDをコピーしていく

    #今現在プレイしているシップリスト(playing_ship_list)に機体メダルスロット装備リスト(ship_equip_slot_list)を参照しながら装備メダルの情報を読み込んでいく関数
    def read_ship_equip_medal_data(self):
        """
        今現在プレイしているシップリスト(playing_ship_list)に機体メダルスロット装備リスト(ship_equip_slot_list)を参照しながら装備メダルの情報を読み込んでいく
        """
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.playing_ship_list[i][LIST_SHIP_SLOT0 + j] = self.ship_equip_slot_list[i][j]

    #機体メダルスロット装備リスト(ship_equip_slot_list)に今現在プレイしているシップリスト(playing_ship_list)を参照しながら装備メダルの情報を書き込んでいく関数
    def write_ship_equip_medal_data(self):
        """
        機体メダルスロット装備リスト(ship_equip_slot_list)に今現在プレイしているシップリスト(playing_ship_list)を参照しながら装備メダルの情報を書き込んでいく
        """
        for i in range(LOOK_AT_LOGO):#iは0=J_pythonからLOOK_AT_LOGOまで変化
            for j in range(6):       #jはスロット0からスロット6まで変化
                self.ship_equip_slot_list[i][j] = self.playing_ship_list[i][LIST_SHIP_SLOT0 + j]

    #装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する関数
    def add_medal_effect_shot_bonus(self):
        """
        装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する
        """
        for i in range(6): #iは0から6(SLOT6)まで変化する
            if  self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_1SHOT_ITEM: #事前ショット1アイテムゲットメダルならば
                self.inc_shot_exp_medal += 1                                                                 #ショット経験値を増やす数値を+1する
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_2SHOT_ITEM:
                self.inc_shot_exp_medal += 2
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_3SHOT_ITEM:
                self.inc_shot_exp_medal += 3
            elif self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_BEFOREHAND_4SHOT_ITEM:
                self.inc_shot_exp_medal += 4
        
        self.shot_exp += self.inc_shot_exp_medal #ショット経験値をメダルの効果のぶん加算する

    #装備されたメダルを調べ、L’ｓシールド装備メダルを作動させる関数
    def medal_effect_ls_shield(self):
        """
        装備されたメダルを調べ、L’ｓシールド装備メダルを作動させる
        """
        for i in range(6): #iは0(SLOT0)から6(SLOT6)まで変化する
            if  self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_EQUIPMENT_LS_SHIELD: #L’ｓシールド装備メダルならば
                self.ls_shield_hp = 10                                                                     #L'sシールドの耐久力を10にする

    #装備されたメダルを調べ、スロット数を拡張するメダルがあればスロット数を増やし、何も無ければスロット数を初期状態にする関数
    def medal_effect_plus_medallion(self):
        """
        装備されたメダルを調べ、スロット数を拡張するメダルがあればスロット数を増やし、何も無ければスロット数を初期状態にする
        """
        for i in range(6): #iは0(SLOT0)から6(SLOT6)まで変化する
            if self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i] == MEDAL_PLUS_MEDALLION: #スロット増加メダルならば・・・
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_INIT_SLOT_NUM] + 2 #空きスロット増加メダルは初期総スロット数＋2つ分空きスロットに増やす
                return
            else:
                self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM] = self.playing_ship_list[self.my_ship_id][LIST_SHIP_INIT_SLOT_NUM] #現在の総スロット数は初期スロット数とする

    #現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする関数
    #例 LIST_SHIP_SLOT_NUMの数値である「総スロット数」が2だったらSLOT0からSLOT1までは使用するのでそのままにして,SLOT2からSLOT6までゼロクリアする
    #現時点での確保しているスロット数は7
    def zero_clear_out_of_range_slot(self):
        """
        現在の総メダルスロット以上のスロット部分をゼロクリアしてメダルなし状態にする
        """
        st = self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]
        for i in range(7 - self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT_NUM]):
            self.playing_ship_list[self.my_ship_id][LIST_SHIP_SLOT0 + i + st] = MEDAL_NO_SLOT
