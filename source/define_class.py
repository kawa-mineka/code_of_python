class Shot:#自機弾のクラス設定
    def __init__(self):
        self.shot_type = 0
        self.posx = 0
        self.posy = 0
        self.vx = 0
        self.vy = 0
        self.width = 0
        self.height = 0
        self.offset_y = 0
        self.shot_power = 0
        self.shot_hp = 0
    def update(self,shot_type, x , y, vx, vy, width, height, offset_y, shot_power, shot_hp):
        self.shot_type = shot_type
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height
        self.offset_y = offset_y
        self.shot_power = shot_power
        self.shot_hp = shot_hp
class Missile:#自機ミサイルのクラス設定
    def __init__(self):
        self.missile_type = 0 #0=右下ミサイル 1=右上ミサイル 2=左下ミサイル 3=左上ミサイル 4=テイルショット 5=ぺネトレートロケット 6=サーチレーザー 7=ホーミングミサイル
        self.posx = 0
        self.posy = 0
        self.vx = 0
        self.vy = 0
        self.missile_power = 0
        self.missile_hp = 0
        self.missile_flag1 = 0
        self.missile_flag2 = 0
        self.x_reverse = 0
        self.y_reverse = 0
        self.width = 0
        self.height = 0
        self.tx = 0
        self.ty = 0
        self.theta = 0
        self.speed = 0
    def update(self,missile_type, x , y, vx, vy, missile_power, missile_hp,missile_flag1,missile_flag2,x_reverse,y_reverse,width,height,tx,ty,theta,speed):
        self.missile_type = missile_type
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.missile_power = missile_power
        self.missile_hp = missile_hp
        self.missile_flag1 = missile_flag1
        self.missile_flag2 = missile_flag2
        self.x_reverse = x_reverse
        self.y_reverse = y_reverse
        self.width = width
        self.height = height
        self.tx = tx
        self.ty = ty
        self.theta = theta
        self.speed = speed
class Claw:#クローのクラス設定
    def __init__(self):
        self.number = 0 #クローのIDナンバー 0~3まで
        self.claw_type = 0 #0=ローリングタイプ 1=トレースタイプ 2=フックスタイプ 3=リバースタイプ
        self.status = 0 #0=回転開始や固定開始の初期位置まで動いていく #1==回転中もしくは固定完了
        self.posx = 0#インスタンス育成時は自機のX座標が入る
        self.posy = 0#インスタンス育成時は自機のY座標が入る
        self.roll_vx = 0
        self.roll_vy = 0
        self.fix_vx = 0
        self.fix_vy = 0
        
        self.reverse_vx = 0
        self.reverse_vy = 0
        
        self.offset_x = 0#クローの現時点での座標オフセット値
        self.offset_y = 0
        self.offset_roll_x = 0      #ローリングクローの処理開始の座標（オフセット値）
        self.offset_roll_y = 0
        self.offset_fix_x = 0        #フックスクローの処理開始の間隔倍率を掛けた座標（オフセット値）実際に比較対象になるのはこっちのほう
        self.offset_fix_y = 0
        self.offset_fix_origin_x = 0  #フックスクローの処理開始の間隔倍率を掛ける前の元の座標（オフセット値）
        self.offset_fix_origin_y = 0
        self.offset_reverse_x = 0    #リバースクローの処理開始の座標（オフセット値）
        self.offset_reverse_y = 0
        self.intensity = 0
        self.timer = 0
        self.degree = 0 #回転角度 度数法（主にこちらを使用するのです！）
        self.radian = 0 #回転角度 弧度法
        self.speed = 0 #回転スピード(弧度法0~360度)
        self.radius = 0 #半径
        self.degree_interval = 0 #クローの個数に応じた回転間隔(1個=設定なし 2個=180度 3個=120度 4個=90度)
        self.angle_difference = 0 #ひとつ前のクローとの回転角度の差（この値がdegree_intarvalと同じ数値になるまで回転スピードを増減させていく）
        self.shot_type = 0
        self.shot_power = 0
        self.animation_number = 0
    def update(self,number,claw_type,status,x,y,roll_vx,roll_vy,fix_vx,fix_vy,reverse_vx,reverse_vy,offset_x,offset_y,offset_roll_x,offset_roll_y,offset_fix_x,offset_fix_y,offset_fix_origin_x,offset_fix_origin_y,offset_reverse_x,offset_reverse_y,intensity,timer,degree,radian,speed,radius,degree_interval,angle_difference,shot_type,shot_power,animation_number):
        self.number = number
        self.claw_type = claw_type
        self.status = status
        self.posx = x
        self.posy = y
        self.roll_vx = roll_vx
        self.roll_vy = roll_vy
        self.fix_vx = fix_vx
        self.fix_vy = fix_vy
        self.reverse_vx = reverse_vx
        self.reverse_vy = reverse_vy
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.offset_roll_x = offset_roll_x
        self.offset_roll_y = offset_roll_y
        self.offset_fix_x = offset_fix_x
        self.offset_fix_y = offset_fix_y
        self.offset_fix_origin_x = offset_fix_origin_x
        self.offset_fix_origin_y = offset_fix_origin_y
        self.offset_reverse_x = offset_reverse_x
        self.offset_reverse_y = offset_reverse_y
        self.intensity = intensity
        self.timer = timer
        self.degree = degree
        self.radian = radian
        self.speed = speed
        self.radius = radius
        self.degree_interval = degree_interval
        self.angle_difference = angle_difference
        self.shot_type = shot_type
        self.shot_power = shot_power
        self.animation_number = animation_number
class Trace_coordinates:#トレースクロー（オプション）座標のクラス設定
    def __init__(self):
        self.posx = 0 #自機のx座標をオプションのx座標としてコピーして使用する
        self.posy = 0 #自機のy座標をオプションのy座標としてコピーして使用する
    def update(self, ox, oy):
        self.posx = ox
        self.posy = oy
class Claw_shot:#クローショット（クローの弾）のクラス設定
    def __init__(self):
        self.shot_type = 0
        self.posx = 0
        self.posy = 0
        self.vx = 0
        self.vy = 0
        self.width = 0
        self.height = 0
        self.offset_x = 0
        self.offset_y = 0
        self.shot_power = 0
        self.shot_hp = 0
    def update(self,shot_type, x , y, vx, vy, width, height, offset_x, offset_y, shot_power, shot_hp):
        self.shot_type = shot_type
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height
        self.offseet_x = offset_x
        self.offset_y = offset_y
        self.shot_power = shot_power
        self.shot_hp = shot_hp
class Star:#背景の流れる星のクラス設定
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.speed = 0
    def update(self,x , y, speed):
        self.posx = x
        self.posy = y
        self.speed = speed
