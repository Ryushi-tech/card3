import numpy as np
n = int(input())
s = np.array(input().split(), np.int64)
mod = 10 ** 9 + 7

res = 0
po2 = 1
for i in range(61):
    bit = (s >> i) & 1
    x = np.count_nonzero(bit)
    y = n - x
    res += x * y % mod * po2
    res %= mod
    po2 *= 2 % mod
print(res)
