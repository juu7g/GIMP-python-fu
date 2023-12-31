"""
画像をコラージュする
GIMP Python-Fuスクリプトをバッチ処理で呼び出す
"""
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinterdnd2 import *
from PIL import Image, ImageTk, ImageColor          # Pillow
import sys, re, os
sys.path.append(os.path.dirname(sys.executable))
import settings_collage

class GIMP_Script():
    """
    GIMP Script 起動クラス
    """
    def __init__(self, view:tk.Frame) -> None:
        """
        コンストラクタ：制御画面クラスを関連付ける
        Args:
            Frame:  画面クラス(ビュー)
        """
        self.app = None     # pywinautoのApplication(またはDesktop)オブジェクトを保持
        self.view = view    # 制御画面クラスのオブジェクト

    def do_gimp_script(self, _files_t:list, border_rgb:tuple, img_width:int, border_width:int, event=None) -> int:
        """
        GIMPスクリプト(バッチ)の実行
        Args:
            list:   ファイルパス(4つ)
            tuple:  境界線の色(RGB)
            int:    再生画像の幅
        Returns:
            int:    バッチの結果(0:OK)
        """
        _shori = 2

        _files_b = (r'image_file_name1', 
                    r'image_file_name2', 
                    r'image_file_name3',  
                    r'image_file_name4')

        gimp1 = settings_collage.gimp1
        gimp2 = settings_collage.gimp2

        _script_encoding = 'utf-8'
        if hasattr(sys, '_MEIPASS'): # under pyinstaller
            scriptpath = os.path.join(sys._MEIPASS, settings_collage.scriptpath)
            # _script_encoding = 'cp932'
        else:
            scriptpath = os.path.join('..', settings_collage.scriptpath)

        with open(scriptpath, encoding=_script_encoding) as f:
            _script = f.readlines()
        _script = "".join(_script)

        # 画像ファイル名置換
        for f_b, f_t in zip(_files_b, _files_t):
            _script = _script.replace(f_b, f_t)

        # 境界線の色置換
        _script = _script.replace('gimpcolor.RGB(255, 255, 255)', f'gimpcolor.RGB({border_rgb[0]},{border_rgb[1]} ,{border_rgb[2]})')

        # 作成画像の幅置換
        _script = _script.replace('_width = 800', f'_width = {img_width}')

        # 境界線の幅置換
        _script = _script.replace('border_width = 4', f'border_width = {border_width}')

        # 保存パス置換
        if hasattr(sys, '_MEIPASS'): # under pyinstaller
            _script = _script.replace('replace_path', f'{os.path.dirname(sys.executable)}')
        else:
            _script = _script.replace('replace_path', '.')

        # GIMPのコンソールモードを置換
        if _shori == 2:
            _script = _script.replace('123456', 'False')

        # GIMPのコマンドライン引数の指定
        if _shori == 2:
            # コンソールモード
            _cmd = [f"{gimp2}", "-i", "-n", "-c", "-d", "-s", "-f"
                , "--batch-interpreter", "python-fu-eval", "-b", "-", "-b", "pdb.gimp_quit(1)"]
        else:
            # 通常モード
            _cmd = [f"{gimp1}", "-n", "-c", "-d", "-s", "-f"
                , "--batch-interpreter", "python-fu-eval", "-b", "-", "-b", "pdb.gimp_quit(1)"]
            # スクリプトにエラーがあった場合、"pdb.gimp_quit(1)"を削除するとGIMP画面が残る

        # GIMPの起動
        result = subprocess.run(_cmd, input=_script, encoding=_script_encoding)

        return result.returncode

