import turtle

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Gambar/Walls/wallutama.gif")
        self.color("White")
        self.penup()
        self.speed(1000)
