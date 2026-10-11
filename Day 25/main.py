import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

guessed_state_list = []

game_over = True
while game_over:

    if len(guessed_state_list) == 50:
        game_over = False

    prompt = screen.textinput(title = f"{len(guessed_state_list)}/50 States Correct",prompt = "What's another state name?")
    prompt = prompt.title()

    if prompt in guessed_state_list:
        continue
    if prompt == "Exit":
        missing = [state for state in state_list if state not in guessed_state_list]
        # missing = []
        # for state in state_list:
        #     if state not in guessed_state_list:
        #         missing.append(state)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("States_to_learn.csv")
        break


    if prompt in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states = data[data.state == prompt]
        t.teleport(x = states.x.item(), y = states.y.item())
        t.write(prompt)
        guessed_state_list.append(prompt)
    if len(guessed_state_list) == 50:
        game_over = False
screen.mainloop()
