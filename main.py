from math import log2, ceil

N1 = 2 ** 24
i1 = ceil(log2(N1))
I0 = 18 * 1024 * 1024 * 8
K1 = I0 / i1
N2 = 2 ** 16
i2 = ceil(log2(N2))
K2 = K1 / 2
print(K2 * i2 / 8 / 1024 / 1024)