class Enemy:#敵キャラ達のクラス設定
    def __init__(self):
        self.enemy_type = 0    #敵のタイプ
        self.enemy_id = 0     #敵のIDナンバー
        self.status = 0       #敵の状態
        self.attack_method = 0 #敵の攻撃方法
        self.posx = 0 #敵の位置座標(x,y)
        self.posy = 0
        self.offset_x = 0 #座標オフセット値
        self.offset_y = 0
        self.offset_p1x = 0 #パーツ1のオフセット座標値(p1x,p1y)
        self.offset_p1y = 0
        self.offset_p2x = 0 #パーツ2のオフセット座標値(p2x,p2y)
        self.offset_p2y = 0
        self.offset_p3x = 0 #パーツ3のオフセット座標値(p3x,p3y)
        self.offset_p3y = 0
        self.offset_p4x = 0 #パーツ4のオフセット座標値(p4x,p4y)
        self.offset_p4y = 0
        
        self.ax = 0 #移動元の座標
        self.ay = 0
        self.bx = 0 #予約座標1
        self.by = 0
        self.cx = 0 #予約座標2
        self.cy = 0 
        self.dx = 0 #移動先の座標(destination_x,y)
        self.dy = 0
        self.qx = 0 #2次ベジェ曲線の制御点qとして使用
        self.qy = 0
        self.vx = 0 #敵の速度ベクトル(vx,vy)
        self.vy = 0
        
        
        self.o1x = 0 #移動元の座標1(origin1_x,y)(リストを使わずにインスタンス育成時に座標を指定してベジェ曲線移動するときに使うメンバ変数)とりあえず5点まで移動できるように変数を確保してます
        self.o1y = 0 
        self.d1x = 0 #移動先の座標1(destination1_x,y)
        self.d1y = 0
        self.q1x = 0 #2次ベジェ曲線の制御点q1として使用
        self.q1y = 0
        self.a1  = 0 #加速度(acceleration1)
        
        self.o2x = 0 #移動元の座標2(origin2_x,y)
        self.o2y = 0 
        self.d2x = 0 #移動先の座標2(destination2_x,y)
        self.d2y = 0
        self.q2x = 0 #2次ベジェ曲線の制御点q2として使用
        self.q2y = 0
        self.a2  = 0 #加速度(acceleration2)
        
        self.o3x = 0 #移動元の座標3(origin3_x,y)
        self.o3y = 0 
        self.d3x = 0 #移動先の座標3(destination3_x,y)
        self.d3y = 0
        self.q3x = 0 #2次ベジェ曲線の制御点q3として使用
        self.q3y = 0
        self.a3  = 0 #加速度(acceleration3)
        
        self.o4x = 0 #移動元の座標4(origin4_x,y)
        self.o4y = 0 
        self.d4x = 0 #移動先の座標4(destination4_x,y)
        self.d4y = 0
        self.q4x = 0 #2次ベジェ曲線の制御点q4として使用
        self.q4y = 0
        self.a4  = 0 #加速度(acceleration4)
        
        self.o5x = 0 #移動元の座標5(origin5_x,y)
        self.o5y = 0 
        self.d5x = 0 #移動先の座標5(destination5_x,y)
        self.d5y = 0
        self.q5x = 0 #2次ベジェ曲線の制御点q5として使用
        self.q5y = 0
        self.a5  = 0 #加速度(acceleration5)      
        
        self.width = 0  #敵の横幅
        self.height = 0 #敵の縦幅
        self.move_speed       = 0 #敵の全体的な移動スピード
        self.move_speed_offset = 0 #敵の全体的な移動スピード(オフセット値)move_speedとかけ合わせたり加減算したりしてスピードを変化とか出来そう
        self.direction = 0    #敵の移動方向
        self.enemy_hp = 0    #敵の耐久力
        self.enemy_flag1 = 0  #フラグ用その1
        self.enemy_flag2 = 0  #フラグ用その２
        self.enemy_size = 0   #敵の全体的な大きさ
        self.enemy_count1 = 0 #汎用カウンタその1
        self.enemy_count2 = 0 #汎用カウンタその2
        self.enemy_count3 = 0 #汎用カウンタその3
        self.parts1_flag = 0 #各部位用のフラグ
        self.parts2_flag = 0
        self.parts3_flag = 0
        self.parts4_flag = 0
        self.item = 0         #0=パワーアップアイテム未所持 1=ショットアイテム 2=ミサイルアイテム 3=シールドアイテム
                            #これ以外の項目については敵キャラが持っているアイテム類のＩＤを参照してね
        self.formation_id = 0   #単独機の場合は0 1番最初に出現した編隊群は1 2番目に出現した編隊群2 3番目の編隊は3 みたいな感じで数値が代入される
        self.timer       = 0   #時間(三角関数系で使用)
        self.speed       = 0   #速度(三角関数系で使用)
        self.intensity    = 0   #振れ幅(三角関数系で使用)
        self.acceleration  = 0  #加速度
        self.move_index    = 0  #2次ベジェ曲線での移動用リストを参照するときに使用するインデックス値（リストの添え字に入る数値）
        self.obj_time     = 0  #2次ベジェ曲線での移動用のtime（現在のタイムフレーム番号が入る）(0~totaltimeまで変化する)ピエール・ベジェさんありがとう・・・
        self.obj_totaltime = 0  #2次ベジェ曲線での移動用のtotaltime（移動元から移動先までに掛けるトータルフレーム数が入る60なら1秒掛けて移動元から移動先まで移動するって事,120なら2秒かかる)
        self.color        = 0  #色
        self.floating_flag = 0  #地上物か空中物かどうかのフラグ 0=空中物 1=地上物 2=地上を移動する物体(装甲車とか)
        self.score_normal  = 0  #通常時の得点
        self.score_attack  = 0  #攻撃時の得点
        self.score_escape  = 0  #撤退時の得点
        self.score_awaiting = 0 #待機中の得点
        self.score_defense  = 0 #防御中の得点
        self.score_berserk  = 0 #怒り状態の得点
    def update(self,enemy_type,enemy_id,status,attack_method,
            x, y,
            offset_x,offset_y,
            offset_p1x,offset_p1y,
            offset_p2x,offset_p2y,
            offset_p3x,offset_p3y,
            offset_p4x,offset_p4y,
            ax,ay,bx,by,cx,cy,dx,dy,qx,qy,
            vx, vy,
            
            o1x,o1y,d1x,d1y,q1x,q1y,a1,
            o2x,o2y,d2x,d2y,q2x,q2y,a2,
            o3x,o3y,d3x,d3y,q3x,q3y,a3,
            o4x,o4y,d4x,d4y,q4x,q4y,a4,
            o5x,o5y,d5x,d5y,q5x,q5y,a5,
            
            width, height,
            move_speed,move_speed_offset,
            direction,
            enemy_hp,
            enemy_flag1, enemy_flag2,
            enemy_size,
            enemy_count1, enemy_count2, enemy_count3,
            parts1_flag,parts2_flag,parts3_flag,parts4_flag,
            
            item,formation_id,
            timer,speed,intensity,
            acceleration,
            move_index,obj_time,obj_totaltime,
            color,floating_flag,
            score_normal,score_attack,score_escape,score_awaiting,score_defense,score_berserk):
        self.enemy_type = enemy_type
        self.enemy_id = enemy_id
        self.status = status
        self.attack_method = attack_method
        self.posx = x
        self.posy = y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.offset_p1x = offset_p1x
        self.offset_p1y = offset_p1y
        self.offset_p2x = offset_p2x
        self.offset_p2y = offset_p2y
        self.offset_p3x = offset_p3x
        self.offset_p3y = offset_p3y
        self.offset_p4x = offset_p4x
        self.offset_p4y = offset_p4y
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy        
        self.dx = dx
        self.dy = dy
        self.qx = qx
        self.qy = qy
        self.vx = vx
        self.vy = vy
        
        self.o1x = o1x
        self.o1y = o1y 
        self.d1x = d1x
        self.d1y = d1y
        self.q1x = q1x
        self.q1y = q1y
        self.a1  = a1
        
        self.o2x = o2x
        self.o2y = o2y 
        self.d2x = d2x
        self.d2y = d2y
        self.q2x = q2x
        self.q2y = q2y
        self.a2  = a2
        
        self.o3x = o3x
        self.o3y = o3y 
        self.d3x = d3x
        self.d3y = d3y
        self.q3x = q3x
        self.q3y = q3y
        self.a3  = a3
        
        self.o4x = o4x
        self.o4y = o4y 
        self.d4x = d4x
        self.d4y = d4y
        self.q4x = q4x
        self.q4y = q4y
        self.a4  = a4
        
        self.o5x = o5x
        self.o5y = o5y 
        self.d5x = d5x
        self.d5y = d5y
        self.q5x = q5x
        self.q5y = q5y
        self.a5  = a5
        
        self.width = width
        self.height = height
        self.move_speed = move_speed
        self.move_speed_offset = move_speed_offset
        self.direction = direction
        self.enemy_hp = enemy_hp
        self.enemy_flag1 = enemy_flag1
        self.enemy_flag2 = enemy_flag2
        self.enemy_size = enemy_size
        self.enemy_count1 = enemy_count1
        self.enemy_count2 = enemy_count2
        self.enemy_count3 = enemy_count3
        self.parts1_flag = parts1_flag
        self.parts2_flag = parts2_flag
        self.parts3_flag = parts3_flag
        self.parts4_flag = parts4_flag
        self.item = item
        self.formation_id = formation_id
        self.timer = timer
        self.speed = speed
        self.intensity = intensity
        self.acceleration  = acceleration
        self.move_index    = move_index
        self.obj_time     = obj_time
        self.obj_totaltime = obj_totaltime
        self.color = color
        self.floating_flag  = floating_flag
        self.score_normal   = score_normal
        self.score_attack   = score_attack
        self.score_escape   = score_escape
        self.score_awaiting = score_awaiting
        self.score_defense  = score_defense
        self.score_berserk  = score_berserk
