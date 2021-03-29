from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for every_car in car.list_cars:
        if every_car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.pass_top():
        turtle.go_to_start()
        car.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()