# Write a function that reverses its string argument, and satisfies these tests below.

import sys


def reversal_of_fortune(s):
    count = 0
    reversestring = ""
    while count < len(s):
        for i in range(1, (len(s)+1)):
            reversestring += s[(len(s)-i):((len(s)-i)+1)]
            count += 1
    return reversestring


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
    test(reversal_of_fortune("happy") == "yppah")
    test(reversal_of_fortune("Python") == "nohtyP")
    test(reversal_of_fortune("") == "")
    test(reversal_of_fortune("a") == "a")


test_suite()  # Here is the call to run the tests
