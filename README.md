# GIMP-python-fu
GIMP Python-Fu script collection

## 概要 Description
GIMP の Python-Fu  スクリプトを使ったツール

## 特徴 Features

- 4つの画像をコラージュするGIMP のスクリプトと起動するバッチ  
	- スクリプトファイル：`fu_collage4bat.py`
	- 起動用バッチ　　　：`gimp_collage.bat`
	- GIMP起動用バッチ ：`gimp_fu_collage.bat`

## 依存関係 Requirement

- GIMP 2.10.18
- Windows 64bit OS

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

## プログラムの説明サイト Program description site

- [コラージュ処理をPython-Fuスクリプトでバッチ処理【GIMP】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/blog/gimp/collage/fu-bat)  
  
## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSEファイルを確認してください。  
This software is released under the MIT License, see LICENSE file.

