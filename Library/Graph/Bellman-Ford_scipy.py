import sys
input = lambda: sys.stdin.readline()

import numpy as np
from scipy.sparse.csgraph import shortest_path, bellman_ford
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
cost = np.zeros((n, n), dtype='i8')
for i in range(m):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    cost[a][b] = -t

try:
    tmp = bellman_ford(csr_matrix(cost), indices=0)
    ans = -tmp[-1]
    ans_i = ans.astype('i8')
    print(ans_i)
except Exception:  # Note that any error could be captured
    print("inf")
