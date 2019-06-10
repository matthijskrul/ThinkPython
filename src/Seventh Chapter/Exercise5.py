# Sum all the elements in a list up to but not including the first even number.
# (Write your unit tests. What if there is no even number?)

def sum_up_to_even(list):
    evenssum = 0
    for i in (list):
       if i % 2 == 0:
           break
       else:
           evenssum += i
    print(evenssum)


sum_up_to_even([1, 3, 5, 0, 10, 12, 23])
