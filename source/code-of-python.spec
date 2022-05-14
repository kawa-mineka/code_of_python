#pyinstaller用
#code of python specファイル
#
#code-of-python.pyが存在するフォルダー上で
#pyinstaller code-of-python.specって感じで
#コマンドプロンプトから実行してね

import sys
#フォルダーの再帰探索数は5000位にしておく
sys.setrecursionlimit(5000)

block_cipher = None

#assetsフォルダー以下のfonts,graphic,music,replay,sound,systemフォルダーを追加します
added_files = [
    ("assets/fonts","assets/fonts"),
    ("assets/graphic","assets/graphic"),
    ("assets/music","assets/music"),
    ("assets/replay","assets/replay"),
    ("assets/sound","assets/sound"),
    ("assets/system","assets/system"),
]
#パスはコマンドを実行したフォルダーと、その下のassetsフォルダーを指定します
paths = [
    "./",
    "./asstes",
]

a = Analysis(
    ['code-of-python.py'],
    pathex=paths,
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='code-of-python',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
