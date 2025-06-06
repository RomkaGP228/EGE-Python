def f(n, base):
    fin = ''
    numeric = '0123456789'
    while n > 0:
        fin = numeric[n % base] + fin
        n //= base
    return fin


count = 0
for i in range(8 ** 6, 8 ** 7):
    si = str(f(i, 8))
    if len(set(si)) == len(si) and len(si) == 7:
        Flag = True
        for j in range(len(si) - 1):
            if (int(si[j]) % 2 == 0 and int(si[j + 1]) % 2 == 0) or \
                    (int(si[j]) % 2 != 0 and int(si[j + 1]) % 2 != 0):
                Flag = False
        if Flag:
            count += 1
print(count)