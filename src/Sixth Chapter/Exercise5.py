# Write a function days_in_month which takes the name of a month, and returns the number of days in the month.
# Ignore leap years. (Tests below)

import sys

calendardays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = (["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"])


def days_in_month(month_name):
    for i in range(12):
        if months[i] == month_name:
            return calendardays[i]
    return


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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)


test_suite()  # Here is the call to run the tests
