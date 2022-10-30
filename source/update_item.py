###########################################################
#  update_itemクラス                                      #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  アイテム関連の更新を行うメソッド                          #
#  ショット、ミサイル、シールド、サブウェポンアイテムの更新    #
#  トライアングルアイテム、スコアスターの更新                 #
# 当たり判定は別のクラス(update_collision)で行う             #
# 2022 04/07からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_obj import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update_se  import * #SE再生で使用するためにインポート

class update_item:
    def __init__(self):
        None

    #パワーアップアイテム類の更新
    def obtain_item(self):
        obtain_item_count = len(self.obtain_item)
        for i in reversed(range (obtain_item_count)):
            if     ITEM_SHOT_POWER_UP     <= self.obtain_item[i].item_type <= ITEM_CLAW_POWER_UP\
                or self.obtain_item[i].item_type == ITEM_SCORE_STAR\
                or ITEM_TAIL_SHOT_POWER_UP <= self.obtain_item[i].item_type <= ITEM_SHOCK_BUMPER_POWER_UP: #ショット、ミサイル、シールド クロー スコアスター テイルショット~ショックバンパーパワーアップの更新
                self.obtain_item[i].vx -= 0.009 #vx速度ベクトルをだんだんと減らしていく
                self.obtain_item[i].intensity -= 0.001 #振れ幅をだんだん減らしていく
                if self.obtain_item[i].intensity < 0.001: #振れ幅は0.001より小さくならないようにします
                    self.obtain_item[i].intensity = 0.001
                self.obtain_item[i].posx  += self.obtain_item[i].vx#X座標をvx分減らして左方向に進む
                self.obtain_item[i].timer += self.obtain_item[i].speed
                self.obtain_item[i].posy  += self.obtain_item[i].intensity * math.sin(self.obtain_item[i].timer)
                
                if self.obtain_item[i].posx <= 0 and self.obtain_item[i].bounce >= 1:#x座標が0以下で画面左端まで行き、bounceが1以上なら
                    self.obtain_item[i].vx = 0.2 + self.obtain_item[i].bounce * 0.2 #vxを右側のベクトルにする(跳ね返り回数の1.2倍の整数値)
                    self.obtain_item[i].bounce -= 1 #跳ね返る回数を1減らす
                #dに自機とアイテムの距離を計算した値を代入！ 
                d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))
                if d <= self.item_range_of_attraction: #アイテムと自機との距離がitem_range_of_attraction以内の場合アイテムのx,y座標を自機の方向へ向かう様に補正を入れる
                    self.obtain_item[i].posy += ((self.my_y >= self.obtain_item[i].posy) - (self.my_y <= self.obtain_item[i].posy)) / (d / 5)
                    self.obtain_item[i].posx += ((self.my_x >= self.obtain_item[i].posx) - (self.my_x <= self.obtain_item[i].posx)) / (d / 5)
                
            elif self.obtain_item[i].item_type == ITEM_TRIANGLE_POWER_UP: #トライアングルアイテムの場合
                #flag1は正三角形の内部に自機が居るかどうかの判別で使用します(0=外部に居る 1=内部に居る)
                #flag2は現在の三角形内部に自機が居た時間（一度でも外に出ると0に戻されます）
                #flag3は三角形内部に自機が居た時間がこの数値まで達したらアイテムを入手できるかの数値です
                #statusは状態遷移を示します
                #0=画面スクロールに合わせて左に流れる状態
                #1=アイテム取得時の高速回転状態
                #2=取得アニメーション描画中
                #3=取得完了
                if self.obtain_item[i].status == 0:#状態遷移statusが「画面スクロールに合わせて左に流れる状態」の場合
                    self.obtain_item[i].posx  -= self.obtain_item[i].vx     #X座標をvx分減らして左方向に進む
                    if (pyxel.frame_count % 2) == 0:
                        if self.obtain_item[i].radius < self.obtain_item[i].radius_max:#もし回転半径が回転半径最大値で無いのなら
                            self.obtain_item[i].radius += 1 #回転半径を1増やして、回転半径最大値まで増加させていく
                    #dに自機とアイテムの距離を計算した値を代入！ 
                    d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))
                    if d > self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]:#離れている距離数がトライアングルアイテムの回転半径より大きい場合は三角形の外なので...
                        self.obtain_item[i].flag2 = 0   #現在の三角形内部に自機が居た時間を強制的に0に戻す
                    else:
                        self.obtain_item[i].flag2 += 1  #現在の三角形内部に自機が居た時間を1増やす
                        if self.obtain_item[i].flag2 >= self.obtain_item[i].flag3:#内部に居た時間が設定時間以上になったのなら
                            self.obtain_item[i].status = 1 #状態遷移を「アイテム取得時の高速回転状態」にする
                    
                elif self.obtain_item[i].status == 1:#状態遷移statusが「アイテム取得時の高速回転状態」の場合
                    self.obtain_item[i].posx  -= self.obtain_item[i].vx / 4    #X座標を(vx/4)分減らして左方向に進む
                    if self.obtain_item[i].speed <= 40:  #SPEED(トライアングルアイテムの場合は回転スピードとして使用してます)が10以下なら
                        self.obtain_item[i].speed +=0.5 #回転スピードをだんだん増やしていく
                    
                    self.obtain_item[i].radius -= 0.2 #回転半径を0.2小さくしていく
                    if self.obtain_item[i].radius <= 6: #回転半径が6より大きいのなら
                        self.obtain_item[i].radius = 6 #回転半径は6より小さくしない
                        self.obtain_item[i].animation_number = 0 #アニメーションナンバーをリセット
                        self.obtain_item[i].status = 2 #状態遷移を「取得アニメーション描画中」にする
                    
                elif self.obtain_item[i].status == 2:#状態遷移statusが「取得アニメーション描画中」の場合
                    if pyxel.frame_count % 4 == 0: #3フレーム毎に
                        self.obtain_item[i].animation_number += 1 #アニメーションパターンオフセット値を増やしていく
                    if self.obtain_item[i].animation_number == 8: #最後のパターン数までいったのなら
                        self.obtain_item[i].status = 3 #状態遷移を「取得完了」にする
                    
                elif self.obtain_item[i].status == 3:#状態遷移statusが「取得完了」の場合
                    self.shot_exp    += self.obtain_item[i].shot    #ショット経験値をショットパワーの増加量の分だけパワーアップさせる
                    self.missile_exp += self.obtain_item[i].missile #ミサイル経験値をミサイルパワーの増加量の分だけパワーアップさせる
                    self.my_shield   += self.obtain_item[i].shield  #シールド値（ヒットポイント）をシールドパワーの増加量の分だけパワーアップさせる
                    
                    if self.replay_status != REPLAY_PLAY: #リプレイ再生している時はカプセル累計取得加算処理を行わない
                        self.get_shot_pow_num    += self.obtain_item[i].shot    #ショットカプセル累計取得数をショットパワーの増加量の分だけ増やす
                        self.get_missile_pow_num += self.obtain_item[i].missile #ミサイルカプセル累計取得数をミサイルパワーの増加量の分だけ増やす
                        self.get_shield_pow_num  += self.obtain_item[i].shield  #シールドカプセル累計取得数をシールドパワーの増加量の分だけ増やす
                        self.get_triangle_pow_num += 1                          #トライアングルアイテム累計取得数を１増やす
                    
                    update_se.se(self,0,SE_POWUP_GET,self.master_se_vol) #パワーアップアイテムゲットの音を鳴らすのだ
                    func.level_up_my_shot(self)    #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    func.level_up_my_missile(self) #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    
                    del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                    if self.shot_level > 10:    #ショットレベルは10を超えないようにする
                        self.shot_level = 10
                    if self.missile_level > 2:   #ミサイルレベルは2を超えないようにする
                        self.missile_level = 2

    #画面外に出たパワーアップアイテム類を消去する
    def clip_obtain_item(self):
        obtain_item_count = len(self.obtain_item)
        for i in reversed(range (obtain_item_count)):
            if -50 < self.obtain_item[i].posx < WINDOW_W + 200 and -150 < self.obtain_item[i].posy < WINDOW_H + 150: #xは-50~160+200 Yは-150~120+150以内？
                continue
            else:
                del self.obtain_item[i]#パワーアップアイテムが画面外に存在するときはインスタンスを破棄する(アイテム消滅)

    #ボス破壊後にリペアアイテムを出現させる 
    def present_repair_item(self):
        if self.present_repair_item_flag == 0: #ボーナスアイテムを出したフラグがまだ建っていないのなら
            #ボーナスアイテムを出現させる
            for _i in range(self.repair_shield):
                y = func.s_rndint(self,30,80)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W,y, 0.5+ (func.s_rndint(self,0,1)-0.5)* 0.2,0 + (func.s_rndint(self,0,4)-2) * 0.6,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item)
                
            self.present_repair_item_flag = 1 #フラグを立ててもう出ないようにする
