import numpy as np
n = 1000
lis = np.zeros((n+1,n+1), dtype=np.int64)
lis[:, 0] = 1
for i in range(1, n+1):
    lis[i, 1:i+1] = lis[i-1, :i] + lis[i-1, 1:i+1]
print(lis[:10, :10].sum(axis=1))
print(lis[1:10:2, 1:10:2])
