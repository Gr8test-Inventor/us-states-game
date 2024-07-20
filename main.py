from turtle import Turtle, Screen
import pandas
import pandas as pd

screen = Screen()
turtle = Turtle()
witten_state = Turtle()
states_data = pandas.read_csv("50_states.csv")


screen.title("U.S. States Game | Guess The State Below")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
list_of_states = states_data.state.to_list()



while len(correct_guesses) < 50:
    guessed_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                     prompt="Name a state:").title()

    # print(answer_state)

    ##  Get data in Rows
    ## print(data[data.day == "Monday"])
    ## print(data[data.temp == data.temp.max()])

    # Writing State Functionality
    state_info = states_data[states_data.state == guessed_state]
    # print(state_info)
    if guessed_state == "Exit":
        break
    if not state_info.empty:
        state_name = state_info.state.item()
        state_x_cor = state_info.x.values[0]
        state_y_cor = state_info.y.values[0]
        #                   (176, 52)
        state_location = (state_x_cor, state_y_cor)

        witten_state.hideturtle()
        witten_state.penup()
        witten_state.goto(state_location)
        # witten_state.goto(int(state_info.x), int(state_info.y)) #Error is here: Series is deprecated to an int and will
        # raise type error in the future
        witten_state.write(state_name)
        correct_guesses.append(state_name)
        # print(correct_guesses)
        # print(state_info.x)
        # print(type(state_info.x))

for state in correct_guesses:
    if state in states_data.state.values:
        list_of_states.remove(state)

# print(correct_guesses)
# print(list_of_states)
# Alabama
# Alaska
# Arizona
# Arkansas

# print(states_to_learn)
data = pandas.DataFrame(list_of_states)
data.to_csv("states_to_learn.csv")



    # How to find x and y values of states
    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)


