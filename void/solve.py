import heapq


def dijkstra_heap(s):
    d = [float("inf")] * n
    used = [True] * n  # True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, [e[0] + d[v], e[1]])
    return d


n, w = map(int, input().split())

edge = [[] for i in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    edge[x].append([z, y])
    edge[y].append([z, x])
print(dijkstra_heap(0))
