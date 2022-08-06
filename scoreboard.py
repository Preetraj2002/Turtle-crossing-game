from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level :{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align="center", font=FONT)
