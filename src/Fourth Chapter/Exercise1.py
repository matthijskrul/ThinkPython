# Write a void (non-fruitful) function to draw a square.
# Use it in a program to draw the image shown below [five pink squares on light green separated, in a row; see textbook]
# Assume each side is 20 units.
# (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

import turtle


def make_window(color, title):
    """
        Sets up the window with the given background color and title.
        Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(color, size):
    """
      Sets up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t


def make_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


def make_pattern(t, distance):
    for i in range(5):
        make_square(t, 20)
        t.penup()
        t.forward(distance)
        t.pendown()


wn = make_window("lightgreen", "squares")
turt = make_turtle("pink", 4)
make_pattern(turt, 40)
wn.mainloop()

