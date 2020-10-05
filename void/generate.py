#!/usr/bin/env python3

import random
lim = 100000
n = random.randint(1, lim)
m = random.randint(1, lim)
print(n, m)
# print(n)

tmp1 = list(range(1, m + 1))
# tmp2 = list(range(1, n + 1))
random.shuffle(tmp1)
# random.shuffle(tmp2)

for x in tmp1:
    print(x, random.uniform(-1, 1), random.uniform(-1, 1))

# tmp = []
# for _ in range(n):
#     v = random.randint(0, lim)
#     tmp.append(v)
# print(" ".join(map(str, tmp)))
