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
            #ビジュアルシーンを開いていく
            if self.visualscene[i].status == VS_STATUS_OPEN:
                if self.visualscene[i].width < self.visualscene[i].open_width:   #widthをopen_widthの数値になるまで増加させていく
                    self.visualscene[i].width += 0.5
                    
                if self.visualscene[i].height < self.visualscene[i].open_height: #heightをopen_heightの数値になるまで増加させていく
                    self.visualscene[i].height += 0.5
                
                #ビジュアルシーンが開ききったのか判断する
                if  -2 <= self.visualscene[i].open_width  - self.visualscene[i].width  <= 2 and\
                    -2 <= self.visualscene[i].open_height - self.visualscene[i].height <= 2:#もしwidthとheightの値がopenした時の数値と+-2以内になったのなら
                    self.visualscene[i].status = VS_STATUS_START #ビジュアルシーンは完全に開ききったとみなしてステータスをVS_STATUS_STARTにしてビジュアルシーンを開始する
                    
                    self.visualscene[i].width  = self.visualscene[i].open_width #小数点以下の座標の誤差を修正するために強制的にopen時の座標数値を現在座標数値に代入してやる
                    self.visualscene[i].height = self.visualscene[i].open_height
            
            #スクロールテキストに何かテキストが入っている時&選択言語が英語の時はスクロールドットカウンタを増やしていく
            if self.visualscene[i].scroll_text != "" and self.language == LANGUAGE_ENG:
                # print (self.visualscene[i].scroll_text)
                if  self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_ENG] != 0: #スクロールスピードが0の時は何もしない(0で割り算をしてエラーになっちゃう為)
                    spd = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_ENG]
                    if int(pyxel.frame_count % spd) == 0:
                        self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] += 1  #スクロールテキストのスクロールしたドットカウンタを1増やしていく
                        self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_COUNT1] += 1  #字幕表示用のカウンタ1も増やしていく
                        if self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] >= self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_MAX_ENG]:
                            self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_ENG] = 0 #スクロールしたドットカウンタが最大値まで行ったら0へ戻してループさせる
                            self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SUBTITLES_COUNT1] = 0 #字幕表示用のカウンタ1もゼロリセットする
            
            #スクロールテキストに何かテキストが入っている時&選択言語が日本語の時はスクロールドットカウンタを増やしていく
            elif self.visualscene[i].scroll_text != "" and self.language == LANGUAGE_JPN:
                if  self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_JPN] != 0: #スクロールスピードが0の時は何もしない(0で割り算をしてエラーになっちゃう為)
                    spd = self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SPEED_JPN]
                    if int(pyxel.frame_count % spd) == 0:
                        self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_JPN] += 1  #スクロールテキストのスクロールしたドットカウンタを1増やしていく
                        if self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_JPN] >= self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_MAX_JPN]:
                            self.visualscene[i].scroll_text[LIST_VS_SCROLL_TEXT_SCROLLED_DOT_JPN] = 0 #スクロールしたドットカウンタが最大値まで行ったら0へ戻してループさせる

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
            VS_STATUS_OPEN,\
            VS_PRIORITY_TITLE_BACK,\
            pyxel.COLOR_WHITE,\
            pyxel.COLOR_BLACK,\
            0,60,\
            0,0,160,60,\
            1,1, 1,1,\
            
            0,0,\
            NO_VS_WAIT_LIST,NO_VS_FLAG_LIST,\
            [[140,16,  IMG2, 0,152,SIZE_16,SIZE_16, 0,  1,1]],\
            NO_VS_FACE_LIST,NO_VS_SOUND_LIST,NO_VS_BGM_LIST,NO_VS_EFFECT_LIST,NO_VS_TEXT_LIST,\
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
            
            
            [[""                                  ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [""                                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            ["（）〔〕［］｛｝〈〉《》「」『』【】"                  ,pyxel.COLOR_WHITE,DISP_LEFT_ALIGN     ,MES_MONOCHROME_FLASH],\
            ["￣＿ヽヾゝゞ〃仝々〆〇ー"                              ,pyxel.COLOR_WHITE,DISP_LEFT_ALIGN     ,MES_MONOCHROME_FLASH],\
            ["、。．，・：；？！゛゜＇｀＂＾"                        ,pyxel.COLOR_WHITE,DISP_LEFT_ALIGN     ,MES_MONOCHROME_FLASH],\
            [ "０１２３４５６７８９ＡＢＣ"                           ,pyxel.COLOR_WHITE,DISP_RIGHT_ALIGN     ,MES_MONOCHROME_FLASH],\
            [ "遊んでいたんだがカイで１０連勝とか"                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_MONOCHROME_FLASH],\
            [ "してるやつがいたんで見ていたら"                       ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "１０連勝の相手は小学生くらいの子供だった"             ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "俺は「恥かしくないのか」ときくと"                     ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "聞こえないフリしていきなり"                           ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "飛ぶながら叩きつけるワザ使っていたが"                 ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "子供は１回攻撃無視のワザを使っていて"                 ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "無残に返り討ち食らっていた"                           ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "子供は「何故？」と苦笑しながら"                       ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "ダウンしてるカイに近付きおきぜめを狙っていたんだが"    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "カイは卑怯にも無敵の昇竜拳を使っていた"                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "だが子供はそれを読んでたみたいで"                      ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "防御してた絶望しひややせかきながら"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "無残に落下してくるカイに"                              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "バスター（最強攻撃）を食らわせてた"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "カイ使いは「今の離れてただろ・・」と"                  ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "一人ごと言っていたが誰も聞いてなかった"                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "卑怯にもきょりがあいたので"                            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "氷だして削っていたんだが"                              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "ぽちょきんも飛び跳ねて頑張っていたら"                  ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "ギャラリーが集まってきてたんだが"                      ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "その攻めが恥かしくなったんだろうな"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "急に「そろそろかな」といって攻撃的になって"            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "空中から攻めて行ったら"                                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "そこにあったポチョムキンの腕で捕まってた"              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "俺は「お前まさか…」というと"                           ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "顔真っ赤にしながら"                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "「今の飛んでないんだが・・」と"                        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "レバーにグルグルまわしてた"                            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "そのかいあってか残念な事に"                            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "強力な追加攻撃はミスしてたみたいだが"                  ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "安心して落下してきたカイに"                            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "またおき攻めで攻め掛かり"                              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "蹴りをガードさせた直後の"                              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "バスター（最強攻撃）で止めを刺されていた"              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "青くなってるカイ使いに"                                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "「お前誰に勝ったの？」と聞くと"                        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "奥のほうでメダルゲームしてる子供を指した"              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "しかも「呼んで来て…」と頼んできたが"                   ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "アワレで仕方が無かった"                                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "" ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "" ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "" ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ],\
            [ "" ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH ]],\
            
            [[""                          ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ "オーガスタ・エイダ"                  ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ "ラブレス＝ニーバイロン"              ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH],\
            [ "１８１５年１２月１０日生まれ"            ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "–--"                                 ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "１８５２年１１月２７日没"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "19世紀のイギリスの貴族・数学者"        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "ジョージゴードンバイロンの"      ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "一人娘であり数学を愛好した"                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "ミドルネームのエイダで知られる"             ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "旧姓はバイロン"                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "主にチャールズバベッジの考案した"                          ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "初期の汎用計算機である解析機関の著作で"          ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "世界初のコンピュータープログラマーとして"       ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ "知られる"                             ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""               ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""        ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""         ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""               ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ],\
            [ ""                                    ,pyxel.COLOR_WHITE,DISP_CENTER     ,MES_NO_FLASH        ]],\
            
            SUBTITLES_ON, 0,90, 160,16,0,0,\
            
            EDGE_SHADOW_ON, pyxel.COLOR_DARK_BLUE, 0,0, BETWEEN_LINE_8,BETWEEN_LINE_13, 0,0, 33*8,50*13,\
            SPEED20,SPEED13, FLAG_OFF, END_ACTION_NONE],\
            NO_VS_SCRIPT_LIST,\
            [[LIST_WINDOW_VECTOR_GRP_LINE  ,XBJ_X001,XBJ_Y001 ,XBJ_X002,XBJ_Y002 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X002,XBJ_Y002 ,XBJ_X003,XBJ_Y003 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X003,XBJ_Y003 ,XBJ_X004,XBJ_Y004 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X004,XBJ_Y004 ,XBJ_X005,XBJ_Y005 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X005,XBJ_Y005 ,XBJ_X006,XBJ_Y006 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X006,XBJ_Y006 ,XBJ_X007,XBJ_Y007 ,pyxel.COLOR_DARK_BLUE],\
            [LIST_WINDOW_VECTOR_GRP_LINE   ,XBJ_X007,XBJ_Y007 ,XBJ_X008,XBJ_Y008 ,pyxel.COLOR_DARK_BLUE],\
            ],\
            NO_VS_TIMELINE_LIST,\
            )
            start_line = 60
            self.attrib_line_col[start_line - 10] = [1,0]
            self.attrib_line_col[start_line - 9] = [0,1]
            self.attrib_line_col[start_line - 8] = [1,0]
            self.attrib_line_col[start_line - 7] = [0,1]
            self.attrib_line_col[start_line - 6] = [1,0]
            
            self.attrib_line_col[start_line - 5] = [1,0]
            self.attrib_line_col[start_line - 4] = [0,1]
            self.attrib_line_col[start_line - 3] = [1,0]
            self.attrib_line_col[start_line - 2] = [0,1]
            self.attrib_line_col[start_line - 1] = [1,0]
            
            self.attrib_line_col[start_line + 0] = [1,1]
            self.attrib_line_col[start_line + 1] = [1,1]
            self.attrib_line_col[start_line + 2] = [1,1]
            self.attrib_line_col[start_line + 3] = [1,1]
            self.attrib_line_col[start_line + 4] = [1,1]
            
            self.attrib_line_col[start_line + 5] = [1,1]
            self.attrib_line_col[start_line + 6] = [1,1]
            self.attrib_line_col[start_line + 7] = [1,1]
            self.attrib_line_col[start_line + 8] = [1,1]
            self.attrib_line_col[start_line + 9] = [1,1]
            
            self.attrib_line_col[start_line + 10] = [1,5]
            self.attrib_line_col[start_line + 11] = [5,1]
            self.attrib_line_col[start_line + 12] = [1,5]
            self.attrib_line_col[start_line + 13] = [5,1]
            self.attrib_line_col[start_line + 14] = [1,5]
            
            self.attrib_line_col[start_line + 15] = [5,5]
            self.attrib_line_col[start_line + 16] = [5,5]
            self.attrib_line_col[start_line + 17] = [5,5]
            self.attrib_line_col[start_line + 18] = [5,5]
            self.attrib_line_col[start_line + 19] = [5,5]
            
            
            self.attrib_line_col[start_line + 20] = [12,12]
            self.attrib_line_col[start_line + 21] = [12,12]
            self.attrib_line_col[start_line + 22] = [12,12]
            self.attrib_line_col[start_line + 23] = [12,12]
            self.attrib_line_col[start_line + 24] = [12,12]
            
            
            self.attrib_line_col[start_line + 25] = [6,12]
            self.attrib_line_col[start_line + 26] = [12,6]
            self.attrib_line_col[start_line + 27] = [6,6]
            self.attrib_line_col[start_line + 28] = [6,6]
            self.attrib_line_col[start_line + 29] = [6,6]
            
            self.attrib_line_col[start_line + 30] = [7,7]
            self.attrib_line_col[start_line + 31] = [7,7]
            self.attrib_line_col[start_line + 32] = [7,7]
            self.attrib_line_col[start_line + 33] = [7,7]
            self.attrib_line_col[start_line + 34] = [7,7]
            
            self.attrib_line_col[start_line + 35] = [7,7]
            self.attrib_line_col[start_line + 36] = [7,7]
            self.attrib_line_col[start_line + 37] = [7,7]
            self.attrib_line_col[start_line + 38] = [7,7]
            self.attrib_line_col[start_line + 39] = [7,7]
            
            self.attrib_line_col[start_line + 40] = [7,7]
            self.attrib_line_col[start_line + 41] = [7,7]
            self.attrib_line_col[start_line + 42] = [7,7]
            self.attrib_line_col[start_line + 43] = [7,7]
            self.attrib_line_col[start_line + 44] = [7,7]
            
            
            
            
        else:
            return
        self.visualscene.append(new_visualscene)       #ビジュアルシーンを作製する
        
        #作製したビジュアルシーンのスクロールテキスト部分だけコンソールに表示(デバッグ用)
        visualscene_count = len(self.visualscene)
        for i in range(visualscene_count):
            print(self.visualscene[i].scroll_text)