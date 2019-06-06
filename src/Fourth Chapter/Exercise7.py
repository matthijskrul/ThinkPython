# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n.
# So sum_to(10) would be 1+2+3...+10 which would return the value 55.


def sum_to(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def sum_to_constant_complexity(n):
    return ((n*n)+n)/2

total = sum_to_constant_complexity(3242374)
print(total)
