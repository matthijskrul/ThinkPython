# Write a void function to draw a star, where the length of each side is 100 units.
# (Hint: You should turn the turtle by 144 degrees at each point.)

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


draw_star(earendil, 100)
wn.mainloop()