class Boss:#ボスキャラのクラス設定
    def __init__(self):
        self.boss_id = 0      #ボスのIDナンバー
        self.boss_type = 0    #ボスの種類
        self.status = 0       #ボスの現在のステータス(状態)
        self.parts_number = 0 #破壊可能部位の数 0なら本体のみ 1なら破壊可能部位が1箇所あり 4なら4箇所あるという事です
        self.main_hp   = 0    #本体の耐久力
        self.parts1_hp = 0    #各部位の耐久力(1~9)
        self.parts2_hp = 0
        self.parts3_hp = 0
        self.parts4_hp = 0
        self.parts5_hp = 0
        self.parts6_hp = 0
        self.parts7_hp = 0
        self.parts8_hp = 0
        self.parts9_hp = 0
        self.parts1_score = 0 #各パーツを破壊した時の得点(1~9)
        self.parts2_score = 0
        self.parts3_score = 0
        self.parts4_score = 0
        self.parts5_score = 0
        self.parts6_score = 0
        self.parts7_score = 0
        self.parts8_score = 0
        self.parts9_score = 0
        self.level = 0 #ボスのレベル
        self.weapon1_status,self.weapon1_interval,self.weapon1_rapid_num,self.weapon1_cool_down_time,self.weapon1_omen_count = 0,0,0,0,0 #武器1の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
        self.weapon2_status,self.weapon2_interval,self.weapon2_rapid_num,self.weapon2_cool_down_time,self.weapon2_omen_count = 0,0,0,0,0 #武器2の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
        self.weapon3_status,self.weapon3_interval,self.weapon3_rapid_num,self.weapon3_cool_down_time,self.weapon3_omen_count = 0,0,0,0,0 #武器3の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
        self.weapon4_status,self.weapon4_interval,self.weapon4_rapid_num,self.weapon4_cool_down_time,self.weapon4_omen_count = 0,0,0,0,0 #武器4の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
        self.weapon5_status,self.weapon5_interval,self.weapon5_rapid_num,self.weapon5_cool_down_time,self.weapon5_omen_count = 0,0,0,0,0 #武器5の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
        self.posx,self.posy         = 0,0 #ボスの座標
        self.bgx,self.bgy           = 0,0 #ボスの座標(BG移動時)
        self.offset_x,self.offset_y = 0,0 #ボスの座標に対する画面オフセット値
        self.ax,self.ay = 0,0 #移動元の座標
        self.bx,self.by = 0,0
        self.cx,self.cy = 0,0
        self.dx,self.dy = 0,0 #移動先の座標(destination_x,y)
        self.qx,self.qy = 0,0 #2次ベジェ曲線の制御点qとして使用
        self.vx,self.vy = 0,0 #速度
        
        self.width  = 0  #画像の横の大きさ
        self.height = 0  #画像の縦の大きさ
        
        self.tilt_now      = 0 #現在の画像の傾き具合 y軸方向にどれだけ傾て(チルト)いるかの数値 0なら通常 -1なら上昇中 1なら下降中(roll とかにした方が良いかも・・・)
        self.tilt_max      = 0 #傾きの最大値        y軸方向に最大どれだけ傾くかの最大値(値は変化しません)
        self.tilt_time_now = 0 #現在の傾き所要時間(フレーム数)
        self.tilt_time     = 0 #傾かせる時にかかる時間(フレーム数)(値は変化しません)
        
        self.col_damage_point1_x,self.col_damage_point1_y = 0,0 #ボスの弱点位置1 始点x,y座標
        self.col_damage_point1_w,self.col_damage_point1_h = 0,0 #    弱点位置1 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
        
        self.col_damage_point2_x,self.col_damage_point2_y = 0,0 #ボスの弱点位置2 始点x,y座標
        self.col_damage_point2_w,self.col_damage_point2_h = 0,0 #    弱点位置2 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
        
        self.col_damage_point3_x,self.col_damage_point3_y = 0,0 #ボスの弱点位置3 始点x,y座標
        self.col_damage_point3_w,self.col_damage_point3_h = 0,0 #    弱点位置3 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
        
        self.col_damage_point4_x,self.col_damage_point4_y = 0,0 #ボスの弱点位置3 始点x,y座標
        self.col_damage_point4_w,self.col_damage_point4_h = 0,0 #    弱点位置3 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
        
        self.col_main1_x = 0 #本体1当たり判定の始点x
        self.col_main1_y = 0 #             始点y          
        self.col_main1_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main1_h = 0 #            縦の長さ
        
        self.col_main2_x = 0 #本体2当たり判定の始点x
        self.col_main2_y = 0 #             始点y          
        self.col_main2_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main2_h = 0 #            縦の長さ
        
        self.col_main3_x = 0 #本体3当たり判定の始点x
        self.col_main3_y = 0 #             始点y          
        self.col_main3_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main3_h = 0 #            縦の長さ
        
        self.col_main4_x = 0 #本体4当たり判定の始点x
        self.col_main4_y = 0 #             始点y          
        self.col_main4_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main4_h = 0 #            縦の長さ
        
        self.col_main5_x = 0 #本体5当たり判定の始点x
        self.col_main5_y = 0 #             始点y          
        self.col_main5_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main5_h = 0 #            縦の長さ
        
        self.col_main6_x = 0 #本体6当たり判定の始点x
        self.col_main6_y = 0 #             始点y          
        self.col_main6_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main6_h = 0 #            縦の長さ
        
        self.col_main7_x = 0 #本体7当たり判定の始点x
        self.col_main7_y = 0 #             始点y          
        self.col_main7_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main7_h = 0 #            縦の長さ
        
        self.col_main8_x = 0 #本体8当たり判定の始点x
        self.col_main8_y = 0 #             始点y          
        self.col_main8_w = 0 #            横の長さ 横の長さが0の場合は当たり判定として使用しない
        self.col_main8_h = 0 #            縦の長さ
        
        
        self.col_parts1_x = 0 #パーツ1当たり判定の始点x
        self.col_parts1_y = 0 #パーツ1当たり判定の始点y          
        self.col_parts1_w = 0 #パーツ1当たり判定(横の長さ）
        self.col_parts1_h = 0 #パーツ1当たり判定(縦の長さ)
        
        self.col_parts2_x = 0 #パーツ2当たり判定の始点x
        self.col_parts2_y = 0 #パーツ2当たり判定の始点y          
        self.col_parts2_w = 0 #パーツ2当たり判定(横の長さ）
        self.col_parts2_h = 0 #パーツ2当たり判定(縦の長さ)
        
        self.col_parts3_x = 0 #パーツ3当たり判定の始点x
        self.col_parts3_y = 0 #パーツ3当たり判定の始点y          
        self.col_parts3_w = 0 #パーツ3当たり判定(横の長さ）
        self.col_parts3_h = 0 #パーツ3当たり判定(縦の長さ)
        
        self.col_parts4_x = 0 #パーツ4当たり判定の始点x
        self.col_parts4_y = 0 #パーツ4当たり判定の始点y          
        self.col_parts4_w = 0 #パーツ4当たり判定(横の長さ）
        self.col_parts4_h = 0 #パーツ4当たり判定(縦の長さ)
        
        self.col_parts5_x = 0 #パーツ5当たり判定の始点x
        self.col_parts5_y = 0 #パーツ5当たり判定の始点y          
        self.col_parts5_w = 0 #パーツ5当たり判定(横の長さ）
        self.col_parts5_h = 0 #パーツ5当たり判定(縦の長さ)
        
        self.col_parts6_x = 0 #パーツ6当たり判定の始点x
        self.col_parts6_y = 0 #パーツ6当たり判定の始点y          
        self.col_parts6_w = 0 #パーツ6当たり判定(横の長さ）
        self.col_parts6_h = 0 #パーツ6当たり判定(縦の長さ)
        
        self.col_parts7_x = 0 #パーツ7当たり判定の始点x
        self.col_parts7_y = 0 #パーツ7当たり判定の始点y          
        self.col_parts7_w = 0 #パーツ7当たり判定(横の長さ）
        self.col_parts7_h = 0 #パーツ7当たり判定(縦の長さ)
        
        self.col_parts8_x = 0 #パーツ8当たり判定の始点x
        self.col_parts8_y = 0 #パーツ8当たり判定の始点y          
        self.col_parts8_w = 0 #パーツ8当たり判定(横の長さ）
        self.col_parts8_h = 0 #パーツ8当たり判定(縦の長さ)
        
        self.col_parts9_x = 0 #パーツ9当たり判定の始点x
        self.col_parts9_y = 0 #パーツ9当たり判定の始点y          
        self.col_parts9_w = 0 #パーツ9当たり判定(横の長さ）
        self.col_parts9_h = 0 #パーツ9当たり判定(縦の長さ)
        
        self.main_hp_bar_offset_x,  self.main_hp_bar_offset_y   = 0,0 #本体のHPバーを表示する座標のオフセット値
        
        self.parts1_hp_bar_offset_x,self.parts1_hp_bar_offset_y = 0,0 #パーツ1のHPバーを表示する座標のオフセット値
        self.parts2_hp_bar_offset_x,self.parts2_hp_bar_offset_y = 0,0 #パーツ2のHPバーを表示する座標のオフセット値
        self.parts3_hp_bar_offset_x,self.parts3_hp_bar_offset_y = 0,0 #パーツ3のHPバーを表示する座標のオフセット値
        self.parts4_hp_bar_offset_x,self.parts4_hp_bar_offset_y = 0,0 #パーツ4のHPバーを表示する座標のオフセット値
        self.parts5_hp_bar_offset_x,self.parts5_hp_bar_offset_y = 0,0 #パーツ5のHPバーを表示する座標のオフセット値
        self.parts6_hp_bar_offset_x,self.parts6_hp_bar_offset_y = 0,0 #パーツ6のHPバーを表示する座標のオフセット値
        self.parts7_hp_bar_offset_x,self.parts7_hp_bar_offset_y = 0,0 #パーツ7のHPバーを表示する座標のオフセット値
        self.parts8_hp_bar_offset_x,self.parts8_hp_bar_offset_y = 0,0 #パーツ8のHPバーを表示する座標のオフセット値
        self.parts9_hp_bar_offset_x,self.parts9_hp_bar_offset_y = 0,0 #パーツ9のHPバーを表示する座標のオフセット値
        
        self.size          = 0 #大きさ
        self.priority      = 0 #画像表示時の優先度
        self.attack_method = 0 #攻撃方法
        self.direction     = 0 #方向
        self.reverse       = 1 #反転フラグ  1=通常表示 -1=反転表示
        self.acceleration  = 0 #加速度
        self.timer  = 0   #時間
        self.degree = 0   #回転角度 度数法（主にこちらを使用するのです！）
        self.radian = 0   #回転角度 弧度法
        self.speed  = 0   #回転スピード(弧度法0~360度)
        self.radius = 0   #半径
        self.flag1 = 0    #フラグ類(1~4)
        self.flag2 = 0
        self.flag3 = 0
        self.flag4 = 0
        self.count1 = 0   #カウンター類(1~4)
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.parts1_flag = 0 #各部位用のフラグ(1~9)
        self.parts2_flag = 0
        self.parts3_flag = 0
        self.parts4_flag = 0
        self.parts5_flag = 0
        self.parts6_flag = 0
        self.parts7_flag = 0
        self.parts8_flag = 0
        self.parts9_flag = 0
        self.animation_number1 = 0 #アニメーションパターンナンバー用(1~4)
        self.animation_number2 = 0
        self.animation_number3 = 0
        self.animation_number4 = 0
        self.move_index     = 0  #移動用のインデックス（リストの添え字に入る数値）
        self.obj_time       = 0  #2次ベジェ曲線での移動用のtime（現在のタイムフレーム番号が入る）(0~totaltimeまで変化する)ピエール・ベジェさんありがとう・・・
        self.obj_totaltime  = 0  #2次ベジェ曲線での移動用のtotaltime（移動元から移動先までに掛けるトータルフレーム数が入る60なら1秒掛けて移動元から移動先まで移動するって事,120なら2秒かかる)
        self.invincible     = 0  #無敵状態かどうかのフラグ(出現時は無敵にするとかで使うかも？)
        self.anime_speed_now  = 0 #現在のアニメーションスピード値(このメンバ変数が変化していきます)
        self.anime_speed_min  = 0 #現在のアニメーションスピードの最低値(これより小さくなったらダメだよ)判定値として使用します
        self.anime_speed_max  = 0 #現在のアニメーションスピードの最大値(超えたらダメだよ)判定値として使用します
        self.anime_speed_init = 0 #アニメーションスピードの初期値
        self.display_time_main_hp_bar   = 0 #耐久力ゲージをどれだけの時間表示させるかのカウント 1=60ミリ秒
        self.display_time_parts1_hp_bar = 0
        self.display_time_parts2_hp_bar = 0
        self.display_time_parts3_hp_bar = 0
        self.display_time_parts4_hp_bar = 0
        self.display_time_parts5_hp_bar = 0
        self.display_time_parts6_hp_bar = 0
        self.display_time_parts7_hp_bar = 0
        self.display_time_parts8_hp_bar = 0
        self.display_time_parts9_hp_bar = 0
    def update(self,boss_id,boss_type,status,parts_number,
            main_hp,
            parts1_hp,parts2_hp,parts3_hp,
            parts4_hp,parts5_hp,parts6_hp,
            parts7_hp,parts8_hp,parts9_hp,
            parts1_score,parts2_score,parts3_score,
            parts4_score,parts5_score,parts6_score,
            parts7_score,parts8_score,parts9_score,
            level,
            
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
            x,y,bgx,bgy,offset_x,offset_y,ax,ay,bx,by,cx,cy,dx,dy,qx,qy,vx,vy,
            width,height,
            
            tilt_now,tilt_max,tilt_time_now,tilt_time,
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
            col_damage_point2_x,col_damage_point2_y,col_damage_point2_w,col_damage_point2_h,
            col_damage_point3_x,col_damage_point3_y,col_damage_point3_w,col_damage_point3_h,
            col_damage_point4_x,col_damage_point4_y,col_damage_point4_w,col_damage_point4_h,
            
            col_main1_x ,col_main1_y ,col_main1_w ,col_main1_h,
            col_main2_x ,col_main2_y ,col_main2_w ,col_main2_h,
            col_main3_x ,col_main3_y ,col_main3_w ,col_main3_h,
            col_main4_x ,col_main4_y ,col_main4_w ,col_main4_h,
            col_main5_x ,col_main5_y ,col_main5_w ,col_main5_h,
            col_main6_x ,col_main6_y ,col_main6_w ,col_main6_h,
            col_main7_x ,col_main7_y ,col_main7_w ,col_main7_h,
            col_main8_x ,col_main8_y ,col_main8_w ,col_main8_h,
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,
            
            main_hp_bar_offset_x,main_hp_bar_offset_y,
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,
            
            size,priority,attack_method,direction,reverse,acceleration,timer,degree,radian,speed,radius,
            flag1,flag2,flag3,flag4,
            count1,count2,count3,count4,
            parts1_flag,parts2_flag,parts3_flag,
            parts4_flag,parts5_flag,parts6_flag,
            parts7_flag,parts8_flag,parts9_flag,
            animation_number1,animation_number2,animation_number3,animation_number4,
            move_index,
            obj_time,obj_totaltime,
            invincible,
            anime_speed_now,anime_speed_min,anime_speed_max,anime_speed_init,
            display_time_main_hp_bar,
            display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
            display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
            display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar,
            ):
        self.boss_id = boss_id
        self.boss_type = boss_type
        self.status = status
        self.parts_number = parts_number
        self.main_hp = main_hp
        self.parts1_hp = parts1_hp
        self.parts2_hp = parts2_hp
        self.parts3_hp = parts3_hp
        self.parts4_hp = parts4_hp
        self.parts5_hp = parts5_hp
        self.parts6_hp = parts6_hp
        self.parts7_hp = parts7_hp
        self.parts8_hp = parts8_hp
        self.parts9_hp = parts9_hp
        self.parts1_score = parts1_score
        self.parts2_score = parts2_score
        self.parts3_score = parts3_score
        self.parts4_score = parts4_score
        self.parts5_score = parts5_score
        self.parts6_score = parts6_score
        self.parts7_score = parts7_score
        self.parts8_score = parts8_score
        self.parts9_score = parts9_score
        self.level = level
        
        self.weapon1_status         = weapon1_status
        self.weapon1_interval       = weapon1_interval
        self.weapon1_rapid_num      = weapon1_rapid_num
        self.weapon1_cool_down_time = weapon1_cool_down_time
        self.weapon1_omen_count     = weapon1_omen_count  
        
        self.weapon2_status         = weapon2_status
        self.weapon2_interval       = weapon2_interval
        self.weapon2_rapid_num      = weapon2_rapid_num
        self.weapon2_cool_down_time = weapon2_cool_down_time
        self.weapon2_omen_count     = weapon2_omen_count  
        
        self.weapon3_status         = weapon3_status
        self.weapon3_interval       = weapon3_interval
        self.weapon3_rapid_num      = weapon3_rapid_num
        self.weapon3_cool_down_time = weapon3_cool_down_time
        self.weapon3_omen_count     = weapon3_omen_count  
        
        self.weapon4_status         = weapon4_status
        self.weapon4_interval       = weapon4_interval
        self.weapon4_rapid_num      = weapon4_rapid_num
        self.weapon4_cool_down_time = weapon4_cool_down_time
        self.weapon4_omen_count     = weapon4_omen_count  
        
        self.weapon5_status         = weapon5_status
        self.weapon5_interval       = weapon5_interval
        self.weapon5_rapid_num      = weapon5_rapid_num
        self.weapon5_cool_down_time = weapon5_cool_down_time
        self.weapon5_omen_count     = weapon5_omen_count  
        
        self.posx = x
        self.posy = y
        self.bgx = bgx
        self.bgy = bgy
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy        
        self.dx = dx
        self.dy = dy
        self.qx = qx
        self.qy = qy
        self.vx = vx
        self.vy = vy
        self.width  = width 
        self.height = height
        self.tilt_now      = tilt_now
        self.tilt_max      = tilt_max
        self.tilt_time_now = tilt_time_now
        self.tilt_time     = tilt_time
        self.col_damage_point1_x = col_damage_point1_x
        self.col_damage_point1_y = col_damage_point1_y
        self.col_damage_point1_w = col_damage_point1_w
        self.col_damage_point1_h = col_damage_point1_h
        
        self.col_damage_point2_x = col_damage_point2_x
        self.col_damage_point2_y = col_damage_point2_y
        self.col_damage_point2_w = col_damage_point2_w
        self.col_damage_point2_h = col_damage_point2_h
        
        self.col_damage_point3_x = col_damage_point3_x
        self.col_damage_point3_y = col_damage_point3_y
        self.col_damage_point3_w = col_damage_point3_w
        self.col_damage_point3_h = col_damage_point3_h
        
        self.col_damage_point4_x = col_damage_point4_x
        self.col_damage_point4_y = col_damage_point4_y
        self.col_damage_point4_w = col_damage_point4_w
        self.col_damage_point4_h = col_damage_point4_h
        
        self.col_main1_x = col_main1_x
        self.col_main1_y = col_main1_y
        self.col_main1_w = col_main1_w
        self.col_main1_h = col_main1_h
        
        self.col_main2_x = col_main2_x
        self.col_main2_y = col_main2_y
        self.col_main2_w = col_main2_w
        self.col_main2_h = col_main2_h
        
        self.col_main3_x = col_main3_x
        self.col_main3_y = col_main3_y
        self.col_main3_w = col_main3_w
        self.col_main3_h = col_main3_h
        
        self.col_main4_x = col_main4_x
        self.col_main4_y = col_main4_y
        self.col_main4_w = col_main4_w
        self.col_main4_h = col_main4_h
        
        self.col_main5_x = col_main5_x
        self.col_main5_y = col_main5_y
        self.col_main5_w = col_main5_w
        self.col_main5_h = col_main5_h
        
        self.col_main6_x = col_main6_x
        self.col_main6_y = col_main6_y
        self.col_main6_w = col_main6_w
        self.col_main6_h = col_main6_h
        
        self.col_main7_x = col_main7_x
        self.col_main7_y = col_main7_y
        self.col_main7_w = col_main7_w
        self.col_main7_h = col_main7_h
        
        self.col_main8_x = col_main8_x
        self.col_main8_y = col_main8_y
        self.col_main8_w = col_main8_w
        self.col_main8_h = col_main8_h
        
        self.col_parts1_x = col_parts1_x
        self.col_parts1_y = col_parts1_y
        self.col_parts1_w = col_parts1_w
        self.col_parts1_h = col_parts1_h
        
        self.col_parts2_x = col_parts2_x
        self.col_parts2_y = col_parts2_y
        self.col_parts2_w = col_parts2_w
        self.col_parts2_h = col_parts2_h
        
        self.col_parts3_x = col_parts3_x
        self.col_parts3_y = col_parts3_y
        self.col_parts3_w = col_parts3_w
        self.col_parts3_h = col_parts3_h
        
        self.col_parts4_x = col_parts4_x
        self.col_parts4_y = col_parts4_y
        self.col_parts4_w = col_parts4_w
        self.col_parts4_h = col_parts4_h
        
        self.col_parts5_x = col_parts5_x
        self.col_parts5_y = col_parts5_y
        self.col_parts5_w = col_parts5_w
        self.col_parts5_h = col_parts5_h
        
        self.col_parts6_x = col_parts6_x
        self.col_parts6_y = col_parts6_y
        self.col_parts6_w = col_parts6_w
        self.col_parts6_h = col_parts6_h
        
        self.col_parts7_x = col_parts7_x
        self.col_parts7_y = col_parts7_y
        self.col_parts7_w = col_parts7_w
        self.col_parts7_h = col_parts7_h
        
        self.col_parts8_x = col_parts8_x
        self.col_parts8_y = col_parts8_y
        self.col_parts8_w = col_parts8_w
        self.col_parts8_h = col_parts8_h
        
        self.col_parts9_x = col_parts9_x
        self.col_parts9_y = col_parts9_y
        self.col_parts9_w = col_parts9_w
        self.col_parts9_h = col_parts9_h
        
        self.main_hp_bar_offset_x = main_hp_bar_offset_x  
        self.main_hp_bar_offset_y = main_hp_bar_offset_y
        
        self.parts1_hp_bar_offset_x = parts1_hp_bar_offset_x
        self.parts1_hp_bar_offset_y = parts1_hp_bar_offset_y
        
        self.parts2_hp_bar_offset_x = parts2_hp_bar_offset_x
        self.parts2_hp_bar_offset_y = parts2_hp_bar_offset_y
        
        self.parts3_hp_bar_offset_x = parts3_hp_bar_offset_x
        self.parts3_hp_bar_offset_y = parts3_hp_bar_offset_y
        
        self.parts4_hp_bar_offset_x = parts4_hp_bar_offset_x
        self.parts4_hp_bar_offset_y = parts4_hp_bar_offset_y
        
        self.parts5_hp_bar_offset_x = parts5_hp_bar_offset_x
        self.parts5_hp_bar_offset_y = parts5_hp_bar_offset_y
        
        self.parts6_hp_bar_offset_x = parts6_hp_bar_offset_x
        self.parts6_hp_bar_offset_y = parts6_hp_bar_offset_y
        
        self.parts7_hp_bar_offset_x = parts7_hp_bar_offset_x
        self.parts7_hp_bar_offset_y = parts7_hp_bar_offset_y
        
        self.parts8_hp_bar_offset_x = parts8_hp_bar_offset_x
        self.parts8_hp_bar_offset_y = parts8_hp_bar_offset_y
        
        self.parts9_hp_bar_offset_x = parts9_hp_bar_offset_x
        self.parts9_hp_bar_offset_y = parts9_hp_bar_offset_y
        
        self.size = size
        self.priority = priority
        self.attack_method = attack_method
        self.direction = direction
        self.reverse = reverse
        self.acceleration = acceleration
        self.timer = timer
        self.degree = degree
        self.radian = radian
        self.speed = speed
        self.radius = radius
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.flag4 = flag4
        self.count1 = count1
        self.count2 = count2
        self.count3 = count3
        self.count4 = count4
        self.parts1_flag = parts1_flag
        self.parts2_flag = parts2_flag
        self.parts3_flag = parts3_flag
        self.parts4_flag = parts4_flag
        self.parts5_flag = parts5_flag
        self.parts6_flag = parts6_flag
        self.parts7_flag = parts7_flag
        self.parts8_flag = parts8_flag
        self.parts9_flag = parts9_flag
        self.animation_number1 = animation_number1
        self.animation_number2 = animation_number2
        self.animation_number3 = animation_number3
        self.animation_number4 = animation_number4
        self.move_index = move_index
        self.obj_time = obj_time
        self.obj_totaltime = obj_totaltime
        self.invincible = invincible
        
        self.anime_speed_now  = anime_speed_now
        self.anime_speed_min  = anime_speed_min
        self.anime_speed_max  = anime_speed_max
        self.anime_speed_init = anime_speed_init
        
        self.display_time_main_hp_bar = display_time_main_hp_bar
        self.display_time_parts1_hp_bar = display_time_parts1_hp_bar
        self.display_time_parts2_hp_bar = display_time_parts2_hp_bar
        self.display_time_parts3_hp_bar = display_time_parts3_hp_bar
        self.display_time_parts4_hp_bar = display_time_parts4_hp_bar
        self.display_time_parts5_hp_bar = display_time_parts5_hp_bar
        self.display_time_parts6_hp_bar = display_time_parts6_hp_bar
        self.display_time_parts7_hp_bar = display_time_parts7_hp_bar
        self.display_time_parts8_hp_bar = display_time_parts8_hp_bar
        self.display_time_parts9_hp_bar = display_time_parts9_hp_bar     
