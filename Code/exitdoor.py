import turtle
import math

class ExitDoor(turtle.Turtle):
    def __init__(self, sc_x, sc_y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(sc_x, sc_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt(a ** 2 + b ** 2)

        if distance < 5:
            return True
        else:
            return False
