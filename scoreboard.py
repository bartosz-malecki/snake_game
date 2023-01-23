
from turtle import Turtle

ALIGMENT = "center"
FONT = ('Arial', 20, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.sety(260)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT,font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


