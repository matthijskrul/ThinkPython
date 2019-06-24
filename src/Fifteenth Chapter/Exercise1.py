# Rewrite the distance function from the chapter titled Fruitful functions
# so that it takes two Points as parameters instead of four numbers.

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

#  Add a method reflect_x to Point which returns a new Point,
#  one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

    def reflect_x(self):
        refx = (self.x)
        refy = -(self.y)
        return Point(refx, refy)

# Rewrite the distance function from the chapter titled Fruitful functions
    # so that it takes two Points as parameters instead of four numbers.
    def distance(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        dsquared = dx*dx + dy*dy
        result = dsquared**0.5
        return result

# Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,
# Point(4, 10).slope_from_origin()
# 2.5

    def slope_from_origin(self):
        return self.y/self.x
# What cases will cause this method to fail? -> division by zero

# The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
# The coefficients a and b completely describe the line.
# Write a method in the Point class so that if a point instance is given another point,
# it will compute the equation of the straight line joining the two points.
# It must return the two coefficients as a tuple of two values. For example,
# print(Point(4, 11).get_line_to(Point(6, 15)))
# (2, 3)

    def get_line_to(self, target):
        mx = target.x-self.x
        my = target.y-self.y
        slope = my/mx
        b = self.y - (slope * self.x)
        return (slope, b)

print(Point(4, 11).get_line_to(Point(6, 15)))
