# Modify num_digits so that it works correctly with any integer value. Tests below.

import sys


def num_digits(n):
    count = 0
    if n == 0:
        count = 1
    else:
        while n > 0:
            count = count + 1
            n = n // 10
        while n < 0:
            count = count + 1
            n = n // 10
            if n == -1:
                break

    return count


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
    test(num_digits(12345) == 5)
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)


test_suite()  # Here is the call to run the tests
