# Sum up all the negative numbers in a list.

def sum_negatives(list):
    negativessum = 0
    for i in (list):
       if i < 0:
           negativessum += i
    print(negativessum)


sum_negatives([25, 3, -0.22, 1.38, -21, -1033, 4, 0])
