import turtle
import random

class Musuh(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Gambar/Enemy/EnemyF.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right", "up", "down"])

    def move(self, walls, player):
        if self.direction == "left":
            dx = -23
            dy = 0
            self.shape("Gambar/Enemy/EnemyL.gif")
        elif self.direction == "right":
            dx = 23
            dy = 0
            self.shape("Gambar/Enemy/EnemyR.gif")
        elif self.direction == "up":
            dx = 0
            dy = 23
            self.shape("Gambar/Enemy/EnemyB.gif")
        elif self.direction == "down":
            dx = 0
            dy = -23
            self.shape("Gambar/Enemy/EnemyF.gif")
        else:
            dx = 0
            dy = 0

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["left", "right", "up", "down"])