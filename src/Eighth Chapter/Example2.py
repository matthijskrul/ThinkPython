import sys

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
       end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


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
    ss = "Python strings have some interesting methods."
    test(find(ss, "s") == 7)
    test(find(ss, "s", 7) == 7)
    test(find(ss, "s", 8) == 13)
    test(find(ss, "s", 8, 13) == -1)
    test(find(ss, ".") == len(ss) - 1)

test_suite()  # Here is the call to run the tests
