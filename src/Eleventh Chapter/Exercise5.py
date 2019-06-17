# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s. Tests below.

import sys


def replace(s, old, new):
    newstring = ""
    newstring = s.split(old)
    newstring = new.join(newstring)
    return newstring

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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
         "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
         "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()  # Here is the call to run the tests
