def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

#test(r_max([2, 9, [1, 13], 8, 6]) == 13)
#test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
#test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
#test(r_max(["joe", ["sam", "ben"]]) == "sam")


def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

recursion_depth(0)
