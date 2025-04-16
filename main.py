def f(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        a = f(i)
        if n % i == 0 and i > 100 and a:
            return i
        elif n % i == 0 and i < 100 and a:
            return 0


for i in range(20222022, 2022, -1):
    a = fn(i)
    if not f(i) and a:
        print(i, a)
