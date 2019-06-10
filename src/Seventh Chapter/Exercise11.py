# Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn,
# and the second item is the distance to move forward.
# Set up a list of pairs so that the turtle draws a house with a cross through the centre,
# as shown here.
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import turtle
wn = turtle.Screen()
domesticus = turtle.Turtle()
domesticus.shape("turtle")

turtlepath = [
    (270, 100),
    (45, 70.71),
    (90, 70.71),
    (135, 100),
    (225, 141.42),
    (135, 100),
    (135, 141.42),
    (135, 100)
]

for angle, steps in turtlepath:
    domesticus.right(angle)
    domesticus.forward(steps)
wn.mainloop()