class Enemy_shot:#敵弾のクラス設定
    def __init__(self):
        self.enemy_shot_type = 0 #敵弾の種類
        self.enemy_shot_id   = 0 #敵弾に振られたIDナンバー
        self.posx = 0          #敵弾の座標x,y
        self.posy = 0
        self.collision_type = 0 #自機との当たり判定の種類 0=単純な小さな正方形で自機との距離を比べて当たったか判断 1=長方形でwidth,heightを見て自機と当たったかどうか判断する
        self.width  = 0 #弾の横幅
        self.height = 0 #弾の縦幅
        self.cx = 0    #回転弾で使用する回転の中心cx,cy
        self.cy = 0
        self.vx = 0    #速度ベクトルvx,vy
        self.vy = 0
        self.accel = 0    #加速度
        self.power = 0    #弾のパワー
        self.hp = 0       #弾のヒットポイント
        self.count1 = 0    #汎用カウンタ1
        self.count2 = 0    #汎用カウンタ2
        self.timer = 0    #時間(三角関数系で使用)
        self.speed = 0    #速度(三角関数系で使用)
        self.intensity = 0 #振れ幅(三角関数系で使用)
        self.aim = 0      #狙い撃つ方向
        self.disappearance_count = 0 #消滅するまでのカウントタイマー
        self.stop_count = 0        #その場に止まり続ける時に使用するカウンタ
        self.priority = 0          #描画優先度 0=1番最前面に表示 1=ボスより奥&敵より手前 2=ボスより奥&敵よりも奥
        self.turn_theta = 0        #誘導弾やホーミングミサイル,レーザーでの最大旋回可能角度(これ以上の角度では曲がることが出来ません)
        self.search_flag = 0             #サーチレーザーなどで自機の位置を調べて曲がる位置を確定させたかどうかのフラグ
        self.rotation_omega = 0           #回転弾などで使用する角度が入ります(現在値)
        self.rotation_omega_incremental = 0 #回転弾などで使用する,1フレームで増加する角度が入ります
        self.radius = 0        #回転弾などで使用する半径(現在値)
        self.radius_max = 0     #回転弾などで使用する半径(目標となる最大値)
        self.division_type = 0  #分裂弾かどうかのフラグとそのタイプ
                                #0=分裂はしない 1=自機狙いの3way 2=自機狙いの5way 3=自機狙いの7way 4=16方向弾 5=誘導弾4個
                                #6=誘導弾8個
        self.division_count = 0       #分裂するまでのカウント
        self.radius_incremental = 0    #回転弾などで使用する半径の増分
        self.division_count_origin = 0 #分裂するまでのカウント(元となる数値です変化はしません)
        self.division_num = 0        #分裂する回数(0なら1回だけ分裂して通常弾に戻る 1なら2分裂(孫分裂),2なら3分裂(ひ孫)後通常弾に戻ります)
        self.angle = 0              #グラフイック表示時に使用する回転角の数値
        self.expansion = 0           #だんだんと広がっていくウェーブやレーザーの広がっていくドット数(毎フレーム)
        self.expansion_flag = 0       #ウェーブやレーザーが最大まで広がったら立てるフラグ
        self.width_max = 0           #拡大ウェーブや拡大レーザーリップルレーザーの横幅の最大値
        self.height_max = 0          #拡大ウェーブや拡大レーザーリップルレーザーの縦幅の最大値
        self.color = 0              #色
        self.anime = 0              #アニメーション用カウンター
    def update(self,enemy_shot_type,enemy_shot_id, x, y,collision_type,width,height, cx,cy, vx,vy,accel,power, hp, count1, count2, timer, speed, intensity, aim,disappearance_count,stop_count,priority,turn_theta,search_flag,rotation_omega,rotation_omega_incremental,radius,radius_max,division_type,division_count,radius_incremental,division_count_origin,division_num,angle,expansion,expansion_flag,width_max,height_max,color,anime):
        self.enemy_shot_type = enemy_shot_type
        self.enemy_shot_id   = enemy_shot_id
        self.posx = x
        self.posy = y
        self.collision_type = collision_type
        self.width = width
        self.height = height
        self.cx = cx
        self.cy = cy
        self.vx = vx
        self.vy = vy
        self.accel = accel
        self.power = power
        self.hp = hp
        self.count1 = count1
        self.count2 = count2
        self.timer = timer
        self.speed = speed
        self.intensity = intensity
        self.aim = aim
        self.disappearance_count = disappearance_count
        self.stop_count = stop_count
        self.priority = priority
        self.turn_theta = turn_theta
        self.search_flag = search_flag
        self.rotation_omega = rotation_omega
        self.rotation_omega_incremental = rotation_omega_incremental
        self.radius = radius
        self.radius_max = radius_max
        self.division_type = division_type
        self.division_count = division_count
        self.radius_incremental = radius_incremental
        self.division_count_origin = division_count_origin
        self.division_num = division_num
        self.angle = angle
        self.expansion = expansion
        self.expansion_flag = expansion_flag
        self.width_max = width_max
        self.height_max = height_max
        self.color = color
        self.anime = anime
