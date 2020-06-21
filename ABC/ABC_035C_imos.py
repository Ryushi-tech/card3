import numpy as np
n, k = map(int, input().split())
tmp = [0] * (n + 1)
for i in range(k):
    l, r = map(int, input().split())
    tmp[l - 1] += 1
    tmp[r] -= 1
s = np.cumsum(tmp)

res = [str(x & 1) for x in s][:-1]
print("".join(res))
