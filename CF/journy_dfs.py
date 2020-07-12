from collections import deque, defaultdict
n = int(input())
g = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append((1, 0, 1))
visited = set()
res = 0

while q:
    v, d, p = q.pop()
    visited.add(v)
    unique = 0
    for x in g[v]:
        if x not in visited:
            unique += 1
    for x in g[v]:
        if x not in visited:
            q.append((x, d + 1, p / unique))
    if unique == 0:
        res += p * d
print(res)
