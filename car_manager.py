from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.cars.append(Car())

    def shift_cars(self):
        for car in self.cars:
            car.move(self.car_speed)
        self.create_car()


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        # Car settings
        self.speed("fastest")
        self.penup()
        self.setheading(180)
        self.turtlesize(stretch_len=2)
        # Randomize color and starting location
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-300, 300))

    def move(self, distance):
        new_x = self.xcor() - distance
        new_y = self.ycor()
        self.goto(new_x, new_y)
