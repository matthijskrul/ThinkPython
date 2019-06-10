# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.

# A call to print_triangular_numbers(5) would produce the following output:

#1       1
#2       3
#3       6
#4       10
#5       15

def print_triangular_numbers(n):
    print(n, int(n*(n+1)/2), end="   ")
    print()


def print_triang_table(high):
    for i in range(1, high+1):
        print_triangular_numbers(i)


print_triang_table(5)
""