from pathlib import Path
import threading
import time
import tkinter as tk
import random
from tkinter import filedialog
from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from PIL import Image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_path():
    f_path = filedialog.askopenfilename()
    print('\n获取的文件地址：', f_path)


def about():
    About()


def open_image():
    time.sleep(5)
    im = Image.open('C:/Users/Kane/HotinGo/gui/main_window/about/assets/res.jpg')
    im.show()


class About(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.count = 0
        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(200.5, 220.0, image=self.entry_image_1)
        entry_1 = Entry(
            self,
            font=("Montserrat Bold", 13),
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_1.insert(0,'C:/Users/Kane/Pictures/Video Projects/trash.jpg')
        entry_1.place(x=60, y=205, width=285.0, height=30.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : open_image(),
            relief="flat",
        )
        button_3.place(x=100.0, y=300.0, width=190.0, height=48.0)

        get_path()
        textbox=Text(self.canvas,
                     height=25,
                     width=35,
                     font=("微软雅黑",13))
        textbox.place(x=400,y=50)
        def fun_textbox(textbox):
            x=str(int(random.random()*100))
            y=str(int(random.random()*100))
            text = "当前坐标为 x : " + x + "  y : " + y + "\n"
            textbox.insert("end",text)
            textbox.update()
            global timer
            timer = threading.Timer(2.5, lambda : fun_textbox(textbox))
            timer.start()

        timer = threading.Timer(1, lambda : fun_textbox(textbox))
        timer.start()
