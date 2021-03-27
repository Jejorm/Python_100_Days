from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.move(position)

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()

    def move(self, position):
        # Move paddle to corresponding coordinates
        self.goto(position)
        # Left paddle
        if position[0] < 0:
            screen.onkey(self.up, "w")
            screen.onkey(self.down, "s")
        # Right paddle
        else:
            screen.onkey(self.up, "Up")
            screen.onkey(self.down, "Down")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



