from collections import deque


def bfs(sx, sy):
    queue = deque([[sx, sy]])
    visit[sx][sy] = 0
    while queue:
        x, y = queue.popleft()
        if [x, y] == [gx, gy]:
            return visit[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if graph[nx][ny] == "." and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx, ny])


h, w = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
graph = [list(input()) for _ in range(h)]

sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1

visit = [[-1 for _ in range(w)] for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(bfs(sx, sy))
