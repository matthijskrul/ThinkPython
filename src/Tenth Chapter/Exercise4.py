# Now that you’ve got a traffic light program with different turtles for each light,
# perhaps the visibility / invisibility trick wasn’t such a great idea.
# If we watch traffic lights, they turn on and off — but when they’re off they are still there,
# perhaps just a darker color. Modify the program now so that the lights don’t disappear:
# they are either on, or off. But when they’re off, they’re still visible.

import turtle           # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
raimond = turtle.Turtle()
florian = turtle.Turtle()


def tess_draw_housing():
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


def tess_traffic_light():
    tess.penup()
    # Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    # Turn tess into a big green circle
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("green")


def other_draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    alex.penup()
    alex.left(180)
    alex.forward(150)
    alex.right(180)
    alex.pendown()
    alex.pensize(3)
    alex.color("black", "darkgrey")
    alex.begin_fill()
    alex.forward(80)
    alex.left(90)
    alex.forward(200)
    alex.circle(40, 180)
    alex.forward(200)
    alex.left(90)
    alex.end_fill()


def other_traffic_light():
    alex.penup()
    # Position tess onto the place where the green light should be
    alex.forward(40)
    alex.left(90)
    alex.forward(50)
    # Turn tess into a big green circle
    alex.shape("circle")
    alex.shapesize(3)
    alex.fillcolor("green")
    x = alex.pos()
    # place raimond in orange circle position
    raimond.penup()
    raimond.goto(x)
    raimond.left(90)
    raimond.forward(70)
    raimond.shape("circle")
    raimond.shapesize(3)
    raimond.fillcolor("orange")
    y = raimond.pos()
    # and florian in red circle position
    florian.penup()
    florian.goto(y)
    florian.left(90)
    florian.forward(70)
    florian.shape("circle")
    florian.shapesize(3)
    florian.fillcolor("red")


tess_draw_housing()
tess_traffic_light()
other_draw_housing()
other_traffic_light()


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        alex.fillcolor("darkgrey")
        florian.fillcolor("darkgrey")
        raimond.fillcolor("orange")
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        alex.fillcolor("darkgrey")
        raimond.fillcolor("darkgrey")
        florian.fillcolor("red")
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        raimond.fillcolor("darkgrey")
        florian.fillcolor("darkgrey")
        alex.fillcolor("green")
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.


wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()