class MyFrame(tk.Frame):
    """
    操作画面クラス
    """
    def __init__(self, master) -> None:
        """
        コンストラクタ：画面作成
        """
        super().__init__(master)

        # self.config(background="lightblue")     # ボタンの境目に色を出すために背景色を指定

        # ボタン用フレーム
        frm_buttons = tk.Frame(self, background='lightblue')
        frm_buttons.pack(side=tk.LEFT, fill=tk.Y)

        # 画像配置用フレーム
        self.frm_images = tk.Frame(self, background='white')
        self.frm_images.pack(side=tk.RIGHT, fill=tk.BOTH)

        # 画像用ラベル
        self.var_width = tk.IntVar(value=800)
        self.var_border = tk.IntVar(value=10)
        self.lbl_imgs = []
        self.image_paths = ["", "", "", ""]
        
        # コマンドライン引数で指定された画像のパスを保存
        if len(sys.argv) > 4:
            self.image_paths = sys.argv[1:5]
        
        for i in range(4):
            _img = self.load_image(self.image_paths[i])
            self.lbl_imgs.append(tk.Label(self.frm_images, image=_img, borderwidth=0))
            self.lbl_imgs[i].img = _img
            self.lbl_imgs[i].grid(row=i//2, column=i%2, padx=(self.var_border.get(), self.var_border.get() * (i%2)), pady=(self.var_border.get(), self.var_border.get() * (i//2)))
            self.lbl_imgs[i].pathx = i
            # D&Dの設定
            self.lbl_imgs[i].dnd_bind(sequence='<<Drop>>', func=self.load_image_to_label)
            self.lbl_imgs[i].drop_target_register(DND_FILES)

        # 作成ボタン
        self.btn_create = tk.Button(frm_buttons, text="作成")
        self.btn_create.pack(fill=tk.X, pady=(5))

        # 色選択ボタン
        self.btn_color = tk.Button(frm_buttons, text="色選択", command=self.get_color)
        self.btn_color.pack(fill=tk.X, pady=(0,5))

        # 色選択コンボボックス
        self.colors = list(ImageColor.colormap.keys())  # 選択候補用データ
        var_color = tk.StringVar()
        self.cmb_color = ttk.Combobox(frm_buttons, values=self.colors, textvariable=var_color
                                    , postcommand=lambda : self.cmb_color.config(values=self.colors)
                                    , validate='key'
                                    , validatecommand=(self.register(self.cmb_validate), '%d', '%P'))
        self.cmb_color.pack(fill=tk.X, pady=(0,5))
        self.cmb_color.bind('<<ComboboxSelected>>', self.set_cmb_color)

        # 生成画像の幅指定 エントリーは検証して数字のみ入力
        frm_width = tk.Frame(frm_buttons)
        self.lbl_width = tk.Label(frm_width, text="生成画像の幅", anchor="e")
        self.ety_width = tk.Entry(frm_width, width=6, textvariable=self.var_width
                                , justify=tk.RIGHT, validate="key"
                                , vcmd=(self.register(self.entry_validate), "%d", "%S"))
        self.ety_width.bind('<Return>', self.change_width)
        self.ety_width.pack(side=tk.RIGHT, padx=5)
        self.lbl_width.pack(side=tk.LEFT, fill=tk.X)
        frm_width.pack(fill=tk.X, pady=(0, 5))

        # 境界線の幅指定 エントリーは検証して数字のみ入力
        frm_border = tk.Frame(frm_buttons)
        lbl_border = tk.Label(frm_border, text="境界線の幅")
        ety_border = tk.Entry(frm_border, width=6, textvariable=self.var_border
                                , justify=tk.RIGHT, validate="key"
                                , vcmd=(self.register(self.entry_validate), "%d", "%S"))
        ety_border.bind('<Return>', self.change_border_width)
        lbl_border.pack(side=tk.LEFT)
        ety_border.pack(side=tk.RIGHT, padx=5)
        frm_border.pack(fill=tk.X, pady=(0, 5))

    @property
    def thumbnail_xy(self):
        """
        コラージュする個々の画像の幅と高さ(生成画像の幅と境界の幅により可変)
        Returns:
            int:    コラージュする画像の幅
            int:    コラージュする画像の高さ
        """
        _width = self.var_width.get()
        _swidth = (_width - self.var_border.get() * 3) // 2  # 横に2分割した時のコラージュ画像の幅
        _sheight = _swidth * 3 // 4   # コラージュ画像の高さ アスペクト比4:3で計算
        return (_swidth, _sheight)

    def load_image(self, path:str) -> ImageTk.PhotoImage:
        """
        画像を読み込んで縮小(pillowを使用)
        self.thumbnail_xyの幅と高さに縮小
        """
        if path:
            _img = Image.open(path)
            _img.thumbnail((self.thumbnail_xy[0], self.thumbnail_xy[0]), Image.BICUBIC)
        else:
            # 画像がない時の初期画像
            _img = Image.new('RGBA', (self.thumbnail_xy[0], self.thumbnail_xy[1]), (255, 0, 0, 0))  # 透明なものにしないとgifの色が変わる
        return ImageTk.PhotoImage(_img)

    def get_color(self, event=None):
        """
        色の選択
        色選択ダイアログを表示して選択された色を取得し、frm_imagesの背景に設定
        """
        _color = colorchooser.askcolor(title="色選択")  # ダイアログを表示し色を選択
        self.frm_images.config(background=_color[1])    # 背景色を設定

    def set_cmb_color(self, event=None):
        """
        色を設定
        色選択コンボボックスで選択された色を取得し、frm_imagesの背景に設定
        コンボボックスから色を選択した時にイベントが発生して起動
        """
        self.frm_images.config(background=self.cmb_color.get())

    def cmb_validate(self, action:str, modify_str:str) -> bool:
        """
        コンボボックスの入力検証
        テキストの内容で色種のリストから一致するものをコンボボックスの出力対象にする
        Args:
            str:    アクション(削除：0、挿入：1、その他：-1)
            str:    変更後のテキスト
        """
        # 入力文字を含むものを色のリストから抽出
        _colors = [s for s in ImageColor.colormap.keys() if re.match(f".*{modify_str}.*", s)]
        # 抽出結果が空なら元のリスト全体を設定
        if _colors:
            self.colors = _colors
        else:
            self.colors = list(ImageColor.colormap.keys())
        return True

    def entry_validate(self, action:str, modify_str:str) -> bool:
        """
        エントリーの入力検証
        Args:
            str:    アクション(削除：0、挿入：1、その他：-1)
            str:    挿入、削除されるテキスト
        """
        if action != "1": return True   # 挿入の時だけ検証
        return modify_str.isdigit()     # 数字かどうか

    def change_width(self, event=None):
        """
        生成画像の幅の変更による画像の読み直しと再表示
        """
        for i in range(4):                          # ラベルの画像の再設定
            self.lbl_imgs[i].img = self.load_image(self.image_paths[i])     # ラベルのimgに画像を読み直し
            self.lbl_imgs[i].config(image=self.lbl_imgs[i].img, borderwidth=0)  # ラベルのimageに再設定
        self.frm_images.update_idletasks()

    def change_border_width(self, event=None):
        """
        境界の幅変更による画像の再描画
        ラベルの外側の間隔を再設定し、画像の幅も変わるので読み直しと再描画
        """
        _bwidth = self.var_border.get()
        for i in range(4):
            self.lbl_imgs[i].grid_remove()  # grid 配置を削除
            self.lbl_imgs[i].grid(row=i//2, column=i%2, padx=(_bwidth, _bwidth * (i%2)), pady=(_bwidth, _bwidth * (i//2)))
            # print(self.lbl_imgs[i].grid_info())
        self.change_width()     # 境界が変わると画像の幅も変える必要がある

    def load_image_to_label(self, event=None):
        """
        ドロップされた画像をラベルに表示
        """
        if not event: return
        path = self.tk.splitlist(event.data)[0]         # ドロップされたパスの取得
        event.widget.img = self.load_image(path)        # 読み込んだ画像の保存
        event.widget.config(image=event.widget.img)     # 読み込んだ画像をラベルに設定
        self.image_paths[event.widget.pathx] = path     # GIMPに渡すパスの更新
        event.widget.update_idletasks()

    def set_control(self, rpa:GIMP_Script):
        """
        コントロールの指定とボタンの操作をパイント
        Args:
            GIMP_Script:    コントロールオブジェクト(GIMPスクリプトを実施するオブジェクト)
        """
        self.rpa = rpa
        # ボタンのバインド
        self.btn_create.config(command=self.do_gimp_script)

    def do_gimp_script(self):
        """
        GIMPスクリプトをバッチで起動
        成功：背景色を緑に エラー：背景色を黄色に
        """
        # 未ロードの画像がある場合はエラー
        if "" in self.image_paths:
            self.btn_create.config(bg="yellow")
            return

        self.btn_create.config(bg="white")
        # 画像表示用フレームの背景色を枠の色に指定してGIMPスクリプトを呼び出す
        _color = ImageColor.getrgb(self.frm_images.cget('background'))
        _result = self.rpa.do_gimp_script(self.image_paths
                    , _color, self.var_width.get(), self.var_border.get())
        # 接続結果に基づいてボタンの背景色を変える(現在結果は常に0)
        if _result == 0:
            self.btn_create.config(bg="lightgreen")
        else:
            self.btn_create.config(bg="yellow")

class App(TkinterDnD.Tk):
    """
    アプリケーションクラス
    """
    def __init__(self) -> None:
        """
        コンストラクタ：操作画面クラスと制御クラスを作成し関連付ける
        """
        super().__init__()

        self.title("GIMPでコラージュ")              # タイトル
        my_frame = MyFrame(self)                    # MyFrameクラス(V)のインスタンス作成
        my_frame.pack()
        rpa_for_browser = GIMP_Script(my_frame)     # 制御クラス(C)のインスタンス作成
        my_frame.set_control(rpa_for_browser)       # MyFrameクラスに制御クラスを関連付ける

if __name__ == '__main__':
    app = App()
    app.mainloop()
