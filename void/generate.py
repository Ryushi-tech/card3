#!/usr/bin/env python3

import random
lim = 500
h = random.randint(1, lim)
w = random.randint(1, lim)
# m = random.randint(2, 2 + n // 300)
print(h, w)
# print(n)
for i in range(h):
    # print(i, i + random.randint(1, 3))
    x = random.randint(0, w)
    if i == 0:
        tmp = ["s"] + ["."] * x + ["#"] * (w - x - 1)
    elif i == h - 1:
        tmp = ["g"] + ["."] * x + ["#"] * (w - x - 1)
    else:
        tmp = ["."] * x + ["#"] * (w - x)
    random.shuffle(tmp)
    print("".join(tmp))
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
