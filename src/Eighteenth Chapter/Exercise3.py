# Write a function, recursive_min, that returns the smallest value in a nested number list.
from unit_tester import test


def recursive_min(data):
    smallest = None
    first_time = True
    for e in data:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False

    return smallest


test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
