from collections import deque

def bfs(sx, sy, maze):
    INF = 100000000
    visit = [[-INF for i in range(w + 2)] for j in range(h + 2)]
    queue = deque([])
    queue.append([sx, sy])
    visit[sx][sy] = 0
    res = 0
    while queue:
        x, y = queue.popleft()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if maze[nx][ny] != '#' and visit[nx][ny] == -INF:
                queue.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1
                res = max(res, visit[nx][ny])
    return res


h, w = map(int, input().split())
maze = [list("#" * (w + 2))]
for _ in range(h):
    maze.append(["#"] + list(input()) + ["#"])
maze += [list("#" * (w + 2))]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
for i in range(h + 2):
    for j in range(w + 2):
        if maze[i][j] == ".":
            ans = max(ans, bfs(i, j, maze))
print(ans)
