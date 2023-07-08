from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-290,265)
        self.hideturtle()
        self.write(f"Level: {self.level}",align="left",font=("Arial",25,"normal"))

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",align="left",font=("Arial",25,"normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over.",align="center",font=("Arial",20,"normal"))

