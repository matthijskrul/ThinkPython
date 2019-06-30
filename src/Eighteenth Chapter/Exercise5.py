# Write a function flatten that returns a simple list containing all the values in a nested list:

from unit_tester import test


def flatten(data):
    flatlist = []
    for e in data:
        if type(e) == list:
            flatlist += (flatten(e))
        else:
            flatlist.append(e)
    return flatlist



test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
         ["this", "a", "thing", "a", "is", "a", "easy"])
test(flatten([]) == [])
