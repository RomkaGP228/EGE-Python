from math import floor

K = 3614 * 5410
i = 24
I1 = 8 * 1024 * 1024 * 1024 * 8
n = 3215
I0 = K * i
n1 = floor(I1 / I0)
while n > n1:
    n -= n1
print(n)
