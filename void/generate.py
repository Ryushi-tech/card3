#!/usr/bin/env python3
import random
lim = 200000
n = random.randint(1, lim)
# m = random.randint(1, lim)
# print(n, m)
print(n)
tmp = []
for _ in range(n):
    v = random.randint(0, lim)
    tmp.append(v)
print(" ".join(map(str, tmp)))
