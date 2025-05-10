import math


def f(n):
    for g in range(2, int(math.sqrt(n)) + 1):
        if n % g == 0:
            return False
    return True


count = 0
br = set()
for i in range(268312, 336492):
    ls = set()
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0 and f(j) and f(i // j) and j != (i // j):
            br.add(i)
            count += 1
            break

print(count, min(br))
