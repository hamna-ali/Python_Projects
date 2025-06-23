import time
from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("white")
screen.setup(600,600)
screen.title("Cross Road")
screen.tracer(0)



is_game_on = True
player = Player()
car_x = Car()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down,"Down")

while is_game_on:
	time.sleep(0.1)
	screen.update()
	car_x.create_cars()
	car_x.move_cars()
	#collision with car

	for car in car_x.all_cars:
		if car.distance(player) < 25:
			is_game_on = False
			scoreboard.game_over()
	# Detect successful completion
	if player.is_at_finish_line():
		player.go_to_start()
		car_x.level_up()
		scoreboard.increase_level()



screen.exitonclick()