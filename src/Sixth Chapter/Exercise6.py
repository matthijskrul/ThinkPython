# Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.
# Extend to_secs so that it can cope with real values as inputs.
# It should always return an integer number of seconds (truncated towards zero).
# Tests below.

import sys


def to_secs(h, m, s):
    hours = float(h)
    minutes = float(m)
    seconds = float(s)
    total_seconds = ((hours*3600)+(minutes*60)+seconds)
    return int(total_seconds)


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
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)


test_suite()  # Here is the call to run the tests
