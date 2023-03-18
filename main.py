from turtle import Turtle, Screen
from data import data, state
from scoreboard import ScoreBoard, StateSet

screen = Screen()
screen.title("Guess the States")
img = "blank_states_img.gif"
screen.addshape(img)

tut = Turtle(img)
state_set = StateSet()
score = ScoreBoard()
s = []

game_is_on = True
while game_is_on:
    answer = screen.textinput(title="", prompt="Enter a state name").title()
    if answer in state and answer not in s:
        s.append(answer)
        state_set.add_state(answer, data[answer])
        score.add_point()

    game_is_on = score.check_status()


screen.exitonclick()
