from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        pass


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.penup()
        self.setheading(180)
        self.turtlesize(stretch_len=2)
        # TODO: starting position
