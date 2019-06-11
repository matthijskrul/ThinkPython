# Write a function that counts how many times a substring occurs in a string.

import sys


def count(stringpart, stringwhole):
    position = 0
    tally = 0
    while position < len(stringwhole):
        x = stringwhole.find(stringpart, position)
        if x == -1:
            break
        tally += 1
        position = x + 1
    return tally


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
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)


test_suite()  # Here is the call to run the tests
