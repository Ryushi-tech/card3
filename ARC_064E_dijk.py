#https://juppy.hatenablog.com/entry/2019/02/20/ARC64_-E_Cosmic_Rays-_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder

from math import hypot
def dijkstra(s):
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True

        for j in range(n):
            d[j] = min(d[j], d[v] + cost[v][j])
    return d


sx, sy, gx, gy = map(int,input().split())
n = int(input())
edge = [(sx, sy, 0)]

for i in range(n):
    x, y, r = map(int,input().split())
    edge.append((x,y,r))
edge.append((gx, gy, 0))

cost = [[0] * (n + 2) for _ in range(n + 2)]
for j, (k1, k2, k3) in enumerate(edge):
    for l, (m1, m2, m3) in enumerate(edge):
        if j == l:
            continue
        else:
            cost[j][l] = max(hypot(k1 - m1, k2 - m2) - k3 - m3, 0)
n += 2

res = dijkstra(0)
print(res[-1])