class Explosion:#爆発のクラス設定
    def __init__(self):
        self.explosion_type = 0 #爆発の種類
        self.priority = 0      #描画優先度
        self.posx = 0 #x座標
        self.posy = 0 #y座標
        self.vx = 0   #速度(ベクトル)
        self.vy = 0
        self.explotion_count = 0 #アニメーションパターン数
        self.return_bullet_type = 0  #打ち返し弾の種類 0=打ち返しなし 1=爆発直後に自機狙い弾1個 2=爆発直後に自機狙い弾1個+爆発の終わりに自機を狙う弾1個
        self.return_buller_count = 0 #打ち返し弾を生み出すまでのカウントタイマー(0になったら打ち返し弾を育成する)
        self.x_reverse = 0         #x軸方向(横)反転フラグ1=通常表示 -1=横に反転する
        self.y_reverse = 0         #y軸方向(横)反転フラグ1=通常表示 -1=縦に反転する
    def update(self,explosion_type,priority,x,y,vx,vy,explosion_count,return_bullet_type,return_buller_count,x_reverse,y_reverse):
        self.explosion_type = explosion_type
        self.priority = priority
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.explosion_count = explosion_count
        self.return_bullet_type = return_bullet_type
        self.return_buller_count = return_buller_count
        self.x_reverse = x_reverse
        self.y_reverse = y_reverse
