from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)
y_axis = -100
all_turtles = []


for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
