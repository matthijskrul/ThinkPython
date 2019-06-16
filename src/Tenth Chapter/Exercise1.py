# Add some new key bindings to the first sample program:
#
# Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
# Pressing keys + or - should increase or decrease the width of tess’ pen.
# Ensure that the pen size stays between 1 and 20 (inclusive).
# Handle some other keys to change some attributes of tess, or attributes of the window,
# or to give her new behaviour that can be controlled from the keyboard.

import turtle           # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def tess_red():
    tess.color("red")


def tess_blue():
    tess.color("blue")


def tess_green():
    tess.color("green")


wn.onkey(tess_red, "r")
wn.onkey(tess_blue, "b")
wn.onkey(tess_green, "g")


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
pensize_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


def tesspenup():
    global pensize_num
    if 20 >= pensize_num > 0:
        tess.pensize(pensize_num)
        pensize_num += pensize_num
    else:
        tess.pensize(20)
        pensize_num = 20


def tesspendown():
    global pensize_num
    if 20 >= pensize_num > 0:
        tess.pensize(pensize_num)
        pensize_num -= pensize_num
    else:
        tess.pensize(1)
        pensize_num = 0


wn.onkey(advance_state_machine, "space")
wn.onkey(tesspenup, "+")
wn.onkey(tesspendown, "-")


wn.listen()                      # Listen for events
wn.mainloop()
