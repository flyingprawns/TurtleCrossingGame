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
game_score = Scoreboard()

# Listen for user commands
screen.listen()
screen.onkey(key="Up", fun=player.move_forwards)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    street.create_car()
    street.shift_cars()
    # Detect player victory
    if player.reached_finish_line():
        time.sleep(1)
        street.next_level()
        player.reset_player()
        game_score.next_level()
        screen.update()
        continue
    # Detect collision
    for car in street.cars:
        if car.distance(player) < 17:
            game_is_on = False
            game_score.game_over()
    screen.update()

# Exit on click
screen.exitonclick()
