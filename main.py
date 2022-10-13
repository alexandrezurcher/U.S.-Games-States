import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#with this method we can get the cordinate on the turtle screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()

correct_answers =[]
while len(correct_answers) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/{len(all_states)} States Correct", prompt="Choose a U.S. State Name").title()
    if answer_state in all_states and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        x_cor = int(data[data['state'] == answer_state]['x'])
        y_cor = int(data[data['state'] == answer_state]['y'])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # alternative way to access x and y cordinates
        # state_data = data[data.state == answer_state]
        # t.goto(int(state_data.x),int(state_data.y))
        t.goto(x_cor, y_cor)
        t.write(arg=answer_state, align='center', font=("Courier", 8, "normal"))


screen.exitonclick()
