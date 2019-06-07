# 1) Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled.
# Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.
#
# Hint: Floating point arithmetic is not always exactly accurate,
# so it is not safe to test floating point numbers for equality.
# If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as:
# if  abs(x-y) < 0.000001:    # If x is approximately equal to y

def is_rightangled():
    triangle_side_a = float(input("What is the length of the first side? "))
    triangle_side_b = float(input("What is the length of the second side? "))
    triangle_side_c = float(input("What is the length of the longest side? "))
    if triangle_side_c == ((triangle_side_a**2) + (triangle_side_b**2))**0.5:
        print(True)
    else:
        print(False)


is_rightangled()
