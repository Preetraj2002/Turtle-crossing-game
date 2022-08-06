import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("GO TURTLE GO")
screen.tracer(0)

player = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Player crossing the finishing_line
    if player.ycor() > 280:
        scoreboard.level_up()
        player.reset_position()
        car_manager.level_up()

    # Detecting collision with the cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
