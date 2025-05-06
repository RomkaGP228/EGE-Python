from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache()
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + 3 * g(n - 1)


@lru_cache()
def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) - 2 * g(n - 1)

print(sum(map(int, str(f(18)))))