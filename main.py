from math import log2, ceil

N1 = 18
N2 = 10
K1 = 1
K2 = 9
n = 25
i1 = ceil(log2(N1))
i2 = ceil(log2(N2))
I = ceil((i1 * K1 + i2 * K2) / 8)  # чисто по кайфу находим кобинации, разделив пароль на два мелких
print(I * n)
