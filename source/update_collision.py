###########################################################
#  update_collisionクラス                                  #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主に衝突当たり判定を行うメソッド群です                     #
#  自機と敵弾、ボス、背景との当たり判定                       #
#  ショットと敵、ボスとの当たり判定                          #
#  ミサイルと敵、ボスとの当たり判定                          #
#  クローショットと敵、ボス,背景との当たり判定                #
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_obj  import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)
from update_ship import * #自機関連の更新関数モジュールの読み込み、クローを取った後の「クローの発生関数の呼び出し」,「自機のダメージ追加」で使用します

class update_collision:
    def __init__(self):
        None

    #################################自機との当たり判定#################################################################
    #自機と敵との衝突判定
    def ship_to_enemy(self):
        if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        
        enemy_count = len(self.enemy)
        for i in range (enemy_count):
            #敵が自機に当たっているか判別
            #敵と自機の位置の2点間の距離を求める
            self.dx = (self.enemy[i].posx - self.my_x)
            self.dy = (self.enemy[i].posy - self.my_y)
            self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
            if self.distance <= self.enemy[i].enemy_size:
                update_ship.damage(self,1)#自機の中心位置と敵の中心位置の距離がenemy_sizeより小さいなら衝突したと判定し自機のシールド値を１減らす

    #自機とボスとの衝突判定
    def ship_to_boss(self):
        if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        boss_count = len(self.boss)
        for i in range (boss_count):
            if self.boss[i].invincible != 1: #もしボスが無敵状態で無いのならば
                #自機がボスの当たり判定矩形の中に存在するのか判別する、存在していたらボスと自機は衝突しています
                #ボス本体当たり判定1との判定
                if     self.boss[i].posx + self.boss[i].col_main1_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main1_x + self.boss[i].col_main1_w\
                    and self.boss[i].posy + self.boss[i].col_main1_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main1_y + self.boss[i].col_main1_h\
                    and self.boss[i].col_main1_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #ボス本体当たり判定2との判定
                elif    self.boss[i].posx + self.boss[i].col_main2_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main2_x + self.boss[i].col_main2_w\
                    and self.boss[i].posy + self.boss[i].col_main2_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main2_y + self.boss[i].col_main2_h\
                    and self.boss[i].col_main2_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #ボス本体当たり判定3との判定
                elif    self.boss[i].posx + self.boss[i].col_main3_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main3_x + self.boss[i].col_main3_w\
                    and self.boss[i].posy + self.boss[i].col_main3_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main3_y + self.boss[i].col_main3_h\
                    and self.boss[i].col_main3_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #ボス本体当たり判定4との判定
                elif    self.boss[i].posx + self.boss[i].col_main4_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main4_x + self.boss[i].col_main4_w\
                    and self.boss[i].posy + self.boss[i].col_main4_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main4_y + self.boss[i].col_main4_h\
                    and self.boss[i].col_main4_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす            
                    
                #ボス本体当たり判定5との判定
                elif    self.boss[i].posx + self.boss[i].col_main5_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main5_x + self.boss[i].col_main5_w\
                    and self.boss[i].posy + self.boss[i].col_main5_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main5_y + self.boss[i].col_main5_h\
                    and self.boss[i].col_main5_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす            
                #ボス本体当たり判定6との判定
                elif    self.boss[i].posx + self.boss[i].col_main6_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main6_x + self.boss[i].col_main6_w\
                    and self.boss[i].posy + self.boss[i].col_main6_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main6_y + self.boss[i].col_main6_h\
                    and self.boss[i].col_main6_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす            
                #ボス本体当たり判定7との判定
                elif    self.boss[i].posx + self.boss[i].col_main7_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main7_x + self.boss[i].col_main7_w\
                    and self.boss[i].posy + self.boss[i].col_main7_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main7_y + self.boss[i].col_main7_h\
                    and self.boss[i].col_main7_w != 0:
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす            
                #ボス本体当たり判定8との判定
                elif    self.boss[i].posx + self.boss[i].col_main8_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main8_x + self.boss[i].col_main8_w\
                    and self.boss[i].posy + self.boss[i].col_main8_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main8_y + self.boss[i].col_main8_h\
                    and self.boss[i].col_main8_w != 0:   
                    update_ship.damage(self,1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす            
                    
                    
                    
                    
                #パーツ1との当たり判定
                elif    self.boss[i].posx + self.boss[i].col_parts1_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts1_x + self.boss[i].col_parts1_w\
                    and self.boss[i].posy + self.boss[i].col_parts1_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts1_y + self.boss[i].col_parts1_h\
                    and self.boss[i].parts1_flag == 1:
                    update_ship.damage(self,1) #ボスのパーツ1の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #パーツ2との当たり判定
                elif    self.boss[i].posx + self.boss[i].col_parts2_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts2_x + self.boss[i].col_parts2_w\
                    and self.boss[i].posy + self.boss[i].col_parts2_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts2_y + self.boss[i].col_parts2_h\
                    and self.boss[i].parts2_flag == 1:
                    update_ship.damage(self,1) #ボスのパーツ2の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #パーツ3との当たり判定
                elif    self.boss[i].posx + self.boss[i].col_parts3_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts3_x + self.boss[i].col_parts3_w\
                    and self.boss[i].posy + self.boss[i].col_parts3_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts3_y + self.boss[i].col_parts3_h\
                    and self.boss[i].parts3_flag == 1:
                    update_ship.damage(self,1) #ボスのパーツ3の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                #パーツ4との当たり判定
                elif    self.boss[i].posx + self.boss[i].col_parts4_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts4_x + self.boss[i].col_parts4_w\
                    and self.boss[i].posy + self.boss[i].col_parts4_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts4_y + self.boss[i].col_parts4_h\
                    and self.boss[i].parts4_flag == 1:
                    update_ship.damage(self,1) #ボスのパーツ4の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす

    #自機と背景障害物との当たり判定
    def ship_to_bg(self):
        if self.bg_collision_Judgment_flag == 0: #デバッグ用の当たり判定を行うフラグが立っていなかったら
            return                        #衝突判定はせずそのまま帰っちゃう
        if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        func.check_bg_collision(self,self.my_x + 6,self.my_y + 4,0,0)
        if self.collision_flag == 1: #コリジョンフラグが建っていたのなら
            update_ship.damage(self,1) #障害物に当たったので自機のシールド値を減らす

    #自機とパワーアップアイテム類との当たり判定（パワーアップアイテムゲット！！）
    def ship_to_obtain_item(self):
        obtain_item_count = len(self.obtain_item)
        for i in reversed(range (obtain_item_count)):
            #パワーアップアイテム類が自機に当たっているか判別
            #パワーアップアイテム類と自機の位置の2点間の距離を求める
            self.dx = (self.obtain_item[i].posx - self.my_x)
            self.dy = (self.obtain_item[i].posy - self.my_y)
            self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
            if self.distance <= 8: #自機の中心位置とパワーアップアイテム類の中心位置の距離が8より小さいなら重なったと判定する
                self.invincible_counter += self.get_item_invincible_time #アイテムを取ったので無敵時間のカウンターを増やす
                if ITEM_SHOT_POWER_UP <= self.obtain_item[i].item_type <= ITEM_SHIELD_POWER_UP: #ショット、ミサイル、シールドパワーアップの処理
                    self.shot_exp    += self.obtain_item[i].shot    #ショット経験値をショットパワーの増加量の分だけパワーアップさせる
                    self.missile_exp += self.obtain_item[i].missile #ミサイル経験値をミサイルパワーの増加量の分だけパワーアップさせる
                    self.my_shield   += self.obtain_item[i].shield  #シールド値（ヒットポイント）をシールドパワーの増加量の分だけパワーアップさせる
                    
                    if self.replay_status != REPLAY_PLAY: #リプレイ再生している時はカプセル累計取得加算処理を行わない
                        self.get_shot_pow_num    += self.obtain_item[i].shot    #ショットカプセル累計取得数をショットパワーの増加量の分だけ増やす
                        self.get_missile_pow_num += self.obtain_item[i].missile #ミサイルカプセル累計取得数をミサイルパワーの増加量の分だけ増やす
                        self.get_shield_pow_num  += self.obtain_item[i].shield  #シールドカプセル累計取得数をシールドパワーの増加量の分だけ増やす
                    
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    func.level_up_my_shot(self)     #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    func.level_up_my_missile(self)   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    
                    del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                    if self.shot_level > 10:    #ショットレベルは10を超えないようにする
                        self.shot_level = 10
                    if self.missile_level > 2:   #ミサイルレベルは2を超えないようにする
                        self.missile_level = 2
                    
                elif self.obtain_item[i].item_type == ITEM_CLAW_POWER_UP:             #クローパワーアップの処理
                    if self.replay_status != REPLAY_PLAY: #リプレイ再生している時はカプセル累計取得加算処理を行わない
                        self.get_claw_num += 1     #クローの累計取得数を1増やす
                    
                    pyxel.play(0,0)               #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]       #クローアイテムのインスタンスを破棄する(アイテム消滅)
                    update_ship.append_claw(self) #クローの発生関数の呼び出し
                    
                elif self.obtain_item[i].item_type == ITEM_TAIL_SHOT_POWER_UP:        #テイルショットパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[TAIL_SHOT] < SUB_WEAPON_LEVEL_MAXIMUM:#テイルショットのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[TAIL_SHOT] += 1  #サブウェポンリスト内のテイルショットの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = TAIL_SHOT #強制的にテイルショットを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_PENETRATE_ROCKET_POWER_UP: #ペネトレートロケットパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[PENETRATE_ROCKET] < SUB_WEAPON_LEVEL_MAXIMUM:#ペネトレートロケットのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[PENETRATE_ROCKET] += 1  #サブウェポンリスト内のペネトレートロケットの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = PENETRATE_ROCKET #強制的にペネトレートロケットを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_SEARCH_LASER_POWER_UP:     #サーチレーザーパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[SEARCH_LASER] < SUB_WEAPON_LEVEL_MAXIMUM:#ーチレーザーのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[SEARCH_LASER] += 1  #サブウェポンリスト内のサーチレーザーの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = SEARCH_LASER #強制的にサーチレーザーを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_HOMING_MISSILE_POWER_UP:   #ホーミングミサイルパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[HOMING_MISSILE] < SUB_WEAPON_LEVEL_MAXIMUM:#ホーミングミサイルのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[HOMING_MISSILE] += 1  #サブウェポンリスト内のホーミングミサイルの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = HOMING_MISSILE #強制的にホーミングミサイルを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_SHOCK_BUMPER_POWER_UP:     #ショックバンバーパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    
                    if self.sub_weapon_list[SHOCK_BUMPER] < SUB_WEAPON_LEVEL_MAXIMUM:#ショックバンバーのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[SHOCK_BUMPER] += 1  #サブウェポンリスト内のショックバンバーの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = SHOCK_BUMPER #強制的にショックバンバーを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_SCORE_STAR:                #スコアスター(得点アイテム)の処理
                    if  self.score_star_magnification >= self.max_score_star_magnification and self.replay_status != REPLAY_PLAY: #スコアスター取得点数の倍率が最大倍率以上＆リプレイ再生では無いの場合は・・・
                            self.max_score_star_magnification = self.score_star_magnification  #最大倍率を更新する
                    
                    func.add_score(self,20 * self.score_star_magnification)    #スコアスター得点上昇！
                    pyxel.play(0,0)             #パワーアップアイテムゲットの音を鳴らすのだ
                    print(" ")
                    print("MAG")
                    print(self.score_star_magnification)
                    print("MAX")
                    print(self.max_score_star_magnification)
                    if self.damaged_flag == FLAG_OFF: #前回スタースコア取得時からダメージを受けたフラグが立っていないのならばノーダメージということなので・・・
                        self.score_star_magnification += 1 #スコアスター取得点数の倍率を1増やす(最大5倍まで)
                        
                    elif self.damaged_flag == FLAG_ON: #ダメージを受けていた場合は
                        self.damaged_flag = FLAG_OFF      #ダメージを受けたかどうかのフラグも下げちゃうのです
                    
                    if self.replay_status != REPLAY_PLAY: #リプレイ再生している時はカプセル累計取得加算処理を行わない
                        self.get_score_star_num += 1 #スコアスター累計所得数を1増やす
                    
                    del self.obtain_item[i]     #スコアスターのインスタンスを破棄する(スターはきえちゃうのです、、、、)

    #################################自機弾との当たり判定##################################################################
    #自機弾と敵の当たり判定
    def my_shot_to_enemy(self):
        shot_hit = len(self.shots)
        for h in reversed(range (shot_hit)):
            enemy_hit = len(self.enemy)
            for e in reversed(range (enemy_hit)):#ウェーブカッターの分も含めてＹ軸方向の幅の大きさも考えた当たり判定にする、Ｘ軸方向の当たり判定は普通に8ドット単位で行う
                if      self.enemy[e].posx                    <= self.shots[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
                    and self.enemy[e].posy - self.shots[h].height <= self.shots[h].posy + 4 <= self.enemy[e].posy + self.enemy[e].height:
                    self.enemy[e].enemy_hp -= self.shots[h].shot_power #敵の耐久力をShot_powerの分だけ減らす
                    if self.enemy[e].enemy_hp <= 0:
                        func.enemy_destruction(self,e) #敵破壊処理関数呼び出し！
                        #パーティクル生成
                        for _number in range(5):
                            update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.shots[h].vx / 2,self.shots[h].vy / 2, 0,0,0)
                        
                        #スコア加算
                        if   self.enemy[e].status == ENEMY_STATUS_NORMAL:   #ステータスが「通常」ならscore_normalをpointとしてスコアを加算する
                            point = self.enemy[e].score_normal
                        elif self.enemy[e].status == ENEMY_STATUS_ATTACK: #ステータスが「攻撃中」ならscore_attackをpointとしてスコアを加算する
                            point = self.enemy[e].score_attack
                        elif self.enemy[e].status == ENEMY_STATUS_ESCAPE: #ステータスが「撤退中」ならscore_escapeをpointとしてスコアを加算する
                            point = self.enemy[e].score_escape
                        elif self.enemy[e].status == ENEMY_STATUS_AWAITING: #ステータスが「待機中」ならscore_awaitingをpointとしてスコアを加算する
                            point = self.enemy[e].score_awaiting
                        elif self.enemy[e].status == ENEMY_STATUS_DEFENSE: #ステータスが「防御中」ならscore_defenseをpointとしてスコアを加算する
                            point = self.enemy[e].score_defense
                        elif self.enemy[e].status == ENEMY_STATUS_BERSERK: #ステータスが「怒り状態」ならscore_berserkをpointとしてスコアを加算する
                            point = self.enemy[e].score_berserk
                        else:                                     #ステータスが以上に当てはまらないときはscore_normalとする
                            point = self.enemy[e].score_normal
                        func.add_score(self,point) #スコアを加算する関数の呼び出し
                        del self.enemy[e] #敵リストから破壊した敵をdel消去破壊するっ！
                        
                    self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させるため
                    pyxel.play(0,2)#変な爆発音を出すのだ～～～☆彡

    #自機弾とボスとの当たり判定
    def my_shot_to_boss(self):
        shot_hit = len(self.shots)
        for h in reversed(range (shot_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):#ウェーブカッターの分も含めてＹ軸方向の幅の大きさも考えた当たり判定にする、Ｘ軸方向の当たり判定は普通に8ドット単位で行う
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main5_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main6_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main7_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main8_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.shots[h].shot_power #パーツ1の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                            #吹っ飛んでいくボスパーツ１を育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts1_x,self.boss[e].posy + self.boss[e].col_parts1_y
                            life   = 1000
                            width     = self.boss[e].grp_parts1_width      #横幅
                            height    = self.boss[e].grp_parts1_height     #縦幅
                            imgb      = self.boss[e].grp_parts1_imgb       #画像が収納されているイメージバンク数
                            u         = self.boss[e].grp_parts1_u          #画像の位置u
                            v         = self.boss[e].grp_parts1_v          #         v
                            offset_x  = self.boss[e].grp_parts1_offset_x   #パーツx軸方向のオフセット値(爆発の煙を育成するときの中心値の指定とかで使うかも？)
                            offset_y  = self.boss[e].grp_parts1_offset_y   #パーツy軸方向のオフセット値(爆発の煙を育成するときの中心値の指定とかで使うかも？)
                            count     = self.boss[e].grp_parts1_count      #カウント用
                            animation = self.boss[e].grp_parts1_animation  #アニメーション関連の値を指定
                            transparent_color = self.boss[e].transparent_color #透明色指定
                            update_obj.append_blow_away_boss_parts(self,x,y,life,width,height,imgb,u,v,offset_x,offset_y,count,animation,transparent_color)
                            
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts1_x,self.boss[e].posy + self.boss[e].col_parts1_y
                            life = 1000
                            update_obj.append_boss_parts_debris(self,2,PARTICLE_BOSS_DEBRIS1,x,y,life)
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.shots[h].shot_power #パーツ2の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts2_x,self.boss[e].posy + self.boss[e].col_parts2_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            # update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_FRONT,x,y,  vx,vy,life,0,col)
                            update_obj.append_boss_parts_debris(self,3,PARTICLE_BOSS_DEBRIS1,x,y,life)
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる 
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.shots[h].shot_power #パーツ3の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts3_x,self.boss[e].posy + self.boss[e].col_parts3_y
                            life = 1000
                            update_obj.append_boss_parts_debris(self,3,PARTICLE_BOSS_DEBRIS1,x,y,life)
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.shots[h].shot_power #パーツ4の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts4_x,self.boss[e].posy + self.boss[e].col_parts4_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            # update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_FRONT,x,y,  vx,vy,life,0,col)
                            update_obj.append_boss_parts_debris(self,3,PARTICLE_BOSS_DEBRIS1,x,y,life)
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_damage_point1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する    

    #自機弾と背景障害物の当たり判定
    def my_shot_to_bg(self):
        if  0 <= self.shot_level <= 6:#ウェーブカッターの場合は背景は貫通する
            shot_count = len(self.shots)
            for i in reversed(range(shot_count)):
                func.check_bg_collision(self,self.shots[i].posx,self.shots[i].posy + 4,0,0)
                if self.collision_flag == 1:
                    update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.shots[i].posx,self.shots[i].posy,0,0, 0,0,0)
                    del self.shots[i]    

    #################################自機ミサイルとの当たり判定###############################################################
    #自機ミサイルと敵の当たり判定
    def missile_to_enemy(self):
        missile_hit = len(self.missile)
        for h in reversed(range (missile_hit)):
            enemy_hit = len(self.enemy)
            for e in reversed(range (enemy_hit)):
                if     self.enemy[e].posx <= self.missile[h].posx + 4 <= self.enemy[e].posx +   self.enemy[e].width  + self.missile[h].width  / 2\
                    and self.enemy[e].posy <= self.missile[h].posy + 4 <= self.enemy[e].posy +   self.enemy[e].height + self.missile[h].height / 2:
                    
                    self.enemy[e].enemy_hp -= self.missile[h].missile_power #敵の耐久力をミサイルパワーの分だけ減らす
                    if self.enemy[e].enemy_hp <= 0:
                        func.enemy_destruction(self,e) #敵破壊処理関数呼び出し！
                        #パーティクル生成
                        for _number in range(5):
                            update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.missile[h].vx / 2,self.missile[h].vy / 2,   0,0,0)    
                        
                        del self.enemy[e]#敵リストから破壊した敵をＤＥＬ消去破壊！
                        self.score += 1#スコア加算（あとあといろんなスコアシステム実装する予定だよ）
                    
                    self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロにしてミサイル移動時にチェックしリストから消去させるため
                    pyxel.play(0,2)#ミサイルが敵を破壊した音！

    #自機ミサイルとボスとの当たり判定
    def missile_to_boss(self):
        missile_hit = len(self.missile)
        for h in reversed(range (missile_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main5_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main6_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main7_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main8_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.missile[h].missile_power #パーツ1の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts1_x,self.boss[e].posy + self.boss[e].col_parts1_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.missile[h].missile_power #パーツ2の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts2_x,self.boss[e].posy + self.boss[e].col_parts2_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.missile[h].missile_power #パーツ3の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts3_x,self.boss[e].posy + self.boss[e].col_parts3_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.missile[h].missile_power #パーツ4の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts4_x,self.boss[e].posy + self.boss[e].col_parts4_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_damage_point1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！ 
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する    

    ################################クローショットとの当たり判定############################################################
    #クローショットと敵の当たり判定
    def claw_shot_to_enemy(self):
        claw_shot_hit = len(self.claw_shot)#クローの弾の数を数える
        for h in reversed(range (claw_shot_hit)):
            enemy_hit = len(self.enemy)
            for e in reversed(range (enemy_hit)):
                if     self.enemy[e].posx <= self.claw_shot[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
                    and self.enemy[e].posy <= self.claw_shot[h].posy + 4 <= self.enemy[e].posy + self.enemy[e].height:
                    
                    self.enemy[e].enemy_hp -= self.claw_shot[h].shot_power #敵の耐久力をクローショットパワーの分だけ減らす
                    if self.enemy[e].enemy_hp <= 0:
                        func.enemy_destruction(self,e) #敵破壊処理関数呼び出し！
                        #パーティクル生成
                        for _number in range(5):
                            update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.claw_shot[h].vx / 2,self.claw_shot[h].vy / 2,    0,0,0)
                        
                        del self.enemy[e]#敵リストから破壊した敵をＤＥＬ消去破壊！
                        self.score += 1#スコア加算（あとあといろんなスコアシステム実装する予定だよ）
                    
                    self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにしてクローショット移動時にチェックしリストから消去させるため
                    pyxel.play(0,2)#クローショットが敵を破壊した音！

    #クローショットとボスとの当たり判定
    def claw_shot_to_boss(self):
        claw_shot_hit = len(self.claw_shot)#クローの弾の数を数える
        for h in reversed(range (claw_shot_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main5_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main6_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main7_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main8_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        update_obj.append_particle(self,PARTICLE_LINE,PRIORITY_FRONT,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.claw_shot[h].shot_power #パーツ1の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts1_x,self.boss[e].posy + self.boss[e].col_parts1_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.claw_shot[h].shot_power #パーツ2の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts2_x,self.boss[e].posy + self.boss[e].col_parts2_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.claw_shot[h].shot_power #パーツ3の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts3_x,self.boss[e].posy + self.boss[e].col_parts3_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.claw_shot[h].shot_power #パーツ4の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                            #ボスのパーツを破壊した後にボスの破片１デブリを育成する
                            x,y = self.boss[e].posx + self.boss[e].col_parts4_x,self.boss[e].posy + self.boss[e].col_parts4_y
                            vx,vy = -0.3 - random() * 2,-0.3 - random()
                            life = 1000
                            col = 0
                            update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS1,PRIORITY_MORE_FRONT,x,y,  vx,vy,life,0,col)
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_damage_point1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        func.boss_processing_after_hitting(self,e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！ 
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する    

    #クローショットと背景との当たり判定
    def claw_shot_to_bg(self):
        claw_shot_count = len(self.claw_shot)
        for i in reversed(range(claw_shot_count)):
            func.check_bg_collision(self,self.claw_shot[i].posx,(self.claw_shot[i].posy) + 4,0,0)
            if self.collision_flag == 1:#背景と衝突したのならクローショットを消滅させる
                del self.claw_shot[i]        

    #敵の弾との当たり判定####################################################################################################
    #敵の弾と背景障害物の当たり判定
    def enemy_shot_to_bg(self):
        enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
        for i in reversed(range(enemy_shot_count)):
            if     self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_WAVE\
                or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_VECTOR_LASER:    #ウェーブ、ベクトルレーザーは当たり判定無し
                continue #当たり判定はしないで次のループ回へ突入！
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_LASER: #レーザービームの場合は障害物にギリギリまで当たり食い込みたいのでx座標を右に1ブロック分(8ドット)だけ補正を入れてやる
                func.check_bg_collision(self,self.enemy_shot[i].posx + 6 + 8,self.enemy_shot[i].posy + 4,0,0)
            else:
                func.check_bg_collision(self,self.enemy_shot[i].posx + 6   ,self.enemy_shot[i].posy + 4,0,0)
                
            if self.collision_flag == 1: #衝突フラグが立っていたらを敵弾を消滅させる
                del self.enemy_shot[i]        


    ################################パワーアップアイテムと敵弾との当たり判定##################################################
    #パワーアップアイテム類と敵弾の当たり判定(難易度によってパワーアップアイテムは敵弾を消す効果あり)
    def obtain_item_to_enemy_shot(self):
        if self.item_erace_bullet_flag == FLAG_OFF: #パワーアップアイテムが敵弾を消すフラグが立っていないのならそのままリターンする
            return
        
        obtain_item_hit = len(self.obtain_item)
        for h in reversed(range(obtain_item_hit)):
            enemy_shot_hit = len(self.enemy_shot)
            for e in reversed(range(enemy_shot_hit)):
                if     -4 <= self.obtain_item[h].posx - self.enemy_shot[e].posx <= 4\
                    and -4 <= self.obtain_item[h].posy - self.enemy_shot[e].posy <= 4:
                    #敵弾消滅時のパーティクル生成
                    for _number in range(5):
                        update_obj.append_particle(self,PARTICLE_DOT,PRIORITY_FRONT,self.enemy_shot[e].posx + 4,self.enemy_shot[e].posy + 4,self.obtain_item[h].vx / 2,self.obtain_item[h].vy / 2,   0,0,0)
                    
                    del self.enemy_shot[e] #敵弾をリストから消去
