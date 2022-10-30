###########################################################
#  define_soundクラス                                      #      
###########################################################
# 主にサブBGMや効果音として再生されるサウンドファイルを定義する#
# クラスメソッド                                           #
# 2022 05/08からファイル分割してモジュールとして運用開始      #
###########################################################
import pygame.mixer #pygameのサウンドクラスにアクセスするのでインポート

class define_sound:
    def __init__(self):
        None

    def load_bgm(self):
        self.game_over_bgm = pygame.mixer.Sound("assets/music/facton-Morning-Dreams-3727468_0_1.ogg") #GAME OVER BGMファイルの読み込み