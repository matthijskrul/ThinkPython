import turtle
wn = turtle.Screen()
claudius = turtle.Turtle()
claudius.shape("turtle")

turtlepath = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for angle, steps in turtlepath:
    claudius.right(angle)
    claudius.forward(steps)