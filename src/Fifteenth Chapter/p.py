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
