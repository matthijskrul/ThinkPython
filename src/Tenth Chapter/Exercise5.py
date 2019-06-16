# Your traffic light controller program has been patented, and you’re about to become seriously rich.
# But your new client needs a change.
# They want four states in their state machine:
# Green, then Green and Orange together, then Orange only, and then Red.
# Additionally, they want different times spent in each state.
# The machine should spend 3 seconds in the Green state, followed by one second in the Green+Orange state,
# then one second in the Orange state, and then 2 seconds in the Red state.
# Change the logic in the state machine.

import turtle           # Tess becomes a traffic light.
import time

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
brian = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.showturtle()
        x = tess.pos()
        brian.penup()
        brian.goto(x)
        brian.setheading(90)
        brian.forward(70)
        brian.shape("circle")
        brian.shapesize(3)
        brian.fillcolor("orange")
        brian.showturtle()
        time.sleep(1)
        state_num = 1
    elif state_num == 1:    # Transition from state 1 to state 2
        tess.hideturtle()
        time.sleep(1)
        state_num = 2
    elif state_num == 2:    # Transition from state 2 to state 3
        brian.hideturtle()
        tess.forward(140)
        tess.fillcolor("red")
        tess.showturtle()
        time.sleep(2)
        state_num = 3
    else:                   # Transition from state 3 to state 0
        brian.hideturtle()
        tess.showturtle()
        tess.back(140)
        tess.fillcolor("green")
        time.sleep(3)
        state_num = 0


while True:
    advance_state_machine()
wn.mainloop()
