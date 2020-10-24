from collections import deque

H, W = map(int, input().split())
si, sj = map(int, input().split())
gi, gj = map(int, input().split())
si, sj, gi, gj = si - 1, sj - 1, gi - 1, gj - 1
C = [input() for i in range(H)]

dist = [[10 ** 9] * W for _ in range(H)]
dist[si][sj] = 0

que = deque()
que.append((si, sj))

while que:
    i, j = que.popleft()
    d = dist[i][j]
    if i == gi and j == gj:
        break
    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if d < dist[ni][nj] and C[ni][nj] == ".":
            dist[ni][nj] = d
            que.appendleft((ni, nj))
    for di in range(-2, 3):
        for dj in range(-2, 3):
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if d + 1 < dist[ni][nj] and C[ni][nj] == ".":
                dist[ni][nj] = d + 1
                que.append((ni, nj))

ans = dist[gi][gj]
print(ans if ans != 10 ** 9 else -1)
