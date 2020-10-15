#!/usr/bin/env python3

import random
lim = 10 ** 5
n = random.randint(1, lim)
d = n // random.randint(1, 5)
a = random.randint(1, 10)
# m = random.randint(2, 2 + n // 300)
print(n, d, a)
# print(n)

tmp1 = [x for x in range(n)]
tmp2 = [x for x in range(n)]
# tmp2 = list(range(1, m + 1))
random.shuffle(tmp1)
random.shuffle(tmp2)
# print(" ".join(map(str, tmp1)))
for x, y in zip(tmp1, tmp2):
    print(x, y)

# tmp = []
# for _ in range(n):
#     v = random.randint(0, lim)
#     tmp.append(v)
# print(" ".join(map(str, tmp)))
