################################################################
#  update_initクラス                                            #      
################################################################
#  Appクラスのupdate関数から呼び出される関数群                    #
#  主にゲームスタート時の初期化                                  #
#      ステージスタート時の初期化の更新を行うメソッドです          #
# 2022 04/06からファイル分割してモジュールとして運用開始           #
################################################################
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from define_stage_data import * #各ステージのイベントリスト登録モジュールの読み込み
from update_replay     import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み リプレイ記録再生の更新を行う関数(メソッド？）です
from update_ship       import * #Appクラスのupdate関数から呼び出される関数群のモジュールの読み込み ゲーム開始時のイージーやベリーイージーでのクローの追加に使用する

class update_init:
    def __init__(self):
        None

    #!ゲームスタート時の初期化#########################################
    def game_start(self):
        self.score = 0               #スコア
        self.my_shield = 5           #自機のシールド耐久値
        self.my_speed = SPEED1       #自機の初期スピード
        
        self.my_x = 24    #自機のx座標の初期値
        self.my_y = 50    #自機のy座標の初期値
        self.my_vx = 1    #自機のx方向の移動量
        self.my_vy = 0    #自機のy方向の移動量
        
        self.camera_offset_y = 0   #縦自由スクロールステージにおけるカメラ位置のオフセットy座標(この数値が背景BGに対してのオフセット値となります・この数値の分だけy座標がずれた分の背景を描画するって訳です)
        
        self.appeared_shot_pow = 0  #現時点で出現したショットパワーカプセルの数
        self.inc_shot_exp_medal = 0 #事前にショットアイテムを入手するタイプのメダルの合計(この値の分だけショットアイテムを取った状態でゲームスタートする)
        
        self.run_away_bullet_probability = 10 #敵が過ぎ去っていくときに弾を出す確率
        
        self.game_playing_flag  = FLAG_ON    #ゲームプレイフラグを「ゲームプレイ中」にする
        self.select_cursor_flag = FLAG_OFF   #セレクトカーソルの移動更新は行わないのでフラグを降ろす
        
        self.select_shot_id = 0        #現在使用しているショットのIDナンバー(ナンバーの詳細はshot_levelを参照するのです！)
        
        self.shot_exp = 0                   #自機ショットの経験値 パワーアップアイテムを取ることにより経験値がたまりショットのレベルが上がっていく
        self.shot_level = 0                 #自機ショットのレベル  0~3バルカンショット  4=レーザー 5=ツインレーザー 6=3WAYレーザー
                                            #7=ウェーブカッターLv1  8=ウェーブカッターLv2  9=ウェーブカッターLv3   10=ウェーブカッターLv4
        self.shot_speed_magnification=1     #自機ショットのスピードに掛ける倍率(vxに掛け合わせる)  
        self.shot_rapid_of_fire = 1         #自機ショットの連射数  初期値は1連射
        
        self.missile_exp = 0                 #自機ミサイルの経験値 パワーアップアイテムを取ることにより経験値が溜まりミサイルのレベルが上がっていく
        self.missile_level = 0               #自機ミサイルのレベル  0~2 0=右下のみ  1=右下左上前方2方向  2=右下右上  左下左上4方向
        self.missile_speed_magnification = 1 #自機ミサイルのスピードに掛ける倍率(vxに掛け合わせる)
        self.missile_rapid_of_fire = 1       #自機ミサイルの連射数  初期値は1連射
        
        self.select_sub_weapon_id = TAIL_SHOT   #現在使用しているサブウェポンのIDナンバー -1だと何も所有していない状態
        self.sub_weapon_list = [1,1,1,1,1]      #どのサブウェポンを所持しているかのリスト(インデックスオフセット値)
                                                #0=テイルショット 1=ペネトレートロケット 2=サーチレーザー 3=ホーミングミサイル 4=ショックバンバー
        
        self.star_scroll_speed = 1          #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
        #self.pow_item_bounce_num = 6       #パワーアップアイテムが画面の左端で跳ね返って戻ってくる回数
                                            #初期値は6でアップグレードすると増えていくです
        
        self.playtime_frame_counter    = 0 #プレイ時間(フレームのカウンター) 60フレームで＝1秒        
        self.one_game_playtime_seconds = 0 #1プレイでのゲームプレイ時間(秒単位)
        
        self.game_play_count = 0        #ゲーム開始から経過したフレームカウント数(1フレームは60分の1秒)1面～今プレイしている面までのトータルフレームカウント数です
        self.rnd09_num = 0              #乱数0~9ルーレットの初期化
        
        self.replay_stage_num = 0       #リプレイ再生、録画時のステージ数を0で初期化します(1ステージ目=0→2ステージ目=1→3ステージ目=2って感じ)
        
        if self.replay_status != REPLAY_PLAY:       #リプレイデータでの再生時は乱数の種の更新は行いません、それ以外の時は更新します
            self.rnd_seed = pyxel.frame_count % 256 #線形合同法を使った乱数関数で使用する乱数種を現在のフレーム数とします(0~255の範囲)
            self.master_rnd_seed = self.rnd_seed    #リプレイデータ記録用として元となる乱数種を保存しておきます
        
        self.claw_type = ROLLING_CLAW   # クローのタイプ 
                                        # 0=ローリングクロー 1=トレースクロー 2=フィックスクロー 3=リバースクロー
        self.claw_number = NO_CLAW      # クローの装備数 0=装備無し 1=1機 2=2機 3=3機 4=4機
        self.claw_difference = 360      # クロ―同士の角度間隔 1機=360 2機=180度 3機=120度 4機=90度
        self.trace_claw_index = 0       #トレースクロー（オプション）時のトレース用配列のインデックス値
        self.trace_claw_distance = 12   #トレースクロー同士の間隔
        self.fix_claw_magnification = 1 #フイックスクロー同士の間隔の倍率 0.5~2まで0.1刻み
        self.reverse_claw_svx = 1       #リバースクロー用の攻撃方向ベクトル(x軸)
        self.reverse_claw_svy = 0       #リバースクロー用の攻撃方向ベクトル(y軸)
        self.claw_shot_speed = 2        #クローショットのスピード（初期値は移動量２ドット）
        
        self.ls_shield_hp = 0           #L'sシールドの耐久力 0=シールド装備していない 1以上はシールド耐久値を示す
        
        self.claw = []                  #クローのリスト初期化 クローのリストはステージスタート時に初期化してしまうと次のステージに進んだときクローが消滅してしまうのでgame_start_initで初期化します
        
        #難易度に応じた数値をリストから取得する
        func.get_difficulty_data(self) #難易度データリストから数値を取り出す関数の呼び出し
        #ランクに応じた数値をリストから取得する
        func.get_rank_data(self) #ランクデータリストから数値を取り出す関数の呼び出し
        
        self.shot_table_list = self.j_python_shot_table_list       #とりあえずショットテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                        #将来的には選択した機体で色々な機体のリストがコピーされるはず
        self.missile_table_list = self.j_python_missile_table_list #とりあえずミサイルテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                        #将来的には選択した機体で色々な機体のリストがコピーされるはず・・・ほんとかなぁ？
        
        #ゲームスタート時のいろいろなボーナスの処理
        self.shot_exp    += self.start_bonus_shot
        self.missile_exp += self.start_bonus_missile
        self.my_shield   += self.start_bonus_shield
        func.add_medal_effect_shot_bonus(self) #装備されたメダルを調べ、事前にショットアイテム入手するタイプのメダルが装備されていたらショット経験値を加算する関数の呼び出し
        func.medal_effect_ls_shield(self)      #装備されたメダルを調べ、L’ｓシールド装備メダルを作動させる関数を呼び出す
        func.medal_effect_plus_medallion(self) #装備されたメダルを調べ、メダルスロットを増やすメダルがはめ込まれていたらスロット数を増やす関数の呼び出し
        
        func.level_up_my_shot(self)            #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
        func.level_up_my_missile(self)         #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
        
        self.damaged_flag                  = FLAG_OFF       #自機がダメージを受けたかどうかのフラグをOFFにします(スコアスターの連続取得時の倍率上昇で使用するフラグです)
        self.score_star_magnification      = 1              #ゲームスタート時のスコアスター取得得点倍率は1

        if self.start_claw == ONE_CLAW:    #ゲーム開始時クローの数が1の時は
            update_ship.append_claw(self)  #クロー追加ボーナスの数値の回数分、追加関数を呼び出す
        elif self.start_claw == TWO_CLAW:  #ゲーム開始時クローの数が2の時は
            update_ship.append_claw(self)  #2回呼び出し
            update_ship.append_claw(self)
        elif self.start_claw == THREE_CLAW:#ゲーム開始時クローの数が3の時は
            update_ship.append_claw(self)  #3回呼び出し
            update_ship.append_claw(self)
            update_ship.append_claw(self)

    #!ステージスタート時の初期化#######################################
    def stage_start(self):
        #画像リソースファイルを読み込みます
        pyxel.load("assets/graphic/min-sht2.pyxres")
        pygame.mixer.init(frequency = 44100)    #pygameミキサー関連の初期化
        pygame.mixer.music.set_volume(0.7)      #音量設定(0~1の範囲内)
        func.load_stage_bgm(self)               #BGMファイルの読み込み
        pygame.mixer.music.play(-1)             #BGMループ再生
        if self.replay_status == REPLAY_RECORD:
            update_replay.save_stage_data(self)    #リプレイ保存時は,ステージスタート時のパラメーターをセーブする関数を呼び出します(リプレイ再生で使用)
            
        elif self.replay_status == REPLAY_PLAY:
            
            update_replay.load_stage_data(self)    #リプレイ再生時は,ステージスタート時のパラメーターをロードする関数を呼び出します
        
        self.pad_data_h = 0b00000000#パッド入力用ビットパターンデータを初期化します
        self.pad_data_l = 0b00000000#各ビットの詳細
                                    #上位バイトから 0,0,0,0, RS,LS,START,SELECT
                                    #下位バイトは   BY,BX,BB,BA, R,L,D,U
                                    # U=上 D=下 L=左 R=右 BA~BY=各ボタン START,SELECT=スタート,セレクト LS,RS=左ショルダー,右ショルダーボタン
        self.replay_frame_index = 0 #リプレイ時のフレームインデックス値を初期化
        
        #各ステージに応じた数値をリストから取得する
        func.get_stage_data(self)             #ステージデータリストからステージごとに設定された数値を取り出す関数の呼び出し
        self.my_x,self.my_y = self.start_my_x,self.start_my_y    #自機のx座標の初期値を各ステージデータから転送する
        self.my_vx = 1    #自機のx方向の移動量
        self.my_vy = 0    #自機のy方向の移動量
        
        
        self.present_repair_item_flag = FLAG_OFF      #ボス破壊後の爆発シーンでリペアアイテムを出すときに使用するフラグ 0=まだアイテム出してない 1=アイテム放出したよ～
        self.rank_down_count      = 0                 #ダメージを受けて難易度別に設定された規定値まで行ったかどうかをカウントする変数
        self.bg_cls_color         = pyxel.COLOR_BLACK #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です) ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
        self.bg_transparent_color = pyxel.COLOR_BLACK #BGタイルマップを敷き詰めるときに指定する透明色です            ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
        
        self.my_boost_injection_count = 0 #ステージクリア後のブースト噴射用のカウンター
        
        self.timer_flare_flag = FLAG_OFF         #タイマーフレア（触れると物質の時間経過が遅くなるフレア）を放出するかどうかのフラグ
        
        self.move_mode_auto_x,self.move_mode_auto_y = 0,0 #自動移動モードがonの時はこの座標に向かって毎フレームごと自動で移動して行きます
        self.move_mode_auto_complete                = 0   #自動移動モードで目標座標まで移動したらこのフラグを立てます
        
        self.add_appear_flag = FLAG_OFF     #敵を追加発生させる時に立てるフラグです
        
        self.no_damage_destroy_boss_flag = FLAG_OFF #ノーダメージボス撃破フラグ初期化
        self.no_damage_stage_clear_flag  = FLAG_OFF #ノーダメージステージクリアフラグ初期化
        self.endurance_one_cleared_flag  = FLAG_OFF #残りシールド1でクリアフラグを初期化
        self.stage_battle_damaged_flag   = FLAG_OFF #1ステージ用のダメージを受けたかどうかのフラグ(ステージスタートした時にオフ、ダメージ受けたらオン)を初期化
        self.boss_battle_damaged_flag    = FLAG_OFF #ボス戦用のダメージを受けたかどうかのフラグ   (ステージスタートした時にオフ、ボス出現時にオフ、ダメージ受けたらオン)を初期化
        self.boss_instank_kill_flag      = FLAG_OFF #ボスを瞬殺したかどうかのフラグを初期化
        self.destroy_all_boss_parts_flag = FLAG_OFF #ボスのパーツをすべて破壊したかどうかのフラグを初期化
        self.fast_forward_flag           = FLAG_OFF #早回し実績取得用のフラグを初期化
        self.record_games_status = 0 #ポーズを掛けたときに直前のゲームステータスを記録しておく変数
        
        self.scroll_count = 0           #ステージ開始からスクロールした背景のドット数カウンタ
                                        #(スクロールスピードが小数になったときはこのカウントも少数になるので注意！)
        self.vertical_scroll_count = 0  #ステージ開始から縦スクロールした背景のドット数カウンタ 主に縦スクロールするステージで使用します
                                        #(スクロールスピードが小数になったときはこのカウントも小数になるので注意！)
        
        self.stage_count = 0          #ステージ開始から経過したフレームカウント数(1フレームは60分の1秒)常に整数だよ
        
        self.side_scroll_speed              = 1  #横スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
        self.side_scroll_speed_set_value    = 1  #横スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
        self.side_scroll_speed_variation    = 0  #横スクロールスピードを変化させる時の差分(変化量)
        
        self.vertical_scroll_speed           = 0  #縦スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
        self.vertical_scroll_speed_set_value = 0  #縦スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
        self.vertical_scroll_speed_variation = 0  #縦スクロールスピードを変化させる時の差分(変化量)
        
        self.display_cloud_flag    = DISP_OFF    #背景の流れる雲を表示するかどうかのフラグ(DISP_OFF=表示しない DISP_ON=表示する)
        
        self.cloud_append_interval = 6    #雲を追加させる間隔
        self.cloud_quantity        = 0    #雲の量
        self.cloud_how_flow        = 0    #雲の流れ方
        self.cloud_flow_speed      = 0    #雲の流れるスピード
        
        self.warning_dialog_flag         = FLAG_OFF #WARINIGダイアログを表示するかどうかのフラグ
        self.warning_dialog_display_time = 0        #WARINIGダイアログの表示時間(フレーム単位)
        self.warning_dialog_logo_time    = 0        #WARNINGグラフイックロゴの表示に掛ける時間(フレーム単位)
        self.warning_dialog_text_time    = 0        #WARNINGテキスト表示に掛ける時間(フレーム単位)
        
        self.stage_clear_dialog_flag         = FLAG_OFF #STAGE CLEARダイアログを表示するかどうかのフラグ
        self.stage_clear_dialog_display_time = 0        #STAGE CLEARダイアログの表示時間(フレーム単位)
        self.stage_clear_dialog_logo_time1   = 0        #STAGE CLEARグラフイックロゴの表示に掛ける時間その１(フレーム単位)
        self.stage_clear_dialog_logo_time2   = 0        #STAGE CLEARグラフイックロゴの表示に掛ける時間その２(フレーム単位)
        self.stage_clear_dialog_text_time    = 0        #STAGE CLEARテキスト表示に掛ける時間(フレーム単位)
        
        self.event_index = 0                #イベントリストのインデックス値（イベントリストが現在どの位置にあるのかを示す値です）
        self.type_check_quantity = 0        #特定のショットタイプがリストにどれだけあるのかチェックして数えた数がここに入る
        self.my_ship_explosion_timer = 0    #自機が爆発した後、まだどれだけゲームが進行するかのタイマーカウント
        self.game_over_timer = 0            #ゲームオーバーダイアログを表示した後まだどれだけゲームが進行するかのタイマーカウント
        self.fade_in_out_counter = 0        #フェードイン＆フェードアウト用エフェクトスクリーン用のカウンタ（基本的にx軸(キャラクター単位）の値です)
                                            #0~19 で 19になった状態が一番右端を描画したという事になります
                                            #19になった時点で完了となります
        self.fade_complete_flag          = FLAG_OFF #フェードイン＆フェードアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
        self.shadow_in_out_counter       = 0        #シャドウイン＆シャドウアウト用エフェクトスクリーン用のカウンタ
        self.shadow_in_out_complete_flag = FLAG_OFF #シャドウイン＆シャドウアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
        
        self.current_formation_id = 1   #現在の敵編隊のＩＤナンバー（0は単独機で編隊群は1からの数字が割り当てられます）
                                        #編隊が1編隊出現するごとにこの数字が1増えていく
                                        #例 1→2→3→4→5→6→7→8→9→10みたいな感じで増えていく
        self.fast_forward_destruction_num = 0       #早回しの条件を満たすのに必要な「破壊するべき編隊の総数」が入ります
        self.fast_forward_destruction_count = 0     #破壊するべき編隊の総数」が1以上ならば編隊を破壊すると次の編隊の出現カウントがこの数値だけ少なくなり出現が早まります
        self.add_appear_flag = FLAG_OFF             #早回しの条件をすべて満たしたときに建つフラグです、このフラグが立った時、イベントリストに「EVENT_ADD_APPEAR_ENEMY」があったらそこで敵編隊を追加発生させます
        
        self.my_rolling_flag = 0        #0=通常の向き  1=下方向に移動中のキャラチップ使用  2=上方向に移動中のキャラチップ使用
        self.my_moved_flag = FLAG_OFF   #自機が移動したかどうかのフラグ（トレースクローの時、自機のＸＹ座標を履歴リストに記録するのか？しないのか？で使う）
                                        #0=自機は止まっているので座標履歴リストに記録はしない 
                                        #1=自機は移動したので座標履歴リストに記録する
        
        self.invincible_counter = 0 #無敵時間(単位はフレーム)のカウンタ 0の時以外は無敵状態です
        self.boss_battle_time = 0   #ボスとの戦闘時間を初期化
        
        self.enemy_bound_collision_flag = FLAG_OFF #ホッパー君が地面に接触してバウンドしたかどうかのフラグ(デバッグ用に使います)
        self.mountain_x = 0                        #8wayフリースクロール＋ラスタースクロール時の背景に表示される山のBGX座標用の変数です（デバッグ様に使用します）
        self.cp = 0                                #外積計算用の変数(何故か判らないけど関数内で宣言せずに使うとintじゃなくてtupleになってしまうので・・・何故？)
        self.point_inside_triangle_flag = FLAG_OFF #三角形の中に点が存在するかを判別する関数用のフラグを初期化
        
        #リスト群の初期化#############################################################################
        #新しいクラスを作った時はここで必ず初期化するコードを記述する事！！！！！！
        #リストは初期化しないと使えないっポイ！？ぞ・・・っと・・・・・・
        #############################################################################################
        self.shots                = [] #自機弾のリスト
        self.missile              = [] #ミサイルのリスト
        self.claw_shot            = [] #クローの弾のリスト
        self.enemy                = [] #敵のリスト
        self.enemy_shot           = [] #敵の弾のリスト
        self.obtain_item          = [] #取得アイテム類のリスト(パワーアップカプセルなど)
        self.stars                = [] #背景の流れる星々のリスト         当たり判定はありません
        self.explosions           = [] #爆発パターン群のリスト           当たり判定はありません
        self.particle             = [] #パーティクル（火花の粒子）のリスト  当たり判定はありません
        self.background_object    = [] #背景オブジェクトのリスト         当たり判定はありません
        self.window               = [] #メッセージウィンドウのリスト       当たり判定はありません
        self.claw_coordinates     = [] #自機クロー（トレースモード）のxy座標リスト まぁオプションのxy座標が入るリストです
        self.enemy_formation      = [] #敵の編隊数のＩＤと出現時の総数と現在の生存数が入るリストです
        self.event_append_request = [] #イベント追加リクエストが入るリストです(敵などの臨時追加発注発生）
        self.boss                 = [] #ボスのリスト
        self.raster_scroll        = [] #ラスタースクロール用のリスト
        
        define_stage_data.event_list(self)        #各ステージのイベントリストの定義関数の呼び出し
        define_stage_data.game_event_list(self)   #ゲーム全体のイベントリストの定義関数の呼び出し
        define_stage_data.bg_animation_list(self) #各ステージのBG書き換えによるアニメーションの為のデータリスト定義関数の呼び出し
        
        if self.boss_test_mode == 1:
            self.event_list = self.event_list_boss_test_mode #ボステストモードが1の時はボスだけが出現するイベントリストを登録します
        else:
            self.event_list = self.game_event_list[self.stage_number - 1][self.stage_loop - 1] 
                                                                #self.event_list_stage_advance_base_l1        
                                                                #とりあえずイベントリストはadvance_baseステージのものをコピーして使用します
                                                                #将来的にはステージやループ回数を反映する・・・はず
        
        
        self.bg_animation_list = self.bg_animation_master_list[self.stage_number - 1]
        print(self.bg_animation_list)
        # self.bg_animation_list = self.bg_animation_list_mountain_region    #とりあえずBGアニメーションパターンリストはmountain_regionのものをコピーして使用します
        # print(self.bg_animation_list)
        
        #自機のXY座標をトレースクローのXY座標としてコピーし、初期化を行う(とりあえず60要素埋め尽くす)(60要素=60フレーム分=1秒過去分まで記録される)
        for _i in range(TRACE_CLAW_BUFFER_SIZE):
            new_traceclaw = Trace_coordinates()
            new_traceclaw.update(self.my_x,self.my_y)
            self.claw_coordinates.append(new_traceclaw)
        
        func.create_raster_scroll_data(self) #ラスタースクロール用のデータの初期化＆育成関数の呼び出し
