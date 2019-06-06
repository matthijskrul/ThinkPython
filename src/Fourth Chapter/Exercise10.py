# Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down,
# and draw the next star.

import turtle
wn = turtle.Screen()
wn.bgcolor("white")
earendil = turtle.Turtle()
earendil.shape("arrow")
earendil.color("black")
earendil.speed(7)


def draw_star(t, length):
    for i in range(5):
        t.forward(length)
        t.right(144)


def draw_stars(t):
    for i in range(5):
        draw_star(t, 100)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()


draw_stars(earendil)
wn.mainloop()
