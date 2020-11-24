import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall, shortest_path

input = sys.stdin.readline


n, m = map(int, input().split())
cost = np.zeros((n, n), dtype='i8')
for i in range(m):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    cost[a][b] = t

dist_mat = shortest_path(cost, directed=False)
res = dist_mat.max(axis=0).min().astype('i8')
print(res)
