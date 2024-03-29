def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

import time
t0 = time.perf_counter()
n = 35
result = fib(n)
t1 = time.perf_counter()

print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))
