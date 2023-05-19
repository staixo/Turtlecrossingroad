from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed(STARTING_MOVE_DISTANCE)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars.append(Car())

    def move_cars(self):
        for car in self.all_cars:
            car.speed(self.car_speed)
            car.backward(MOVE_INCREMENT+random.randint(-5,5))

    def level_up(self):
        self.car_speed *= 2
    
    def create_car(self):
        self.all_cars.append(Car())
