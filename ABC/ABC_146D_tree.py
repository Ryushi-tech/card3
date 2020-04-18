from collections import deque
n = int(input())
g = [[] for _ in range(n)]
ab = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
    ab.append((a,b))

q = deque([0])
par = [0] * n
order = []

while q:
    x = q.pop()
    order.append(x)
    for y in g[x]:
        if y == par[x]:
            continue
        par[y] = x
        q.append(y)

color = [-1] * n
for x in order:
    ng = color[x]
    c = 1
    for y in g[x]:
        if y == par[x]:
            continue
        if c == ng:
            c += 1
        color[y] = c
        c += 1

ans = []
for a, b in ab:
    if par[a] == b:
        ans.append(color[a])
    else:
        ans.append(color[b])

k = max(ans)
print(k)
print("\n".join(map(str, ans)))
