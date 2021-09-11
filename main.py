import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, car manager, and scoreboard
player = Player()
street = CarManager()

# Listen for user commands
screen.listen()
screen.onkey(key="Up", fun=player.move_forwards)

game_is_on = True
while game_is_on:
    street.shift_cars()
    for i in range(10):
        time.sleep(0.1)
        screen.update()

