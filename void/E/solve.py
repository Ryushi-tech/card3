import os
import io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

h, w, n, m = map(int, input().split())
g = [[0 for _ in range(w)] for _ in range(h)]
res1 = [[0 for _ in range(w)] for _ in range(h)]
res2 = [[0 for _ in range(w)] for _ in range(h)]

lights = []
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    lights.append((x, y))
    res1[x][y] = 1
    res2[x][y] = 1

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    g[x][y] = 1


def solve():
    def bfs(s, move, res):
        queue = [s]
        while queue:
            x, y = queue.pop()
            dx, dy = move
            nx, ny = x + dx, y + dy
            if not -1 < nx < h or not -1 < ny < w:
                continue
            if res[nx][ny] == 1:
                break
            if g[nx][ny] == 1:
                continue
            queue.append((nx, ny))
            res[nx][ny] = 1
        return 0

    for m in [(0, 1), (0, -1)]:
        for l in lights:
            bfs(l, m, res1)

    for m in [(1, 0), (-1, 0)]:
        for l in lights:
            bfs(l, m, res2)

    ans = 0
    for i in range(h):
        for j in range(w):
            if res1[i][j] == 1 or res2[i][j] == 1:
                ans += 1
    print(ans)


solve()
