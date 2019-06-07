# Write a function find_hypot which, given the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)


def find_hypot():
    triangle_side_a = float(input("What is the length of the first side? "))
    triangle_side_b = float(input("What is the length of the second side? "))
    hypotenuse = ((triangle_side_a**2) + (triangle_side_b**2))**0.5
    print(hypotenuse)


find_hypot()

