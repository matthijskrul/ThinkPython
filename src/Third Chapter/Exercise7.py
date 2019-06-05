#Write a program to depict a turtle stamp clock (as shown in textbook)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
kronos = turtle.Turtle()
kronos.shape("turtle")
kronos.color("blue")

kronos.stamp()
for i in range(12):
    kronos.penup()
    kronos.forward(75)
    kronos.pendown()
    kronos.forward(10)
    kronos.penup()
    kronos.forward(15)
    kronos.stamp()
    kronos.penup()
    kronos.forward(-100)
    kronos.right(30)
wn.mainloop()
