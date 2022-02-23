from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh()

    def refresh(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-160, 265)
        self.write("Score: " + str(self.score), align="right", font=('Courier', 20, 'bold'))

    def add_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=('Courier', 20, 'bold'))
