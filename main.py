game_over = 68


def fn(x1, x2, c, pob, func=all):
    if (x1 + x2) >= game_over or c > max(pob):
        return c in pob
    c += 1
    moves = [fn(x1 + 2, x2, c, pob), fn(x1, x2 + 2, c, pob), fn(x1 * 2, x2, c, pob), fn(x1, x2 * 2, c, pob)]
    if c % 2 == max(pob) % 2:
        return any(moves)
    else:
        return func(moves)

print("#19")
s1 = 7
for s2 in range(1, 61):
    if fn(s1, s2, 0, [2], any):
        print(s2)
        break
print()
print("#20")
for s2 in range(1, 61):
    if not fn(s1, s2, 0, [1], all) and fn(s1, s2, 0, [3], all):
        print(s2)
        break
print()
print("#21")
for s2 in range(1, 61):
    if not fn(s1, s2, 0, [2], all) and fn(s1, s2, 0, [2, 4], all):
        print(s2)