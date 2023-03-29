import turtle
from turtle import Turtle,Screen
ALİGNMENT ="center"
FONT= ("courier",24,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.highscore}", align=ALİGNMENT, font=FONT)

    def increasscore(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore =self.score
            with open("highscore.txt",mode="w") as file:
                file.write(f"{self.highscore}")

        self.score =0
        self.update_score()