class Particle:#パーティクル（粒子）クラスの設定
    def __init__(self):
        self.particle_type = 0 #パーティクルの種類
        self.priority = 0      #描画優先度
        self.posx = 0 #x座標
        self.posy = 0 #y座標
        self.size = 0 #大きさ
        self.vx = 0 #速度(ベクトル)
        self.vy = 0
        self.life = 0 #パーティクルの生存期間
        self.wait = 0 #ウェイト(どれだけその場所に停止し続けるのかのウェイトカウンター)
        self.color = 0 #パーティクルの色
    def update(self,particle_type,priority,x,y,size,vx,vy,life,wait,color):
        self.particle_type = particle_type
        self.priority = priority
        self.posx = x
        self.posy = y
        self.size = size
        self.vx = vx
        self.vy = vy
        self.life = life
        self.wait = wait
        self.color = color
class Background_object:#背景の物体(背景オブジェクト）クラスの設定 (雲や鳥や泡や木葉や背景を移動する艦隊とか当たり判定の無い大き目の物体)
    def __init__(self):
        self.background_object_type = 0 #背景オブジェクトの種類
        self.posx,self.posy = 0,0 #x,y座標
        self.size         = 0   #大きさ
        self.ax,self.ay    = 0,0 #加速度
        self.bx,self.by    = 0,0
        self.cx,self.cy    = 0,0
        self.dx,self.dy    = 0,0
        self.vx,self.vy    = 0,0 #速度(ベクトル)
        self.width        = 0   #横
        self.height        = 0   #縦
        self.life         = 0   #生存時間
        self.wait         = 0   #停止時間
        self.color        = 0   #色
        self.speed        = 0   #速度(倍率)
        self.direction     = 0   #方向
        self.flag1,self.flag2,self.flag3    = 0,0,0 #フラグ1~3
        self.count1,self.count2,self.count3 = 0,0,0 #カウント1~3
        self.animation_number1,self.animation_number2,self.animation_number3 = 0,0,0 #アニメーション番号1~3
    def update(self,background_object_type,
            posx,posy,
            size,
            ax,ay, bx,by, cx,cy, dx,dy, vx,vy,
            width,height,
            life,wait,color,speed,direction,
            flag1,flag2,flag3,
            count1,count2,count3,
            animation_number1,animation_number2,animation_number3
            ):
        self.background_object_type = background_object_type
        self.posx,self.posy = posx,posy
        self.size         = size
        self.ax,self.ay    = ax,ay
        self.bx,self.by    = bx,by
        self.cx,self.cy    = cx,cy
        self.dx,self.dy    = dx,dy
        self.vx,self.vy    = vx,vy
        self.width        = width
        self.height        = height
        self.life         = life
        self.wait         = wait
        self.color        = color
        self.speed        = speed
        self.direction     = direction
        self.flag1,self.flag2,self.flag3    = flag1,flag2,flag3
        self.count1,self.count2,self.count3 = count1,count2,count3
        self.animation_number1,self.animation_number2,self.animation_number3 = animation_number1,animation_number2,animation_number3
