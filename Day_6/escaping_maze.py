# Class 63, Escaping the maze proyect.
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19115662

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()