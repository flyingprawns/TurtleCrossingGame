from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.reset_player()

    def move_forwards(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_player(self):
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)