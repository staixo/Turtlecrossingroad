import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(player.up, "z")
screen.onkey(player.down, "s")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_score()
    
    time.sleep(0.1)
    if(random.randint(1,5) == 3):
        car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()