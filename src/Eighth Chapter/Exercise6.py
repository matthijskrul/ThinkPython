# Write a function that mirrors its argument. Tests below.

import sys


def mirror(s):
    count = 0
    reversestring = ""
    while count < len(s):
        for i in range(1, (len(s) + 1)):
            reversestring += s[(len(s) - i):((len(s) - i) + 1)]
            count += 1
    return s+reversestring


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
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")


test_suite()  # Here is the call to run the tests
