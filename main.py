for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 1
    P = 15 <= x <= 50
    Q = 35 <= x <= 60
    f = ((not A) <= P) <= (A <= Q)
    if f != 0:
        print(x)