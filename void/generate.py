#!/usr/bin/env python3
import random
lim = 200000
n = random.randint(1, lim)
# m = random.randint(1, lim)
# print(n, m)
print(n)

tmp1 = list(range(1, n + 1))
tmp2 = list(range(1, n + 1))
random.shuffle(tmp1)
random.shuffle(tmp2)

for x, y in zip(tmp1, tmp2):
    print(x, y)

# tmp = []
# for _ in range(n):
#     v = random.randint(0, lim)
#     tmp.append(v)
# print(" ".join(map(str, tmp)))
