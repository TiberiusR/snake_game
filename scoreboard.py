from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 21, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def score_print(self):
        self.score += 1
        self.update_scoreboard()
