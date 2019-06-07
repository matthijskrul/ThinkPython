# Write a function which is given an exam mark,
# and it returns a string — the grade for that mark — according to this scheme:
#
# Mark  Grade
#
# >= 75 First
#
# [70-75) Upper Second
#
# [60-70) Second
#
# [50-60)  Third
#
# [45-50) F1 Supp
#
# [40-45) F2
#
# < 40    F3

# The square and round brackets denote closed and open intervals.
# A closed interval includes the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2.

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

# Test your function by printing the mark and the grade for all the elements in this list.


def grade():
    for i in xs:
        float(i)
        if i >= 75:
            print(i, "First")
        elif 75 > i >= 70:
            print(i, "Upper Second")
        elif 70 > i >= 60:
            print(i, "Second")
        elif 60 > i >= 50:
            print(i, "Third")
        elif 50 > i >= 45:
            print(i, "F1 Supp.")
        elif 45 > i >= 40:
            print(i, "F2")
        else:
            print(i, "F3")


grade()

