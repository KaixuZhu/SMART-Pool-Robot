import time
from pathlib import Path
from datetime import datetime
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)
from tkinter import Label
from controller import *
from gui.main_window.dashboard.gui import Dashboard
from gui.main_window.reservations.main import Reservations
from gui.main_window.about.main import About
from gui.main_window.rooms.main import Rooms
from gui.main_window.guests.main import Guests
from .. import login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def mainWindow():
    MainWindow()

def open_about(self):
    About(self)
    self.handle_btn_press(self.about_btn, "abt")


class MainWindow(Toplevel):
    global user

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("泳池助手")

        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.dashboard_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.dashboard_btn, "dash"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.dashboard_btn.place(x=7.0, y=133.0, width=208.0, height=47.0)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.rooms_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.rooms_btn, "roo"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.rooms_btn.place(x=7.0, y=183.0, width=208.0, height=47.0)

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.guests_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.guests_btn.place(x=7.0, y=283.0, width=208.0, height=47.0)

        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.about_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_about(self),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.about_btn.place(x=7.0, y=333.0, width=208.0, height=47.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat",
        )
        self.logout_btn.place(x=10.0, y=441.0, width=215.0, height=47.0)

        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.reservations_btn = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.reservations_btn, "res"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.reservations_btn.place(x=7.0, y=233.0, width=208.0, height=47.0)

        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="Hello",
            fill="#5E95FF",
            font=("Gen Jyuu Gothic P Bold", 26 * -1),
        )

        def get_time():
            time2 = time.strftime('%Y-%m-%d %H:%M')
            clock = Label(self, text=time2, font=("Gen Jyuu Gothic P Bold", 12), bg="#FFFFFF", fg="#808080")
            clock.place(x=830, y=20)
            clock.after(1000, get_time)

        get_time()

        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="泳池助手",
            fill="#FFFFFF",
            font=("Gen Jyuu Gothic P Bold", 36 * -1),
        )

        self.canvas.create_text(
            844.0,
            43.0,
            anchor="nw",
            text="Administrator",
            fill="#808080",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            341.0,
            213.0,
            anchor="nw",
            text="(The screens below",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        self.canvas.create_text(
            420.0,
            272.0,
            anchor="nw",
            text="will come here)",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        # Loop through windows and place them
        self.windows = {
            "dash": Dashboard(self),
            "roo": Rooms(self),
            "gue": Guests(self),
            "res": Reservations(self),
            "abt": About(self),
        }

        self.handle_btn_press(self.dashboard_btn, "dash")
        self.sidebar_indicator.place(x=0, y=133)

        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def logout(self):
        confirm = messagebox.askyesno(
            "确认退出", "你想登出账户吗?"
        )
        if confirm == True:
            user = None
            self.destroy()
            login.gui.loginWindow()

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set current Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)
        if self.windows.get(name)._name.split("!")[-1].capitalize()=='Dashboard':
            current_name = '首页'
        elif self.windows.get(name)._name.split("!")[-1].capitalize()=='Rooms':
            current_name = '模式切换'
        elif self.windows.get(name)._name.split("!")[-1].capitalize()=='Guests':
            current_name = '添加订单'
        elif self.windows.get(name)._name.split("!")[-1].capitalize()=='Reservations':
            current_name = '遥控机器人'
        elif self.windows.get(name)._name.split("!")[-1].capitalize() == 'About':
            current_name = '目标检测'
        # Handle label change
        self.canvas.itemconfigure(self.heading, text=current_name)

    def handle_dashboard_refresh(self):
        # Recreate the dash window
        self.windows["dash"] = Dashboard(self)