class Window: #メッセージ表示ウィンドウのクラスの設定
    def __init__(self):
        self.window_id = 0          #それぞれのウィンドウに与えられるIDです
        self.window_id_sub = 0      #ウィンドウIDに対しての補助的なIDです(はい」「いいえ」などの2択メニューとかで使用)
        self.window_type = 0        #ウィンドウの種類です
        self.window_frame = 0       #ウィンドウのフレーム(外枠)の種類です WINDOW_FRAME_NORMAL=通常枠ありのウィンドウ WINDOW_FRAME_NONE=枠無しBGのみのウィンドウ
        self.window_bg = 0          #ウィンドウの下地(主に背景の事です) 0=シースルー 1=完全な青地 2=ちょっとシースルー
        self.window_priority = 0    #描画優先度 0~4番最前面に表示 0=手前 値が増えるごとに奥方向 初期値は6とする
        self.open_direction = 0     #ウィンドウが開いて行く方向 (通常は左上から右下へ開いて行く)
        self.close_direction = 0    #ウィンドウが閉まっていく方向(通常右下から左上へ閉まって行く)
        self.window_status = 0      #ウィンドウの現在の状態を表しますステータスです WINDOW_OPEN=ウィンドウ開き中 WINDOW_CLOSE=ウィンドウ閉じ中
                                    #                                           WINDOW_WRITE_MESSAGE=メッセージテキスト表示中
        self.between_line = 0       #テキスト表示時の行と行の間隔(通常は7ドット)
        self.title_text = []                      #タイトルが入ります
        self.item_text       = [[] for i in range(12)] #アイテムテキスト(選択メニューの項目文章)が入ります
        self.item_kanji_text = [[] for i in range(12)] #アイテムテキスト(選択メニューの項目文章)が入ります(日本語)
        self.edit_text    = []                      #編集できるテキストが入ります
        self.animation_text = []                    #アニメーション表示されるテキストが入ります
        self.scroll_text  = []                      #スクロール表示されるテキストが入ります
        self.script       = []                      #スクリプト(書記系)が入ります
        
        self.posx = 0          #現在のウィンドウの座標(posx,posy)
        self.posy = 0
        self.dx = 0            #移動先の座標(destination_x,y)
        self.dy = 0
        self.width = 0         #現在のウィンドウの横幅と縦幅(width,height)最初は0でだんだんと(open_width,open_height)に近づいていきます
        self.height = 0
        self.open_width = 0    #ウィンドウが完全に開いた状態の横幅と縦幅(width,heighがこの値になったらウィンドウオープン完了)
        self.open_height = 0   
        self.change_x = 0      #ウィンドウを開閉する時の変化ドット数
        self.change_y = 0
        self.open_speed  = 0   #ウィンドウを開くスピード (change_x,change_y)に掛け合わされます
        self.close_speed = 0   #ウィンドウを閉じるスピード(change_x,change_y)に掛け合わされます
        self.open_accel  = 0   #ウィンドウオープン時の加速度(毎フレームごとopen_speedと掛け合わされた数値がopen_speedに入ります)
        self.close_accel = 0   #ウィンドウクローズ時の加速度(毎フレームごとclose_speedと掛け合わされた数値がclose_speedに入ります)
        self.marker = 0        #マーカー(印)用フラグ      予約用
        self.color = 0         #ウィンドウの色            予約用
        self.vx = 0            #ウィンドウの速度(vx,vy)
        self.vy = 0
        self.vx_accel = 0      #速度に掛け合わせる加速度(accel)
        self.vy_accel = 0
        self.wait_count = 0    #ウェイトカウント(このカウントが0になった時点でvx,vy,vx_accel,vy_accelの掛け合わせを始める)1フレームごとに1減算され0まで減少します
        
        self.ok_button_disp_flag = 0  #OKボタン(決定ボタン)を表示するかどうかのフラグ DISP_OFF=0=表示しない DISP_ON=1=表示する
        self.ok_button_x = 0          #OKボタンを表示する座標(オフセット値)
        self.ok_button_y = 0
        self.ok_button_size = 0       #OKボタンのサイズ
        
        self.no_button_disp_flag = 0  #NOボタン(決定ボタン)を表示するかどうかのフラグ DISP_OFF=0=表示しない DISP_ON=1=表示する
        self.no_button_x = 0          #NOボタンを表示する座標(オフセット値)
        self.no_button_y = 0
        self.no_button_size = 0       #NOボタンのサイズ
        
        self.cursor_move_se   = 0  #カーソルを動かしたときの効果音
        self.cursor_push_se   = 0  #カーソルでボタンを押したときの効果音
        self.cursor_ok_se     = 0  #カーソルでokボタンを押したときの効果音
        self.cursor_cancel_se = 0  #カーソルでキャンセルボタンを押したときの効果音
        self.cursor_bounce_se = 0  #カーソルが障害物に当たった時の跳ね返り効果音
        
        self.ship_equip_medal_disp_flag = 0        #ship_listに含まれている装備メダルを表示するかどうかのフラグ(今現在選択中の機体のみメダル表示されます)
        
        self.ship_list                = []   #所有している機体のリストが入ります
        self.ship_medal_list          = []   #所有している機体の「装備中メダル」をどう表示するのかを指し示すリストが入ります
        self.weapon_list              = []   #所有している武器のリストが入ります
        self.weapon_graph_list        = []   #所有しているの武器グラフイックデータを指し示すリストが入ります
        self.sub_weapon_list          = []   #所有しているのサブウェポンリストが入ります
        self.sub_weapon_graph_list    = []   #所有しているのサブウェポンのグラフイックデータを指し示すリストが入ります
        self.missile_list             = []   #所有しているのミサイルリストが入ります
        self.missile_graph_list       = []   #所有しているのミサイルのグラフイックデータを指し示すリストが入ります
        self.medal_list               = []   #所有しているのメダルリストが入ります
        self.medal_graph_list         = []   #所有しているのメダルのグラフイックデータを指し示すリストが入ります
        self.item_list                = [[] for i in range(128)] #所有しているのアイテムリストが入ります
        self.item_graph_list          = [[] for i in range(128)] #所有しているのアイテムのグラフイックデータを指し示すリストが入ります
        self.flag_list                = [[] for i in range(128)] #各フラグ群のリストが入ります
        self.graph_list               = [[] for i in range(128)] #ウィンドウに表示するグラフイックデータチップを指し示すリストが入ります
        self.time_counter_list        = [[] for i in range(128)] #ウィンドウに表示する時間系のカウンターや色んなカウンターを指し示すリストが入ります
        
        self.equip_medal_graph_list   = []   #各機体が装備しているメダルのグラフイックデータを指し示すリストが入ります
        self.equip_medal_comment_list = []   #各機体が装備しているメダルの説明文(コメント)データを指し示すリストが入ります
        
        self.comment_flag           = 0   #カーソルが現在指し示しているアイテムの説明文を表示するかどうかのフラグ(全体管理)
        self.comment_ox_eng         = 0   #アイテムの説明文を表示する座標(英語)(comment_ox_eng,comment_oy_eng)(ウィンドウの座標からのオフセット値となります)
        self.comment_oy_eng         = 0
        self.comment_ox_jpn         = 0   #アイテムの説明文を表示する座標(日本語)(comment_ox_jpn,comment_oy_jpn)(ウィンドウの座標からのオフセット値となります)
        self.comment_oy_jpn         = 0
        self.comment_disp_flag      = []  #個々のアイテムの説明文を表示するかのフラグcomment_list_eng,comment_list_jpn,item_idのリスト群のそれぞれの座標位置のアイテムが1セットとなります
        self.comment_list_eng       = []  #アイテムの説明文(英語)
        self.comment_list_jpn       = []  #アイテムの説明文(日本語)
        self.item_id                = []  #カーソル位置に存在するアイテムIDナンバー
    def update(self,window_id,window_id_sub,window_type,window_frame,window_bg,window_priority,open_direction,close_direction,window_status,\
        between_line,\
        
        title_text,\
        item_text,\
        item_kanji_text,\
        edit_text,\
        animation_text,\
        scroll_text,\
        script,\
        
        x,y,dx,dy,width,height,open_width,open_height,change_x,change_y,open_speed,close_speed,open_accel,close_accel,marker,color,\
        vx,vy,vx_accel,vy_accel,wait_count,\
        ok_button_disp_flag,ok_button_x,ok_button_y,ok_button_size,\
        no_button_disp_flag,no_button_x,no_button_y,no_button_size,\
        cursor_move_se,cursor_push_se,cursor_ok_se,cursor_cancel_se,cursor_bounce_se,\
        
        ship_equip_medal_disp_flag,\
        
        ship_list,ship_medal_list,\
        weapon_list,weapon_graph_list,\
        sub_weapon_list,sub_weapon_graph_list,\
        missile_list,missile_graph_list,\
        medal_list,medal_graph_list,\
        item_list,item_graph_list,\
        flag_list,graph_list,time_counter_list,\
        
        equip_medal_graph_list,\
        equip_medal_comment_list,\
        
        comment_flag,comment_ox_eng,comment_oy_eng,comment_ox_jpn,comment_oy_jpn,comment_disp_flag,comment_list_eng,comment_list_jpn,item_id ):
        
        self.window_id = window_id
        self.window_id_sub = window_id_sub
        self.window_type = window_type
        self.window_frame = window_frame
        self.window_bg = window_bg
        self.window_priority = window_priority
        self.open_direction = open_direction
        self.close_direction = close_direction
        self.window_status = window_status
        
        self.between_line = between_line
        
        self.title_text   = title_text
        self.item_text    = item_text
        self.item_kanji_text = item_kanji_text
        self.edit_text    = edit_text
        self.animation_text = animation_text
        self.scroll_text  = scroll_text
        self.script       = script
        
        self.posx = x
        self.posy = y
        self.dx = dx
        self.dy = dy
        self.width  = width
        self.height = height
        self.open_width  = open_width
        self.open_height = open_height
        self.change_x = change_x
        self.change_y = change_y
        self.open_speed  = open_speed
        self.close_speed = close_speed
        self.open_accel  = open_accel
        self.close_accel = close_accel
        self.marker = marker
        self.color = color
        self.vx = vx
        self.vy = vy
        self.vx_accel = vx_accel
        self.vy_accel = vy_accel
        self.wait_count = wait_count
        
        self.ok_button_disp_flag = ok_button_disp_flag   
        self.ok_button_x = ok_button_x      
        self.ok_button_y = ok_button_y
        self.ok_button_size = ok_button_size       
        
        self.no_button_disp_flag = no_button_disp_flag  
        self.no_button_x = no_button_x 
        self.no_button_y = no_button_y
        self.no_button_size = no_button_size
        
        self.cursor_move_se   = cursor_move_se
        self.cursor_push_se   = cursor_push_se
        self.cursor_ok_se     = cursor_ok_se
        self.cursor_cancel_se = cursor_cancel_se
        self.cursor_bounce_se = cursor_bounce_se
        
        self.ship_equip_medal_disp_flag = ship_equip_medal_disp_flag
        
        self.ship_list             = ship_list
        self.ship_medal_list       = ship_medal_list
        self.weapon_list           = weapon_list
        self.weapon_graph_list     = weapon_graph_list
        self.sub_weapon_list       = sub_weapon_list
        self.sub_weapon_graph_list = sub_weapon_graph_list
        self.missile_list          = missile_list
        self.missile_graph_list    = missile_graph_list
        self.medal_list            = medal_list
        self.medal_graph_list      = medal_graph_list
        self.item_list             = item_list
        self.item_graph_list       = item_graph_list
        self.flag_list             = flag_list
        self.graph_list            = graph_list
        self.time_counter_list     = time_counter_list
        
        equip_medal_graph_list     = equip_medal_graph_list
        equip_medal_comment_list   = equip_medal_comment_list
        
        self.comment_flag      = comment_flag
        self.comment_ox_eng    = comment_ox_eng
        self.comment_oy_eng    = comment_oy_eng
        self.comment_ox_jpn    = comment_ox_jpn
        self.comment_oy_jpn    = comment_oy_jpn
        self.comment_disp_flag = comment_disp_flag
        self.comment_list_eng  = comment_list_eng
        self.comment_list_jpn  = comment_list_jpn
        self.item_id           = item_id
