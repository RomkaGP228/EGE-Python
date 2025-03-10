from itertools import *

t = product("НРДО", repeat=4)

for k, i in enumerate(t):
    if ''.join(i) == 'ДРОН':
        print(k + 1)  # тк нумерация с 0
