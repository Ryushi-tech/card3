import sys
sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())

dist = [-1] * (n + 1)

g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)


def rec(x):
    if dist[x] != -1:
        return dist[x]
    res = 0
    for v in g[x]:
        res = max(res, rec(v) + 1)
    dist[x] = res
    return dist[x]


ans = 0
for i in range(1, n + 1):
    ans = max(ans, rec(i))
print(ans)
