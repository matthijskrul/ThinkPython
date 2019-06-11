# Write a function that recognizes palindromes.

import sys


def is_palindrome(s):
    count = 0
    reversestring = ""
    while count < len(s):
        for i in range(1, (len(s)+1)):
            reversestring += s[(len(s)-i):((len(s)-i)+1)]
            count += 1
    if reversestring == s:
        return True


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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))


test_suite()  # Here is the call to run the tests
