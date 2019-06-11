# Write a function that removes the first occurrence of a string from another string.

import sys


def remove(substring, string):
    index = string.find(substring)
    if substring not in string:
        return string
    else:
        before_occurrence = string[:index]
        after_occurrence = string[index+len(substring):]
        return before_occurrence + after_occurrence



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
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")

test_suite()  # Here is the call to run the tests
