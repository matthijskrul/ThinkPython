# Adapt the merge algorithm to write each of these functions, as was suggested there:
#
# Return only those items that are present in both lists.
import random


def return_common_items(xs, ys):
    """ merge sorted lists xs and ys. Return only those items that are present in both lists. """
    result = []
    xi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # We're done.

        if xs[xi] in ys:
            result.append(xs[xi])
            xi += 1

        else:
            xi += 1


# randomized lists by way of testing


mergelist = (return_common_items(random.sample(range(0, 100), 15), random.sample(range(0, 100), 15)))
mergelist.sort()
print(mergelist)
