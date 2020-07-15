from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    import heapq
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append((b, c))
        g[b].append((a, c))
    inf = 10**14
    dist = [inf] * n

    def dijkstra(s):
        q = []
        dist[s] = 0
        heapq.heappush(q, [0, s])
        while q:
            p, v = heapq.heappop(q)
            if dist[v] < p:
                continue
            for i, x in g[v]:
                if dist[i] > dist[v] + x:
                    dist[i] = dist[v] + x
                    heapq.heappush(q, [dist[i], i])

    m, k = map(int, input().split())
    k = k - 1
    dijkstra(k)
    for _ in range(m):
        e, f = map(int, input().split())
        res = dist[e - 1] + dist[f - 1]
        print(res)


solve()
