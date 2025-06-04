from math import log2, ceil

K = 427
N = 1008 + 10
i = ceil(log2(N))
n = 524288
I = ceil((K * i) / 8)  # ближайшее - 540
I0 = (I * n) / (1024 * 1024)
print(I0) # 270