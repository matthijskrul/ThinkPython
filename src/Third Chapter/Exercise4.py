#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#
#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)

import turtle
wn = turtle.Screen()
turt=turtle.Turtle()
for i in range(3):
    turt.forward(100)
    turt.left(120)

for i in range(4):
    turt.forward(100)
    turt.left(90)

for i in range(6):
    turt.forward(100)
    turt.left(60)

for i in range(8):
    turt.forward(100)
    turt.left(45)
wn.mainloop()
