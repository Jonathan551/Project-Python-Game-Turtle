from tkinter import *
import tkinter as tk
from MenuUtama import GameMenu

class Win:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Maze Game")
        self.window.geometry("700x700")
        self.window.configure(bg="black")
        self.window.resizable(width=False, height=False)
        
        self.bg = PhotoImage(file="Gambar/UI/bgscreen.png")
        self.pic = PhotoImage(file="Gambar/UI/win.png")
        self.pic2 = PhotoImage(file="Gambar/UI/backk.png")
        
        self.my_label = tk.Label(self.window, image=self.bg)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.frame = tk.Frame(self.window, bg="black")
        self.frame.pack(expand=True, pady=200)
        
        self.label = tk.Label(self.frame, image=self.pic, borderwidth=0, highlightthickness=0)
        self.label.pack(pady=0)

        self.start_button = tk.Button(self.frame, image=self.pic2, command=self.kembali, borderwidth=0, highlightthickness=0)
        self.start_button.pack(pady=10)
        
        self.window.mainloop()
        
    def kembali(self):
        self.window.destroy()
        GameMenu()
    