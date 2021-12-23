from turtle import *
from paddle import *
from ball import *
from scoreboard import *
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600 , width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on= True

while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
