import turtle
import Paddle
import time
import random


scr=turtle.Screen()
scr.screensize(600,600,"#800080")
scr.title("PingPong Game")
scr.tracer(0)

tpen=turtle.Turtle()
tpen.penup()
tpen.hideturtle()
tpen.goto(0,252)

tpen.write("PING PONG", font=("Arial", 20, "normal"))

# ball
tball=turtle.Turtle()
tball.shape("circle")
tball.color("white")

# Paddle
game_on=True
pos=(0,-100)
pd=Paddle.Paddle(pos)
scr.listen()
scr.onkey(pd.move_left, "Left")
scr.onkey(pd.move_right, "Right")
tball.penup()
tball.setheading(270)

while(game_on):
    time.sleep(0.1)
    scr.update()                                        ###########
    tball.forward(30)
    if (tball.ycor() > 300):
        tball.setheading(random.randint(225,315))
    if ( (tball.xcor() < -350) or (tball.xcor() > 350)):
        tball.setheading(180-tball.heading())
    if (pd.distance(tball.xcor(), tball.ycor()) < 40):
        tball.setheading(random.randint(45,135))
    if( tball.ycor()<-350):
        tpen.clear()
        tpen.write("Game Over", font=("Arial", 20, "normal"))
        game_on=False




scr.exitonclick()