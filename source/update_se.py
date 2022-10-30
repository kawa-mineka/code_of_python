###########################################################
#  update_seクラス                                         #      
###########################################################
# 効果音(SE)を出すクラスメソッド                            #
# 2022 10/22からファイル分割してモジュールとして運用開始      #
###########################################################
import pyxel        #効果音(SE)再生時に使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class update_se:
    def __init__(self):
        None

    #各効果音のVOLのリストを原本として保存しておくメソッド
    def backup_se_vol_list(self):
        for i in range(62): #sndは(0~62)まであるので iを0~62まで増加させていく
            vol_list = ""   #ボリュームリストを初期化する
            vol_len = len(pyxel.sound(i).volumes) #vol_lenにsnd(i)のVOL値が記録された全体の個数が入る
            print("SOUND " + str(i))
            for j in range(vol_len): #vol_lenの数だけ繰り返す
                num = pyxel.sound(i).volumes[j] #VOLの数値を取り出す(型は整数で収まっている)
                print(num,end = '') #改行無しで数値を表示
                vol_list += str(num)#ボリュームリストに文字列化したボリューム値を右端に追加していく
            
            print(" ")
            print("vol_list = " + vol_list)
            print(" ")
            
            self.master_se_vol_list[i] = vol_list
        
        print(" ")
        print("master se vol list")
        print(self.master_se_vol_list)

    #マスターSEボリュームリストを参考にボリューム調整を施したリストを作り上げる
    def create_adjustable_se_vol_list(self):
        print(self.adjustable_se_vol_list)
        for i in range(62): #sndは(0~62)まであるので iを0~62まで増加させていく
            tmp_vol_list = "" #編集用一時ボリュームリストを作製宣言
            tmp_vol_list = self.master_se_vol_list[i] #マスターボリュームリストを一時編集用ボリュームリストにコピー
            if tmp_vol_list == "": #リストが空だったら何もせずにforから抜ける
                continue
            else:
                for j in range(7+1): #VOL0からVOL7まで繰り返し作成する 8回繰り返すって事
                    new_vol_list = ""
                    for k in range(len(self.master_se_vol_list[i])):
                        str_num = int(tmp_vol_list[k]) #(k+1)文字目の文字の取得 kは0始まりなので一番最初は1文字目を取得しないといけないので+1してます(0文字目だとおかしいからね)???なんかK+1にしない方がいいっぽい？なんで？？？
                        str_num -= (7 - j) #VOL値を減算する
                        if str_num < 0: #str_numがマイナスになった時は強制的に0にする
                            str_num = 0
                        
                        new_vol_list += str(str_num) #新しいボリュームリストに右端から文字列として文字を繋げていく
                    
                    self.adjustable_se_vol_list[i].append(new_vol_list)
        
        print("adjustable se vol list")
        print(self.adjustable_se_vol_list)

    #サウンドエフェクト(SE)を再生する
    def se(self,ch,num,vol): #ch=再生チャンネル,num=SEナンバー,vol=ボリューム値
        if self.master_se_vol == 0: #SEボリューム値が0ならば効果音を鳴らさずそのままリターンする
            return
        
        if   vol == 1:
            pyxel.sound(num).set_volumes("1")
        elif vol == 2:
            pyxel.sound(num).set_volumes("2")
        elif vol == 3:
            pyxel.sound(num).set_volumes("3")
        elif vol == 4:
            pyxel.sound(num).set_volumes("4")
        elif vol == 5:
            pyxel.sound(num).set_volumes("5")
        elif vol == 6:
            pyxel.sound(num).set_volumes("6")
        elif vol == 7:
            pyxel.sound(num).set_volumes("7")
        else:
            pyxel.sound(num).set_volumes("5")
        
        pyxel.play(ch,num) #チャンネルchでサウンドナンバーnumを鳴らす

