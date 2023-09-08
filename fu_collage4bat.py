#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *
import gimpcolor

_width = 800							# 完成画像の幅(１つの画像の幅ではない)
border_width = 10						# 境界線の幅(偶数で)
_color = gimpcolor.RGB(211, 211, 2111)	# 色のRGBを指定(255,255,255は白)

_debug = 123456							# デバッグ用バッチで変更するのでここでは変更不可
offset = border_width // 2
_height = _width * 3 // 4   # アスペクト比4:3で計算
_swidth = (_width - border_width * 3) / 2        # 横には2分割
_sheight = (_height - border_width * 3) / 2      # 縦には2分割
_type = 0 # RGB(0), GRAY(1), INDEXED(2)
# ダミーの名前を定義、後で置換して目的のファイル名にする
_files = (r'image_file_name1', 
            r'image_file_name2', 
            r'image_file_name3',  
            r'image_file_name4')

pdb.gimp_message("My Python-fu開始(My Python-fu start)")
img = pdb.gimp_image_new(_width, _height, _type)
layer_ids = []
for _filename in _files:
    layer_id = pdb.gimp_file_load_layer(img, _filename)
    layer_ids.append(layer_id)
    pdb.gimp_image_insert_layer(img, layer_id, None, 0)    # parent(None):no group, position(0):top

pdb.gimp_image_resize_to_layers(img)				# キャンバスのサイズをレイヤーに合わせる
pdb.gimp_image_scale(img, _swidth, _sheight)		# 画像の拡大縮小
pdb.gimp_image_resize(img, _width, _height, 0, 0)	# キャンバスのサイズ変更

pdb.gimp_message("整列開始(Alignment start)")
pdb.gimp_layer_set_offsets(layer_ids[0], border_width, border_width)
pdb.gimp_layer_set_offsets(layer_ids[1], _swidth + border_width * 2, border_width)
pdb.gimp_layer_set_offsets(layer_ids[2], border_width, _sheight + border_width * 2)
pdb.gimp_layer_set_offsets(layer_ids[3], _swidth + border_width * 2, _sheight + border_width * 2)

pdb.gimp_message("グリッドフィルター開始(Start grid filter)")
# グリッド用レイヤーの作成(画像、幅、高さ、タイプ(1:RGBA(透明付 ))、名前、透明度、モード)
grid = pdb.gimp_layer_new(img, _width, _height, 1, "grid", 100, 0)
pdb.gimp_image_insert_layer(img, grid, None, 0)    # parent(None):no group, position(0):top
pdb.gimp_message("グリッドレイヤー作成完(Grid layer created)")
# グリッド(レガシー)
# 画像、対象、水平線幅、間隔、オフセット、色、透明度(0-255)、垂直線高さ、間隔、オフセット、色、透明度、交点幅、間隔、オフセット、色、透明度
hspace_width = _width // 2 - offset
vspace_width = _height // 2 - offset
# pdb.gimp_message('bd:{}, hspace:{}, vspace:{}'.format(border_width, hspace_width, vspace_width))
pdb.plug_in_grid(img, grid, border_width, vspace_width, offset, _color, 255
                          , border_width, hspace_width, offset, _color, 255
                          , 0, 0, 0, _color, 0)
pdb.gimp_message("グリッド作成完(Grided)")

if _debug:
    pdb.gimp_display_new(img)
    pdb.gimp_message("イメージ表示(image display)")

# 表示されているレイヤーをマージして一つのレイヤーに
layer = pdb.gimp_image_merge_visible_layers(img, EXPAND_AS_NECESSARY)

# 画像の保存
from datetime import datetime
out_f_name = "GIMP" + datetime.now().strftime('%y%m%d%H%M') + ".jpg"
pdb.gimp_file_save(img, layer, out_f_name, "")
