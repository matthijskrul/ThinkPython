# Define a new kind of Turtle, TurtleGTX, that comes with some extra features: it can jump forward a given distance,
# and it has an odometer that keeps track of how far the turtle has travelled since it came off the production line.
# (The parent class has a number of synonyms like fd, forward, back, backward, and bk: for this exercise,
# just focus on putting this functionality into the forward method.)
# Think carefully about how to count the distance if the turtle is asked to move forward by a negative amount.
# After travelling some random distance, your turtle should break down with a flat tyre.
# After this happens, raise an exception whenever forward is called.
# Also provide a change_tyre method that can fix the flat.

import turtle
import random


class TurtleGTX(turtle.Turtle):
    def __init__(self, odometer=0, brokentyre=False):
        self.odometer = odometer
        self.brokentyre = brokentyre

    def forward(self, distance, rng=random.randrange(1, 101)):
        self.odometer += abs(distance)
        pen = turtle.Pen()
        if rng > 90:
            self.brokentyre = True
        if self.brokentyre:
            exception = ValueError("The turtle has got a flat tyre!")
            raise exception
        pen.penup()
        pen.forward(distance)
        pen.pendown()

    def change_tyre(self):
        self.brokentyre = False