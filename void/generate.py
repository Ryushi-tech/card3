#!/usr/bin/env python3

import random
lim = 90000
n = random.randint(1, lim)
m = random.randint(2, 2 + n // 300)
print(n, m)
# print(n)

tmp1 = [0] * (n // 2) + [1] * (n - n // 2)
# tmp2 = list(range(1, m + 1))
random.shuffle(tmp1)
# random.shuffle(tmp2)
print("".join(map(str, tmp1)))
# for x, y in zip(tmp1[::2], tmp1[1::2]):
#     print(x, y)

# tmp = []
# for _ in range(n):
#     v = random.randint(0, lim)
#     tmp.append(v)
# print(" ".join(map(str, tmp)))
