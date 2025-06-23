from turtle import  Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter color")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []
for t_index in range(0,6):
    t1 = Turtle("turtle")
    t1.color(colors[t_index])
    t1.penup()
    t1.goto(-230, y_pos[t_index])
    all_turtles.append(t1)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations!!! You Won........The {winning_color} turtle is the Winner")
            else:
                print(f"You Lose........The {winning_color} turtle is the Winner")
        rand_distance = random.randint(0,10)
        t.forward(rand_distance)


screen.exitonclick()