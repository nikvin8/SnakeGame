from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 21, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def new_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!', align=ALIGNMENT, font=FONT)
