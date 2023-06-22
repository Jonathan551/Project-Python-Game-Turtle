import turtle
import math

class Player(turtle.Turtle):
    def __init__(self, player, walls, selected_character, selected_character2, selected_character3, selected_character4):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.player = player
        self.walls = walls
        self.selected_character = selected_character
        self.selected_character2 = selected_character2
        self.selected_character3 = selected_character3
        self.selected_character4 = selected_character4
        self.shape(selected_character) 
    
        self.is_paused = False

    def go_up(self):
        if not self.is_paused:
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 23

            self.shape(self.selected_character4)
            
            if (move_to_x, move_to_y) not in self.walls:
                self.goto(move_to_x, move_to_y)
    
    def go_down(self):
        if not self.is_paused:
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 23

            self.shape(self.selected_character)
            
            if(move_to_x, move_to_y) not in self.walls:
                self.goto(move_to_x,move_to_y)
        
    def go_left(self):
        if not self.is_paused:
            move_to_x = self.xcor() - 23
            move_to_y = self.ycor() 

            self.shape(self.selected_character2)

            if(move_to_x, move_to_y) not in self.walls:
                self.goto(move_to_x,move_to_y)

    def go_right(self):
        if not self.is_paused:
            move_to_x = self.xcor() + 23
            move_to_y = self.ycor() 

            self.shape(self.selected_character3)
                
            if(move_to_x, move_to_y) not in self.walls:
                self.goto(move_to_x,move_to_y)

    def is_colisi(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        jarak = math.sqrt((a * a) + (b * b))

        if jarak < 5:
            return True
        else:
            return False
