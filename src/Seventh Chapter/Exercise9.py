# Write a function, is_prime,
# which takes a single integer argument and returns True when the argument is a prime number
# and False otherwise. Add tests for cases like below.
import sys


def is_prime(n):
    if n > 1:
        for i in range(2, n//2):
            if n % i == 0:
                return False
        return True
    else:
        return False


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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(0))
    test(not is_prime(-22))


test_suite()  # Here is the call to run the tests

