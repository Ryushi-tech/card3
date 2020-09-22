#!/usr/bin/env python3
import random
lim = 10000
n = random.randint(1, lim)
m = random.randint(1, lim)
print(n, m)
for _ in range(m):
    v = random.randint(1, n)
    w = random.randint(1, n)
    print(v, w)
