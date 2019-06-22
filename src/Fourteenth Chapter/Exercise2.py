# Adapt the merge algorithm to write each of these functions, as was suggested there:
#
# Return only those items that are present in the first list, but not in the second.

import random


def return_xs_unique(xs, ys):
    """ merge sorted lists xs and ys. Return only those items that are present in the first list,
    but not in the second. """
    result = []
    xi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # We're done.

        if xs[xi] not in ys:  # this time it just checks the reverse condition compared to exercise 1
            result.append(xs[xi])
            xi += 1

        else:
            xi += 1


# randomized lists by way of testing


mergelist = (return_xs_unique(random.sample(range(0, 100), 15), random.sample(range(0, 100), 15)))
mergelist.sort()
print(mergelist)


# Return only those items that are present in the second list, but not in the first.

def return_ys_unique(xs, ys):
    """ merge sorted lists xs and ys. Return only those items that are present in the second list,
    but not in the first. """
    result = []
    yi = 0

    while True:
        if yi >= len(ys):          # If xs list is finished,
            return result          # We're done.

        if ys[yi] not in xs:
            result.append(ys[yi])
            yi += 1

        else:
            yi += 1


# randomized lists by way of testing


mergelist = (return_ys_unique(random.sample(range(0, 100), 15), random.sample(range(0, 100), 15)))
mergelist.sort()
print(mergelist)


# Return items that are present in either the first or the second list.


def mergeuniques(xs, ys):
    """ merge lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    xs.sort()  # sort clause unneeded if lists already sorted (as in instructions), but added for generalising
    ys.sort()
    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        if xs[xi] == ys[yi]:        # if equal, skip the identical ys[yi], so that only one is appended
            result.append(xs[xi])
            xi += 1
            yi += 1

        else:
            result.append(ys[yi])
            yi += 1


# randomized lists by way of testing


mergelist = (mergeuniques(random.sample(range(0, 100), 15), random.sample(range(0, 100), 15)))
mergelist.sort()
print(mergelist)


# Return items from the first list that are not eliminated by a matching element in the second list.
# In this case, an item in the second list “knocks out” just one matching item in the first list.
# This operation is sometimes called bagdiff.


def mergebagdiff(xs, ys):
    """ merge lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    xs.sort()  # sort clause unneeded if lists already sorted (as in instructions), but added for generalising
    ys.sort()
    while True:
        if xi == len(xs):          # If xs list is finished,
            return result          # We're done.

        if xs[xi] in ys:
            ys.remove(xs[xi])
            xs.remove(xs[xi])

        if xs[xi] not in ys:
            result.append(xs[xi])
            xi += 1


mergelist = (mergebagdiff([5,7,11,11,11,12,13], [7,8,11]))  # examples from instruction
mergelist.sort()
print(mergelist)

