from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    from collections import deque
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append((b, c))
        g[b].append((a, c))
    dist = [0] * n

    def dfs(v, p=-1, d=0):
        q = deque()
        q.append((v, p, d))
        while q:
            v, p, d = q.pop()
            dist[v] = d
            for i, x in g[v]:
                if i == p:
                    continue
                q.append((i, v, d + x))

    m, k = map(int, input().split())
    k = k - 1
    dfs(k)
    for _ in range(m):
        e, f = map(int, input().split())
        res = dist[e - 1] + dist[f - 1]
        print(res)


solve()
