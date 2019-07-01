# Write a function named readposint that uses the input dialog to prompt the user for a positive integer
# and then checks the input to confirm that it meets the requirements.
# It should be able to handle inputs that cannot be converted to int,
# as well as negative ints,
# and edge cases (e.g. when the user closes the dialog, or does not enter anything at all.)


def readposint():
    posint = input("Please provide a positive integer: ")
    if type(posint) is int and posint > 0:
        print(posint)
    elif type(posint) is not int:
        typeerror = TypeError("{0} is not an integer".format(posint))
        raise typeerror
    elif posint <= 0:
        negerror = ValueError("{0} is not a positive integer".format(posint))
        raise negerror
    else:
        edgecase = SystemExit(posint)
        raise edgecase



readposint()