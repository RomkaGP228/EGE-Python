from itertools import product

count = 0
a = 'УСЛОВИЕ'
ls = list(product(a, repeat=7))
for i in ls:
    s = ''.join(i)
    if s[0] != 'И' and s[-1] != 'О' and '' not in s and '' not in s and '' not in s and '' not in s and '' not in s and \
            '' not in s and '' not in s and '' not in s and '' not in s and '' not in s and '' not in s and '' not in s:
        print(s)
