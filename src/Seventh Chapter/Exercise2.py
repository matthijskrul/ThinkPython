# Sum up all the even numbers in a list.


def sum_evens(list):
    evenssum = 0
    for i in (list):
       if i % 2 == 0:
           evenssum += i
    print(evenssum)


sum_evens([1, 3, 5, 8, 10, 12, 23])
