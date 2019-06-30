# Rewrite the fibonacci algorithm without using recursion.
# Can you find bigger terms of the sequence?
# Can you find fib(200)?
import time


def fibonacci(n):
    fibonaccinumber1 = 0
    fibonaccinumber2 = 1
    if n > 1:
        for i in range(2, n+1):
            fibonaccinumber3 = fibonaccinumber1 + fibonaccinumber2
            fibonaccinumber1 = fibonaccinumber2
            fibonaccinumber2 = fibonaccinumber3
        return fibonaccinumber2



t0 = time.perf_counter()
n = 9
result = fibonacci(n)
t1 = time.perf_counter()

print("fibonacci({0}) = {1}, ({2:.2f} secs)".format(n, result, t1 - t0))
