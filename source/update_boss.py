###########################################################
#  update_bossクラス                                      #      
###########################################################
# Appクラスのupdate関数から呼び出される関数群                #
# 主にボスの更新を行うメソッド                               #
# ボスの移動更新、ボスのクリッピング                         #
# 当たり判定は別のクラス(update_collision)で行う             #
# 2022 04/06からファイル分割してモジュールとして運用開始      #
###########################################################
import math         #三角関数などを使用したいのでインポートぉぉおお！
from random import random    #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel        #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from func  import * #汎用性のある関数群のモジュールの読み込み

from update_obj import * #背景オブジェクト更新関数モジュール読み込み(パーティクルで使用)

class update_boss:
    def __init__(self):
        None

    #!各面のボスをBossクラスに定義して出現させる
    def born_boss(self):
        #col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8,1*8,5*8,2*8
        if       self.stage_number == STAGE_MOUNTAIN_REGION:   #1面ボス ブリザーディア
            new_boss = Boss()
            boss_id = 0
            boss_type = BOSS_BREEZARDIA
            boss_status = BOSS_STATUS_MOVE_LEMNISCATE_CURVE
            parts_number = 0
            main_hp = 300
            parts1_hp,parts2_hp,parts3_hp,parts4_hp = 50,50,50,50
            parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
            parts9_hp = 0
            parts1_score,parts2_score,parts3_score = 1,1,1
            parts4_score,parts5_score,parts6_score = 1,1,1
            parts7_score,parts8_score,parts9_score = 1,1,1 
            level = LV00
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,4,0,0,0  #上部メイン主砲
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,30,0,0,0 #前部グリーンレーザー砲
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
            posx,posy = -64,50
            bgx,bgy   = 0,0
            offset_x,offset_y = 0,0
            ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
            width,height = 14*8,6*8
            transparent_color = pyxel.COLOR_PEACH
            tilt_now      = 0
            tilt_max      = 0
            tilt_time_now = 0
            tilt_time     = 0
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h =  5 ,3*8,1*8,1*8
            col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 7*8,2*8,1*8,1*8
            col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 0,0,0,0
            col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 0,0,0,0
            
            col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8  ,1*8+5,    6*8-2,2*8
            col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 2*8  ,4*8  ,    6*8,2*8-2
            col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 7*8  ,3*8  ,   4*8  ,1*8 
            col_main4_x, col_main4_y, col_main4_w, col_main4_h  =   0  ,    0,    0,    0
            col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   0  ,    0,    0,    0
            col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   0  ,    0,    0,    0
            col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   0  ,    0,    0,    0
            col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   0  ,    0,    0,    0
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =10*8 ,5*8,  8,  8
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h =9*8-4,5*8,  8,  8
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h =5*8-3,  2,  8,  8
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h =2*8  ,1*8-6,8,  8
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =    0,  0,  0,  0
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =    0,  0,  0,  0
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =    0,  0,  0,  0
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =    0,  0,  0,  0
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =    0,  0,  0,  0
            
            main_hp_bar_offset_x,main_hp_bar_offset_y    = 8,-3
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 10*8  ,5*8+10
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y =  9*8-4,5*8+10
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y =  5*8-3, -2
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y =  2*8  ,  0
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y =     0,  0
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y =     0,  0
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y =     0,  0
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y =     0,  0
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y =     0,  0
            
            size = 0
            priority = 0
            attack_method = BOSS_ATTACK_FRONT_5WAY
            direction = 0
            reverse = BOSS_GRP_NORMAL
            acceleration = 0
            timer = 0
            degree = 0
            radian = 0
            speed = 0
            radius = 0
            flag1,flag2,flag3,flag4 = 0,0,0,0
            count1,count2,count3,count4 = 0,0,0,0
            parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
            parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
            parts9_flag = 0
            animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
            move_index = 0
            obj_time = 0
            obj_totaltime = 0
            invincible = 0
            anime_speed_now  = 0
            anime_speed_min  = 0
            anime_speed_max  = 0
            anime_speed_init = 0
            display_time_main_hp_bar = 0
            display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
            display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
            display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
            display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
            display_time_parts9_hp_bar = 0
            
            grp_parts1_width,grp_parts1_height = 9,9
            grp_parts1_imgb = 0
            grp_parts1_u,grp_parts1_v = 152,223
            grp_parts1_offset_x,grp_parts1_offset_y = 0,0
            grp_parts1_count,grp_parts1_animation = 0,0
            
            grp_parts2_width,grp_parts2_height = 9,7
            grp_parts2_imgb = 0
            grp_parts2_u,grp_parts2_v = 157,208
            grp_parts2_offset_x,grp_parts2_offset_y = 0,0
            grp_parts2_count,grp_parts2_animation = 0,0
            
            grp_parts3_width,grp_parts3_height = 21,12
            grp_parts3_imgb = 0
            grp_parts3_u,grp_parts3_v = 0,216
            grp_parts3_offset_x,grp_parts3_offset_y = 0,0
            grp_parts3_count,grp_parts3_animation = 0,0
            
            grp_parts4_width,grp_parts4_height = 0,0
            grp_parts4_imgb = 0
            grp_parts4_u,grp_parts4_v = 0,0
            grp_parts4_offset_x,grp_parts4_offset_y = 0,0
            grp_parts4_count,grp_parts4_animation = 0,0
            
            grp_parts5_width,grp_parts5_height = 0,0
            grp_parts5_imgb = 0
            grp_parts5_u,grp_parts5_v = 0,0
            grp_parts5_offset_x,grp_parts5_offset_y = 0,0
            grp_parts5_count,grp_parts5_animation = 0,0
            
            grp_parts6_width,grp_parts6_height = 0,0
            grp_parts6_imgb = 0
            grp_parts6_u,grp_parts6_v = 0,0
            grp_parts6_offset_x,grp_parts6_offset_y = 0,0
            grp_parts6_count,grp_parts6_animation = 0,0
            
            grp_parts7_width,grp_parts7_height = 0,0
            grp_parts7_imgb = 0
            grp_parts7_u,grp_parts7_v = 0,0
            grp_parts7_offset_x,grp_parts7_offset_y = 0,0
            grp_parts7_count,grp_parts7_animation = 0,0
            
            grp_parts8_width,grp_parts8_height = 0,0
            grp_parts8_imgb = 0
            grp_parts8_u,grp_parts8_v = 0,0
            grp_parts8_offset_x,grp_parts8_offset_y = 0,0
            grp_parts8_count,grp_parts8_animation = 0,0
            
            grp_parts9_width,grp_parts9_height = 0,0
            grp_parts9_imgb = 0
            grp_parts9_u,grp_parts9_v = 0,0
            grp_parts9_offset_x,grp_parts9_offset_y = 0,0
            grp_parts9_count,grp_parts9_animation = 0,0
            
            new_boss.update(boss_id,boss_type,boss_status,
                parts_number,
                main_hp,
                parts1_hp,parts2_hp,parts3_hp,parts4_hp,
                parts5_hp,parts6_hp,parts7_hp,parts8_hp,
                parts9_hp,
                parts1_score,parts2_score,parts3_score,
                parts4_score,parts5_score,parts6_score,
                parts7_score,parts8_score,parts9_score,
                level,
                
                weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                
                posx,posy,bgx,bgy,offset_x,offset_y,
                ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                width,height,
                transparent_color,
                
                tilt_now,tilt_max,tilt_time_now,tilt_time,
                
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
                
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
                anime_speed_now,
                anime_speed_min,
                anime_speed_max,
                anime_speed_init,
                
                display_time_main_hp_bar,
                
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar,
                
                grp_parts1_width,grp_parts1_height,
                grp_parts1_imgb,
                grp_parts1_u,grp_parts1_v,
                grp_parts1_offset_x,grp_parts1_offset_y,
                grp_parts1_count,grp_parts1_animation,
                
                grp_parts2_width,grp_parts2_height,
                grp_parts2_imgb,
                grp_parts2_u,grp_parts2_v,
                grp_parts2_offset_x,grp_parts2_offset_y,
                grp_parts2_count,grp_parts2_animation,
                
                grp_parts3_width,grp_parts3_height,
                grp_parts3_imgb,
                grp_parts3_u,grp_parts3_v,
                grp_parts3_offset_x,grp_parts3_offset_y,
                grp_parts3_count,grp_parts3_animation,
                
                grp_parts4_width,grp_parts4_height,
                grp_parts4_imgb,
                grp_parts4_u,grp_parts4_v,
                grp_parts4_offset_x,grp_parts4_offset_y,
                grp_parts4_count,grp_parts4_animation,
                
                grp_parts5_width,grp_parts5_height,
                grp_parts5_imgb,
                grp_parts5_u,grp_parts5_v,
                grp_parts5_offset_x,grp_parts5_offset_y,
                grp_parts5_count,grp_parts5_animation,
                
                grp_parts6_width,grp_parts6_height,
                grp_parts6_imgb,
                grp_parts6_u,grp_parts6_v,
                grp_parts6_offset_x,grp_parts6_offset_y,
                grp_parts6_count,grp_parts6_animation,
                
                grp_parts7_width,grp_parts7_height,
                grp_parts7_imgb,
                grp_parts7_u,grp_parts7_v,
                grp_parts7_offset_x,grp_parts7_offset_y,
                grp_parts7_count,grp_parts7_animation,
                
                grp_parts8_width,grp_parts8_height,
                grp_parts8_imgb,
                grp_parts8_u,grp_parts8_v,
                grp_parts8_offset_x,grp_parts8_offset_y,
                grp_parts8_count,grp_parts8_animation,
                
                grp_parts9_width,grp_parts9_height,
                grp_parts9_imgb,
                grp_parts9_u,grp_parts9_v,
                grp_parts9_offset_x,grp_parts9_offset_y,
                grp_parts9_count,grp_parts9_animation
                
                )
            self.boss.append(new_boss)      
            
        elif     self.stage_number == STAGE_ADVANCE_BASE:      #2面ボス ファッティバルガード
            new_boss = Boss()
            boss_id = 0
            boss_type = BOSS_FATTY_VALGUARD
            boss_status = BOSS_STATUS_MOVE_COORDINATE_INIT
            parts_number = 0
            main_hp = 400
            parts1_hp,parts2_hp,parts3_hp,parts4_hp = 70,70,70,200
            parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
            parts9_hp = 0
            parts1_score,parts2_score,parts3_score = 1,1,1
            parts4_score,parts5_score,parts6_score = 1,1,1
            parts7_score,parts8_score,parts9_score = 1,1,1 
            level = LV00
            
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,0,0,0,0
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,0,0,0,0
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
            
            posx,posy = -64,50
            bgx,bgy   = 0,0
            offset_x,offset_y = 0,0
            ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
            width,height = 8*8,5*8
            transparent_color = pyxel.COLOR_PEACH
            
            tilt_now      = 0
            tilt_max      = 0
            tilt_time_now = 0
            tilt_time     = 0
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h = 1*8,1*8,5*8,2*8
            col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 6*8,2*8,1*8,1*8
            col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 3*8,3*8,3*8,1*8
            col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 2*8,  6,  8,  6
            
            col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8+4,1*8,5*8-4,2*8
            col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 6*8+4,2*8,1*8-4,1*8
            col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 3*8+4,3*8,3*8-4,1*8 
            col_main4_x, col_main4_y, col_main4_w, col_main4_h  = 2*8+4,  6,  8-4,  6 
            col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   8,  8,  0,  0 
            col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   8,  8,  0,  0
            col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   8,  8,  0,  0 
            col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   8,  8,  0,  0 
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =   0,2*8,2*8,  8
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h = 1*8,  0,2*8,  8
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h = 1*8,3*8,  8,  8
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h = 6*8,3*8,  8,  8
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =   0,  0,  0,  0
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =   0,  0,  0,  0
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =   0,  0,  0,  0
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =   0,  0,  0,  0
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =   0,  0,  0,  0
            
            main_hp_bar_offset_x  ,main_hp_bar_offset_y   = 8,-2
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 0,24
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y = 0,4
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y = 8,32
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y = 48+2,32
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y = 0,0
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y = 0,0
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y = 0,0
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y = 0,0
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y = 0,0
            
            size = 0
            priority = 0
            attack_method = 0
            direction = 0
            reverse = BOSS_GRP_NORMAL
            acceleration = 0
            timer = 0
            degree = 0
            radian = 0
            speed = 0
            radius = 0
            flag1,flag2,flag3,flag4 = 0,0,0,0
            count1,count2,count3,count4 = 0,0,0,0
            parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
            parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
            parts9_flag = 0
            animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
            move_index = 0
            obj_time = 0
            obj_totaltime = 0
            invincible = 0
            anime_speed_now  = 0
            anime_speed_min  = 0
            anime_speed_max  = 0
            anime_speed_init = 0
            display_time_main_hp_bar = 0
            display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
            display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
            display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
            display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
            display_time_parts9_hp_bar = 0
            
            grp_parts1_width,grp_parts1_height = 0,0
            grp_parts1_imgb = 0
            grp_parts1_u,grp_parts1_v = 0,0
            grp_parts1_offset_x,grp_parts1_offset_y = 0,0
            grp_parts1_count,grp_parts1_animation = 0,0
            
            grp_parts2_width,grp_parts2_height = 0,0
            grp_parts2_imgb = 0
            grp_parts2_u,grp_parts2_v = 0,0
            grp_parts2_offset_x,grp_parts2_offset_y = 0,0
            grp_parts2_count,grp_parts2_animation = 0,0
            
            grp_parts3_width,grp_parts3_height = 0,0
            grp_parts3_imgb = 0
            grp_parts3_u,grp_parts3_v = 0,0
            grp_parts3_offset_x,grp_parts3_offset_y = 0,0
            grp_parts3_count,grp_parts3_animation = 0,0
            
            grp_parts4_width,grp_parts4_height = 0,0
            grp_parts4_imgb = 0
            grp_parts4_u,grp_parts4_v = 0,0
            grp_parts4_offset_x,grp_parts4_offset_y = 0,0
            grp_parts4_count,grp_parts4_animation = 0,0
            
            grp_parts5_width,grp_parts5_height = 0,0
            grp_parts5_imgb = 0
            grp_parts5_u,grp_parts5_v = 0,0
            grp_parts5_offset_x,grp_parts5_offset_y = 0,0
            grp_parts5_count,grp_parts5_animation = 0,0
            
            grp_parts6_width,grp_parts6_height = 0,0
            grp_parts6_imgb = 0
            grp_parts6_u,grp_parts6_v = 0,0
            grp_parts6_offset_x,grp_parts6_offset_y = 0,0
            grp_parts6_count,grp_parts6_animation = 0,0
            
            grp_parts7_width,grp_parts7_height = 0,0
            grp_parts7_imgb = 0
            grp_parts7_u,grp_parts7_v = 0,0
            grp_parts7_offset_x,grp_parts7_offset_y = 0,0
            grp_parts7_count,grp_parts7_animation = 0,0
            
            grp_parts8_width,grp_parts8_height = 0,0
            grp_parts8_imgb = 0
            grp_parts8_u,grp_parts8_v = 0,0
            grp_parts8_offset_x,grp_parts8_offset_y = 0,0
            grp_parts8_count,grp_parts8_animation = 0,0
            
            grp_parts9_width,grp_parts9_height = 0,0
            grp_parts9_imgb = 0
            grp_parts9_u,grp_parts9_v = 0,0
            grp_parts9_offset_x,grp_parts9_offset_y = 0,0
            grp_parts9_count,grp_parts9_animation = 0,0
            
            new_boss.update(boss_id,boss_type,boss_status,
                parts_number,
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
                
                posx,posy,bgx,bgy,offset_x,offset_y,
                ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                width,height,
                transparent_color,
                
                tilt_now,tilt_max,tilt_time_now,tilt_time,
                
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
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
                anime_speed_now,
                anime_speed_min,
                anime_speed_max,
                anime_speed_init,
                display_time_main_hp_bar,
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar,
                
                grp_parts1_width,grp_parts1_height,
                grp_parts1_imgb,
                grp_parts1_u,grp_parts1_v,
                grp_parts1_offset_x,grp_parts1_offset_y,
                grp_parts1_count,grp_parts1_animation,
                
                grp_parts2_width,grp_parts2_height,
                grp_parts2_imgb,
                grp_parts2_u,grp_parts2_v,
                grp_parts2_offset_x,grp_parts2_offset_y,
                grp_parts2_count,grp_parts2_animation,
                
                grp_parts3_width,grp_parts3_height,
                grp_parts3_imgb,
                grp_parts3_u,grp_parts3_v,
                grp_parts3_offset_x,grp_parts3_offset_y,
                grp_parts3_count,grp_parts3_animation,
                
                grp_parts4_width,grp_parts4_height,
                grp_parts4_imgb,
                grp_parts4_u,grp_parts4_v,
                grp_parts4_offset_x,grp_parts4_offset_y,
                grp_parts4_count,grp_parts4_animation,
                
                grp_parts5_width,grp_parts5_height,
                grp_parts5_imgb,
                grp_parts5_u,grp_parts5_v,
                grp_parts5_offset_x,grp_parts5_offset_y,
                grp_parts5_count,grp_parts5_animation,
                
                grp_parts6_width,grp_parts6_height,
                grp_parts6_imgb,
                grp_parts6_u,grp_parts6_v,
                grp_parts6_offset_x,grp_parts6_offset_y,
                grp_parts6_count,grp_parts6_animation,
                
                grp_parts7_width,grp_parts7_height,
                grp_parts7_imgb,
                grp_parts7_u,grp_parts7_v,
                grp_parts7_offset_x,grp_parts7_offset_y,
                grp_parts7_count,grp_parts7_animation,
                
                grp_parts8_width,grp_parts8_height,
                grp_parts8_imgb,
                grp_parts8_u,grp_parts8_v,
                grp_parts8_offset_x,grp_parts8_offset_y,
                grp_parts8_count,grp_parts8_animation,
                
                grp_parts9_width,grp_parts9_height,
                grp_parts9_imgb,
                grp_parts9_u,grp_parts9_v,
                grp_parts9_offset_x,grp_parts9_offset_y,
                grp_parts9_count,grp_parts9_animation
                
                )
            self.boss.append(new_boss)
            
        elif     self.stage_number == STAGE_VOLCANIC_BELT:     #3面ボス マッドクラブンガー
            new_boss = Boss()
            boss_id = 0
            boss_type = BOSS_MAD_CLUBUNGER
            boss_status = BOSS_STATUS_MOVE_COORDINATE_INIT
            parts_number = 0
            main_hp = 400
            parts1_hp,parts2_hp,parts3_hp,parts4_hp =   0,  0,  0,  0
            parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
            parts9_hp = 0
            parts1_score,parts2_score,parts3_score = 1,1,1
            parts4_score,parts5_score,parts6_score = 1,1,1
            parts7_score,parts8_score,parts9_score = 1,1,1 
            level = LV00
            
            weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,0,0,0,0
            weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,0,0,0,0
            weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
            weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
            weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
            
            posx,posy = -64,50
            bgx,bgy   = 0,0
            offset_x,offset_y = 0,0
            ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
            width,height = 6*8,5*8
            transparent_color = pyxel.COLOR_PEACH
            
            tilt_now      = 0
            tilt_max      = 4  #機体が傾くドット数は4ドット
            tilt_time_now = 0
            tilt_time     = 20 #20フレームごとに1ドット傾いていきます
            
            col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h = 1*8,1*8,5*8,2*8
            col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 6*8,2*8,1*8,1*8
            col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 3*8,3*8,3*8,1*8
            col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 2*8,  6,  8,  6
            
            col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8+4,1*8,5*8-4,2*8
            col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 6*8+4,2*8,1*8-4,1*8
            col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 3*8+4,3*8,3*8-4,1*8 
            col_main4_x, col_main4_y, col_main4_w, col_main4_h  = 2*8+4,  6,  8-4,  6 
            col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   8,  8,  0,  0 
            col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   8,  8,  0,  0
            col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   8,  8,  0,  0 
            col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   8,  8,  0,  0 
            
            col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =   0,2*8,2*8,  8
            col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h = 1*8,  0,2*8,  8
            col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h = 1*8,3*8,  8,  8
            col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h = 6*8,3*8,  8,  8
            col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =   0,  0,  0,  0
            col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =   0,  0,  0,  0
            col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =   0,  0,  0,  0
            col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =   0,  0,  0,  0
            col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =   0,  0,  0,  0
            
            main_hp_bar_offset_x  ,main_hp_bar_offset_y   = 8,-2
            
            parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 0,24
            parts2_hp_bar_offset_x,parts2_hp_bar_offset_y = 0,4
            parts3_hp_bar_offset_x,parts3_hp_bar_offset_y = 8,32
            parts4_hp_bar_offset_x,parts4_hp_bar_offset_y = 48+2,32
            parts5_hp_bar_offset_x,parts5_hp_bar_offset_y = 0,0
            parts6_hp_bar_offset_x,parts6_hp_bar_offset_y = 0,0
            parts7_hp_bar_offset_x,parts7_hp_bar_offset_y = 0,0
            parts8_hp_bar_offset_x,parts8_hp_bar_offset_y = 0,0
            parts9_hp_bar_offset_x,parts9_hp_bar_offset_y = 0,0
            
            size = 0
            priority = 0
            attack_method = BOSS_ATTACK_HOMING_LASER
            direction = 0
            # reverse = BOSS_GRP_REVERSE
            reverse = BOSS_GRP_NORMAL
            acceleration = 0
            timer = 0
            degree = 0
            radian = 0
            speed = 0
            radius = 0
            flag1,flag2,flag3,flag4 = 0,0,0,0
            count1,count2,count3,count4 = 0,4,0,6
            parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
            parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
            parts9_flag = 0
            animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
            move_index = 0
            obj_time = 0
            obj_totaltime = 0
            invincible = 0
            anime_speed_now  = 0
            anime_speed_min  = 0
            anime_speed_max  = 6000
            anime_speed_init = 0
            display_time_main_hp_bar = 0
            display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
            display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
            display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
            display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
            display_time_parts9_hp_bar = 0
            
            grp_parts1_width,grp_parts1_height = 0,0
            grp_parts1_imgb = 0
            grp_parts1_u,grp_parts1_v = 0,0
            grp_parts1_offset_x,grp_parts1_offset_y = 0,0
            grp_parts1_count,grp_parts1_animation = 0,0
            
            grp_parts2_width,grp_parts2_height = 0,0
            grp_parts2_imgb = 0
            grp_parts2_u,grp_parts2_v = 0,0
            grp_parts2_offset_x,grp_parts2_offset_y = 0,0
            grp_parts2_count,grp_parts2_animation = 0,0
            
            grp_parts3_width,grp_parts3_height = 0,0
            grp_parts3_imgb = 0
            grp_parts3_u,grp_parts3_v = 0,0
            grp_parts3_offset_x,grp_parts3_offset_y = 0,0
            grp_parts3_count,grp_parts3_animation = 0,0
            
            grp_parts4_width,grp_parts4_height = 0,0
            grp_parts4_imgb = 0
            grp_parts4_u,grp_parts4_v = 0,0
            grp_parts4_offset_x,grp_parts4_offset_y = 0,0
            grp_parts4_count,grp_parts4_animation = 0,0
            
            grp_parts5_width,grp_parts5_height = 0,0
            grp_parts5_imgb = 0
            grp_parts5_u,grp_parts5_v = 0,0
            grp_parts5_offset_x,grp_parts5_offset_y = 0,0
            grp_parts5_count,grp_parts5_animation = 0,0
            
            grp_parts6_width,grp_parts6_height = 0,0
            grp_parts6_imgb = 0
            grp_parts6_u,grp_parts6_v = 0,0
            grp_parts6_offset_x,grp_parts6_offset_y = 0,0
            grp_parts6_count,grp_parts6_animation = 0,0
            
            grp_parts7_width,grp_parts7_height = 0,0
            grp_parts7_imgb = 0
            grp_parts7_u,grp_parts7_v = 0,0
            grp_parts7_offset_x,grp_parts7_offset_y = 0,0
            grp_parts7_count,grp_parts7_animation = 0,0
            
            grp_parts8_width,grp_parts8_height = 0,0
            grp_parts8_imgb = 0
            grp_parts8_u,grp_parts8_v = 0,0
            grp_parts8_offset_x,grp_parts8_offset_y = 0,0
            grp_parts8_count,grp_parts8_animation = 0,0
            
            grp_parts9_width,grp_parts9_height = 0,0
            grp_parts9_imgb = 0
            grp_parts9_u,grp_parts9_v = 0,0
            grp_parts9_offset_x,grp_parts9_offset_y = 0,0
            grp_parts9_count,grp_parts9_animation = 0,0
            
            new_boss.update(boss_id,boss_type,boss_status,
                parts_number,
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
                
                posx,posy,bgx,bgy,offset_x,offset_y,
                ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                width,height,
                transparent_color,
                
                tilt_now,tilt_max,tilt_time_now,tilt_time,
                
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
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
                anime_speed_now,
                anime_speed_min,
                anime_speed_max,
                anime_speed_init,
                display_time_main_hp_bar,
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar,
                
                grp_parts1_width,grp_parts1_height,
                grp_parts1_imgb,
                grp_parts1_u,grp_parts1_v,
                grp_parts1_offset_x,grp_parts1_offset_y,
                grp_parts1_count,grp_parts1_animation,
                
                grp_parts2_width,grp_parts2_height,
                grp_parts2_imgb,
                grp_parts2_u,grp_parts2_v,
                grp_parts2_offset_x,grp_parts2_offset_y,
                grp_parts2_count,grp_parts2_animation,
                
                grp_parts3_width,grp_parts3_height,
                grp_parts3_imgb,
                grp_parts3_u,grp_parts3_v,
                grp_parts3_offset_x,grp_parts3_offset_y,
                grp_parts3_count,grp_parts3_animation,
                
                grp_parts4_width,grp_parts4_height,
                grp_parts4_imgb,
                grp_parts4_u,grp_parts4_v,
                grp_parts4_offset_x,grp_parts4_offset_y,
                grp_parts4_count,grp_parts4_animation,
                
                grp_parts5_width,grp_parts5_height,
                grp_parts5_imgb,
                grp_parts5_u,grp_parts5_v,
                grp_parts5_offset_x,grp_parts5_offset_y,
                grp_parts5_count,grp_parts5_animation,
                
                grp_parts6_width,grp_parts6_height,
                grp_parts6_imgb,
                grp_parts6_u,grp_parts6_v,
                grp_parts6_offset_x,grp_parts6_offset_y,
                grp_parts6_count,grp_parts6_animation,
                
                grp_parts7_width,grp_parts7_height,
                grp_parts7_imgb,
                grp_parts7_u,grp_parts7_v,
                grp_parts7_offset_x,grp_parts7_offset_y,
                grp_parts7_count,grp_parts7_animation,
                
                grp_parts8_width,grp_parts8_height,
                grp_parts8_imgb,
                grp_parts8_u,grp_parts8_v,
                grp_parts8_offset_x,grp_parts8_offset_y,
                grp_parts8_count,grp_parts8_animation,
                
                grp_parts9_width,grp_parts9_height,
                grp_parts9_imgb,
                grp_parts9_u,grp_parts9_v,
                grp_parts9_offset_x,grp_parts9_offset_y,
                grp_parts9_count,grp_parts9_animation
                
                )
            self.boss.append(new_boss)

    ####################################ボス関連の処理関数########################################
    #!ボスの更新
    def boss(self):
        boss_count = len(self.boss)
        for i in reversed (range(boss_count)):
            if   self.boss[i].boss_type == BOSS_FATTY_VALGUARD: #2面ボス  ファッティ・バルガード  ############################
                if   self.boss[i].status == BOSS_STATUS_MOVE_COORDINATE_INIT:  #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                    func.boss_get_bezier_curve_coordinate(self,i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                    self.boss[i].status = BOSS_STATUS_MOVE_BEZIER_CURVE #状態遷移を「ベジェ曲線で移動」に設定
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_BEZIER_CURVE:     #「ベジェ曲線」で移動」
                    t = self.boss[i].obj_time / self.boss[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        self.boss[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする                    
                        self.boss[i].move_index += 1 #目的座標のリストのインデックスを1進める
                        if self.boss_move_data1[self.boss[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                            self.boss[i].move_index = 0 #リストインデックス値を0にしてリセットする
                        func.boss_get_bezier_curve_coordinate(self,i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                        t = self.boss[i].obj_time / self.boss[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                    
                    #          A(移動元)--D(移動先)
                    #            \    点P /     
                    #(AとQの内分点)P1\     /P2(QとDの内分点)    
                    #              \   /
                    #               Q(制御点)
                    #
                    #内分の公式からP1の座標は((1-t)ax+t*qx,(1-t)ay+t*qy)
                    #           P2の座標は((1-t)qx+t*dx,(1-t)qy+t*dy)
                    #したがってPの座標も内分の公式から求められる
                    #P1の座標を(p1x,p1y),P2の座標を(p2x,p2y)とすると点Pの座標は
                    #        ((1-t)p1x+t*p2x,(1-t)p1y+t*p2y)となり
                    #先に求めたP1,P2を代入してやると
                    #        ((1-t)(1-t)ax+t*qx+t*(1-t)qx+t*dx,(1-t)(1-t)ay+t*qy+t*(1-t)qy+t*dy)となる
                    p1x = (1-t) * self.boss[i].ax + t * self.boss[i].qx
                    p1y = (1-t) * self.boss[i].ay + t * self.boss[i].dy
                    p2x = (1-t) * self.boss[i].qx + t * self.boss[i].dx
                    p2y = (1-t) * self.boss[i].qy + t * self.boss[i].dy
                    
                    px = (1-t) * p1x + t * p2x
                    py = (1-t) * p1y + t * p2y
                    
                    self.boss[i].posx = px 
                    self.boss[i].posy = py
                    
                    self.boss[i].speed = self.boss[i].speed * self.boss[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします
                    if self.boss[i].speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                        self.boss[i].speed = 0.2
                    self.boss[i].obj_time += self.boss[i].speed #タイムフレーム番号をスピード分加算していく
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方で「レムニスケート曲線」を使った上下運動をさせる
                    self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                    if self.boss[i].degree >= 360:
                        self.boss[i].degree = 0
                    
                    #(x**2+y**2)**2=2a**2(x**2-y**2) (ベルヌーイのレムニスケート曲線)を使用
                    #極座標を(r,θ）とする
                    #
                    #x**2 + y**2 = r**2
                    #x = r*cos(θ)
                    #y = r*cos(θ)より
                    #(r**2)**2 = 2(r**2(cos(θ)**2) - r**2(sin(θ)**2)
                    #(r**2)**2 = 2r**2(cos(θ)**2 - sin(θ)**2)
                    #
                    #cos(θ)**2 + sin(θ)**2 = 1 尚且つ・・・
                    #cos(θ)**2 - sin(θ)**2 = cos(2θ) となるので・・・
                    #
                    #(r**2)**2 = 2r**2(cos(2θ))
                    #r**2 = 2a2cos(2θ)
                    #となるはず・・・・多分
                    #
                    #
                    #x = sqrt(2)*cos(degree) / (sin(degree)**2+1)
                    #y = sqrt(2)*cos(degree)*sin(degree) / (sin(degree)**2+1)
                    #
                    #？？？「ベルヌーイだよ、レムニスケートは別名ヤコブ・ベルヌーイのレムニスケートとも呼ばれてるよ」
                    #
                    #横スクロールシューティングで縦に倒した状態のレムニスケート曲線を描きたいのでx座標とy座標を入れ替えて使用します
                    self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 50
                    self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 30 + 80
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:       #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:             #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:     #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:           #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS3,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS4,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:         #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機のオートムーブモードをonにして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                               #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if   self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY:            #→ 画面上部を左から右に弧を描いて移動中
                    if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら60フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                    
                    if (pyxel.frame_count % 100) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら100フレーム毎に
                        ex = self.boss[i].posx + 16
                        ey = self.boss[i].posy
                        length = 2
                        speed =  1
                        func.enemy_red_laser(self,ex,ey,length,speed) #レッドレーザービーム発射！
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_RIGHT_GREEN_LASER:     #↑ 背後で下から上に移動中
                    if (pyxel.frame_count % 30) == 0: #30フレーム毎に
                        ex = self.boss[i].posx + 48
                        ey = self.boss[i].posy + 27
                        length = 4
                        speed = -3 #画面左端にボスが居るので右方向にレーザー発射（マイナスのスピードだと反転され右方向に射出される）
                        func.enemy_green_laser(self,ex,ey,length,speed) #グリーンレーザービーム発射！
                    
                    if (pyxel.frame_count % 30) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら30フレーム毎に
                        ex = self.boss[i].posx + 16
                        ey = self.boss[i].posy
                        length = 2
                        speed =  1
                        func.enemy_red_laser(self,ex,ey,length,speed) #レッドレーザービーム発射！
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_AIM_BULLET: #↓ 矢印前方で上から下に移動中
                    if (pyxel.frame_count % int(40 * self.enemy_bullet_interval / 100)) == 0: #40フレーム毎に
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                        
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_aim_bullet(self,ex,ey,0,0,0,0,1)        #狙い撃ち弾発射
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_ARROW:      #← 下部を右から左に弧を描いて移動中
                    if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #60フレーム毎に5way砲台が健在なら
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                    if self.boss[i].posx < 10:
                        if (pyxel.frame_count % 20) == 0: #20フレーム毎に
                            if len(self.enemy) < 400:
                                new_enemy = Enemy()#敵8ツインアローを1機生み出す
                                new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.boss[i].posx + 48,self.boss[i].posy + 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   1,-1,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,1,       0,0,0,0,        E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                self.enemy.append(new_enemy)#リストにアペンド追加！
                
            elif self.boss[i].boss_type == BOSS_BREEZARDIA:     #1面ボス  ブリザーディア         ############################
                #flag1  = 主砲が発射中なのかのフラグ
                #direction = 前進か更新かの方向フラグ(1=前進 0=後進)
                #count1 = 主砲が何発撃ったのか？のカウント用
                #count2 = ボスを破壊した時に真っ二つになる演出全体のフレーム数
                #count3 = 主砲の待ち時間用カウンタ
                #offset_x = x軸のオフセット値
                #weapon2を前部グリーンレーザー砲とします
                if   self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                    if self.boss[i].direction == 0: #x軸の移動方向が後進だったのなら
                        self.boss[i].offset_x -= 0.05 #x軸のオフセット値を減らす
                    else:
                        self.boss[i].offset_x += 0.3 #前進だったのでx軸のオフセット値を増やす
                    
                    self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                    if self.boss[i].degree >= 360:
                        self.boss[i].degree = 0
                    self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 40 + 60
                    self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 80/2 + 20 + self.boss[i].offset_x
                    
                    if self.boss[i].posx > WINDOW_W - 40: #x座標が画面右端を超えたのなら
                        self.boss[i].direction = 0         #方向を後退(0)にする
                    elif self.boss[i].posx < -60:        #x座標が画面左端を超えたのなら
                        self.boss[i].direction = 1         #方向を前進(1)にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:      #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:           #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:    #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:         #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS3,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS4,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします 
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:        #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag             = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time     = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機の移動モードをを「AUTO」にして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                                 #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY: #画面上部を左から右に弧を描いて移動中
                    if (pyxel.frame_count % 120) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら120フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_3way_bullet(self,ex,ey) #前方3way発射！
                    
                    if (pyxel.frame_count % 180) == 0 and self.boss[i].parts4_flag == 1: #上部グリーンカッターが健在なら180フレーム毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -1,0,      1.05,    1,1,    0,0,  0,0,0,            0,   0,0,PRIORITY_BOSS_BACK,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
                    
                    if self.boss[i].weapon1_status == WEAPON_READY and self.boss[i].parts3_flag == 1: #上部主砲が健在で主砲待機中ならば・・
                        if self.boss[i].weapon1_cool_down_time > 0:
                            self.boss[i].weapon1_cool_down_time -= 1 #主砲の休憩時間カウンタを1減らして行く
                        
                        if self.my_x > self.boss[i].posx + 48 and self.my_y < self.boss[i].posy + 4 and self.boss[i].weapon1_cool_down_time == 0: #自機主砲の右上に居るかどうか判別し・・・更に主砲の休憩時間が0以下になったのなら
                            self.boss[i].weapon1_status = WEAPON_FIRE #主砲発射中フラグを建てる
                    
                    if self.boss[i].weapon1_status == WEAPON_FIRE and pyxel.frame_count % self.boss[i].weapon1_interval == 0: #主砲発射中フラグが建っており尚且つweapon1_interval(4フレームごとに)・・
                        posx = self.boss[i].posx + 48
                        posy = self.boss[i].posy + 4
                        func.enemy_aim_bullet_nway(self,posx,posy,20,3, 0,0,0,0) #自機狙い3way発射！
                        
                        self.boss[i].weapon1_rapid_num += 1 #主砲が発射した弾数を1増やす
                        if self.boss[i].weapon1_rapid_num >= 3 + self.enemy_bullet_append: #(3+ランクに応じた追加数)ぶん発射したのならば・・
                            self.boss[i].weapon1_rapid_num = 0    #主砲が発射した弾数をリセット
                            self.boss[i].weapon1_cool_down_time = 600  #主砲の待ち時間用カウンタを設定してやる
                            self.boss[i].weapon1_status  = WEAPON_READY    #主砲発射中フラグを降ろす
                    
                    if self.boss[i].posx <= -30: #x座標がマイナスの時(左画面外)時,は右方向にグリーンレーザーを出す
                        if pyxel.frame_count % self.boss[i].weapon2_interval == 0:
                            ex = self.boss[i].posx + 8*13 +4
                            ey = self.boss[i].posy + 8*4 -3
                            length = 2
                            speed = -2
                            func.enemy_green_laser(self,ex,ey,length,speed)
                
            elif self.boss[i].boss_type == BOSS_MAD_CLUBUNGER:  #3面ボス  マッドクラブンガー     #############################
                #count1 = 現時点でのホーミングレーザーを発射した数
                #count2 = ホーミングレーザーを発射する予定数
                #count3 = 現時点で5way弾を発射した数
                #count4 = 5way弾を発射する予定数
                if   self.boss[i].status == BOSS_STATUS_MOVE_COORDINATE_INIT:  #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                    if not self.boss_bg_move_point or self.boss_test_mode == FLAG_ON: #boss_bg_move_point移動リストが空もしくはボステストモードだったのならば(BGマップに移動ポイントが全く存在してない状態) 公式ではリストが空かどうかを調べる方法はこれが推奨らしい・・・知らなかったDEATH
                        self.boss[i].status = BOSS_STATUS_MOVE_LEMNISCATE_CURVE #状態遷移を「レムニスケート曲線で移動」に設定
                    else:                                                       #移動リストに何らかの座標データがあったのなら
                        func.boss_bg_move_get_bezier_curve_coordinate(self,i)   #ボスをBG背景上でベジェ曲線移動させるために必要な座標をリストから取得する関数の呼び出し
                        self.boss[i].status = BOSS_STATUS_MOVE_BEZIER_CURVE     #状態遷移を「ベジェ曲線で移動」に設定
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_BEZIER_CURVE:     #「ベジェ曲線で移動」
                    t = self.boss[i].obj_time / self.boss[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        print(self.boss[i].move_index)
                        if self.boss[i].move_index >= len(self.boss_bg_move_point) - 2: #移動リストのインデックス値がリストの要素数の数と一致したら、もう通過すべき座標値がないので
                            self.boss[i].status = BOSS_STATUS_MOVE_2POINT_INIT #状態遷移を「2点間移動のポイント設定初期化」に設定
                        else:
                            self.boss[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする                    
                            self.boss[i].move_index += 1 #目的座標のリストのインデックスを1進める
                            
                            func.boss_bg_move_get_bezier_curve_coordinate(self,i) #ボスをBG背景上でベジェ曲線移動させるために必要な座標をリストから取得する関数の呼び出し
                            t = self.boss[i].obj_time / self.boss[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                    
                    #          A(移動元)--D(移動先)
                    #            \    点P /     
                    #(AとQの内分点)P1\     /P2(QとDの内分点)    
                    #              \   /
                    #               Q(制御点)
                    #
                    #内分の公式からP1の座標は((1-t)ax+t*qx,(1-t)ay+t*qy)
                    #           P2の座標は((1-t)qx+t*dx,(1-t)qy+t*dy)
                    #したがってPの座標も内分の公式から求められる
                    #P1の座標を(p1x,p1y),P2の座標を(p2x,p2y)とすると点Pの座標は
                    #        ((1-t)p1x+t*p2x,(1-t)p1y+t*p2y)となり
                    #先に求めたP1,P2を代入してやると
                    #        ((1-t)(1-t)ax+t*qx+t*(1-t)qx+t*dx,(1-t)(1-t)ay+t*qy+t*(1-t)qy+t*dy)となる
                    p1x = (1-t) * self.boss[i].ax + t * self.boss[i].qx
                    p1y = (1-t) * self.boss[i].ay + t * self.boss[i].dy
                    p2x = (1-t) * self.boss[i].qx + t * self.boss[i].dx
                    p2y = (1-t) * self.boss[i].qy + t * self.boss[i].dy
                    
                    px = (1-t) * p1x + t * p2x
                    py = (1-t) * p1y + t * p2y
                    
                    self.boss[i].posx = px - (self.scroll_count - 256 * 8) / 2 #BGマップに仕込まれた通過点ポイントの座標値はキャラ単位なので8倍してドット単位にする そしてスクロールさせたドット数を引いてやる
                    self.boss[i].posy = py
                    
                    self.boss[i].speed = self.boss[i].speed * self.boss[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします
                    if self.boss[i].speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                        self.boss[i].speed = 0.2
                    self.boss[i].obj_time += self.boss[i].speed #タイムフレーム番号をスピード分加算していく
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_2POINT_INIT:      #移動元と移動先の2点間でので移動の為の座標設定初期処理
                    ax,ay = self.boss[i].posx,self.boss[i].posy #現在のボスが居る座標位置を移動元に設定する
                    self.boss[i].ax,self.boss[i].ay = ax,ay
                    
                    #レムニスケート曲線で最初に計算して設定した座標値を移動先に設定する
                    dy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 50
                    dx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 30 + 80
                    self.boss[i].dx,self.boss[i].dy = dx,dy
                    #移動元と移動先の距離dを求める
                    d = math.sqrt((dx-ax) * (dx-ax) + (dy - ay) * (dy - ay))
                    #速度を求める
                    if d == 0: #距離がゼロの時は0で割る処理になってしまいエラーになるのでvx=1 vy=0(右移動)にする
                        vx = 1
                        vy = 0
                    else:
                        vx = (dx - ax) / d
                        vy = (dy - ay) / d
                    
                    self.boss[i].vx,self.boss[i].vy = vx,vy #ボスクラスのメンバ変数vx,vy(速度)に今計算してやった速度を代入する
                    self.boss[i].status = BOSS_STATUS_MOVE_2POINT           #ボスの移動ステータスを「2点間の移動状態」にする
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_2POINT:           #ボスの移動ステータスが「2点間の移動状態」の処理
                    #速度を加算した座標ax,ayを計算する
                    ax = self.boss[i].posx +self.boss[i].vx
                    ay = self.boss[i].posy +self.boss[i].vy
                    #移動先の座標取得
                    dx,dy = self.boss[i].dx,self.boss[i].dy
                    #移動先との距離dを計算する
                    d = math.sqrt((dx-ax) * (dx-ax) + (dy - ay) * (dy - ay))
                    if d<=1: #移動先と現在の座標の距離が1以下なら移動完了！
                        self.boss[i].status = BOSS_STATUS_MOVE_LEMNISCATE_CURVE #ボスの移動ステータスを「レムニスケート曲線で移動」にする
                    
                    self.boss[i].posx,self.boss[i].posy = ax,ay #ボスの位置座標更新！
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                    old_posy = self.boss[i].posy #移動前のy座標を保存しておく
                    self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                    if self.boss[i].degree >= 360:
                        self.boss[i].degree = 0
                    
                    #(x**2+y**2)**2=2a**2(x**2-y**2) (ベルヌーイのレムニスケート曲線)を使用
                    #極座標を(r,θ）とする
                    #
                    #x**2 + y**2 = r**2
                    #x = r*cos(θ)
                    #y = r*cos(θ)より
                    #(r**2)**2 = 2(r**2(cos(θ)**2) - r**2(sin(θ)**2)
                    #(r**2)**2 = 2r**2(cos(θ)**2 - sin(θ)**2)
                    #
                    #cos(θ)**2 + sin(θ)**2 = 1 尚且つ・・・
                    #cos(θ)**2 - sin(θ)**2 = cos(2θ) となるので・・・
                    #
                    #(r**2)**2 = 2r**2(cos(2θ))
                    #r**2 = 2a2cos(2θ)
                    #となるはず・・・・多分
                    #
                    #
                    #x = sqrt(2)*cos(degree) / (sin(degree)**2+1)
                    #y = sqrt(2)*cos(degree)*sin(degree) / (sin(degree)**2+1)
                    #
                    #？？？「ベルヌーイだよ、レムニスケートは別名ヤコブ・ベルヌーイのレムニスケートとも呼ばれてるよ」
                    #
                    #横スクロールシューティングで縦に倒した状態のレムニスケート曲線を描きたいのでx座標とy座標を入れ替えて使用します
                    self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 50
                    self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 30 + 80
                    
                    #上下(ボスさんからみたら左右)のブースターユニットの傾きの計算
                    if int(pyxel.frame_count % self.boss[i].tilt_time - abs(self.boss[i].tilt_now)) == 0 : #現在のフレームカウントが(tilt_time - self.boss[i].tilt_now)で割り切れる数値の時に傾け動作を開始する 0で割ることに成らないよう注意せよ！
                        if old_posy > self.boss[i].posy: #下向きか上向き移動かの判別
                            self.boss[i].tilt_now += 1
                            if self.boss[i].tilt_now >= self.boss[i].tilt_max:    #もし傾きドット数の最大値を超えていたのなら最大値に丸める
                                self.boss[i].tilt_now = self.boss[i].tilt_max
                        else:
                            self.boss[i].tilt_now -= 1
                            if self.boss[i].tilt_now <= -(self.boss[i].tilt_max): #もし傾きドット数の最小値を超えていたのなら最小値に丸める(self.boss[i].tilt_maxにマイナス符号をつけて最小値として扱ってます)
                                self.boss[i].tilt_now = -(self.boss[i].tilt_max)
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:       #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:             #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].anime_speed_now += 1 #ブースターエンジン回転用のアニメスピードを遅くしていくためのカウンターをインクリメント
                    if self.boss[i].anime_speed_now >= self.boss[i].anime_speed_max: #最大値を超えないように補正する
                        self.boss[i].anime_speed_now = self.boss[i].anime_speed_max
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:     #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:           #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + func.s_rndint(self,0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + func.s_rndint(self,0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS3,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        update_obj.append_particle(self,PARTICLE_BOSS_DEBRIS4,PRIORITY_FRONT,self.boss[i].posx + 30 + func.s_rndint(self,0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:         #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機のオートムーブモードをonにして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                               #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if   self.boss[i].attack_method == BOSS_ATTACK_HOMING_LASER:            #ホーミングレーザー攻撃
                    if (pyxel.frame_count % 180)  == 0:                                 #3秒毎に
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 3*8
                        performance = 20                                                #誘導性能の数値を代入
                        func.enemy_homing_laser(self,ex,ey,performance)                 #ホーミングレーザー発射！
                        
                        if self.boss[i].main_hp <= 200:                              #ボスのHPが200以下なら
                            if self.boss[i].posy >= self.my_y:                       #ボスが自機より下にいたのなら
                                func.enemy_up_laser(self,ex,ey,-0.3,-0.3,0.2,80,3)   #アップレーザー発射
                            else:                                                    #ボスが自機より上の場合は
                                func.enemy_down_laser(self,ex,ey,-0.3,0.3,0.2,80,3)  #ダウンレーザー発射
                        
                        self.boss[i].count1 += 1 #ホーミングレーザーを発射した数をインクリメント
                        if self.boss[i].count1 >= self.boss[i].count2:
                            self.boss[i].count1 = 0
                            self.boss[i].attack_method = BOSS_ATTACK_FRONT_5WAY_AIM_BULLET
                
                if  self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_AIM_BULLET:
                    if (pyxel.frame_count % 100) == 0 :                               #100フレーム毎に
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_forward_5way_bullet(self,ex,ey) #前方5way発射！
                        
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        func.enemy_aim_bullet(self,ex,ey,0,0,0,0,1) #狙い撃ち弾発射
                        self.boss[i].count3 += 1 #5way+AIM弾を発射した数をインクリメント
                        if self.boss[i].count3 >= self.boss[i].count4:
                            self.boss[i].count3 = 0
                            self.boss[i].attack_method = BOSS_ATTACK_HOMING_LASER


