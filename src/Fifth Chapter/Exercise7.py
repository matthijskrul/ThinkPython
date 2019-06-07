# Extend Exercise 6 so that the sides can be given to the function in any order.


def is_rightangled():
    triangle_side_a = float(input("What is the length of the first side? "))
    triangle_side_b = float(input("What is the length of the second side? "))
    triangle_side_c = float(input("What is the length of the third side? "))
    if triangle_side_c == ((triangle_side_a**2) + (triangle_side_b**2))**0.5 or triangle_side_a == ((triangle_side_c**2) + (triangle_side_b**2))**0.5 or triangle_side_b == ((triangle_side_c**2) + (triangle_side_a**2))**0.5:
        print(True)
    else:
        print(False)


is_rightangled()
