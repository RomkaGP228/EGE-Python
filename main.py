from functools import lru_cache


@lru_cache
def F(n):
    if n <= 5:
        return n
    elif n > 5 and n % 5 == 0:
        return n + F(n // 5 + 1)
    elif n > 5 and n % 5 != 0:
        return n + F(n + 6)


for n in range(5, 1000):
    try:
        if F(n) > 1000:
            print(n)
            break
    except RecursionError:
        print(f'Change {n} bitch')
