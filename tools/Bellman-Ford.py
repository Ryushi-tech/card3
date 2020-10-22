import sys
input = lambda: sys.stdin.readline()


def bellman_ford(E, a, v):
    dist = [float("inf")] * v
    dist[a] = 0
    for i in range(v):
        # update = False
        for s, t, d in E:
            if dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
                # update = True
                if i == v - 1 and t == v - 1:  # Negative cycle affection to goal
                    return "inf"
        # if not update:
        #     break
    return -dist[-1]


n, m = map(int, input().split())
g = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g.append([a - 1, b - 1, -c])

ans = bellman_ford(g, 0, n)
print(ans)
