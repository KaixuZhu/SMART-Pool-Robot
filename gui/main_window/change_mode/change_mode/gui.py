from pathlib import Path

from tkinter import (
    Frame,
    Canvas,
    Entry,
    StringVar,
    Text,
    Button,
    PhotoImage,
    messagebox,
)
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_rooms():
    AddRooms()


class AddRooms(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = {"r_no": StringVar(), "type": StringVar(), "price": StringVar()}

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
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        button_1.place(x=264.0, y=322.0, width=190.0, height=48.0)
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        button_2.place(x=249.0, y=70.0, width=211.0, height=74.0)
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        button_3.place(x=249.0, y=170.0, width=211.0, height=74.0)
