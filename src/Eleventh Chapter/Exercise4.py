# Write a function cross_product(u, v) that takes two lists of numbers of length 3 and returns their cross product.
# You should write your own tests.

import sys


def cross_product(u, v):
    newlist = []
    if len(u) and len(v) == 3:
        cpx = u[1] * v[2] - u[2] * v[1]
        newlist.append(cpx)
        cpy = u[2] * v[0] - u[0] * v[2]
        newlist.append(cpy)
        cpz = u[0] * v[1] - u[1] * v[0]
        newlist.append(cpz)
    else:
        return False
    return newlist


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
    test(cross_product([3, 0, 0], [0, 4, 0]) == [0, 0, 12])

test_suite()  # Here is the call to run the tests
