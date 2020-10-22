#!/usr/bin/env python3

import random
lim = 100000
h = random.randint(200, lim)
w = random.randint(200, h // 2)
# m = random.randint(2, 2 + n // 300)
print(h, w)
# print(n)
for i in range(1, w + 1):
    print(i, i + random.randint(1, 3))
    # x = random.randint(0, w)
    # tmp = ["."] * x + ["#"] * (w - x)
    # random.shuffle(tmp)
    # print("".join(tmp))
# tmp1 = [x for x in range(n)]
# tmp2 = [x for x in range(n)]
# random.shuffle(tmp1)
# random.shuffle(tmp2)
# print(" ".join(map(str, tmp1)))
# for x, y in zip(tmp1, tmp2):
#     print(x, y)

# tmp = []
# start = 1
# for _ in range(k):
#     v = random.randint(start, start + 20)
#     w = random.randint(v, v + 20)
#     start = w
#     print(v, w)
