from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, high_score=0):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.refresh()

    def refresh(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-100, 235)
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.hideturtle()
    #     self.color("red")
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("Game Over.", align="center", font=('Courier', 20, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.high_score}", align="right", font=('Courier', 20, 'bold'))

