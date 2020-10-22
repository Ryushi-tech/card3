import sys
sys.setrecursionlimit(10 ** 7)


def dfs(x, y):
    if x < 0 or h <= x or y < 0 or w <= y:
        return 0
    if graph[x][y] == "#" or seen[x][y]:
        return 0
    seen[x][y] = 1
    for k in range(4):
        dfs(x + dx[k], y + dy[k])


h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
seen = [[0 for _ in range(w)] for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sx, sy, gx, gy = 0, 0, 0, 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == "s":
            sx, sy = i, j
        elif graph[i][j] == "g":
            gx, gy = i, j

dfs(sx, sy)
print("Yes") if seen[gx][gy] else print("No")
