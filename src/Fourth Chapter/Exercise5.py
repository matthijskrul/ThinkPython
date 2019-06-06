# Draw two spiral patterns (see textbook).

import turtle
wn = turtle.Screen()
wn.bgcolor("white")
tess = turtle.Turtle()
tess.shape("arrow")
tess.color("black")
tess.speed(0)


def basic_pattern(t, length):
    t.right(90)
    t.forward(length)


def larger_pattern(t, n, length):
    for i in range(n):
        basic_pattern(t, length*i)


def basic_angled_pattern(t, angle, length):
    t.right(angle)
    t.forward(length)


def larger_angled_pattern(t, angle, n, length):
    for i in range(n):
        basic_angled_pattern(t, angle-1, length*i)


tess.penup()
tess.forward(-300)
tess.pendown()
larger_pattern(tess, 99, 2)
tess.right(90)
tess.penup()
tess.forward(600)
tess.right(90)
tess.forward(100)
tess.left(90)
tess.pendown()
larger_angled_pattern(tess, 90, 99, 2)
wn.mainloop()
