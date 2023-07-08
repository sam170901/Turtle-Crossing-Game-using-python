from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DIST = 20
class Player(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def goUp(self):
        self.forward(MOVE_DIST)

    def reset_Position(self):
        self.goto(STARTING_POSITION)
