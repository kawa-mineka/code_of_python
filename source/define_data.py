from const import *             #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from const_visualscene import * #Visualsceneクラスで使用する定数定義のよみこみ

class define_data:
    def __init__(self):
        None

    def ipl_mes(self):                      #IPLで使用するテキストメッセージの定義
        """
        IPLメッセージテキストの定義
        """
        #IPLメッセージデータその1
        self.ipl_mes1 = [
            ["INITIAL PROGRAM LOADING",7],
            [".",7],
            ["..",7],
            ["...",7],
            ["....",7],
            ['LOADING PROGRAM "CODE OF PYTHON"',7],
            ["POWERD BY PYXEL",6],
            ["POWERD BY PYGAME",5],
            ["FILE CHECK OK",7],
            ["BOOTING PROGRAM",7],
            ["2021 PROJECT MINE",6],
            ["SINCE 2020",7],
            ["...",7],
            ["....",7],
            ["MAIN SYSYTEM OK",7],
            ["SUB SYSYTEM OK",6],
            ["L'S SYSTEM OK",5],
            ["DISPLAY OK",5],
            ["DIALOG SYSYTEM OK",8],
            
            [".",7],
            ["..",7],
            ["...",7],
            ["....",7],
            ["EXECUTE OPERETING SYSTEM",8],
            ["GOOD LUCK!",8],
            ]

    def default_score_board(self):          #スコアボードの初期データ 
        """
        スコアボードの初期データの定義を行います
        """
        # [難易度ID,       順位,名前,      得点,周回数,最終到達ステージ,使用した機体]
        self.default_score_board = [
        [
        [GAME_VERY_EASY, 1,"KITAO   ",573,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 2,"SOW74656", 90,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 3,"KONIMIRU", 80,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 4,"ABURI680", 70,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 5,"AKAILORI", 60,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 6,"DOC100  ", 50,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 7,"ONTAKE44", 40,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 8,"KOIDEMIZ", 30,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY, 9,"ODANNY  ", 20,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY,10,"2DGAMES_", 10,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_EASY,11,"        ",  1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]],
        
        [
        [GAME_EASY,      1,"GYUDON  ",100,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      2,"UNADON  ", 90,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      3,"KATHUDON", 80,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      4,"TENDON  ", 70,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      5,"OYAKODON", 60,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      6,"MABODON ", 50,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      7,"MISOKATU", 40,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      8,"YAKITORI", 30,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,      9,"TAKOYAKI", 20,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,     10,"KARAAGE ", 10,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_EASY,     11,"        ",  1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]],
        
        [
        [GAME_NORMAL,    1,"FOO     ", 100,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,  MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_TWINKLE,MEDAL_NO_SLOT],
        [GAME_NORMAL,    2,"BAR     ",  90,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    3,"SPAM    ",  80,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    4,"HAM     ",  70,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    5,"EGG     ",  60,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    6,"HOGE    ",  50,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    7,"FUGA    ",  40,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    8,"PIYO    ",  30,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,    9,"ALICE   ",  20,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,   10,"BOB     ",  10,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_NORMAL,   11,"        ",   1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]],
        
        [
        [GAME_HARD,      1,"ISEUDON ",100,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      2,"YAKIUDON", 90,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      3,"YAKISOBA", 80,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      4,"KISHIMEN", 70,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      5,"HIYAMUGI", 60,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      6,"UDON    ", 50,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      7,"SOMEN   ", 40,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      8,"PASTA   ", 30,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,      9,"RAMEN   ", 20,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,     10,"SOBA    ", 10,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_HARD,     11,"        ",  1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]],
        
        [
        [GAME_VERY_HARD ,1,"KANAYAMA",100,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,2,"OOSONE  ", 90,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,3,"FUKIAGE ", 80,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,4,"HIRABARI", 70,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,5,"CHIKUSA ", 60,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,6,"TSURUMAI", 50,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,7,"MIZUHO  ", 40,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,8,"GOKISO  ", 30,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD ,9,"IMAIKE  ", 20,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD,10,"OSU     ", 10,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_VERY_HARD,11,"        ",  1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]],
        
        [
        [GAME_INSAME,    1,"MINE2021",2021,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    2,"NIHONKOK",1946,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_BEFOREHAND_4SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    3,"DAINIHON",1889,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_BEFOREHAND_3SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    4,"SEKIGAHA",1600,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    5,"HONNOUZI",1582,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_BEFOREHAND_2SHOT_ITEM,MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    6,"KAMAKURA",1192,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    7,"KENTOUSH", 894,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    8,"HEIANKYO", 794,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,    9,"HEIZYOKY", 710,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,   10,"TAIKANOK", 645,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_BEFOREHAND_1SHOT_ITEM,MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT],
        [GAME_INSAME,   11,"        ",   1,LOOP01,STAGE_BOSS_RUSH,J_PYTHON,   MEDAL_NO_SLOT,              MEDAL_NO_SLOT,              MEDAL_NO_SLOT,  MEDAL_NO_SLOT,MEDAL_NO_SLOT,MEDAL_NO_SLOT]]
        ]

    def default_achievement_list(self):     #実績(アチーブメント)のIDナンバーとそれに対するグラフイックチップの位置や英語コメント、日本語コメントのデータリスト
        """
        実績(アチーブメント)のIDナンバーとそれに対するグラフイックチップの位置や英語コメント、日本語コメントの定義を行います
        """
        self.default_achievement_list = [
            [ACHIEVEMENT_FIRST_CAMPAIGN,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST CAMPAIGN",               "",  "戦火への誘い",                    "初めての出撃！",                           "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE01_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BREEZARDIA",           "",  "巨大なる衝撃",                    "ブリザーディアを破壊した",                  "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE02_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY FATTY VALGUARD",       "",  "重爆撃機との死闘",                 "ファッティバルガードを破壊した",            "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE03_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS3",                "",  "ボス３撃破",                      "ボス３を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE04_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS4",                "",  "ボス４撃破",                      "ボス４を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE05_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS5",                "",  "ボス５撃破",                      "ボス５を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE06_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS6",                "",  "ボス６撃破",                      "ボス６を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE07_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS7",                "",  "ボス７撃破",                      "ボス７を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE08_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS8",                "",  "ボス８撃破",                      "ボス８を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE09_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS9",                "",  "ボス９撃破",                      "ボス９を破壊した",                         "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_STAGE10_BOSS,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS10",               "",  "ボス１０撃破",                    "ボス１０を破壊した",                       "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_POW_UP,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST POWUP",                  "",  "物資回収成功",                    "初めてパワーカプセル回収に成功した",         "20210828",LV01,10],
            [ACHIEVEMENT_1STAGE_CLEAR,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST STAGE CLEAR",            "",  "初回任務完了",                    "初めてステージをクリアした",                "20210828",LV01,10],
            [ACHIEVEMENT_DESTROY_BOSS_10TIME,   RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROY BOSS 10TIMES",         "",  "ボス１０体撃墜",                  "ボス撃墜数１０超え",                       "20210828",LV01,10],
            [ACHIEVEMENT_NO_DAMAGE_DESTROY_BOSS,RESULTS_NOT_OBTAINED,168     ,176,IMG2,"NO DAMAGE DESTROY BOSS",       "",  "ボス撃破、被害ゼロ",              "ノーダメージでボスを撃破しました",          "20210828",LV01,10],
            [ACHIEVEMENT_SCORE_STAR_5CHAIN,     RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SCORE STAR 5CHAIN",            "",  "得点なる星⑤連続回収",             "スコアスターの連続取得が⑤回を超えました",     "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_CLAW,            RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST CLAW",                   "",  "引き裂きし爪",                    "初めてクローを装備した",                   "20210828",LV01,10],
            
            [ACHIEVEMENT_10_SHOT_POW,           RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 10 OF THEM",  "", "ショットカプセル１０個入手",        "ショットカプセルを累計１０個手に入れた",     "20210828",LV01,10],
            [ACHIEVEMENT_50_SHOT_POW,           RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 50 OF THEM",  "", "ショットカプセル５０個入手",        "ショットカプセルを累計５０個手に入れた",     "20210828",LV01,10],
            [ACHIEVEMENT_100_SHOT_POW,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 100 OF THEM", "", "ショットカプセル１００個入手",      "ショットカプセルを累計１００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_200_SHOT_POW,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 200 OF THEM", "", "ショットカプセル２００個入手",      "ショットカプセルを累計２００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_500_SHOT_POW,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 500 OF THEM", "", "ショットカプセル５００個入手",      "ショットカプセルを累計５００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_1000_SHOT_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 1000 OF THEM","", "ショットカプセル１０００個入手",    "ショットカプセルを累計１０００個手に入れた",  "20210828",LV01,10],
            [ACHIEVEMENT_2000_SHOT_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 2000 OF THEM","", "ショットカプセル２０００個入手",    "ショットカプセルを累計２０００個手に入れた",  "20210828",LV01,10],
            [ACHIEVEMENT_2465_SHOT_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHOT ITEMS I GOT 2465 OF THEM","", "ショットカプセル２４６５個入手",    "ショットカプセルを累計２４６５個手に入れた",  "20210828",LV01,10],
            
            [ACHIEVEMENT_10_MISSILE_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 10 OF THEM",  "", "ミサイルカプセル１０個入手",        "ミサイルカプセルを累計１０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_50_MISSILE_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 50 OF THEM",  "", "ミサイルカプセル５０個入手",        "ミサイルカプセルを累計５０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_100_MISSILE_POW,       RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 100 OF THEM", "", "ミサイルカプセル１００個入手",      "ミサイルカプセルを累計１００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_200_MISSILE_POW,       RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 200 OF THEM", "", "ミサイルカプセル２００個入手",      "ミサイルカプセルを累計２００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_400_MISSILE_POW,       RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 400 OF THEM", "", "ミサイルカプセル４００個入手",      "ミサイルカプセルを累計４００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_765_MISSILE_POW,       RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 765 OF THEM","",  "ミサイルカプセル７６５個入手",      "ミサイルカプセルを累計７６５個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_1000_MISSILE_POW,      RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 1000 OF THEM","", "ミサイルカプセル１０００個入手",    "ミサイルカプセルを累計１０００個手に入れた",   "20210828",LV01,10],
            [ACHIEVEMENT_2465_MISSILE_POW,      RESULTS_NOT_OBTAINED,168     ,176,IMG2,"MISSILE ITEMS I GOT 2465 OF THEM","", "ミサイルカプセル２４６５個入手",    "ミサイルカプセルを累計２４６５個手に入れた",   "20210828",LV01,10],
            
            [ACHIEVEMENT_10_SHIELD_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 10 OF THEM",  "", "シールドカプセル１０個入手",        "シールドカプセルを累計１０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_50_SHIELD_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 50 OF THEM",  "", "シールドカプセル５０個入手",        "シールドカプセルを累計５０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_100_SHIELD_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 100 OF THEM", "", "シールドカプセル１００個入手",       "シールドカプセルを累計１００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_200_SHIELD_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 200 OF THEM", "", "シールドカプセル２００個入手",       "シールドカプセルを累計２００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_400_SHIELD_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 400 OF THEM", "", "シールドカプセル４００個入手",       "シールドカプセルを累計４００個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_530_SHIELD_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"SHIELD ITEMS I GOT 530 OF THEM","",  "シールドカプセル５３０個入手",       "シールドカプセルを累計５３０個手に入れた",    "20210828",LV01,10],
            
            [ACHIEVEMENT_10_CLAW_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"CLAW ITEMS I GOT 10 OF THEM",  "", "クローカプセル１０個入手",        "クローカプセルを累計１０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_20_CLAW_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"CLAW ITEMS I GOT 20 OF THEM", "", "クローカプセル２０個入手",       "クローカプセルを累計２０個手に入れた",    "20210828",LV01,10],
            [ACHIEVEMENT_50_CLAW_POW,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"CLAW ITEMS I GOT 50 OF THEM",  "", "クローカプセル５０個入手",        "クローカプセルを累計５０個手に入れた",      "20210828",LV01,10],
            [ACHIEVEMENT_100_CLAW_POW,        RESULTS_NOT_OBTAINED,168     ,176,IMG2,"CLAW ITEMS I GOT 100 OF THEM", "", "クローカプセル１００個入手",       "クローカプセルを累計１００個手に入れた",    "20210828",LV01,10],
            
            [ACHIEVEMENT_FIRST_5WAY_SHOT,     RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST 5WAY SHOT",  "", "５連装バルカンショット",        "５連装バルカンショットを初装備",      "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_LASER,         RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST LASER",  "", "レーザー",                         "レーザー初装備！",      "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_TWIN_LASER,    RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST TWIN LASER", "", "ツインレーザー",                "ツインレーザーを初装備した！",    "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_SHOWER_LASER,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST SHOWER LASER", "", "シャワーレーザー",            "シャワーレーザーの衝撃初体験",    "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_WAVE,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST WAVE", "", "ウェーブカッター",                    "全てを貫く波を見た",    "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_MAX_WAVE,      RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST MAX WAVE","",  "ウェーブカッターマキシマム",       "何もかもを貫く音の壁を見る",    "20210828",LV01,10],
            
            [ACHIEVEMENT_FIRST_TWIN_MISSILE,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST TWIN MISSILE",  "", "ツインミサイル",             "ツインミサイル初装備",      "20210828",LV01,10],
            [ACHIEVEMENT_FIRST_MULTI_MISSILE, RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST MULTI MISSILE",  "", "マルチミサイル",            "マルチミサイル初装備！",      "20210828",LV01,10],
            
            [ACHIEVEMENT_NO_DAMAGE_STAGE_CLEAR,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"NO DAMAGE STAGE CLEAR",      "", "ノーダメージステージクリア",        "被弾せずステージクリア！",                 "20210828",LV01,10],
            [ACHIEVEMENT_NO_SHOT_STAGE_CLEAR,            RESULTS_NOT_OBTAINED,168     ,176,IMG2,"NO SHOT STAGE CLEAR",        "", "ノーショットクリア",               "全く攻撃せずステージクリアしたぞ！",        "20210828",LV01,10],
            [ACHIEVEMENT_NO_DAMAGE_AND_SHOT_STAGE_CLEAR, RESULTS_NOT_OBTAINED,168     ,176,IMG2,"NO DAMAGE & NO SHOT CLEAR",  "", "ノーダメージ＆ノーショットクリア",   "弾も撃たず、被弾もせずステージクリア！！！","20210828",LV01,10],
            
            [ACHIEVEMENT_BOSS_INSTANK_KILL,          RESULTS_NOT_OBTAINED,168     ,176,IMG2,"BOSS INSTANK KILL",        "", "ボスを瞬殺した！",           "ボスを30秒以内で破壊した",                    "20210828",LV01,10],
            
            [ACHIEVEMENT_FIRST_REPLAY_PLAY_COMPLETE, RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST REPLAY COMPLETE",    "", "リプレイ再生完了",           "リプレイを最後まで正常に再生できた",           "20210828",LV01,10],
            
            [ACHIEVEMENT_FIRST_GET_TRIANGLE_ITEM,    RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST GET TRIANGLE ITEM",  "", "トライアングルアイテム入手",  "初めてのトライアングルアイテム入手",           "20210828",LV01,10],
            [ACHIEVEMENT_ENDURANCE_ONE_CLEARED,      RESULTS_NOT_OBTAINED,168     ,176,IMG2,"ENDURANCE ONE CLEARED",    "", "シールド値１でクリア",       "残りシールド値１でギリギリステージクリアした",  "20210828",LV01,10],
            
            [ACHIEVEMENT_DESTROYED_ALL_BOSS_PARTS,   RESULTS_NOT_OBTAINED,168     ,176,IMG2,"DESTROYED ALL BOSS PARTS",    "", "ボスのパーツを全破壊",    "ボスのパーツをすべて破壊した",  "20210828",LV01,10],
            
            [ACHIEVEMENT_FIRST_FAST_FORWARD, RESULTS_NOT_OBTAINED,168     ,176,IMG2,"FIRST FAST FORWARD","", "初めて敵機を追加発生させた",    "はじめて早回しを達成した",  "20210828",LV01,10],
            [ACHIEVEMENT_8_FAST_FORWARD,     RESULTS_NOT_OBTAINED,168     ,176,IMG2,"8 FAST FORWARD",    "", "敵機を８回追加発生させた",      "敵機を８回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_16_FAST_FORWARD,    RESULTS_NOT_OBTAINED,168     ,176,IMG2,"16 FAST FORWARD",   "", "敵機を１６回追加発生させた",    "敵機を１６回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_32_FAST_FORWARD,    RESULTS_NOT_OBTAINED,168     ,176,IMG2,"32 FAST FORWARD",   "", "敵機を３２回追加発生させた",    "敵機を３２回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_64_FAST_FORWARD,    RESULTS_NOT_OBTAINED,168     ,176,IMG2,"64 FAST FORWARD",   "", "敵機を６４回追加発生させた",    "敵機を６４回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_128_FAST_FORWARD,   RESULTS_NOT_OBTAINED,168     ,176,IMG2,"128 FAST FORWARD",  "", "敵機を１２８回追加発生させた",  "敵機を１２８回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_256_FAST_FORWARD,   RESULTS_NOT_OBTAINED,168     ,176,IMG2,"256 FAST FORWARD",  "", "敵機を２５６回追加発生させた",  "敵機を２５６回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_512_FAST_FORWARD,   RESULTS_NOT_OBTAINED,168     ,176,IMG2,"512 FAST FORWARD",  "", "敵機を５１２回追加発生させた",  "敵機を５１２回追加発生させた",  "20210828",LV01,10],
            [ACHIEVEMENT_1024_FAST_FORWARD,  RESULTS_NOT_OBTAINED,168     ,176,IMG2,"1024 FAST FORWARD", "", "敵機を１０２４回追加発生させた","敵機を１０２４回追加発生させた",  "20210828",LV01,10],
            
            
            ]

    def stage_asset_list(self):             #ステージごとのアセットファイル名(pyxresファイル)が登録されたリストを作成する
        """
        各ステージのアセットファイル名(pyxresファイル)が登録されたリストを作成します
        """
        self.stage_asset_list = [
            [STAGE_MOUNTAIN_REGION,         "min-sht2.pyxres"],
            [STAGE_ADVANCE_BASE,            "min-sht2.pyxres"],
            [STAGE_VOLCANIC_BELT,           "min-sht2.pyxres"],
            [STAGE_NIGHT_SKYSCRAPER,        "min-sht2.pyxres"],
            [STAGE_AMPHIBIOUS_ASSAULT_SHIP, "min-sht2.pyxres"],
            [STAGE_DEEP_SEA_TRENCH,         "min-sht2.pyxres"],
            [STAGE_INTERMEDIATE_FORTRESS,   "min-sht2.pyxres"],
            [STAGE_ESCAPE_FORTRESS,         "min-sht2.pyxres"],
            [STAGE_BOSS_RUSH,               "min-sht2.pyxres"],
            [STAGE_CHANCE_MEETING,          "min-sht2.pyxres"],
            ]

    def medal_graph_and_comment_list(self): #メダルのIDナンバーとそれに対するグラフイックチップの位置や英語コメント、日本語コメントのデータリスト
        """
        メダルのIDナンバーとそれに対するグラフイックチップの位置や英語コメント、日本語コメントのデータリストを作製します
        """
        self.medal_graph_and_comment_list = [
            [MEDAL_NO_SLOT              ,168         ,176,IMG2,"NO SLOT"                   ,"空スロット",                 "","",                                                                                "",""],
            [MEDAL_BEFOREHAND_1SHOT_ITEM,168 + 8 * 1 ,176,IMG2,"BEFOREHAND 1 SHOT"         ,"事前にショットアイテム１個取得","TOTAL PLAY TIME EXCEEDED","10 MINUTES",                                              "トータルプレイ時間が１０分を超えました！",""],
            [MEDAL_BEFOREHAND_2SHOT_ITEM,168 + 8 * 2 ,176,IMG2,"BEFOREHAND 2 SHOT"         ,"事前にショットアイテム２個取得","COMPLETED DEFEATING THE BOSS","ON THE FIRST PAGE",                                   "１面ボスを撃破完了！",""],
            [MEDAL_BEFOREHAND_3SHOT_ITEM,168 + 8 * 3 ,176,IMG2,"BEFOREHAND 3 SHOT"         ,"事前にショットアイテム３個取得","OBTAINED WITH A TOTAL SCORE OF","2000 POINTS",                                       "トータルスコア２０００点超え！",""],
            [MEDAL_BEFOREHAND_4SHOT_ITEM,168 + 8 * 4 ,176,IMG2,"BEFOREHAND 4 SHOT"         ,"事前にショットアイテム４個取得","OBTAINED WITH A TOTAL PLAY TIME OF 180 MINUTES", "OR A TOTAL SCORE OF 10000 POINTS", "トータルプレイタイム１８０分","またはトータルスコア１万点超え！"],
            [MEDAL_EQUIPMENT_LS_SHIELD  ,168 + 8 * 5 ,176,IMG2,"EQUIP L's SHIELD"          ,"エルズシールド装備",           "","",                                                                                "",""],
            [MEDAL_PLUS_MEDALLION       ,168 + 8 * 6 ,176,IMG2,"2 OPTION SLOT"             ,"スロットが２個増える",         "STAR SCORING MULTIPLIER IS","OVER 7",                                                "スター得点倍率が７を超えました",""],
            [MEDAL_CONCENTRATION        ,168 + 8 * 7 ,176,IMG2,"ONE POINT OF CONCENTRATION","一点集中",                   "THE THIRD BOSS IS DEFEATED!","",                                                     "３面ボスを撃破完了！",""],
            [MEDAL_FRAME_RESIST         ,168 + 8 * 8 ,176,IMG2,"INFLAMMATION RESISTANCE+"  ,"炎耐性＋",                   "OBTAINED BY PLAYING 20 TIMES","OR MORE",                                             "プレイ回数が２０回を超えました","" ],
            [MEDAL_RECOVERY_OVER_TIME   ,168 + 8 * 9 ,176,IMG2,"RECOVERY OVER TIME"        ,"時間経過で回復",              "","",                                                                                "",""],
            [MEDAL_TWINKLE              ,168 + 8 *10 ,176,IMG2,"TWINKLE!!"                 ,"ぴかぴか光る！",              "","",                                                                                "",""],
            ]

    def font_code_table(self):              #美咲フォント(漢字)コードテーブルの定義 
        #いきなり美咲フォントコードテーブルを直接代入という破天荒なコード・・・・
        #「シールド」は「シ─ルド」と入力しないと文字化けするので注意 ー→─
        """
        美咲フォント(漢字)コードテーブルの定義 
        """
        self.font_code_table = (
            "　+−±×÷=≠<>≦≧∞∴♂♀°′″℃¥$¢£%#&*@§☆★○●◎◇\n"
            "◆□■△▲▽▼※〒→←↑↓〓         ∈∋⊆⊇⊂⊃∪∩       ∧∨¬⇒⇔∀∃         ∠⊥⌒∂∇≡≒≪≫√∽∝∵∫∬      Å‰♯♭♪†‡¶    ◯\n"
            "\n" 
            "　　　　　　　　　　　　　　　　ＡＢＣDEFGHIJKLMNOPQRSTUVWXYZ     abcdefghijklmnopqrstuvwxyz\n"
            "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん\n"
            "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ\n"
            "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ♤♠♢♦♡♥♧♣αβγδεζηθικλμνξοπρστυφχψω\n"
            "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ            абвгдеёжзийклмнопрстуфхцчшщъыьэюя\n"
            "ー│┌┐┘└├┬┤┴┼━┃┏┓┛┗┣┳┫┻╋┠┯┨┷┿┝┰┥┸╂\n"
            "　、。．，・：；？！゛゜＇｀＂＾￣＿ヽヾゝゞ〃仝々〆〇ー　　／＼～∥｜　‥　　　　（）〔〕［］｛｝〈〉《》「」『』【】\n"
            "\n"
            "\n"
            "\n"
            "０１２３４５６７８９⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪ㍉㌔㌢㍍㌘㌧㌃㌶㍑㍗㌍㌦㌣㌫㍊㌻㎜㎝㎞㎎㎏㏄㎡            ㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼∮∟⊿❖☞\n"
            "\n"          
            "\n"
            "亜唖娃阿哀愛挨姶逢葵茜穐悪握渥旭葦芦鯵梓圧斡扱宛姐虻飴絢綾鮎或粟袷安庵按暗案闇鞍杏以伊位依偉囲夷委威尉惟意慰易椅為畏異移維緯胃萎衣謂違遺医井亥域育郁磯一壱溢逸稲茨芋鰯允印咽員因姻引飲淫胤蔭\n"
            "院陰隠韻吋右宇烏羽迂雨卯鵜窺丑碓臼渦嘘唄欝蔚鰻姥厩浦瓜閏噂云運雲荏餌叡営嬰影映曳栄永泳洩瑛盈穎頴英衛詠鋭液疫益駅悦謁越閲榎厭円園堰奄宴延怨掩援沿演炎焔煙燕猿縁艶苑薗遠鉛鴛塩於汚甥凹央奥往応\n"
            "押旺横欧殴王翁襖鴬鴎黄岡沖荻億屋憶臆桶牡乙俺卸恩温穏音下化仮何伽価佳加可嘉夏嫁家寡科暇果架歌河火珂禍禾稼箇花苛茄荷華菓蝦課嘩貨迦過霞蚊俄峨我牙画臥芽蛾賀雅餓駕介会解回塊壊廻快怪悔恢懐戒拐改\n"
            "魁晦械海灰界皆絵芥蟹開階貝凱劾外咳害崖慨概涯碍蓋街該鎧骸浬馨蛙垣柿蛎鈎劃嚇各廓拡撹格核殻獲確穫覚角赫較郭閣隔革学岳楽額顎掛笠樫橿梶鰍潟割喝恰括活渇滑葛褐轄且鰹叶椛樺鞄株兜竃蒲釜鎌噛鴨栢茅萱\n"
            "粥刈苅瓦乾侃冠寒刊勘勧巻喚堪姦完官寛干幹患感慣憾換敢柑桓棺款歓汗漢澗潅環甘監看竿管簡緩缶翰肝艦莞観諌貫還鑑間閑関陥韓館舘丸含岸巌玩癌眼岩翫贋雁頑顔願企伎危喜器基奇嬉寄岐希幾忌揮机旗既期棋棄\n"
            "機帰毅気汽畿祈季稀紀徽規記貴起軌輝飢騎鬼亀偽儀妓宜戯技擬欺犠疑祇義蟻誼議掬菊鞠吉吃喫桔橘詰砧杵黍却客脚虐逆丘久仇休及吸宮弓急救朽求汲泣灸球究窮笈級糾給旧牛去居巨拒拠挙渠虚許距鋸漁禦魚亨享京\n"
            "供侠僑兇競共凶協匡卿叫喬境峡強彊怯恐恭挟教橋況狂狭矯胸脅興蕎郷鏡響饗驚仰凝尭暁業局曲極玉桐粁僅勤均巾錦斤欣欽琴禁禽筋緊芹菌衿襟謹近金吟銀九倶句区狗玖矩苦躯駆駈駒具愚虞喰空偶寓遇隅串櫛釧屑屈\n"
            "掘窟沓靴轡窪熊隈粂栗繰桑鍬勲君薫訓群軍郡卦袈祁係傾刑兄啓圭珪型契形径恵慶慧憩掲携敬景桂渓畦稽系経継繋罫茎荊蛍計詣警軽頚鶏芸迎鯨劇戟撃激隙桁傑欠決潔穴結血訣月件倹倦健兼券剣喧圏堅嫌建憲懸拳捲\n"
            "検権牽犬献研硯絹県肩見謙賢軒遣鍵険顕験鹸元原厳幻弦減源玄現絃舷言諺限乎個古呼固姑孤己庫弧戸故枯湖狐糊袴股胡菰虎誇跨鈷雇顧鼓五互伍午呉吾娯後御悟梧檎瑚碁語誤護醐乞鯉交佼侯候倖光公功効勾厚口向\n"
            "后喉坑垢好孔孝宏工巧巷幸広庚康弘恒慌抗拘控攻昂晃更杭校梗構江洪浩港溝甲皇硬稿糠紅紘絞綱耕考肯肱腔膏航荒行衡講貢購郊酵鉱砿鋼閤降項香高鴻剛劫号合壕拷濠豪轟麹克刻告国穀酷鵠黒獄漉腰甑忽惚骨狛込\n"
            "此頃今困坤墾婚恨懇昏昆根梱混痕紺艮魂些佐叉唆嵯左差査沙瑳砂詐鎖裟坐座挫債催再最哉塞妻宰彩才採栽歳済災采犀砕砦祭斎細菜裁載際剤在材罪財冴坂阪堺榊肴咲崎埼碕鷺作削咋搾昨朔柵窄策索錯桜鮭笹匙冊刷\n"
            "察拶撮擦札殺薩雑皐鯖捌錆鮫皿晒三傘参山惨撒散桟燦珊産算纂蚕讃賛酸餐斬暫残仕仔伺使刺司史嗣四士始姉姿子屍市師志思指支孜斯施旨枝止死氏獅祉私糸紙紫肢脂至視詞詩試誌諮資賜雌飼歯事似侍児字寺慈持時\n"
            "次滋治爾璽痔磁示而耳自蒔辞汐鹿式識鴫竺軸宍雫七叱執失嫉室悉湿漆疾質実蔀篠偲柴芝屡蕊縞舎写射捨赦斜煮社紗者謝車遮蛇邪借勺尺杓灼爵酌釈錫若寂弱惹主取守手朱殊狩珠種腫趣酒首儒受呪寿授樹綬需囚収周\n"
            "宗就州修愁拾洲秀秋終繍習臭舟蒐衆襲讐蹴輯週酋酬集醜什住充十従戎柔汁渋獣縦重銃叔夙宿淑祝縮粛塾熟出術述俊峻春瞬竣舜駿准循旬楯殉淳準潤盾純巡遵醇順処初所暑曙渚庶緒署書薯藷諸助叙女序徐恕鋤除傷償\n"
            "勝匠升召哨商唱嘗奨妾娼宵将小少尚庄床廠彰承抄招掌捷昇昌昭晶松梢樟樵沼消渉湘焼焦照症省硝礁祥称章笑粧紹肖菖蒋蕉衝裳訟証詔詳象賞醤鉦鍾鐘障鞘上丈丞乗冗剰城場壌嬢常情擾条杖浄状畳穣蒸譲醸錠嘱埴飾\n"
            "拭植殖燭織職色触食蝕辱尻伸信侵唇娠寝審心慎振新晋森榛浸深申疹真神秦紳臣芯薪親診身辛進針震人仁刃塵壬尋甚尽腎訊迅陣靭笥諏須酢図厨逗吹垂帥推水炊睡粋翠衰遂酔錐錘随瑞髄崇嵩数枢趨雛据杉椙菅頗雀裾\n"
            "澄摺寸世瀬畝是凄制勢姓征性成政整星晴棲栖正清牲生盛精聖声製西誠誓請逝醒青静斉税脆隻席惜戚斥昔析石積籍績脊責赤跡蹟碩切拙接摂折設窃節説雪絶舌蝉仙先千占宣専尖川戦扇撰栓栴泉浅洗染潜煎煽旋穿箭線\n"
            "繊羨腺舛船薦詮賎践選遷銭銑閃鮮前善漸然全禅繕膳糎噌塑岨措曾曽楚狙疏疎礎祖租粗素組蘇訴阻遡鼠僧創双叢倉喪壮奏爽宋層匝惣想捜掃挿掻操早曹巣槍槽漕燥争痩相窓糟総綜聡草荘葬蒼藻装走送遭鎗霜騒像増憎\n"
            "臓蔵贈造促側則即息捉束測足速俗属賊族続卒袖其揃存孫尊損村遜他多太汰詑唾堕妥惰打柁舵楕陀駄騨体堆対耐岱帯待怠態戴替泰滞胎腿苔袋貸退逮隊黛鯛代台大第醍題鷹滝瀧卓啄宅托択拓沢濯琢託鐸濁諾茸凧蛸只\n"
            "叩但達辰奪脱巽竪辿棚谷狸鱈樽誰丹単嘆坦担探旦歎淡湛炭短端箪綻耽胆蛋誕鍛団壇弾断暖檀段男談値知地弛恥智池痴稚置致蜘遅馳築畜竹筑蓄逐秩窒茶嫡着中仲宙忠抽昼柱注虫衷註酎鋳駐樗瀦猪苧著貯丁兆凋喋寵\n"
            "帖帳庁弔張彫徴懲挑暢朝潮牒町眺聴脹腸蝶調諜超跳銚長頂鳥勅捗直朕沈珍賃鎮陳津墜椎槌追鎚痛通塚栂掴槻佃漬柘辻蔦綴鍔椿潰坪壷嬬紬爪吊釣鶴亭低停偵剃貞呈堤定帝底庭廷弟悌抵挺提梯汀碇禎程締艇訂諦蹄逓\n"
            "邸鄭釘鼎泥摘擢敵滴的笛適鏑溺哲徹撤轍迭鉄典填天展店添纏甜貼転顛点伝殿澱田電兎吐堵塗妬屠徒斗杜渡登菟賭途都鍍砥砺努度土奴怒倒党冬凍刀唐塔塘套宕島嶋悼投搭東桃梼棟盗淘湯涛灯燈当痘祷等答筒糖統到\n"
            "董蕩藤討謄豆踏逃透鐙陶頭騰闘働動同堂導憧撞洞瞳童胴萄道銅峠鴇匿得徳涜特督禿篤毒独読栃橡凸突椴届鳶苫寅酉瀞噸屯惇敦沌豚遁頓呑曇鈍奈那内乍凪薙謎灘捺鍋楢馴縄畷南楠軟難汝二尼弐迩匂賑肉虹廿日乳入\n"
            "如尿韮任妊忍認濡禰祢寧葱猫熱年念捻撚燃粘乃廼之埜嚢悩濃納能脳膿農覗蚤巴把播覇杷波派琶破婆罵芭馬俳廃拝排敗杯盃牌背肺輩配倍培媒梅楳煤狽買売賠陪這蝿秤矧萩伯剥博拍柏泊白箔粕舶薄迫曝漠爆縛莫駁麦\n"
            "函箱硲箸肇筈櫨幡肌畑畠八鉢溌発醗髪伐罰抜筏閥鳩噺塙蛤隼伴判半反叛帆搬斑板氾汎版犯班畔繁般藩販範釆煩頒飯挽晩番盤磐蕃蛮匪卑否妃庇彼悲扉批披斐比泌疲皮碑秘緋罷肥被誹費避非飛樋簸備尾微枇毘琵眉美\n"
            "鼻柊稗匹疋髭彦膝菱肘弼必畢筆逼桧姫媛紐百謬俵彪標氷漂瓢票表評豹廟描病秒苗錨鋲蒜蛭鰭品彬斌浜瀕貧賓頻敏瓶不付埠夫婦富冨布府怖扶敷斧普浮父符腐膚芙譜負賦赴阜附侮撫武舞葡蕪部封楓風葺蕗伏副復幅服\n"
            "福腹複覆淵弗払沸仏物鮒分吻噴墳憤扮焚奮粉糞紛雰文聞丙併兵塀幣平弊柄並蔽閉陛米頁僻壁癖碧別瞥蔑箆偏変片篇編辺返遍便勉娩弁鞭保舗鋪圃捕歩甫補輔穂募墓慕戊暮母簿菩倣俸包呆報奉宝峰峯崩庖抱捧放方朋\n"
            "法泡烹砲縫胞芳萌蓬蜂褒訪豊邦鋒飽鳳鵬乏亡傍剖坊妨帽忘忙房暴望某棒冒紡肪膨謀貌貿鉾防吠頬北僕卜墨撲朴牧睦穆釦勃没殆堀幌奔本翻凡盆摩磨魔麻埋妹昧枚毎哩槙幕膜枕鮪柾鱒桝亦俣又抹末沫迄侭繭麿万慢満\n"
            "漫蔓味未魅巳箕岬密蜜湊蓑稔脈妙粍民眠務夢無牟矛霧鵡椋婿娘冥名命明盟迷銘鳴姪牝滅免棉綿緬面麺摸模茂妄孟毛猛盲網耗蒙儲木黙目杢勿餅尤戻籾貰問悶紋門匁也冶夜爺耶野弥矢厄役約薬訳躍靖柳薮鑓愉愈油癒\n"
            "諭輸唯佑優勇友宥幽悠憂揖有柚湧涌猶猷由祐裕誘遊邑郵雄融夕予余与誉輿預傭幼妖容庸揚揺擁曜楊様洋溶熔用窯羊耀葉蓉要謡踊遥陽養慾抑欲沃浴翌翼淀羅螺裸来莱頼雷洛絡落酪乱卵嵐欄濫藍蘭覧利吏履李梨理璃\n"
            "痢裏裡里離陸律率立葎掠略劉流溜琉留硫粒隆竜龍侶慮旅虜了亮僚両凌寮料梁涼猟療瞭稜糧良諒遼量陵領力緑倫厘林淋燐琳臨輪隣鱗麟瑠塁涙累類令伶例冷励嶺怜玲礼苓鈴隷零霊麗齢暦歴列劣烈裂廉恋憐漣煉簾練聯\n"
            "蓮連錬呂魯櫓炉賂路露労婁廊弄朗楼榔浪漏牢狼篭老聾蝋郎六麓禄肋録論倭和話歪賄脇惑枠鷲亙亘鰐詫藁蕨椀湾碗腕\n"
            "弌丐丕个丱丶丼丿乂乖乘亂亅豫亊舒弍于亞亟亠亢亰亳亶从仍仄仆仂仗仞仭仟价伉佚估佛佝佗佇佶侈侏侘佻佩佰侑佯來侖儘俔俟俎俘俛俑俚俐俤俥倚倨倔倪倥倅伜俶倡倩倬俾俯們倆偃假會偕偐偈做偖偬偸傀傚傅傴傲\n"
            "僉僊傳僂僖僞僥僭僣僮價僵儉儁儂儖儕儔儚儡儺儷儼儻儿兀兒兌兔兢竸兩兪兮冀冂囘册冉冏冑冓冕冖冤冦冢冩冪冫决冱冲冰况冽凅凉凛几處凩凭凰凵凾刄刋刔刎刧刪刮刳刹剏剄剋剌剞剔剪剴剩剳剿剽劍劔劒剱劈劑辨\n"
            "辧劬劭劼劵勁勍勗勞勣勦飭勠勳勵勸勹匆匈甸匍匐匏匕匚匣匯匱匳匸區卆卅丗卉卍凖卞卩卮夘卻卷厂厖厠厦厥厮厰厶參簒雙叟曼燮叮叨叭叺吁吽呀听吭吼吮吶吩吝呎咏呵咎呟呱呷呰咒呻咀呶咄咐咆哇咢咸咥咬哄哈咨\n"
            "咫哂咤咾咼哘哥哦唏唔哽哮哭哺哢唹啀啣啌售啜啅啖啗唸唳啝喙喀咯喊喟啻啾喘喞單啼喃喩喇喨嗚嗅嗟嗄嗜嗤嗔嘔嗷嘖嗾嗽嘛嗹噎噐營嘴嘶嘲嘸噫噤嘯噬噪嚆嚀嚊嚠嚔嚏嚥嚮嚶嚴囂嚼囁囃囀囈囎囑囓囗囮囹圀囿圄圉\n"
            "圈國圍圓團圖嗇圜圦圷圸坎圻址坏坩埀垈坡坿垉垓垠垳垤垪垰埃埆埔埒埓堊埖埣堋堙堝塲堡塢塋塰毀塒堽塹墅墹墟墫墺壞墻墸墮壅壓壑壗壙壘壥壜壤壟壯壺壹壻壼壽夂夊夐夛梦夥夬夭夲夸夾竒奕奐奎奚奘奢奠奧奬奩\n"
            "奸妁妝佞侫妣妲姆姨姜妍姙姚娥娟娑娜娉娚婀婬婉娵娶婢婪媚媼媾嫋嫂媽嫣嫗嫦嫩嫖嫺嫻嬌嬋嬖嬲嫐嬪嬶嬾孃孅孀孑孕孚孛孥孩孰孳孵學斈孺宀它宦宸寃寇寉寔寐寤實寢寞寥寫寰寶寳尅將專對尓尠尢尨尸尹屁屆屎屓\n"
            "屐屏孱屬屮乢屶屹岌岑岔妛岫岻岶岼岷峅岾峇峙峩峽峺峭嶌峪崋崕崗嵜崟崛崑崔崢崚崙崘嵌嵒嵎嵋嵬嵳嵶嶇嶄嶂嶢嶝嶬嶮嶽嶐嶷嶼巉巍巓巒巖巛巫已巵帋帚帙帑帛帶帷幄幃幀幎幗幔幟幢幤幇幵并幺麼广庠廁廂廈廐廏\n"
            "廖廣廝廚廛廢廡廨廩廬廱廳廰廴廸廾弃弉彝彜弋弑弖弩弭弸彁彈彌彎弯彑彖彗彙彡彭彳彷徃徂彿徊很徑徇從徙徘徠徨徭徼忖忻忤忸忱忝悳忿怡恠怙怐怩怎怱怛怕怫怦怏怺恚恁恪恷恟恊恆恍恣恃恤恂恬恫恙悁悍惧悃悚\n"
            "悄悛悖悗悒悧悋惡悸惠惓悴忰悽惆悵惘慍愕愆惶惷愀惴惺愃愡惻惱愍愎慇愾愨愧慊愿愼愬愴愽慂慄慳慷慘慙慚慫慴慯慥慱慟慝慓慵憙憖憇憬憔憚憊憑憫憮懌懊應懷懈懃懆憺懋罹懍懦懣懶懺懴懿懽懼懾戀戈戉戍戌戔戛\n"
            "戞戡截戮戰戲戳扁扎扞扣扛扠扨扼抂抉找抒抓抖拔抃抔拗拑抻拏拿拆擔拈拜拌拊拂拇抛拉挌拮拱挧挂挈拯拵捐挾捍搜捏掖掎掀掫捶掣掏掉掟掵捫捩掾揩揀揆揣揉插揶揄搖搴搆搓搦搶攝搗搨搏摧摯摶摎攪撕撓撥撩撈撼\n"
            "據擒擅擇撻擘擂擱擧舉擠擡抬擣擯攬擶擴擲擺攀擽攘攜攅攤攣攫攴攵攷收攸畋效敖敕敍敘敞敝敲數斂斃變斛斟斫斷旃旆旁旄旌旒旛旙无旡旱杲昊昃旻杳昵昶昴昜晏晄晉晁晞晝晤晧晨晟晢晰暃暈暎暉暄暘暝曁暹曉暾暼\n"
            "曄暸曖曚曠昿曦曩曰曵曷朏朖朞朦朧霸朮朿朶杁朸朷杆杞杠杙杣杤枉杰枩杼杪枌枋枦枡枅枷柯枴柬枳柩枸柤柞柝柢柮枹柎柆柧檜栞框栩桀桍栲桎梳栫桙档桷桿梟梏梭梔條梛梃檮梹桴梵梠梺椏梍桾椁棊椈棘椢椦棡椌棍\n"
            "棔棧棕椶椒椄棗棣椥棹棠棯椨椪椚椣椡棆楹楷楜楸楫楔楾楮椹楴椽楙椰楡楞楝榁楪榲榮槐榿槁槓榾槎寨槊槝榻槃榧樮榑榠榜榕榴槞槨樂樛槿權槹槲槧樅榱樞槭樔槫樊樒櫁樣樓橄樌橲樶橸橇橢橙橦橈樸樢檐檍檠檄檢檣\n"
            "檗蘗檻櫃櫂檸檳檬櫞櫑櫟檪櫚櫪櫻欅蘖櫺欒欖鬱欟欸欷盜欹飮歇歃歉歐歙歔歛歟歡歸歹歿殀殄殃殍殘殕殞殤殪殫殯殲殱殳殷殼毆毋毓毟毬毫毳毯麾氈氓气氛氤氣汞汕汢汪沂沍沚沁沛汾汨汳沒沐泄泱泓沽泗泅泝沮沱沾\n"
            "沺泛泯泙泪洟衍洶洫洽洸洙洵洳洒洌浣涓浤浚浹浙涎涕濤涅淹渕渊涵淇淦涸淆淬淞淌淨淒淅淺淙淤淕淪淮渭湮渮渙湲湟渾渣湫渫湶湍渟湃渺湎渤滿渝游溂溪溘滉溷滓溽溯滄溲滔滕溏溥滂溟潁漑灌滬滸滾漿滲漱滯漲滌\n"
            "漾漓滷澆潺潸澁澀潯潛濳潭澂潼潘澎澑濂潦澳澣澡澤澹濆澪濟濕濬濔濘濱濮濛瀉瀋濺瀑瀁瀏濾瀛瀚潴瀝瀘瀟瀰瀾瀲灑灣炙炒炯烱炬炸炳炮烟烋烝烙焉烽焜焙煥煕熈煦煢煌煖煬熏燻熄熕熨熬燗熹熾燒燉燔燎燠燬燧燵燼\n"
            "燹燿爍爐爛爨爭爬爰爲爻爼爿牀牆牋牘牴牾犂犁犇犒犖犢犧犹犲狃狆狄狎狒狢狠狡狹狷倏猗猊猜猖猝猴猯猩猥猾獎獏默獗獪獨獰獸獵獻獺珈玳珎玻珀珥珮珞璢琅瑯琥珸琲琺瑕琿瑟瑙瑁瑜瑩瑰瑣瑪瑶瑾璋璞璧瓊瓏瓔珱\n"
            "瓠瓣瓧瓩瓮瓲瓰瓱瓸瓷甄甃甅甌甎甍甕甓甞甦甬甼畄畍畊畉畛畆畚畩畤畧畫畭畸當疆疇畴疊疉疂疔疚疝疥疣痂疳痃疵疽疸疼疱痍痊痒痙痣痞痾痿痼瘁痰痺痲痳瘋瘍瘉瘟瘧瘠瘡瘢瘤瘴瘰瘻癇癈癆癜癘癡癢癨癩癪癧癬癰\n"
            "癲癶癸發皀皃皈皋皎皖皓皙皚皰皴皸皹皺盂盍盖盒盞盡盥盧盪蘯盻眈眇眄眩眤眞眥眦眛眷眸睇睚睨睫睛睥睿睾睹瞎瞋瞑瞠瞞瞰瞶瞹瞿瞼瞽瞻矇矍矗矚矜矣矮矼砌砒礦砠礪硅碎硴碆硼碚碌碣碵碪碯磑磆磋磔碾碼磅磊磬\n"
            "磧磚磽磴礇礒礑礙礬礫祀祠祗祟祚祕祓祺祿禊禝禧齋禪禮禳禹禺秉秕秧秬秡秣稈稍稘稙稠稟禀稱稻稾稷穃穗穉穡穢穩龝穰穹穽窈窗窕窘窖窩竈窰窶竅竄窿邃竇竊竍竏竕竓站竚竝竡竢竦竭竰笂笏笊笆笳笘笙笞笵笨笶筐\n"
            "筺笄筍笋筌筅筵筥筴筧筰筱筬筮箝箘箟箍箜箚箋箒箏筝箙篋篁篌篏箴篆篝篩簑簔篦篥籠簀簇簓篳篷簗簍篶簣簧簪簟簷簫簽籌籃籔籏籀籐籘籟籤籖籥籬籵粃粐粤粭粢粫粡粨粳粲粱粮粹粽糀糅糂糘糒糜糢鬻糯糲糴糶糺紆\n"
            "紂紜紕紊絅絋紮紲紿紵絆絳絖絎絲絨絮絏絣經綉絛綏絽綛綺綮綣綵緇綽綫總綢綯緜綸綟綰緘緝緤緞緻緲緡縅縊縣縡縒縱縟縉縋縢繆繦縻縵縹繃縷縲縺繧繝繖繞繙繚繹繪繩繼繻纃緕繽辮繿纈纉續纒纐纓纔纖纎纛纜缸缺\n"
            "罅罌罍罎罐网罕罔罘罟罠罨罩罧罸羂羆羃羈羇羌羔羞羝羚羣羯羲羹羮羶羸譱翅翆翊翕翔翡翦翩翳翹飜耆耄耋耒耘耙耜耡耨耿耻聊聆聒聘聚聟聢聨聳聲聰聶聹聽聿肄肆肅肛肓肚肭冐肬胛胥胙胝胄胚胖脉胯胱脛脩脣脯腋\n"
            "隋腆脾腓腑胼腱腮腥腦腴膃膈膊膀膂膠膕膤膣腟膓膩膰膵膾膸膽臀臂膺臉臍臑臙臘臈臚臟臠臧臺臻臾舁舂舅與舊舍舐舖舩舫舸舳艀艙艘艝艚艟艤艢艨艪艫舮艱艷艸艾芍芒芫芟芻芬苡苣苟苒苴苳苺莓范苻苹苞茆苜茉苙\n"
            "茵茴茖茲茱荀茹荐荅茯茫茗茘莅莚莪莟莢莖茣莎莇莊荼莵荳荵莠莉莨菴萓菫菎菽萃菘萋菁菷萇菠菲萍萢萠莽萸蔆菻葭萪萼蕚蒄葷葫蒭葮蒂葩葆萬葯葹萵蓊葢蒹蒿蒟蓙蓍蒻蓚蓐蓁蓆蓖蒡蔡蓿蓴蔗蔘蔬蔟蔕蔔蓼蕀蕣蕘蕈\n"
            "蕁蘂蕋蕕薀薤薈薑薊薨蕭薔薛藪薇薜蕷蕾薐藉薺藏薹藐藕藝藥藜藹蘊蘓蘋藾藺蘆蘢蘚蘰蘿虍乕虔號虧虱蚓蚣蚩蚪蚋蚌蚶蚯蛄蛆蚰蛉蠣蚫蛔蛞蛩蛬蛟蛛蛯蜒蜆蜈蜀蜃蛻蜑蜉蜍蛹蜊蜴蜿蜷蜻蜥蜩蜚蝠蝟蝸蝌蝎蝴蝗蝨蝮蝙\n"
            "蝓蝣蝪蠅螢螟螂螯蟋螽蟀蟐雖螫蟄螳蟇蟆螻蟯蟲蟠蠏蠍蟾蟶蟷蠎蟒蠑蠖蠕蠢蠡蠱蠶蠹蠧蠻衄衂衒衙衞衢衫袁衾袞衵衽袵衲袂袗袒袮袙袢袍袤袰袿袱裃裄裔裘裙裝裹褂裼裴裨裲褄褌褊褓襃褞褥褪褫襁襄褻褶褸襌褝襠襞\n"
            "襦襤襭襪襯襴襷襾覃覈覊覓覘覡覩覦覬覯覲覺覽覿觀觚觜觝觧觴觸訃訖訐訌訛訝訥訶詁詛詒詆詈詼詭詬詢誅誂誄誨誡誑誥誦誚誣諄諍諂諚諫諳諧諤諱謔諠諢諷諞諛謌謇謚諡謖謐謗謠謳鞫謦謫謾謨譁譌譏譎證譖譛譚譫\n"
            "譟譬譯譴譽讀讌讎讒讓讖讙讚谺豁谿豈豌豎豐豕豢豬豸豺貂貉貅貊貍貎貔豼貘戝貭貪貽貲貳貮貶賈賁賤賣賚賽賺賻贄贅贊贇贏贍贐齎贓賍贔贖赧赭赱赳趁趙跂趾趺跏跚跖跌跛跋跪跫跟跣跼踈踉跿踝踞踐踟蹂踵踰踴蹊\n"
            "蹇蹉蹌蹐蹈蹙蹤蹠踪蹣蹕蹶蹲蹼躁躇躅躄躋躊躓躑躔躙躪躡躬躰軆躱躾軅軈軋軛軣軼軻軫軾輊輅輕輒輙輓輜輟輛輌輦輳輻輹轅轂輾轌轉轆轎轗轜轢轣轤辜辟辣辭辯辷迚迥迢迪迯邇迴逅迹迺逑逕逡逍逞逖逋逧逶逵逹迸\n"
            "遏遐遑遒逎遉逾遖遘遞遨遯遶隨遲邂遽邁邀邊邉邏邨邯邱邵郢郤扈郛鄂鄒鄙鄲鄰酊酖酘酣酥酩酳酲醋醉醂醢醫醯醪醵醴醺釀釁釉釋釐釖釟釡釛釼釵釶鈞釿鈔鈬鈕鈑鉞鉗鉅鉉鉤鉈銕鈿鉋鉐銜銖銓銛鉚鋏銹銷鋩錏鋺鍄錮\n"
            "錙錢錚錣錺錵錻鍜鍠鍼鍮鍖鎰鎬鎭鎔鎹鏖鏗鏨鏥鏘鏃鏝鏐鏈鏤鐚鐔鐓鐃鐇鐐鐶鐫鐵鐡鐺鑁鑒鑄鑛鑠鑢鑞鑪鈩鑰鑵鑷鑽鑚鑼鑾钁鑿閂閇閊閔閖閘閙閠閨閧閭閼閻閹閾闊濶闃闍闌闕闔闖關闡闥闢阡阨阮阯陂陌陏陋陷陜陞\n"
            "陝陟陦陲陬隍隘隕隗險隧隱隲隰隴隶隸隹雎雋雉雍襍雜霍雕雹霄霆霈霓霎霑霏霖霙霤霪霰霹霽霾靄靆靈靂靉靜靠靤靦靨勒靫靱靹鞅靼鞁靺鞆鞋鞏鞐鞜鞨鞦鞣鞳鞴韃韆韈韋韜韭齏韲竟韶韵頏頌頸頤頡頷頽顆顏顋顫顯顰\n"
            "顱顴顳颪颯颱颶飄飃飆飩飫餃餉餒餔餘餡餝餞餤餠餬餮餽餾饂饉饅饐饋饑饒饌饕馗馘馥馭馮馼駟駛駝駘駑駭駮駱駲駻駸騁騏騅駢騙騫騷驅驂驀驃騾驕驍驛驗驟驢驥驤驩驫驪骭骰骼髀髏髑髓體髞髟髢髣髦髯髫髮髴髱髷\n"
            "髻鬆鬘鬚鬟鬢鬣鬥鬧鬨鬩鬪鬮鬯鬲魄魃魏魍魎魑魘魴鮓鮃鮑鮖鮗鮟鮠鮨鮴鯀鯊鮹鯆鯏鯑鯒鯣鯢鯤鯔鯡鰺鯲鯱鯰鰕鰔鰉鰓鰌鰆鰈鰒鰊鰄鰮鰛鰥鰤鰡鰰鱇鰲鱆鰾鱚鱠鱧鱶鱸鳧鳬鳰鴉鴈鳫鴃鴆鴪鴦鶯鴣鴟鵄鴕鴒鵁鴿鴾鵆鵈\n"
            "鵝鵞鵤鵑鵐鵙鵲鶉鶇鶫鵯鵺鶚鶤鶩鶲鷄鷁鶻鶸鶺鷆鷏鷂鷙鷓鷸鷦鷭鷯鷽鸚鸛鸞鹵鹹鹽麁麈麋麌麒麕麑麝麥麩麸麪麭靡黌黎黏黐黔黜點黝黠黥黨黯黴黶黷黹黻黼黽鼇鼈皷鼕鼡鼬鼾齊齒齔齣齟齠齡齦齧齬齪齷齲齶龕龜龠\n"
            "堯槇遙瑤凜熙\n")

    def flash_color_list(self):             #点滅用カラーリスト群の定義
        """
        点滅用カラーコードリストの定義
        """
        #サブウェポンセレクターカーソルなどで使用する点滅用カラーリスト群(pyxelのカラーナンバーだよ)
        self.blinking_color         = [0,1,5,12, 6,7,6,12,5,1]
        self.red_flash_color        = [0,1,5, 4, 2,8,2, 4,5,1]
        self.green_flash_color      = [0,1,5, 3,11,11,3,5,1,0]
        self.yellow_flash_color     = [0,2,4,9,9,10,9,9,4,2,0]
        self.monochrome_flash_color = [0,0,1,5,12,13,15,7,7,15,13,12,5,1,0]
        self.rainbow_flash_color    = [3,4,5,6,7,8,9,10,11,12,13,14,15,1,2]

    def expansion_shrink(self):             #サブウェポンアイテムの外を回っている四角形描画で使用するための「おっきくなったり、ちいさくなったりするオフセット数値」のリスト群(単位はドット)
        """
        サブウェポンアイテムの外を回っている四角形描画で使用するための「おっきくなったり、ちいさくなったりするオフセット数値」のリスト群(単位はドット)定義
        """
        self.expansion_shrink_number = [1,1,1,2,2,2,3,3,3,4,   4,5,5,6,6,7,8,9,10,9,   8,7,6,6,5,5,4,4,3,3,   3,2,2,2,1,1,1,1,1,1,1,1]

    def game_difficulty_list(self):         #難易度ごとの各種設定数値のリストの定義
        """
        難易度ごとの各種設定数値のリストの定義
        """
        #フォーマット
        #[s=start b=bonusの略です
        #難易度名,   説明文,sショットb,sミサイルb,sシールドb,クロー初期値,ステージ後に回復するシールド値,撃ち返し弾の有無,      スコア倍率, ランク上昇frame,sランク数,被弾後無敵時間,アイテム取得後無敵時間,アイテム敵弾消去,ランク限界,撃ち返し開始loop,撃ち返し開始stage,1ランクダウンに必要なダメージ数,ループ時の動作,        アイテムが接近開始してくる距離, アイテムバウンド数]
        #]
        self.game_difficulty_list = [
            [GAME_VERY_EASY,"VERY EASY" ,2,2,2,             TWO_CLAW,   REPAIR_SHIELD3,           RETURN_BULLET_NONE,         1.0,        1500,           0,     60,           10,                  1,              50,       2,              7,               1,                         LOOP_POWER_CONTINUE,     1600,                       8], 
            [GAME_EASY     ,"EASY"      ,1,1,1,             ONE_CLAW,   REPAIR_SHIELD2,           RETURN_BULLET_NONE,         1.0,        1300,           5,     45,            5,                  1,              60,       2,              5,               1,                         LOOP_ONE_LEVEL_DOWN,      900,                       7],
            [GAME_NORMAL   ,"NORMAL"    ,0,0,0,             NO_CLAW,    REPAIR_SHIELD2,           RETURN_BULLET_AIM,          1.0,        1200,          10,     30,            3,                  0,              70,       2,              3,               2,                         LOOP_TWO_LEVEL_DOWN,      800,                       6],
            [GAME_HARD     ,"HARD"      ,0,0,0,             NO_CLAW,    REPAIR_SHIELD1,           RETURN_BULLET_AIM,          2.0,        1000,          20,     29,            2,                  0,              80,       1,             10,               2,                         LOOP_THREE_LEVEL_DOWN,    700,                       5],
            [GAME_VERY_HARD,"VERY HARD" ,0,0,0,             NO_CLAW,    REPAIR_SHIELD1,           RETURN_BULLET_DELAY_AIM,    3.0,         800,          40,     26,            0,                  0,              85,       1,              8,               3,                         LOOP_FIVE_LEVEL_DOWN,     600,                       4],
            [GAME_INSAME   ,"INSAME"    ,0,0,0,             NO_CLAW,    REPAIR_SHIELD0,           RETURN_BULLET_DELAY_AIM,    4.0,         600,          60,     23,            0,                  0,              99,       1,              5,               3,                         LOOP_ALL_RESET,           500,                       3],
            ]

    def game_rank_data_list(self):          #ランク値による各種設定数値のリストの定義
        """
        ランク値による各種設定数値のリストの定義
        """
        #フォーマット
        #敵スピード倍率は3.9までにしておいてください、追尾戦闘機のスピードが速すぎると一瞬で画面外に飛んでいくみたいで・・
        # [ランク, 敵スピード倍率, 敵弾スピード倍率, 撃ち返し弾確率%, 敵耐久力倍率, 弾追加数, 弾発射間隔%, nWAY弾レベル]
        self.game_rank_data_list = [
            [ 0,    1.0,         1.0,             0,               1.0,        0,       100,          0],
            [ 1,    1.0,         1.0,             0,               1.0,        0,       100,          0],
            [ 2,    1.1,         1.0,             1,               1.0,        0,        99,          0],
            [ 3,    1.1,         1.0,             1,               1.0,        0,        99,          0],
            [ 4,    1.2,         1.0,             1,               1.0,        0,        99,          0],
            [ 5,    1.2,         1.1,             1,               1.0,        0,        99,          0],
            [ 6,    1.2,         1.1,             2,               1.0,        0,        98,          0],
            [ 7,    1.2,         1.1,             2,               1.0,        0,        98,          0],
            [ 8,    1.2,         1.1,             2,               1.0,        0,        98,          0],
            [ 9,    1.2,         1.1,             2,               1.0,        0,        98,          0],
            [10,    1.3,         1.1,             3,               1.0,        1,        98,          0],
            [11,    1.3,         1.1,             3,               1.0,        1,        97,          0],
            [12,    1.3,         1.2,             3,               1.0,        1,        97,          0],
            [13,    1.3,         1.2,             4,               1.0,        1,        97,          0],
            [14,    1.3,         1.2,             4,               1.0,        1,        96,          0],
            [15,    1.3,         1.3,             4,               1.0,        1,        96,          0],
            [16,    1.3,         1.3,             5,               1.0,        1,        96,          0],
            [17,    1.3,         1.3,             5,               1.0,        1,        95,          0],
            [18,    1.3,         1.3,             5,               1.0,        1,        95,          0],
            [19,    1.3,         1.3,             5,               1.0,        1,        95,          0],
            [20,    1.3,         1.4,             6,               1.0,        2,        94,          0],
            [21,    1.3,         1.4,             6,               1.0,        2,        94,          0],
            [22,    1.3,         1.4,             6,               1.0,        2,        93,          0],
            [23,    1.3,         1.4,             6,               1.0,        2,        93,          1],
            [24,    1.3,         1.4,             6,               1.0,        2,        93,          1],
            [25,    1.3,         1.5,             6,               1.0,        2,        92,          1],
            [26,    1.3,         1.5,             6,               1.0,        2,        92,          1],
            [27,    1.3,         1.5,             7,               1.1,        2,        92,          1],
            [28,    1.3,         1.5,             7,               1.1,        2,        91,          1],
            [29,    1.3,         1.5,             7,               1.1,        2,        91,          1],
            [30,    1.3,         1.5,             7,               1.1,        3,        91,          1],
            [31,    1.4,         1.5,             7,               1.1,        3,        91,          1],
            [32,    1.4,         1.5,             7,               1.1,        3,        91,          1],
            [33,    1.4,         1.5,             7,               1.1,        3,        91,          1],        
            [34,    1.4,         1.5,             8,               1.1,        3,        90,          1],
            [35,    1.4,         1.5,             8,               1.2,        3,        90,          1],
            [36,    1.4,         1.5,             8,               1.2,        3,        89,          1],
            [37,    1.4,         1.5,             8,               1.2,        3,        89,          1],
            [38,    1.4,         1.5,             9,               1.2,        3,        89,          1],
            [39,    1.4,         1.5,             9,               1.2,        3,        88,          1],
            [40,    1.4,         1.5,             9,               1.2,        3,        88,          2],
            [41,    1.5,         1.5,            10,               1.2,        3,        87,          2],
            [42,    1.5,         1.5,            10,               1.2,        3,        87,          2],
            [43,    1.5,         1.5,            11,               1.2,        3,        87,          2],
            [44,    1.5,         1.5,            11,               1.2,        3,        86,          2],
            [45,    1.5,         1.5,            12,               1.3,        3,        86,          2],
            [46,    1.5,         1.6,            12,               1.3,        3,        86,          2],
            [47,    1.5,         1.6,            12,               1.3,        3,        85,          2],
            [48,    1.5,         1.6,            12,               1.3,        3,        85,          2],
            [49,    1.5,         1.6,            12,               1.3,        3,        84,          2],
            [50,    1.5,         1.6,            12,               1.3,        4,        84,          2],
            
            [51,    1.5,         1.6,            12,               1.3,        4,        83,          2],
            [52,    1.5,         1.6,            13,               1.3,        4,        83,          2],
            [53,    1.5,         1.6,            13,               1.3,        4,        83,          2],
            [54,    1.5,         1.6,            13,               1.3,        4,        82,          2],
            [55,    1.5,         1.6,            13,               1.3,        4,        82,          2],
            [56,    1.5,         1.6,            13,               1.3,        4,        82,          2],
            [57,    1.5,         1.6,            13,               1.3,        4,        81,          2],
            [58,    1.5,         1.6,            13,               1.3,        4,        81,          2],
            [59,    1.6,         1.6,            13,               1.3,        4,        81,          2],
            [60,    1.6,         1.7,            14,               1.3,        4,        81,          2],
            [61,    1.6,         1.7,            14,               1.4,        4,        80,          2],
            [62,    1.6,         1.7,            14,               1.4,        4,        80,          2],
            [63,    1.6,         1.7,            14,               1.4,        4,        80,          2],
            [64,    1.6,         1.7,            14,               1.4,        5,        80,          2],
            [65,    1.6,         1.7,            14,               1.4,        5,        79,          2],
            [66,    1.6,         1.7,            14,               1.4,        5,        79,          2],
            [67,    1.6,         1.7,            15,               1.4,        5,        79,          2],
            [68,    1.6,         1.7,            15,               1.4,        5,        78,          2],
            [69,    1.6,         1.7,            15,               1.4,        5,        78,          2],
            [70,    1.6,         1.7,            15,               1.4,        5,        77,          3],
            [71,    1.6,         1.7,            15,               1.4,        5,        77,          3],
            [72,    1.6,         1.7,            15,               1.4,        5,        76,          3],
            [73,    1.6,         1.7,            16,               1.4,        5,        75,          3],
            [74,    1.6,         1.7,            16,               1.4,        5,        74,          3],
            [75,    1.6,         1.8,            16,               1.4,        5,        73,          3],
            [76,    1.6,         1.8,            16,               1.4,        5,        72,          3],
            [77,    1.6,         1.8,            16,               1.4,        5,        72,          3],
            [78,    1.6,         1.8,            16,               1.4,        5,        72,          3],
            [79,    1.6,         1.8,            16,               1.4,        5,        71,          3],
            [80,    1.6,         1.8,            16,               1.4,        5,        71,          3],
            [81,    1.6,         1.8,            17,               1.4,        5,        70,          3],
            [82,    1.6,         1.8,            17,               1.4,        5,        70,          3],
            [83,    1.6,         1.8,            17,               1.4,        5,        69,          3],
            [84,    1.6,         1.8,            17,               1.4,        5,        69,          3],
            [85,    1.6,         1.8,            17,               1.5,        5,        69,          3],
            [86,    1.6,         1.9,            17,               1.5,        5,        68,          3],
            [87,    1.6,         1.9,            17,               1.5,        6,        68,          3],
            [88,    1.6,         1.9,            17,               1.5,        6,        67,          3],
            [89,    1.6,         1.9,            17,               1.5,        6,        66,          3],
            [90,    1.6,         1.9,            17,               1.5,        6,        66,          4],
            [91,    1.6,         1.9,            17,               1.5,        6,        65,          4],
            [92,    1.6,         1.9,            17,               1.5,        6,        64,          4],
            [93,    1.6,         1.9,            17,               1.5,        6,        63,          4],
            [94,    1.6,         1.9,            18,               1.5,        6,        62,          4],
            [95,    1.6,         1.9,            18,               1.6,        6,        61,          4],
            [96,    1.6,         2.0,            18,               1.6,        7,        60,          4],
            [97,    1.7,         2.0,            18,               1.6,        7,        59,          4],
            [98,    1.7,         2.0,            19,               1.6,        7,        58,          4],
            [99,    1.7,         2.0,            20,               1.6,        7,        57,          4],
            ]

    def storyboard(self):                  #タイトルデモ、ミドルデモなどのビジュアルシーンの絵コンテ(ストーリーボード）の定義とか
        """
        タイトルデモ、ミドルデモなどのビジュアルシーンの絵コンテ(ストーリーボード）の定義とかそういうの
        """
        #フォーマット
        #   ビジュアルシーンID,            トータルタイムカウンタ(フレーム), 終了時の動作
        self.title_storyboard = [
            [VS_ID_OPENING_STORY1,         100000,                         END_ACTION_DEL            ],
            [VS_ID_OPENING_STORY1,         100000,                         END_ACTION_LOOP            ],
            ]
