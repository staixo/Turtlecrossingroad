from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle,STARTING_POSITION,MOVE_DISTANCE,FINISH_LINE_Y):
    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("Yellow")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)
        self.player.speed(200)
    
    def up(self):
        self.player.forward(MOVE_DISTANCE)
    
    def down(self):
        self.player.backward(MOVE_DISTANCE)
    def is_at_finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
