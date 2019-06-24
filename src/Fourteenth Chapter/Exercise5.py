# Every week a computer scientist buys four lotto tickets. She always chooses the same prime numbers,
# with the hope that if she ever hits the jackpot, she will be able to go onto TV and Facebook
# and tell everyone her secret. This will suddenly create widespread public interest in prime numbers,
# and will be the trigger event that ushers in a new age of enlightenment.
# She represents her weekly tickets in Python as a list of lists:
#
# my_tickets = [ [ 7, 17, 37, 19, 23, 43],
#                [ 7,  2, 13, 41, 31, 43],
#                [ 2,  5,  7, 11, 13, 17],
#                [13, 17, 37, 19, 23, 43] ]
#
# 1) Each lotto draw takes six random balls, numbered from 1 to 49. Write a function to return a lotto draw.
# 2) Write a function that compares a single ticket and a draw, and returns the number of correct picks on that ticket,
# see test below.
# 3) Write a function that takes a list of tickets and a draw,
# and returns a list telling how many picks were correct on each ticket. See test below.
# 4) Write a function that takes a list of integers, and returns the number of primes in the list.
# 5) Write a function to discover whether the computer scientist has missed any prime numbers
# in her selection of the four tickets. Return a list of all primes that she has missed.
# 6) Write a function that repeatedly makes a new draw, and compares the draw to the four tickets (eg count overlaps).

import random
from unit_tester import test

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
                [ 7,  2, 13, 41, 31, 43],
                [ 2,  5,  7, 11, 13, 17],
                [13, 17, 37, 19, 23, 43] ]


def lotto_6_from_49():  # first assignment
    count = 0
    draw = []
    while count < 6:
        draw.append(random.randrange(1, 49))
        count += 1
    return draw


def lotto_match(d, t):  # second assignment
    count = 0
    for i in d:
        if i in t:
            count += 1
    return count


test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)


def lotto_matches(d, t):  # third assignment
    resultlist = []
    count = 0
    for i in t:
        for j in i:
            if j in d:
                count += 1
        resultlist.append(count)
        count = 0
    return resultlist


test(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets) == [1, 2, 3, 1])


def is_prime(n):
    if n > 1:
        for i in range(2, (n//2) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False


def primes_in(l):  # fourth assignment
    count = 0
    for i in l:
        if is_prime(i):
            count += 1
    return count


test(primes_in([42, 4, 7, 11, 1, 13]) == 3)


def primes_between(x, y):
    primes = []
    for n in range(x, y+1):
        if is_prime(n):
            primes.append(n)

    return primes


def prime_misses(l):  # fifth assignment
    primes = primes_between(1, 49)
    for list in l:
        for element in list:
            if element in primes:
                primes.remove(element)
    return primes


test(prime_misses(my_tickets) == [3, 29, 47])


def draw_comparison():  # sixth assignment
    drawcount = 0
    while drawcount <= 20:  # or any desired number for higher success rates
        draw = lotto_6_from_49()
        drawcount += 1
        successrate = lotto_matches(draw, my_tickets)
        print(successrate)


draw_comparison()
