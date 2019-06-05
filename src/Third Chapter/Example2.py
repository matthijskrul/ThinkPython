#learning to modify the attributes of the turtle and window objects

#Modify this program so that before it creates the window, it prompts the user to enter the desired background color. It should store the user’s responses in a variable, and modify the color of the window according to the user’s wishes.
#Do similar changes to allow the user, at runtime, to set tess‘ color.
#Do the same for the width of tess‘ pen. Hint: your dialog with the user will return a string, but tess‘ pensize method expects its argument to be an int. So you’ll need to convert the string to an int before you pass it to pensize.


import turtle

background = input("What background color should the window have? ")
turtlecolor = input("What color should Tess have? ")
pensize = int(input("And what should the width of Tess' pen be? "))
wn = turtle.Screen()
wn.bgcolor(background)  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

tess = turtle.Turtle()
tess.color(turtlecolor)  # Tell tess to change her color
tess.pensize(3)  # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()