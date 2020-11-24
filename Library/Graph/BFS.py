from collections import deque


def bfs(k, l):
    queue = deque([[k, l]])
    visit[k][l] = 0
    while queue:
        x, y = queue.popleft()
        if [x, y] == [gx, gy]:
            return visit[x][y]
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if not -1 < nx < h or not -1 < ny < w:
                continue
            if graph[nx][ny] == "." and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx, ny])
    return -1


h, w = 411, 411
ofs = h // 2
sx, sy = 0, 0
n, gx, gy = map(int, input().split())
sx, sy, gx, gy = sx + ofs, sy + ofs, gx + ofs, gy + ofs
graph = [["."] * w for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a + ofs, b + ofs
    graph[a][b] = "#"

visit = [[-1 for _ in range(w)] for _ in range(h)]
move = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]

res = bfs(sx, sy)
print(res)
