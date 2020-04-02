from collections import deque

n, q = map(int, input().split())
cnt = [0] * (n + 1)
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for _ in range(q):
    x, y = map(int, input().split())
    cnt[x] += y

q = deque()
q.append(1)
chk = [0] * (n + 1)

while q:
    v = q.pop()
    chk[v] = 1
    for u in g[v]:
        if chk[u] == 1:
            continue
        cnt[u] += cnt[v]
        q.append(u)
print(*cnt[1:])
