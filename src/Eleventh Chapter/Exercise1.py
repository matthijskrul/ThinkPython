# Write a function add_vectors(u, v) that takes two lists of numbers of the same length,
# and returns a new list containing the sums of the corresponding elements of each. Tests below.
import sys

def add_vectors(u, v):
    newlist = []
    for i in range(len(u)):
        ls = u[i] + v[i]
        newlist.append(ls)
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
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


test_suite()  # Here is the call to run the tests
