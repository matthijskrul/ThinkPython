# Write a function that helps answer questions like ‘“Today is Wednesday.
# I leave on holiday in 19 days time. What day will that be?”’
# So the function must take a day name and a delta argument — the number of days to add —
# and should return the resulting day name. Use previous code. (Tests below)

import sys
weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def day_add(day_name, days_to_add):
    for i in range(7):
        if weekday[i] == day_name:
            leaving_day = (i + days_to_add) % 7
            return weekday[leaving_day]
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
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()  # Here is the call to run the tests
