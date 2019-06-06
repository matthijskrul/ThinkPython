# Draw a pattern (see textbook).

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

def draw_inner_square(t):
    for i in range(4):
        t.forward(50)
        t.left(90)

def draw_outer_square(t):
    for i in range(4):
        draw_inner_square(t)
        t.right(90)

def draw_square_pattern(t):
    for i in range(5):
        draw_outer_square(t)
        t.right(18)

draw_square_pattern(tess)
wn.mainloop()
