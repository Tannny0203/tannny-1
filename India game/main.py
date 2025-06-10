import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "inde34.gif"
screen.addshape(image)
turtle.shape(image)

data =pandas.read_csv("states.csv")
all_states = data.states.to_list()
guessed_state = []

while len(guessed_state)<28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct",
                                    prompt="What's another state's name?").title()
    if answer_state =="Exit":
        missing_states= []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to-learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)





screen.exitonclick()








