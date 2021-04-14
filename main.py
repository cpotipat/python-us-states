import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To get Coordinate on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv("States_to_learn")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(state_data.x), int(state_data.y))
        state.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))


