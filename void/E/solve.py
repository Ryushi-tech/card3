import sys
input = lambda: sys.stdin.readline()

from collections import deque, defaultdict

h, w = map(int, input().split())
C = [input() for i in range(h)]
D = defaultdict(list)
si, sj, gi, gj = 0, 0, 0, 0
for j in range(w):
    for i in range(h):
        x = C[i][j]
        if x == "S":
            si, sj = i, j
        elif x == "G":
            gi, gj = i, j
        elif x != "." and x != "#":
            D[x].append((i, j))

INF = float("inf")
dist = [[INF] * w for _ in range(h)]
dist[si][sj] = 0

que = deque()
que.append((si, sj))
seen = set()

while que:
    i, j = que.popleft()
    d = dist[i][j] + 1
    x = C[i][j]
    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if not (0 <= ni < h and 0 <= nj < w):
            continue
        if C[ni][nj] == "#":
            continue
        if d < dist[ni][nj]:
            dist[ni][nj] = d
            que.append((ni, nj))
    if x.islower():
        if x in seen:
            continue
        for vi, vj in D[x]:
            if d < dist[vi][vj]:
                dist[vi][vj] = d
                que.append((vi, vj))
        seen.add(x)

ans = dist[gi][gj]
print(ans if ans != INF else -1)
