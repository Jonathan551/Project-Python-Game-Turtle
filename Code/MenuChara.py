import tkinter as tk
from tkinter import *

class CharaSelection:
    def __init__(self):
        self.selected_character = ""
        self.selected_character2 = ""
        self.selected_character3 = ""
        self.selected_character4 = ""

    def emily_select(self):
        self.window.destroy()
        self.selected_character = "Gambar/Chara/EmilyF.gif"
        self.selected_character2 = "Gambar/Chara/EmilyL.gif"
        self.selected_character3 = "Gambar/Chara/EmilyR.gif"
        self.selected_character4 = "Gambar/Chara/EmilyB.gif"
   
    
    def william_select(self):
        self.window.destroy()
        self.selected_character = "Gambar/Chara/WilliamF.gif"
        self.selected_character2 = "Gambar/Chara/WilliamL.gif"
        self.selected_character3 = "Gambar/Chara/WilliamR.gif"
        self.selected_character4 = "Gambar/Chara/WilliamB.gif"
       
    
    def gracia_select(self):
        self.window.destroy()
        self.selected_character = "Gambar/Chara/GraciaF.gif"
        self.selected_character2 = "Gambar/Chara/GraciaL.gif"
        self.selected_character3 = "Gambar/Chara/GraciaR.gif"
        self.selected_character4 = "Gambar/Chara/GraciaB.gif"
    
    
    def justin_select(self):
        self.window.destroy()
        self.selected_character = "Gambar/Chara/JustinF.gif"
        self.selected_character2 = "Gambar/Chara/JustinL.gif"
        self.selected_character3 = "Gambar/Chara/JustinR.gif"
        self.selected_character4 = "Gambar/Chara/JustinB.gif"
       
    def draw_menu(self):
        self.window = tk.Tk()
        self.window.title("Simple Maze Game")
        self.window.geometry("700x700")
        self.window.configure(bg="black")
        self.window.resizable(width=False, height=False)
        
        bg = PhotoImage(file = "Gambar/UI/spacebg.png")
        lab = PhotoImage(file = "Gambar/UI/select_chara.png")
        pic = PhotoImage(file = "Gambar/UI/emilyprof.png")
        pic2 = PhotoImage(file = "Gambar/UI/williamprof.png")
        pic3 = PhotoImage(file = "Gambar/UI/justinprof.png")
        pic4 = PhotoImage(file = "Gambar/UI/graciaprof.png")

        my_label = Label(self.window, image=bg)
        my_label.place(x=0,y=0, relwidth=1, relheight=1)

        frame2 = tk.Frame(self.window, bg="black")
        frame2.pack(pady=50)
        
        frame = tk.Frame(self.window, bg="black")
        frame.pack(pady=0)
        
        label = tk.Label(frame2, image=lab, borderwidth=0, highlightthickness=0)
        label.pack(pady=0)  

        emily_button = tk.Button(frame, image = pic, command=self.emily_select, borderwidth=0, highlightthickness=0)
        emily_button.grid(row=0, column=0, pady=10, padx=20)

        william_button = tk.Button(frame, image = pic2, command=self.william_select, borderwidth=0, highlightthickness=0)
        william_button.grid(row=0, column=1, pady=10, padx=20)

        justin_button = tk.Button(frame, image = pic3, command=self.justin_select, borderwidth=0, highlightthickness=0)
        justin_button.grid(row=1, column=0, pady=20, padx=20)

        gracia_button = tk.Button(frame, image = pic4, command=self.gracia_select, borderwidth=0, highlightthickness=0)
        gracia_button.grid(row=1, column=1, pady=20, padx=20)

        self.window.mainloop()
        

