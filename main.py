def f(n):
    if n <= 10:
        return n
    elif n > 10 and n % 10 == 0:
        return f(n % 5) + 1
    else:
        return n * f(n - 1)


def g(n):
    if n >= 21:
        return n * n + 1 * n + 3
    elif n < 21 and n % 2 == 0:
        return 2 * g(n - 2) * g(n - 4)
    else:
        return 2 * g(n - 1) * g(n - 3)


a = f(g(f(g(22))))
print(sum(map(int, str(a))))
