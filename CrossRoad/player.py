STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.goto(STARTING_POSITION)
		self.setheading(90)

	def go_up(self):
		self.forward(MOVE_DISTANCE)

	def go_down(self):
		self.backward(MOVE_DISTANCE)

	def go_to_start(self):
		self.goto(STARTING_POSITION)
	def is_at_finish_line(self):
		if self.ycor() > 280:
			return True
		else:
			return False
