# 1) in a function named count_letters,
# and generalize it so that it accepts the string and the letter as arguments.
# Make the function return the number of characters, rather than print the answer. The caller should do the printing.
# 2) Now rewrite the count_letters function so that instead of traversing the string,
# it repeatedly calls the find method,
# with the optional third parameter to locate new occurrences of the letter being counted.


def count_letters(s, l):
    count = 0
    found_position = 0
    while found_position != -1:
        found_position = s.find(l, found_position)
        if found_position != -1:
            count += 1
            # Increment the starting character by one, past the last occurrence.
            found_position += 1
    return count


print(count_letters("abanana", "a"))
