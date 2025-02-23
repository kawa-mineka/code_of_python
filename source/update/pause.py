###########################################################
#  pauseクラス                                             #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にゲーム中のポーズ更新を行うメソッドですよ～♪            #
# 2022 04/07からファイル分割してモジュールとして運用開始      #
###########################################################
# import math         #三角関数などを使用したいのでインポートぉぉおお！
# from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from common.func  import *
from update.system import * #汎用性のある関数群のモジュールの読み込み
from update.window        import * #ポーズウィンドウ作成時に使用するのでインポート
from update.medal         import * #リプレイ再生後のポーズメッセージダイアログの後に通常のメダルを装備しなおすのでインポートが必要です

class pause:
    def __init__(self):
        None

    #ポーズ時の処理
    def pause_menu(self):
        """
        ポーズ時の処理
        """
        if   self.cursor_menu_layer == MENU_LAYER0: #メニューが0階層目の選択分岐
            if   self.cursor_decision_item_y == 0:    #選択したアイテムが「BACK TO GAMES」ならば
                self.game_status = self.record_games_status #一時記憶しておいたゲームステータスを元に戻してあげます
                self.star_scroll_speed = 1                  #星のスクロールスピードを倍率1に戻す
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                if func.search_window_id(self,Window_id.PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = func.search_window_id(self,Window_id.PAUSE_MENU)
                    self.window[i].vy = -0.3            #PAUSE_MENUウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.select_cursor_flag = FLAG_OFF         #セレクトカーソル移動フラグを降ろす
                    
                    pyxel.play(CH0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                
            elif self.cursor_decision_item_y == 1:    #選択したアイテムが「RETURN TITLE」ならば
                if func.search_window_id(self,Window_id.RETURN_TITLE) == -1: #リターンタイトルウィンドウが存在しないのなら・・
                    window.move_down_pause_menu(self) #ポーズメニューウィンドウを下にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「RETURN TITLE」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,Window_id.PAUSE_MENU)         #ポーズメニューのカーソルデータをPUSH
                    window.create(self,Window_id.RETURN_TITLE,50,69)                  #リターンタイトルウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = Window_id.RETURN_TITLE    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(CH0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == 3:    #選択したアイテムが「EXIT GAME」ならば
                if func.search_window_id(self,Window_id.EXIT) == -1: #ゲーム終了(退出)ウィンドウが存在しないのなら・・
                    window.move_down_pause_menu(self) #ポーズメニューウィンドウを下にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「EXIT GAME」を前のレイヤー選択アイテムとしてコピーする
                    func.push_cursor_data(self,Window_id.PAUSE_MENU)         #ポーズメニューのカーソルデータをPUSH
                    window.create(self,Window_id.EXIT,50,69)                  #ゲーム終了(退出)ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    func.set_cursor_data(self,CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = Window_id.EXIT    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(CH0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
            
        elif self.cursor_menu_layer == MENU_LAYER1: #メニューが1階層目の選択分岐
            if     self.cursor_pre_decision_item_y == 1 and self.cursor_decision_item_y == 0: #「RETURN TITLE」→「NO」
                window.move_up_pause_menu(self) #ポーズメニューウィンドウを上にずらす関数の呼び出し
                i = func.search_window_id(self,Window_id.RETURN_TITLE)
                self.window[i].vy = -0.3            #RETURN_TITLEウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.2
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,Window_id.PAUSE_MENU)          #ポーズメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(CH0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = Window_id.PAUSE_MENU        #1階層前ポーズメニューウィンドウIDを最前列でアクティブなものとする
            elif   self.cursor_pre_decision_item_y == 1 and self.cursor_decision_item_y == 1: #「RETURN TITLE」→「YES」
                self.game_status = Scene.TITLE_INIT         #ステータスを「TITLE INIT」にする
                self.game_playing_flag  = FLAG_OFF          #ゲームプレイ中フラグを降ろす
                self.select_cursor_flag = FLAG_OFF          #セレクトカーソル移動フラグを降ろす
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                
                if func.search_window_id(self,Window_id.RETURN_TITLE) != -1: #リターンタイトルウィンドウが存在するのならば・・
                    i = func.search_window_id(self,Window_id.RETURN_TITLE)
                    self.window[i].vy = -0.3            #RETURN_TITLEウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                if func.search_window_id(self,Window_id.PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = func.search_window_id(self,Window_id.PAUSE_MENU)
                    self.window[i].vy = -0.3            #PAUSE_MENUウィンドウを左上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = -0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                if self.replay_status == REPLAY_PLAY: #リプレイ再生中からのタイトルリターンの場合は
                    func.restore_status_data_for_replay_mode(self) #リプレイ再生後記録しておいたステータスを復帰させる
                
                medal.write_ship_equip_medal_data(self)           #機体メダルスロット装備リストに現在プレイ中のシップリストのメダル情報を書き込む関数の呼び出し
                system.save_data(self)                    #システムデータをセーブします
                pyxel.play(CH0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif   self.cursor_pre_decision_item_y == 3 and self.cursor_decision_item_y == 0: #「EXIT GAME」→「NO」
                window.move_up_pause_menu(self) #ポーズメニューウィンドウを上にずらす関数の呼び出し
                i = func.search_window_id(self,Window_id.EXIT)
                self.window[i].vy = -0.3            #EXITウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.2
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                func.pop_cursor_data(self,Window_id.PAUSE_MENU)          #ポーズメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(CH0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = Window_id.PAUSE_MENU        #1階層前ポーズメニューウィンドウIDを最前列でアクティブなものとする
            elif   self.cursor_pre_decision_item_y == 3 and self.cursor_decision_item_y == 1: #「EXIT GAME」→「YES」
                if func.search_window_id(self,Window_id.EXIT) != -1: #ゲーム終了ウィンドウが存在するのならば・・
                    i = func.search_window_id(self,Window_id.EXIT)
                    self.window[i].vy = -0.1            #EXITウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.03
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.04
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                if func.search_window_id(self,Window_id.PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = func.search_window_id(self,Window_id.PAUSE_MENU)
                    self.window[i].vy = -0.1            #PAUSE_MENUウィンドウを左上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.05
                    self.window[i].vx = -0.1
                    self.window[i].vx_accel = 1.04
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.bg_cls_color = 0                        #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)
                self.game_playing_flag = FLAG_ON             #ゲームプレイ中フラグを立てる
                self.game_quit_from_playing = FLAG_ON        #ゲームプレイ中からの終了フラグを立てる
                self.game_status = Scene.GAME_QUIT_START     #ステータスを「GAME QUIT START」(ゲームプレイ中からのゲーム終了工程開始)にする