class Cursor: #メッセージ表示ウィンドウで使用するカーソルのデータ群のクラス設定
    def __init__(self): #コンストラクタ
        self.window_id = 0         #このウィンドウIDがアクティブになったらこのカーソルデータを使用してカーソルを表示開始します
        self.cursor_type = 0       #セレクトカーソルの種類
        self.posx = 0              #セレクトカーソルのx座標
        self.posy = 0              #セレクトカーソルのy座標
        self.step_x = 0            #横方向の移動ドット数
        self.step_y = 0            #縦方向の移動ドット数
        self.page = 0              #いま指し示しているページナンバー
        self.page_max = 0          #セレクトカーソルで捲ることが出来る最多ページ数
        self.item_x = 0            #いま指し示しているアイテムナンバーx軸方向
        self.item_y = 0            #いま指し示しているアイテムナンバーy軸方向
        self.max_item_x = 0        #x軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.max_item_y = 0        #y軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.decision_item_x = -1  #ボタンが押されて「決定」されたアイテムのナンバーx軸方向 -1は未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.decision_item_y = -1  #ボタンが押されて「決定」されたアイテムのナンバーy軸方向 -1は未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.color = 0             #セレクトカーソルの色
        self.menu_layer = 0        #現在選択中のメニューの階層の数値が入ります
        self.move_direction = 0    #セレクトカーソルがどう動かせることが出来るのか？の状態遷移変数です
    def update(self,window_id,cursor_type,x,y,step_x,step_y,page,page_max,item_x,item_y,max_item_x,max_item_y,decision_item_x,decision_item_y,color,menu_layer,move_direction):
        self.window_id = window_id
        self.cursor_type = cursor_type
        self.posx = x
        self.posy = y
        self.step_x = step_x
        self.step_y = step_y
        self.page = page
        self.page_max = page_max
        self.item_x = item_x
        self.item_y = item_y
        self.max_item_x = max_item_x
        self.max_item_y = max_item_y
        self.decision_item_x = decision_item_x
        self.decision_item_y = decision_item_y
        self.color = color
        self.menu_layer = menu_layer
        self.move_direction = move_direction
class Obtain_item:#手に入れるアイテム類（パワーアップ勲章とかコインアイテムとか）のクラス設定
    def __init__(self):
        self.item_type = 0                  #アイテムのタイプ 1=ショットパワーアップ 2=ミサイルパワーアップ 3=シールドパワーアップ
                                            #これ以外はパワーアップアイテム類のtype定数の定義を参照してください
        self.posx = 0                       #x座標
        self.posy = 0                       #y座標
        self.vx = 0                         #速度ベクトル
        self.vy = 0
        self.width = 0                      #横の大きさ
        self.height = 0                     #縦の大きさ
        self.color = 0                      #色
        self.intensity = 0                  #振れの度合い
        self.timer = 0                      #時間
        self.degree = 0                     #回転角度 度数法（主にこちらを使用するのです！）
        self.radian = 0                     #回転角度 弧度法
        self.speed = 0                      #回転スピード(弧度法0~360度)
        self.radius = 0                     #半径
        self.radius_max = 0                 #半径の最大値(回転半径が変化する物ではこの数値を最大値として設定することにします)
        self.animation_number = 0           #アニメーションパターンのオフセット指定番号用
        self.score = 0                      #得点
        self.shot = 0                       #ショットパワーの増加量
        self.missile = 0                    #ミサイルパワーの増加量
        self.shield = 0                     #シールドパワーの増加量
        self.flag1 = 0                      #フラグ用その１
        self.flag2 = 0                      #フラグ用その２
        self.flag3 = 0                      #フラグ用その３
        self.bounce = 0                     #画面左端で跳ね返って戻ってくる回数(バウンス回数)
        self.status = 0                     #状態遷移用（ステータス）
    def update(self,item_type,x,y,vx,vy,width,height,color,intensity,timer,degree,radian,speed,radius,radius_max,animation_number,score,shot,missile,shield,flag1,flag2,flag3,bounce,status):
        self.item_type = item_type
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height
        self.color = color
        self.intensity = intensity
        self.timer = timer
        self.degree = degree
        self.radian = radian
        self.speed = speed
        self.radius = radius
        self.radius_max = radius_max
        self.animation_number = animation_number
        self.score = score
        self.shot = shot
        self.missile = missile
        self.shield = shield
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.bounce = bounce
        self.status = status
class Enemy_formation: #敵の編隊数のリストのクラス設定
    def __init__(self):
        self.formation_id = 0            #それぞれの編隊に与えられたidナンバー(1~?)(0は単独機で使用してるので編隊では未使用です) 
        self.formation_number = 0         #何機編隊なのか編隊の総数が入ります
        self.on_screen_formation_number = 0 #画面上に存在する編隊数(撃墜されたり画面からいなくなったらだんだん数が減ってきます0になったらリストからインスタンス破棄します)
        self.shoot_down_number = 0        #撃墜するべき編隊総数 (7機編隊なら最初は7で1機撃墜すると1減らしていく、この値が0になったらパワーアップアイテム出現！って事ね)
    def update(self,formation_id,formation_number,on_screen_formation_number,shoot_down_number):
        self.formation_id               = formation_id
        self.formation_number           = formation_number
        self.on_screen_formation_number = on_screen_formation_number
        self.shoot_down_number          = shoot_down_number
class Event_append_request: #早回しなどの敵の追加や乱入中ボス,臨時のスクロールスピードや方向の調整などの追加リクエストが入るリストのクラス設定です
    def __init__(self):
        self.timer = 0      #イベントが開始されるカウントタイマー
        self.event_type = 0 #イベントのタイプ
        self.enemy_type = 0 #敵の種類
        self.posx = 0       #x座標
        self.posy = 0       #y座標
        self.number = 0     #敵の数
    def update(self,timer,event_type,enemy_type,x,y,number):
        self.timer = timer
        self.event_type = event_type
        self.enemy_type = enemy_type
        self.posx = x
        self.posy = y
        self.number = number
class Raster_scroll: #背景でラスタースクロールするときに使用する横ラインのデータ設定値のクラス
    def __init__(self):
        self.scroll_id = 0       #複数のラスタースクロールを動作させる時に使用するidナンバー
        self.raster_type = 0     #ラスタースクロールの種類
        self.priority  = 0       #描画時の優先度
        self.display = 0         #描画するかどうかの判定用 (RASTER_SCROLL_OFF=描画しない RASTER_SCROLL_ON=描画する)
        self.scroll_line_no = 0  #ラスタースクロール時に使用するそれぞれの横ラインの割り当てられた番号(上方向から0~任意の数値)
        self.total_line_num = 0  #どこまでラスタスクロールさせるかの縦軸総ライン数 (scroll_line_noに入る最大値(任意の数値)が入る)
        self.posx = 0            #x座標
        self.posy = 0            #y座標
        self.offset_x = 0        #現在のx座標値に対してのオフセット値
        self.offset_y = 0        #現在の垂直スクロールカウント数に対してのy軸オフセット値
        self.img_bank = 0        #グラフイックパターンのあるイメージバンクの数値
        self.posu = 0            #グラフイックパターンが記録されている横座標(pyxelのblt命令のuの値)
        self.posv = 0            #グラフイックパターンが記録されている縦座標(pyxelのblt命令のvの値)
        self.width = 0           #各ラインを描画するときの横幅の数値(単位はドット)
        self.height = 0          #縦幅(通常は1だけど上下スクロールするときに1ドットだと隙間が出来る可能性があるので2ドットでもいいかも？)
        self.speed = 0           #スクロールスピード
        self.transparent_color=0 #透明色の指定
        self.wave_timer = 0      #ウェーブラスタースクロール用のタイマー
        self.wave_speed = 0      #ウェーブラスタースクロール用のスピード
        self.wave_intensity = 0  #ウェーブラスタースクロール用の振れ幅
    def update(self,scroll_id,raster_type,priority,display,scroll_line_no,total_line_num,
            x,y,offset_x,offset_y,img_bank,u,v,width,height,speed,transparent_color,
            wave_timer,wave_speed,wave_intensity):
        self.scroll_id = scroll_id
        self.raster_type = raster_type
        self.priority = priority
        self.display = display
        self.scroll_line_no = scroll_line_no
        self.total_line_num = total_line_num
        self.posx = x
        self.posy = y
        self.offsrt_x = offset_y
        self.offset_y = offset_y
        self.img_bank = img_bank
        self.posu = u
        self.posv = v
        self.width = width
        self.height = height
        self.speed = speed
        self.transparent_color = transparent_color
        self.wave_timer = wave_timer
        self.wave_speed = wave_speed
        self.wave_intensity = wave_intensity