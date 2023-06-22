import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
        
class GameStage:    
    def __init__(self, chara):
        self.chara = chara
        self.chara.draw_menu()
        self.stage_menu = tk.Tk()
        self.stage_menu.title("Simple Maze Game")
        self.stage_menu.configure(bg="black")
        self.stage_menu.geometry("700x700")
        self.stage_menu.resizable(width=False, height=False)

        bg = Image.open("Gambar/UI/bglevel.png")
        bg_image = ImageTk.PhotoImage(bg)
        lab = Image.open("Gambar/UI/levelselect.gif")
        lab_image = ImageTk.PhotoImage(lab)
        pic = Image.open("Gambar/UI/level1.gif")
        pic_image = ImageTk.PhotoImage(pic)
        pic2 = Image.open("Gambar/UI/level2.gif")
        pic2_image = ImageTk.PhotoImage(pic2)
        pic3 = Image.open("Gambar/UI/level3.gif")
        pic3_image = ImageTk.PhotoImage(pic3)
        pic4 = Image.open("Gambar/UI/level4.gif")
        pic4_image = ImageTk.PhotoImage(pic4)
        pic5 = Image.open("Gambar/UI/level5.gif")
        pic5_image = ImageTk.PhotoImage(pic5)
        pic6 = Image.open("Gambar/UI/exitstage.gif")
        pic6_image = ImageTk.PhotoImage(pic6)

        self.my_label = tk.Label(self.stage_menu, image=bg_image)
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = tk.Frame(self.stage_menu, bg="black")
        self.frame.pack(pady=20)

        level_sudah = open("level_sudah.txt","r")
        file = level_sudah.read()
        level_sudah.close()
        
        self.label = tk.Label(self.stage_menu, image=lab_image, borderwidth=0, highlightthickness=0)
        self.label.pack(pady=0)

        if( "1" not in file):
            self.stage1_button = tk.Button(self.stage_menu, image=pic_image, command=self.stage1_action, borderwidth=0, highlightthickness=0)
            self.stage1_button.pack(pady=10)
        

        if("2" not in file):
            self.stage2_button = tk.Button(self.stage_menu, image=pic2_image, command=self.stage2_action, borderwidth=0, highlightthickness=0)
            self.stage2_button.pack(pady=10)

        if("3" not in file):
            stage3_button = tk.Button(self.stage_menu, image=pic3_image, command=self.stage3_action, borderwidth=0, highlightthickness=0)
            stage3_button.pack(pady=10)

        if("4" not in file):
            stage4_button = tk.Button(self.stage_menu, image=pic4_image, command=self.stage4_action, borderwidth=0, highlightthickness=0)
            stage4_button.pack(pady=10)

        if("5" not in file):
            stage5_button = tk.Button(self.stage_menu, image=pic5_image, command=self.stage5_action, borderwidth=0, highlightthickness=0)
            stage5_button.pack(pady=10)
        
        exit_button = tk.Button(self.stage_menu, image=pic6_image, command=self.exit_action, borderwidth=0, highlightthickness=0)
        exit_button.pack(pady=10)
            
        self.stage_menu.mainloop()

            
    def stage1_action(self):        
        level_sudah = open("level_sudah.txt","a")
        level_sudah.write("1")
        level_sudah.close()
        
        self.stage_menu.destroy()
        from Stage1 import Game
        game = Game()
        game.setup(self.chara.selected_character, self.chara.selected_character2, self.chara.selected_character3,
                self.chara.selected_character4)
        
        
    def stage2_action(self):
        level_sudah = open("level_sudah.txt","a")
        level_sudah.write("2")
        level_sudah.close()
        
        self.stage_menu.destroy()
        from Stage2 import Game2
        game = Game2()
        game.setup(self.chara.selected_character, self.chara.selected_character2, self.chara.selected_character3,
                self.chara.selected_character4)


    def stage3_action(self):
        level_sudah = open("level_sudah.txt","a")
        level_sudah.write("3")
        level_sudah.close()
        
        self.stage_menu.destroy()
        from Stage3 import Game3
        game = Game3()
        game.setup(self.chara.selected_character, self.chara.selected_character2, self.chara.selected_character3,
                self.chara.selected_character4)


    def stage4_action(self):
        level_sudah = open("level_sudah.txt","a")
        level_sudah.write("4")
        level_sudah.close()
        
        self.stage_menu.destroy()
        from Stage4 import Game4
        game = Game4()
        game.setup(self.chara.selected_character, self.chara.selected_character2, self.chara.selected_character3,
                self.chara.selected_character4)


    def stage5_action(self):
        level_sudah = open("level_sudah.txt","a")
        level_sudah.write("5")
        level_sudah.close()
        
        self.stage_menu.destroy()
        from Stage5 import Game5
        game = Game5()
        game.setup(self.chara.selected_character, self.chara.selected_character2, self.chara.selected_character3, self.chara.selected_character4)
        
    def exit_action(self):
        self.stage_menu.destroy()