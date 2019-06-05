#write a program to draw a pentagram

import turtle
wn = turtle.Screen()
gardner = turtle.Turtle()
gardner.shape("turtle")

for i in range(5):
    gardner.forward(100)
    gardner.right(144)
gardner.hideturtle()
wn.mainloop()
