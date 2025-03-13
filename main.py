from math import log2, ceil, floor

K = 32
N = 311
i = ceil(log2(N))
n = 256
I1 = n * i * K / 8
I0 = 15 * 1024
print((I0 - I1) / n)
