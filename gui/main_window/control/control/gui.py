from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_reservations():
    AddReservations()


class AddReservations(Frame):
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
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.print_res(param="已开机"),
            relief="flat",
        )
        button_1.place(x=269.0, y=322.0, width=190.0, height=48.0)

        self.canvas.create_text(
            200.0,
            30.0,
            anchor="nw",
            text="控制机器人",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            549.0,
            59.0,
            anchor="nw",
            text="Operations",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_rectangle(
            515.0, 59.0, 517.0, 370.0, fill="#EFEFEF", outline=""
        )
        # Set default value for entry

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_go.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.print_res(param="已前进"),
            relief="flat",
        )
        button_4.place(x=250.0, y=55.0, width=209.0, height=74.0)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_back.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.print_res(param="已后退"),
            relief="flat",
        )
        button_5.place(x=250.0, y=220.0, width=209.0, height=74.0)

        self.button_image_6 = PhotoImage(file=relative_to_assets("button_left.png"))
        button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.print_res(param="已左转"),
            relief="flat",
        )
        button_6.place(x=100.0, y=137.5, width=209.0, height=74.0)

        self.button_image_7 = PhotoImage(file=relative_to_assets("button_right.png"))
        button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.print_res(param="已右转"),
            relief="flat",
        )
        button_7.place(x=400, y=137.5, width=209.0, height=74.0)

    def print_res(self, param):
        if param == "已开机" and self.count == 0:
            self.count = 1
        elif param == "已开机" and self.count == 1:
            self.count = 0
            param = "已关机"
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(141.5, 165.0, image=self.entry_image_2)
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=("Gen Jyuu Gothic P Bold", 18 * -1),
            foreground="#777777",
        )
        entry_2.insert(0,param)
        entry_2.place(x=52.0, y=53.0, width=80.0, height=22.0)

