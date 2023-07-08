from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import Car_Manager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carManager = Car_Manager()

screen.listen()
screen.onkey(player.goUp,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_cars()

    for car in carManager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.gameOver()

    if(player.ycor()>280):
        player.reset_Position()
        scoreboard.update()
        carManager.increase()


screen.exitonclick()