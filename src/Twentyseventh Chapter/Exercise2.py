# Write a function that takes an expression string and returns a token list.


def tokenize(expression):
    tokenlist = []
    ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # bit hacky
    expression.split()
    for char in expression:
        if char == " ":
            continue
        if char in ints:
            tokenlist.append(int(char))
        else:
            tokenlist.append(char)
    tokenlist.append("end")
    return tokenlist


print(tokenize("(3 + 7) * 9"))
