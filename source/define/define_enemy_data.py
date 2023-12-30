from const.const import *         #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？

class define_enemy_data:
    def anime_ptn(self):     #敵のアニメーションパターンのキャラチップ番号を定義するメソッド
        """
        敵のアニメーションパターンのキャラチップ番号を定義するメソッド
        """
        #敵１のアニメーションパターンのキャラチップ番号定義
        self.anime_enemy001 = [0,0,   8,8,   16,16,    24,   16,16,   8,8,   0,0,  0,0]
        #敵２のアニメーションパターンのキャラチップ番号定義
        self.anime_enemy002 =  [40,40,40,40,40,
                                48,48,48,48,48,
                                56,56,56,56,56,
                                64,64,64,64,64,
                                72,72,72,72,72,
                                80,80,80,80,80,
                                88,88,88,88,88,
                                96,96,96,96,96]
        #敵３のアニメーションパターンのキャラチップ番号定義
        self.anime_enemy003 =  [32,32,32,
                                40,40,40,
                                48,48,48,
                                40,40,40,
                                32,32,32]
        #敵５のアニメーションパターンのキャラチップ番号定義
        self.anime_enemy005 =  [104,104,104,104,104,
                                112,112,112,112,112,
                                120,120,120,120,120,
                                128,128,128,128,128,
                                136,136,136,136,136,
                                144,144,144,144,144,
                                152,152,152,152,152,
                                160,160,160,160,160]
        #敵９のアニメーションパターンのキャラチップ番号定義
        self.anime_enemy009 = [ 0, 0, 0, 0, 0,
                                8, 8, 8, 8, 8,
                                16,16,16,16,16,
                                24,24,24,24,24,
                                32,32,32,32,32,
                                40,40,40,40,40,
                                48,48,48,48,48,
                                56,56,56,56,56]

    def move_data(self):     #敵の移動データリスト
        """
        敵の移動データリストを定義します
        """
        
        #[移動元座標ax,ay, 移動先座標dx,dy,2次ベジェ曲線向けの制御点qx,qy, 現在のフレーム番号を移動に使う総フレーム数で割ったもの=t,移動速度,加速度,攻撃方法]
        #axが9999の時はエンドコードとみなし最初に戻る
        
        #ダミー用
        self.enemy_move_data_dummy = [
            [ 0,   0,   0,  0,    0, 0,    0,   0,0,   ENEMY_ATTACK_NO_FIRE],
            [9999],]
        #敵17用
        self.enemy_move_data17 = [
            [ 160, 8,    400,  120,    -80,  60,    240,   1.0,1.0,   ENEMY_ATTACK_NO_FIRE],
            
            
            [9999],]
        
        #敵の移動データリスト(タイプナンバーの並びで各リストへ渡すテーブルリストとなっています)(意味不明な日本語・・・自分でも言ってる意味が分からない）
        self.enemy_move_data_list = [[ 0,self.enemy_move_data_dummy],[ 1,self.enemy_move_data_dummy],[ 2,self.enemy_move_data_dummy],
                                [ 3,self.enemy_move_data_dummy],[ 4,self.enemy_move_data_dummy],[ 5,self.enemy_move_data_dummy],
                                [ 6,self.enemy_move_data_dummy],[ 7,self.enemy_move_data_dummy],[ 8,self.enemy_move_data_dummy],
                                [ 9,self.enemy_move_data_dummy],[10,self.enemy_move_data_dummy],[11,self.enemy_move_data_dummy],
                                [12,self.enemy_move_data_dummy],[13,self.enemy_move_data_dummy],[14,self.enemy_move_data_dummy],
                                [15,self.enemy_move_data_dummy],[16,self.enemy_move_data_dummy],[17,self.enemy_move_data17    ],
                                [18,self.enemy_move_data_dummy],[19,self.enemy_move_data_dummy],[20,self.enemy_move_data_dummy],
                                [21,self.enemy_move_data_dummy],[22,self.enemy_move_data_dummy],[23,self.enemy_move_data_dummy],
                                [24,self.enemy_move_data_dummy],[25,self.enemy_move_data_dummy],[26,self.enemy_move_data_dummy],
                                ]
