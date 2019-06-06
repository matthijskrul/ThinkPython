# Write a function area_of_circle(r) which returns the area of a circle of radius r.

import math
def area_of_circle(r):
    area = (r**2)*math.pi
    return area

area = area_of_circle(3)
print(area)