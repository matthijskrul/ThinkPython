# Add a print function to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.


def newton_sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better
        print(better)


newton_sqrt(25)