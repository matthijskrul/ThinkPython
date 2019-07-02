# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order
# which occur in the string together with the number of times each letter occurs.
# Case should be ignored.


def lettercount(s):
    tally = {}
    s = s.lower()
    for letter in s:
        if not letter.isalpha():
            continue
        tally[letter] = tally.get(letter, 0) + 1
    letterlist = list(tally.items())
    letterlist.sort()
    for pair in letterlist:
        print("".join(str(pair[0])), "".join(str(pair[1])))  # so it doesn't return a list of tuples, ie format cleanup


# lettercount("The Quick Brown Fox Jumps Over The Lazy Dog")  #test case
