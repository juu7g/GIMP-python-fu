# GIMP-python-fu
GIMP Python-Fu script collection

## 概要 Description
GIMP の Python-Fu  スクリプトを使ったツール

## 特徴 Features

- 4つの画像をコラージュするGIMP のスクリプトと起動するバッチ  
	- スクリプトファイル：`fu_collage4bat.py`
	- 起動用バッチ　　　：`gimp_collage.bat`
	- GIMP起動用バッチ ：`gimp_fu_collage.bat`
- 4つの画像をコラージュするGIMP のスクリプトと起動するプログラム  
	- スクリプトファイル：`fu_collage.py`
	- プログラム　　　　：`collage_by_GIMP.py`
	- 設定ファイル　　　：`settings_collage.py`

## 依存関係 Requirement

- 共通
	- GIMP 2.10.18
	- Windows 64bit OS
- プログラム
	- Python 3.8.5
	- Pillow 10.0.0

## 使い方 Usage

- 4つの画像をコラージュするGIMP のスクリプトと起動するバッチ  
	- 起動方法  
		1. エクスプローラなどでコラージュしたい４つの画像を選択（Ctrl を押しながらクリック）
		2. `gimp_collage.bat` に4つの画像をドラックアンドドロップ
		3. ４つの画像があるフォルダに `GIMPyymmddhhmm.jpg` 画像を作成
	- 設定方法  
		`fu_collage4bat.py` を修正
		- 作成される画像の幅：`_width = 800` の800を変更(px)
		- ４つの図形の境界線の幅：`border_width = 10` の10を変更(px)
		- 境界線の色：`_color = gimpcolor.RGB(211, 211, 2111)` の数字を変更

- 4つの画像をコラージュするGIMP のスクリプトと起動するプログラム  
	- 起動方法
		- RPA_GIMP_collage.exe を実行します
		- または RPA_GIMP_collage.exe のアイコンにコラージュしたい画像をドラッグアンドドロップします

	- 操作方法  
		- ドラッグ＆ドロップでの操作
			- アプリ画面上の4つの枠ににコラージュしたい画像をドラッグ＆ドロップ  
		- 生成画像の幅を指定
			- テキストボックスに生成画像の幅を入力しEnterを押します
				- 画面が指定した幅に変わります
		- 境界線の幅を指定
			- テキストボックスに境界線の幅を入力しEnterを押します
				- 画面が指定した幅に変わります
		- 色の選択
			- 色選択ボタンで選択  
				- 色選択ボタンを押すと色選択ダイアログが表示されます
				- 希望の色を選択して OK ボタンを押します
			- 色選択コンボボックスで選択
				- コンボボックスの▼を押すと色名の選択肢が出るので選択します
				- コンボボックスに色名の一部を入れて↓キーを押すと入力した文字を持つ色名を出力します  
		- 画像の生成
			- 作成ボタンを押します

	  - 画面の説明  
		- 作成ボタン　　　　　：コラージュした画像を作成します
		- 色選択ボタン　　　　：境界線の色を指定します
		- 色選択コンボボックス：境界線の色を色名で指定します
		- 生成画像の幅　　　　：生成画像の幅を px で指定します
		- 境界線の幅　　　　　：境界線の幅を px で指定します
		- ４つの四角　　　　　：コラージュする画像を表示します

	- 設定方法  
		`settings_collage.py` を修正  
		- GIMP の exe のパス　　　　　：`gimp1 = r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe"`
		- GIMP のコンソール exe のパス：`gimp2 = r"C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"`
		- GIMP のスクリプトのパス　　 ：`scriptpath = r'scripts\fu_collage.py'`  
			アプリを使用する場合、スクリプトのパスはそのまま使用してください。  
			ソースを利用する場合、スクリプトのパスはソースを置いたフォルダの親フォルダからの相対パスを指定してください。 

## 制限事項  

- 横向きでアスペクト比が 4:3 の画像が対象  

## プログラムの説明サイト Program description site

- [コラージュ処理をPython-Fuスクリプトでバッチ処理【GIMP】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/blog/gimp/collage/fu-bat)  
- [コラージュ処理をPython-FuスクリプトでPythonのGUIを付けて【GIMP、Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/blog/gimp/collage/fu-python)  
  
## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSEファイルを確認してください。  
This software is released under the MIT License, see LICENSE file.

