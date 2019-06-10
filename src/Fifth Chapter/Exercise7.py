# Extend Exercise 6 so that the sides can be given to the function in any order.


def is_rightangled(a, b, c):
    return a == ((b**2)+c**2)**0.5


triangle_side_a = float(input("What is the length of the first side? "))
triangle_side_b = float(input("What is the length of the second side? "))
triangle_side_c = float(input("What is the length of the third side? "))

if (is_rightangled(triangle_side_a, triangle_side_b, triangle_side_c)
    or is_rightangled(triangle_side_b, triangle_side_a, triangle_side_c)
    or is_rightangled(triangle_side_c, triangle_side_a, triangle_side_b)):
    print(True)
else:
    print(False)
