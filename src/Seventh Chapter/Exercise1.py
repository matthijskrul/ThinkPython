# Write a function to count how many odd numbers are in a list.

def count_odds(list):
    oddscount = 0
    for i in (list):
        if i % 2 == 0:
            continue
        oddscount += 1
    print(oddscount)



# (test) count_odds([1, 3, 5, 8, 10, 12, 23])
