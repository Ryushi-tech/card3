import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    cost = np.zeros((n, n), dtype=np.float64)
    for i in range(m):
        a, b, t = map(int, input().split())
        a, b = a - 1, b - 1
        cost[a][b] = t

    dist_mat = shortest_path(cost, directed=False)
    res = dist_mat.max(axis=0).min().astype(int)
    print(res)


if __name__ == '__main__':
    main()
