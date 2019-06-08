# Write the inverse function of 2: day_num which is given a day name, and returns its number. (Tests below.)

import sys
weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def day_name(d):
    if 6 >= int(d) >= 0:
        return weekday[d]
    else:
        return


def day_num(weekday_name):
    for i in range(7):
        if weekday[i] == weekday_name:
            return i

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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)


test_suite()  # Here is the call to run the tests
