# Write a program to draw embedded squares.
# Assume the innermost square is 20 units per side,
# and each successive square is 20 units bigger, per side, than the one inside it

import turtle
from math import sqrt


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

def repeat_square(t, size):
    for i in range(1,6):
        make_square(t, size * i)
        t.right(135)
        t.penup()
        t.forward((size * sqrt(2)/2))
        t.left(135)
        t.pendown()


wn = make_window("lightgreen", "squares")
turt = make_turtle("pink", 4)
repeat_square(turt, 20)
wn.mainloop()
