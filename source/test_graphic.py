import pyxel               #グラフイックキャラやバックグラウンドグラフイック(背景(BG))の表示効果音、キーボードパッド入力などで使用 メインコアゲームエンジン
from const.const  import * #定数定義モジュールの読み込み(公式ではワイルドカードインポート(import *)は推奨されていないんだけど・・・定数定義くらいはいいんじゃないかな？の精神！？
from draw.graph   import * #Appクラスのdraw関数から呼び出される関数群のモジュールの読み込み 基本的に画像表示だけを行う関数(メソッド)群です
import os
import sys

abs_path = os.path.abspath(__file__) #絶対パスを取得
print ("現在の実行ファイル")
print(abs_path) #このプログラム自体がどのフォルダーで起動してるのかコンソールに表示

rel_path = os.path.relpath(__file__) #相対パスを取得
print ("相対パス")
print(rel_path) #相対パスをコンソールに表示

dire = os.getcwd()
print("現地点のパス: {}".format(dire))

for path in sys.path:
    print(path)

class App:
    def __init__(self):
        pyxel.init(256,256,title="test graphic",fps = 60,quit_key=pyxel.KEY_NONE)
        pyxel.load(dire + "/source/assets/graphic/min-sht2.pyxres")
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        # Draw sky
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
App()



