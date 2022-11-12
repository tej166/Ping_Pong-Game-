from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("black")
        self.penup()
        self.goto(position)
    def move_left(self):
        self.goto(self.xcor()-30, self.ycor())
    def move_right(self):
        self.goto(self.xcor()+30, self.ycor())