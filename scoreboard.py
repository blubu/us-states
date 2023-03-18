from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.point = 0
        self.update_score()

    def update_score(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Guessed {self.point} states out of 50", align="center")

    def add_point(self):
        self.point += 1
        self.update_score()

    def check_status(self):
        if self.point == 55:
            return False
        else:
            return True


class StateSet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def add_state(self, state, co_ords):
        self.goto(co_ords)
        self.write(state, align="center")
