from turtle import Turtle
import random

COLORS = ["red","blue","black","yellow","green","orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car_Manager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250,250)
            new_car.goto(300,y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
    
    def increase(self):
        self.car_speed += MOVE_INCREMENT





