from p import Point
from unit_tester import test

# 1. Add a method area to the Rectangle class that returns the area of any instance (see tests)
# 2. Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance.
# 3. Write a flip method in the Rectangle class that swaps the width and the height of any rectangle instance.
# 4. Write a new method in the Rectangle class to test if a Point falls within the rectangle.
# For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width
# and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded,
# and from [0 to 5) in the y direction. So it does not contain the point (10, 2). See tests below.
# In games, we often put a rectangular “bounding box” around our sprites.
# (A sprite is an object that can move about in the game, as we will see shortly.)
# We can then do collision detection between, say, bombs and spaceships,
# by comparing whether their rectangles overlap anywhere.
# Write a function to determine whether two rectangles collide.


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):  # assignment 1
        return self.width*self.height

    def perimeter(self):  # assignment 2
        return self.width*2 + self.height*2

    def flip(self):  # assignment 3
        self.width, self.height = self.height, self.width
        return Rectangle(self.corner, self.width, self.height)

    def contains(self, point):  # assignment 4
        if self.corner.x <= point.x < self.width and self.corner.y <= point.y < self.height:
            return True
        else:
            return False

    def collision_detection(self, rec2):  # assignment 5
        upper_right = (self.corner.x + self.width, self.corner.y)
        lower_right = (self.corner.x + self.width, self.corner.y - self.height)
        lower_left = (self.corner.x, self.corner.y - self.height)
        rec2_upper_right = (rec2.corner.x + rec2.width, rec2.corner.y)
        rec2_lower_right = (rec2.corner.x + rec2.width, rec2.corner.y - rec2.height)
        rec2_lower_left = (rec2.corner.x, rec2.corner.y - rec2.height)
        if upper_right[1] < rec2_lower_left[1] or lower_left[1] > rec2_upper_right[1]:
            return False
        elif lower_right[0] < rec2_lower_left[0] or lower_left[0] > rec2_lower_right[0]:
            return False
        else:
            return True


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
test(r.perimeter() == 30)
r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
r = Rectangle(Point(0, 0), 10, 10)
ry = Rectangle(Point(0, 0), 5, 5)
rz = Rectangle(Point(20, 20), 10, 10)
test(r.collision_detection(ry))
test(not r.collision_detection(rz))

