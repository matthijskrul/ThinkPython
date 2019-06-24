# Chess boards are symmetric: if we have a solution to the queens problem, its mirror solution —
# either flipping the board on the X or in the Y axis, is also a solution.
# And giving the board a 90 degree, 180 degree, or 270 degree rotation is also a solution.
# In some sense, solutions that are just mirror images or rotations of other solutions — in the same family — are less
# interesting than the unique “core cases”.
# Of the 92 solutions for the 8 queens problem,
# there are only 12 unique families if you take rotations and mirror images into account.
# Wikipedia has some fascinating stuff about this.
#
# Write a function to mirror a solution in the Y axis,
#
# Write a function to mirror a solution in the X axis,
#
# Write a function to rotate a solution by 90 degrees anti-clockwise,
# and use this to provide 180 and 270 degree rotations too.

import math


def queens_puzzle_y_mirror(solution):
    newsolution = []
    newsolution.extend(solution[math.ceil(len(solution)/2):])
    newsolution.extend(solution[:math.floor(len(solution)/2)])
    print(newsolution)


def queens_puzzle_x_mirror(solution):
    newsolution = []
    for pos in solution:
        newsolution.append(max(solution)-pos)
    print(newsolution)


def queens_puzzle_90d(solution):
    newsolution = []
    count = 0
    while count <= max(solution):
        for pos in solution:
            if pos == max(solution)-count:
                newsolution.insert(count, solution.index(pos))
                count += 1
    print(newsolution)


def queens_puzzle_180d(solution):
    newsolution = []
    for pos in solution[::-1]:
        newsolution.append(max(solution)-pos)
    print(newsolution)


def queens_puzzle_270d(solution):
    newsolution = solution.copy()
    for pos in solution:
        newsolution[pos] = (max(solution))-(solution.index(pos))
    print(newsolution)


board = [1, 3, 5, 7, 2, 0, 6, 4]  # test values from Wikipedia