from collections import deque

n, m = map(int, input().split())

dist = [0] * (n + 1)
seen = [0] * (n + 1)

g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    seen[b] += 1

que = deque()
for i in range(1, n + 1):
    if seen[i] == 0:
        que.append(i)

while que:
    x = que.pop()
    for v in g[x]:
        seen[v] -= 1
        if seen[v] == 0:
            que.append(v)
        dist[v] = max(dist[v], dist[x] + 1)

res = 0
for i in range(1, n + 1):
    res = max(res, dist[i])
print(res)
