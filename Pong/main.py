from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score_board
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
print(f"Right paddle X: {right_paddle.xcor()} — should be 350")
print(f"Left paddle X: {left_paddle.xcor()} — should be -350")

ball = Ball()
scoreboard = Score_board()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


is_game_on = True
while is_game_on:
	ball.move()
	screen.update()
	time.sleep(ball.move_speed)

	#collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	#collision with paddle
	# RIGHT paddle collision
	# Right paddle collision
	if ball.xcor() > 320 and ball.xcor() < 350:
		if right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50:
			ball.bounce_x()

	# Left paddle collision
	if ball.xcor() < -320 and ball.xcor() > -350:
		if left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50:
			ball.bounce_x()

	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.left_point()

	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.right_point()





screen.exitonclick()
