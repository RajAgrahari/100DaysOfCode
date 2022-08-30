import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "US_state_outline_map.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

data = pandas.read_csv("us_states_data.csv")
state_list = data["state"].to_list()
print(state_list)
is_game_on = True
guessed_state = set()
while is_game_on:
    ans_state = (screen.textinput(title=f"Guessed {len(guessed_state)}/50 states",
                                  prompt="What's your choice of state?")).title()
    if ans_state == "Exit":
        missed_states = [x for x in state_list if x not in guessed_state]
        # for x in state_list:
        #     if x not in guessed_state:
        #         missed_states.append(x)
        data_csv = pandas.DataFrame(missed_states)
        data_csv.to_csv("to_be_learned.csv")
        break
    if ans_state in state_list:
        if ans_state not in guessed_state:
            guessed_state.add(ans_state)
            state = data[data.state == ans_state]
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.color("black")
            state_turtle.penup()
            state_turtle.goto(int(state.x), int(state.y))
            state_turtle.write(ans_state)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
