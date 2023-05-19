from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 4
        self.level = 1
        self.scoreboard = Turtle()
    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
    def increase_level(self):
        self.score += 1
        self.update_score()
    def get_score(self):
        return self.score
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)