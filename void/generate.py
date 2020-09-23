#!/usr/bin/env python3
import random
lim = 100
n = random.randint(1, lim)
m = random.randint(1, lim)
print(n, m)
for _ in range(n):
    tmp = []
    for _ in range(m):
        v = random.randint(0, 1)
        if v:
            tmp.append("#")
        else:
            tmp.append(".")
    print("".join(tmp))
