# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon.

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


draw_poly(tess, 8, 50)
wn.mainloop()
