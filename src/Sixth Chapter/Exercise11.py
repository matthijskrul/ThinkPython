# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number
# and False if it is odd.
# Now write the function is_odd(n) that returns True when n is odd and False otherwise.
# Include unit tests for this function too.
# Finally, modify it so that it uses a call to is_even to determine if its argument is an odd integer,
# and ensure that its test still pass.
# Add your own tests to the test suite.

import sys


def is_even(n):
    return int(n) % 2 == 0


def is_odd(n):
    return not is_even(n)


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
    test(is_even(4))
    test(is_even(-4))
    test(not is_even(3))
    test(not is_even(3.9999))
    test(not is_even(2**0.2))
    test(is_odd(3))
    test(not is_odd(2))


test_suite()  # Here is the call to run the tests
