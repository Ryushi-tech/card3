import numpy as np
import bisect

n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
s = np.cumsum(a)

res = 0
for i in a:
    b = bisect.bisect_left(s, k)
    k = k + i
    res += n - b
print(res)
