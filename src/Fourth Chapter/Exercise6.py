# Write a void function draw_equitriangle(t, sz)
# which calls draw_poly from exercise 3 to have its turtle draw a equilateral triangle.

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("pink")


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


def draw_equitriangle (t, sz):
    draw_poly(t, 3, sz)


draw_equitriangle(tess, 100)
wn.mainloop()
