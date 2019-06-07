# 1) Modify the turtle bar chart example so that the pen is up for the small gaps between each bar.
# 2) Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red,
# values between [100 and 200) are filled with yellow,
# and bars representing values less than 100 are filled with green.
# 3) Change the program so that when it prints the text value for the negative bars,
# it puts the text below the bottom of the bar.

import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    if height >= 0:
        t.write("  " + str(height))
    else:
        t.penup()
        t.forward(-20)
        t.write("  " + str(height))
        t.forward(20)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()
    t.forward(10)
    t.pendown()


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)

xs = [48, 117, -200, 240, 160, 260, -220]

for a in xs:
    if a >= 200:
        tess.color("blue", "red")
    elif 200 > a >= 100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")
    draw_bar(tess, a)

wn.mainloop()
