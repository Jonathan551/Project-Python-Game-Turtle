import tkinter as tk
from tkinter import messagebox
from tkinter import *
from MenuStage import GameStage
from MenuChara import CharaSelection

class GameMenu:    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Maze Game")
        self.window.configure(bg="black")
        self.window.geometry("700x700")
        self.window.resizable(width=False, height=False)
        
        self.bg = PhotoImage(file="Gambar/UI/background.png")
        self.lab = PhotoImage(file="Gambar/UI/welcome.png")
        self.pic = PhotoImage(file="Gambar/UI/play.png")
        self.pic2 = PhotoImage(file="Gambar/UI/quit.png")

        self.my_label = tk.Label(self.window, image=self.bg)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = tk.Frame(self.window, bg="black")
        self.frame.pack(expand=True, pady=0)

        self.label = tk.Label(self.frame, image=self.lab, borderwidth=0, highlightthickness=0)
        self.label.pack(pady=0)

        self.start_button = tk.Button(self.frame, image=self.pic, command=self.show_stage_menu, borderwidth=0, highlightthickness=0)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.frame, image=self.pic2, command=self.quit_menu, borderwidth=0,highlightthickness=0)
        self.quit_button.pack(pady=10)

        self.window.mainloop()

    def show_stage_menu(self):
        self.window.destroy()
        Chara = CharaSelection()
        GameStage(Chara)

    def quit_menu(self):
        self.window.destroy()
