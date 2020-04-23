from collections import deque

def bfs(sx, sy):
    queue = deque([[sx, sy]])
    visit[sx][sy] = 0
    while queue:
        x, y = queue.popleft()
        if [x, y] == [gx, gy]:
            return visit[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or h <= nx or ny < 0 or w <= ny or graph[nx][ny] == "#":
                continue
            elif graph[nx][ny] == "." and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx, ny])

h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
visit = [[-1 for _ in range(w)] for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sx, sy = 0, 0
gx, gy = h-1, w-1

cnt = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == "#":
            cnt += 1

bfs(sx, sy)
path = visit[gx][gy] + 1
if visit[gx][gy] == -1:
    print(-1)
else:
    print(h * w - path - cnt)
