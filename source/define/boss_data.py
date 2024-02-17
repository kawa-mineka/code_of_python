from const.const import *         #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class boss_data:
    def move_data(self):     #ボスの移動データリスト
        """
        ボスの移動データリストを定義します
        """
        #ボス１の移動データリスト
        #[移動元座標ax,ay, 移動先座標dx,dy,2次ベジェ曲線向けの制御点qx,qy, 現在のフレーム番号を移動に使う総フレーム数で割ったもの=t,移動速度,加速度,攻撃方法]
        #axが9999の時はエンドコードとみなし最初に戻る
        self.boss_move_data1 = [
            [-40,  0,   120,  0,    80, 240,    240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY],
            [120,  0,   120,120,    0,   60,    240,   1.2,0.999,   BOSS_ATTACK_FRONT_5WAY_AIM_BULLET],
            [120,120,   -40,120,    80, -240,   240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY_ARROW],
            [-40,120,   -40,  0,    160, 60,    240,   0.7,0.999,   BOSS_ATTACK_RIGHT_GREEN_LASER],     
            [9999],]
        
        self.boss_move_data2 = [
            [-40,  0,   120,  0,    80, 240,    240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY],
            [120,  0,   120,120,    0,   60,    240,   1.2,0.999,   BOSS_ATTACK_FRONT_5WAY_AIM_BULLET],
            [120,120,   -40,120,    80, -240,   240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY_ARROW],
            [-40,120,   -40,  0,    160, 60,    240,   0.7,0.999,   BOSS_ATTACK_RIGHT_GREEN_LASER],     
            [9999],]
