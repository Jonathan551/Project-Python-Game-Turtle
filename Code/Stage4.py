import turtle
import time
from pen import Pen
from player import Player
from harta import Harta
from musuh import Musuh
from exitdoor import ExitDoor
from MenuUtama import GameMenu

turtle.Turtle._screen = None
turtle.TurtleScreen._RUNNING = True 
        
class Game4:
    def __init__(self):
        self.window = None
        self.paused = False
  
    def setup(self, selected_character, selected_character2, selected_character3, selected_character4):
        self.window = turtle.Screen()
        self.window.bgcolor("black")
        self.window.title("Simple Maze Game")
        self.window.setup(700, 700)
        self.window.tracer(0)
        self.HP = 3
        self.Treasure = 0
        
        self.selected_character = selected_character
        self.selected_character2 = selected_character2
        self.selected_character3 = selected_character3
        self.selected_character4 = selected_character4
         
        turtle.register_shape("Gambar/Walls/wallutama.gif")
        turtle.register_shape("Gambar/Walls/wall1.gif")
        turtle.register_shape("Gambar/Walls/wall2.gif")
        turtle.register_shape("Gambar/Walls/wall3.gif")
        turtle.register_shape("Gambar/Walls/wall4.gif")
        turtle.register_shape("Gambar/Walls/wall5.gif")
        turtle.register_shape("Gambar/Walls/wall6.gif")
        turtle.register_shape("Gambar/Walls/wall7.gif")
        turtle.register_shape("Gambar/HomeButton2.gif")
        turtle.register_shape("Gambar/chest.gif")
        turtle.register_shape("Gambar/Enemy/EnemyF.gif")
        turtle.register_shape("Gambar/Enemy/EnemyB.gif")
        turtle.register_shape("Gambar/Enemy/EnemyL.gif")
        turtle.register_shape("Gambar/Enemy/EnemyR.gif")
        turtle.register_shape(self.selected_character)
        turtle.register_shape(self.selected_character2)
        turtle.register_shape(self.selected_character3)
        turtle.register_shape(self.selected_character4)

        self.Ket = turtle.Turtle()
        self.Ket.speed(0)
        self.Ket.shape("square")
        self.Ket.color("white")
        self.Ket.penup()
        self.Ket.hideturtle()
        self.Ket.goto(-300, 310)
        self.Ket.write("HP: 3     Treasure: 0/5", align="left", font=("Times New Roman", 15, "normal"))
        
        self.Level = turtle.Turtle()
        self.Level.speed(0)
        self.Level.shape("square")
        self.Level.color("white")
        self.Level.penup()
        self.Level.hideturtle()
        self.Level.goto(195, 310)
        self.Level.write("LEVEL 4", align="left", font=("Times New Roman", 15, "normal"))
        
        self.Timer = turtle.Turtle()
        self.Timer.speed(0)
        self.Timer.shape("square")
        self.Timer.color("white")
        self.Timer.penup()
        self.Timer.hideturtle()
        self.Timer.goto(-90, 310)
        self.Timer.write("Timer : 100", align="left", font=("Times New Roman", 15, "normal"))
        
        self.Pause = turtle.Turtle()
        self.Pause.speed(0)
        self.Pause.shape("square")
        self.Pause.color("white")
        self.Pause.penup()
        self.Pause.hideturtle()
        self.Pause.goto(-300, -305)
        self.Pause.write("press 'p' for pause game", align="left", font=("Times New Roman", 15, "normal"))

        self.Write = turtle.Turtle()
        self.Write.speed(0)
        self.Write.shape("square")
        self.Write.color("red")
        self.Write.penup()
        self.Write.hideturtle()
        self.Write.goto(60, -305)
        self.Write.write("colect all treasure before exit!", align="left", font=("Times New Roman", 15, "normal"))
        
        self.Button = turtle.Turtle()
        self.Button.shape("Gambar/HomeButton2.gif")
        self.Button.penup()
        self.Button.hideturtle()
        self.Button.goto(290, 320)
        self.Button.showturtle()
        self.Button.onclick(self.button_click)             
            
        self.levels = [""]
        self.level_4 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXX3  XXX54XXX  XXX34XXX",
            "XD                       X",
            "XXXXX2XXXXX   X6XTXXX    X",
            "X           X            X",
            "X   XXXX42XXX74XXX XX    X",
            "X             XXXX XX    X",
            "X  E  X X     XXT  XX    X",
            "X    XX4XX    XXXXXXX    X",
            "XXX2XX  XXXXXXXX  4XXXXX X",
            "X            E           X",
            "X   XXXX  XXXXXX4  XXX   X",
            "X    XXXXT XPXXXX XXXX   X",
            "X   XXXXXX X XXXX2XXXX   X",
            "X  XXXXXX5   XXXXXXXX    X",
            "X   XXXX6XX   XXXXX3XX   X",
            "X   4                X   X",
            "X   XX              XX   X",
            "X   XXX X3X  XXX 6XXXX   X",
            "X E         X            X",
            "X          XX   6        X",
            "5    XXTXX      XXTXX    7",
            "XXX  XXXXXX2EX  XXXXXX 3XX",
            "X              X         X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXX"
        ]

        self.Hadiah = []
        self.Enemy = []
        self.Keluar = []
        self.walls = []

        self.pen = Pen()
        self.selected_character = ()
        self.player = Player(self.pen, self.walls, selected_character, selected_character2, selected_character3, selected_character4)

        self.setup_maze(self.level_4)

        turtle.listen()
        turtle.onkeypress(self.player.go_left, "a")
        turtle.onkeypress(self.player.go_right, "d")
        turtle.onkeypress(self.player.go_up, "w")
        turtle.onkeypress(self.player.go_down, "s")
        turtle.onkeypress(self.player.go_left, "Left")
        turtle.onkeypress(self.player.go_right, "Right")
        turtle.onkeypress(self.player.go_up, "Up")
        turtle.onkeypress(self.player.go_down, "Down")
        turtle.onkeypress(self.toggle_pause, "p")
        
        self.time_limits = 100
        self.start_time = time.time()
            
        while True:
            if not self.paused:
                elapsed = time.time() - self.start_time
                self.Timer.clear()
                self.Timer.write("Timer : {}".format(self.time_limits-int(elapsed)), align="left",
                                    font=("Times New Roman", 15, "normal"))
                if elapsed > self.time_limits:
                    self.window.bye()
                    from timesup import TimeUp
                    TimeUp()

                for harta in self.Hadiah:
                    if self.player.is_colisi(harta):
                        harta.destroy()
                        self.Hadiah.remove(harta)
                        self.Treasure += 1
                        self.Ket.clear()
                        self.Ket.write("HP: {}     Treasure: {}/5".format(self.HP, self.Treasure), align="left",
                                    font=("Times New Roman", 15, "normal"))

                for musuh in self.Enemy:
                    if self.player.is_colisi(musuh):
                        self.HP -= 1
                        self.Ket.clear()
                        self.Ket.write("HP: {}     Treasure: {}/5".format(self.HP, self.Treasure), align="left",
                                    font=("Times New Roman", 15, "normal"))

                        if self.HP <= 0:
                            self.window.bye()
                            from gameover import GameOver
                            GameOver()

                for musuh in self.Enemy:
                    turtle.ontimer(musuh.move(self.walls, self.player), t=20)

                for keluar in self.Keluar:
                    if self.player.is_colisi(keluar) and self.Treasure == 5:
                        self.window.bye()
                        from win import Win
                        Win()  
                self.window.update()
            else:
                self.start_time = time.time() - elapsed
                self.window.update()

    def setup_maze(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                char = level[y][x]
                sc_x = -288 + (x * 23)
                sc_y = 288 - (y * 23)

                if char == "X":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wallutama.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "1":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall1.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "2":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall2.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "3":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall3.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "4":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall4.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "5":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall5.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "6":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall6.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))
                
                if char == "7":
                    self.pen.goto(sc_x, sc_y)
                    self.pen.shape("Gambar/Walls/wall7.gif")
                    self.pen.stamp()
                    self.walls.append((sc_x, sc_y))

                if char == "P":
                    self.player.goto(sc_x, sc_y)

                if char == "T":
                    self.Hadiah.append(Harta(sc_x, sc_y))

                if char == "E":
                    self.Enemy.append(Musuh(sc_x, sc_y))

                if char == "D":
                    self.Keluar.append(ExitDoor(sc_x, sc_y))
                
    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.player.is_paused = True
        else:
            self.player.is_paused = False
            
    def button_click(self, x, y):
        self.window.bye()
        GameMenu()
    