# Thursday: Recursive Functions and Memoization

# Writing a Factorial Function

# writing a factorial using recursive functions
def factorial(n):
    if n < 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(5))

# writing the recursive fibonacci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(3))

# Understanding Memoization

# using memoization with the fibonacci sequence

cache = {}  # used to cache values to be used later


def fib_with_cache(n):
    if n in cache:
        print("yei! si esta en el cache! no calcular nada")
        return cache[n]
    result = 0

    # base case
    if n <= 1:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    cache[n] = result
    return result

print(fib_with_cache(20))

# using @lru_cache, Python’s default moization/caching technique
from functools import lru_cache
@lru_cache()
def fib_with_lru_cache(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib_with_lru_cache(20))