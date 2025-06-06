count = 0

for x in range(-5000, 5000):
    A = 0
    P = x in [2, 7, 14, 28, 34, 102]
    Q = x in [7, 12, 24, 28, 56, 94]
    f = A or ((not P) <= (not Q))
    if not f:
        count += x
print(count)