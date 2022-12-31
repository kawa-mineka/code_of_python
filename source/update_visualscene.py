###########################################################
#  update_visualsceneクラス                                #      
###########################################################
#  Appクラスのupdate関数から呼び出される関数群               #
#  主にビジュアルシーンの更新を行う関数(メソッド？）ですよ～♪#
# 2022 12/30からモジュールとして運用開始                   #
###########################################################

import math               #三角関数などを使用したいのでインポートぉぉおお！
from random import random #random.random() と呼ぶと、0から1の範囲(1は含まない)のランダムな実数が返される(主にパーティクル系で使用します)
import pyxel              #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン

from const             import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from const_visualscene import * #主にビジュアルシーンクラスで使用する定数定義の読み込み

from func        import * #汎用性のある関数群のモジュールの読み込み

class update_visualscene:
    def __init__(self):
        None

    #ビジュアルシーンの更新
    def visualscene(self):
        """
        ビジュアルシーンの更新
        """
        visualscene_count = len(self.visualscene)
        for i in range(visualscene_count):
            #スクロールテキストに何かテキストが入っている時はスクロールドットカウンタを増やしていく
            if self.visualscene[i].scroll_text != "":
                # print (self.visualscene[i].scroll_text)
                if  self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_ENG] != 0: #スクロールスピードが0の時は何もしない(0で割り算をしてエラーになっちゃう為)
                    spd = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_ENG]
                    if int(pyxel.frame_count % spd) == 0:
                        self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] += 1  #スクロールテキストのスクロールしたドットカウンタを1増やしていく
                        if self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] >= self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_MAX_ENG]:
                            self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] = 0 #スクロールしたドットカウンタが最大値まで行ったら0へ戻してループさせる


    #各種ビジュアルシーンの作製             id=ビジュアルシーンのidナンバー
    def create(self,id):
        """
        ビジュアルシーンの作製
        
        id=作製するビジュアルシーンのidナンバーですに
        """
        new_visualscene = Visualscene()
        if id == VS_ID_OPENING_STORY1:                 #オープニングのストーリーテキストその1
            new_visualscene.update(\
            VS_ID_OPENING_STORY1,\
            VS_ID_SUB_NORMAL,\
            VS_TYPE_NORMAL,\
            VS_STATUS_NORMAL,\
            VS_PRIORITY_TITLE_BACK,\
            pyxel.COLOR_WHITE,\
            pyxel.COLOR_BLACK,\
            0,60,  160,60,\
            1,1, 1,1,\
            0,0,\
            NO_VS_WAIT_LIST,NO_VS_FLAG_LIST,NO_VS_GRP_LIST,NO_VS_FACE_LIST,NO_VS_SOUND_LIST,NO_VS_BGM_LIST,NO_VS_EFFECT_LIST,NO_VS_TEXT_LIST,\
            [0,60,  120,40,\
            
            [[""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            ["Augusta Ada King"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            ["Countess of Lovelace née Byron"      ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            ["10 December 1815"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["–--"                                 ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["27 November 1852"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["was an English mathematician"        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["and writer"                          ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["chiefly known for her work"          ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["on Charles Babbage's proposed"       ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["mechanical general-purpose computer" ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["the Analytical Engine."              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["She was the first to recognise"      ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["that the machine"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["had applications beyond"             ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["pure calculation"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["and to have published"               ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["the first algorithm intended"        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["to be carried out by"                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["such a machine. As a result"         ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["she is often regarded"               ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            ["as the first computer programmer"    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ]],\
            
            NO_VS_TEXT_JPN,\
            
            SUBTITLES_OFF, 0,0, 160,16,  EDGE_SHADOW_ON, pyxel.COLOR_DARK_BLUE, 8,8, 8,8, 0,0, 33*8,33*8,\
            SPEED20,SPEED20, FLAG_OFF, END_ACTION_NONE],\
            NO_VS_SCRIPT_LIST,NO_VS_VECTOR_GRP_LIST,NO_VS_TIMELINE_LIST,\
            )
        else:
            return
        self.visualscene.append(new_visualscene)       #ビジュアルシーンを作製する
        
        #作製したビジュアルシーンのスクロールテキスト部分だけコンソールに表示(デバッグ用)
        visualscene_count = len(self.visualscene)
        for i in range(visualscene_count):
            print(self.visualscene[i].scroll_text)