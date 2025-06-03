from itertools import product

count = 0
a = 'КРУЖА'
ls = list(product(a, repeat=7))
for i in ls:
    st = ''.join(i)
    if (st.count('А') == 2 and st.count('У') == 0) or (st.count('А') == 1 and st.count('У') == 1) or \
            (st.count('А') == 0 and st.count('У') == 2):
        count += 1
print(count)


