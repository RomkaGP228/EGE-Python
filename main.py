for A in range(7000, 1, -1):
    Flag = True
    for x in range(300):
        Flag2 = True
        for y in range(300):
            a = (y - x ** 2) != 80
            b = A < (13 * x - 14)
            c = A < (y ** 2 + 15)
            if not (a or b or c):
                Flag = False
                break
        if not Flag2:
            break
    if Flag:
        print(A)
        break

