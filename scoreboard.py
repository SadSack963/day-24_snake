from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def read_high_score():
    # Using absolute path
    # with open("E:/Python/Projects/day-24_snake/high_score.txt", "rt") as file:
    with open("high_score.txt", "rt") as file:
#    with open("E:\\Python\\Projects\\day-24_snake\\high_score.txt", "rt") as file:
        high_score = int(file.read())
    return high_score


def write_high_score(high_score):
    # Using relative path
    with open("./high_score.txt", "wt") as file:
        file.write(str(high_score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

