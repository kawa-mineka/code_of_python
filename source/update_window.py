###########################################################
#  update_windowクラス                                    #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にウィンドウの更新を行う関数(メソッド？）ですよ～♪        #
#  あとウィンドウシステムで使用するセレクトカーソルとかも      #
# 2022 04/05からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

class update_window:
    def __init__(self):
        None

    #ウィンドウの更新
    def window(self):
        window_count = len(self.window)
        for i in range(window_count):
            if   self.window[i].window_status == WINDOW_OPEN:     #ステータスが「オープン」の時は・・・・・・・・・・・・
                if self.window[i].width < self.window[i].open_width:#widthをopen_widthの数値になるまで増加させていく
                    self.window[i].width += int(self.window[i].change_x * self.window[i].open_speed)
                
                if self.window[i].height < self.window[i].open_height:#heightをopen_heightの数値になるまで増加させていく
                    self.window[i].height += int(self.window[i].change_y * self.window[i].open_speed)
                
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].open_width  - self.window[i].width  <= 2 and\
                    -2 <= self.window[i].open_height - self.window[i].height <= 2:#もしwidthとheightの値がopenした時の数値と+-2以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウは完全に開ききったとみなしてステータスをWINDOW_WRITE_MESSAGEにしてメッセージを表示開始する
                    
                    self.window[i].width  = self.window[i].open_width #小数点以下の座標の誤差を修正するために強制的にopen時の座標数値を現在座標数値に代入してやる
                    self.window[i].height = self.window[i].open_height
            elif self.window[i].window_status == WINDOW_CLOSE:    #ステータスが「クローズ」の時は・・・・・・・・・・・・
                if self.window[i].width > 0 :#widthを0になるまで減少させていく
                        self.window[i].width -= int(self.window[i].change_x * self.window[i].close_speed)
                    
                if self.window[i].height >0 :#heightを0になるまで減少させていく
                    self.window[i].height -= int(self.window[i].change_y * self.window[i].close_speed)
                    
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].width  <= 2 and\
                    -2 <= self.window[i].height <= 2:#もしwidthとheightの値が+-2以内になったのなら
                    self.window[i].window_status = WINDOW_CLOSE_COMPLETED#ウィンドウは完全に閉めきったとみなしてステータスをWINDOW_CLOSE_COMPLETEDにする
                    
                    self.window[i].width  = 0 #小数点以下の座標の誤差を修正するために0を現在のウィンドウ縦横幅とする
                    self.window[i].height = 0
            elif self.window[i].window_status == WINDOW_MOVE:     #ステータスが「ムーブ」の時は・・・・・・・・・・・・・
                if      -3 <= self.window[i].dx - self.window[i].posx <= 3\
                    and -3 <= self.window[i].dy - self.window[i].posy <= 3: #移動先の座標(dx,dy)と現在の座標が+-3以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウ移動は完了とみなしてステータスをWINDOW_WRITE_MESSAGEにする
                    
                    self.window[i].posx = self.window[i].dx #小数点以下の座標の誤差を修正するために強制的に移動先の座標を現在座標数値に代入してやる
                    self.window[i].posy = self.window[i].dy
                    self.window[i].vx = 0       #移動速度,加速度初期化
                    self.window[i].vy = 0
                    self.window[i].vx_accel = 1
                    self.window[i].vy_accel = 1
            
            #ウィンドウ位置の更新
            if self.window[i].wait_count <= 0: #ウェイトカウンターが0以下まで減少したらウィンドウは動き出す
                self.window[i].vx *= self.window[i].vx_accel #速度に加速度を掛け合わせて変化させていく
                self.window[i].vy *= self.window[i].vy_accel
                self.window[i].posx += self.window[i].vx #ウィンドウ位置の更新
                self.window[i].posy += self.window[i].vy
            else:
                self.window[i].wait_count -= 1  #カウンターをデクリメント

    #ウィンドウのはみだしチェック（表示座標が完全に画面外になったのなら消去する）
    def clip_window(self):
        window_count = len(self.window)#ウィンドウの数を数える
        rect_ax,rect_ay = 0,0
        rect_aw,rect_ah = WINDOW_W,WINDOW_H
        for i in reversed(range(window_count)):
            #ゲームの画面(0,0)-(160,120)とウィンドウ(wx1,wy1)-(wx2,wy2)の2つの矩形の衝突判定を行い
            #衝突して一部が重なっている→ウィンドウのどこかの部分を表示しないといけないのでウィンドウは生存させる
            #衝突していない→お互いに干渉していないので画面にウィンドウが表示されることは無い→ウィンドウを消去する
            rect_bx,rect_by = self.window[i].posx,self.window[i].posy
            rect_bw,rect_bh = self.window[i].open_width,self.window[i].open_height
            
            #矩形A(ゲーム画面)と矩形B(ウィンドウ)の衝突判定を行う関数の呼び出し
            if func.collision_rect_rect(self,rect_ax,rect_ay,rect_aw,rect_ah,rect_bx,rect_by,rect_bw,rect_bh) == False:
                del self.window[i] #ウィンドウが画面外に存在するとき(2つの矩形が衝突していないとき)はインスタンスを破棄する(ウィンドウ消滅)

    #現在どのウィンドウがもつインデックス値が最前面にあるのか調べあげ,アクティブウィンドウインデックス値に登録し更新する
    def active_window(self):
        i = func.search_window_id(self,self.active_window_id) #アクティブなウィンドウIDを元にインデックス値を求める関数の呼び出し
        self.active_window_index = i           #アクティブになっているウィンドウのインデックスナンバー(i)を代入

    #セレクトカーソルの更新
    def select_cursor(self):
        # 上入力されたら  y座標を  -7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
            self.cursor_move_data = PAD_UP
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y-1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y -= self.cursor_step_y#y座標をcursor_step_y減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y -= self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            break #カーソルの移動先が見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    for ty in range(self.cursor_item_y): #現在のカーソルy座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y-(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y-(ty+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #上方向がスキップエリアで尚且つ調べる対象のitem_yが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_y -= self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)減算してカーソルを上に移動させる
                            self.cursor_item_y -= (ty+1) #現在指し示しているアイテムナンバーをty+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
            
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュを鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character += 1 #文字のアスキーコードを1増やす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        # 下入力されたら  y座標を  +7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
            self.cursor_move_data = PAD_DOWN
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y+1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y += self.cursor_step_y#y座標をcursor_step_y加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            continue #選択すべき項目テキストは見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            break #選択すべき項目テキストが見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(self.cursor_max_item_y - self.cursor_item_y): #(y軸アイテム最大値-現在のカーソルy座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y+(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y+(ty+1) > self.cursor_max_item_y:
                                break #下方向がスキップエリアで尚且つ調べる対象がmax_item_yより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)加算してカーソルを下に移動させる
                            self.cursor_item_y += (ty+1) #現在指し示しているアイテムナンバーをty+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character -= 1 #文字のアスキーコードを1減らす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(いみゅーたぶる変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        #右入力されたらcursor_pageを +1する
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_RIGHTSHOULDER):
            self.cursor_move_data = PAD_RIGHT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page += 1 #ページ数インクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page > self.cursor_page_max: #カーソルページ数が最大ページ数を超えたのなら
                    self.cursor_page = 0                    #ページ数は0にする
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数でないのなら右方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    self.cursor_x += self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）加算してカーソルを右に移動させる
                    self.cursor_item_x += 1 #現在指示しているアイテムナンバーを1増やす
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーが最大項目数でないのなら右方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for tx in range(self.cursor_max_item_x - self.cursor_item_x): #(x軸アイテム最大値-現在のカーソルx座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x+(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x+(tx+1) > self.cursor_max_item_x:
                                break #右方向がスキップエリアで尚且つ調べる対象がmax_item_xより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_x += self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)加算してカーソルを右に移動させる
                            self.cursor_item_x += (tx+1) #現在指し示しているアイテムナンバーをtx+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_NUM:#操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k < self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MAX_NUMより小さい時は
                        k += 1 #オブジェクトの数値をインクリメント
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        func.restore_master_flag_list(self)
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        
        #左入力されたらcursor_pageを -1する
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_LEFTSHOULDER):
            self.cursor_move_data = PAD_LEFT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page -= 1 #ページ数デクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page < 0:                    #カーソルページ数が0より小さくなったのなら
                    self.cursor_page = self.cursor_page_max                    #ページ数はmaxにする
                
            elif   self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーx軸方向が0以外ならでないのなら左方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    self.cursor_x -= self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）減算してカーソルを左に移動させる
                    self.cursor_item_x -= 1#現在指示しているアイテムナンバーを1減らす
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーが一番左の項目の0以外なら左方向にカーソルは移動できるので・・・
                    for tx in range(self.cursor_item_x): #現在のカーソルx座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x-(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x-(tx+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #左方向がスキップエリアで尚且つ調べる対象のitem_xが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_x -= self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)減算してカーソルを左に移動させる
                            self.cursor_item_x -= (tx+1) #現在指し示しているアイテムナンバーをtx+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE]  == OPE_OBJ_TYPE_NUM: #操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k > self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MIN_NUMより大きい時は
                        k -= 1 #オブジェクトの数値をデクリメント
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        func.restore_master_flag_list(self)
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        
        #ABXYスペースキーが押された場合の処理
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_B) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) or pyxel.btnp(pyxel.GAMEPAD2_BUTTON_Y):
            self.cursor_move_data = PAD_A
            self.cursor_decision_item_x = self.cursor_item_x #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_xに代入！
            self.cursor_decision_item_y = self.cursor_item_y #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_yに代入！
            if self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_ON_OFF:#操作テキストオブジェクトは「ON」「OFF」の二つから選ぶシンプルなタイプの時は
                    if k == 0: #k=0(off)の時はk=1(on)に、k=1(on)の時はk=0(off)にする
                        k = 1
                    else:
                        k = 0
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルok音を鳴らす
