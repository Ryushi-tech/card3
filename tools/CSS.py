import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline()


def scc(N, G, RG):
    order = []
    used = [0] * (N + 1)
    group = [None] * (N + 1)

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)

    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * (N + 1)
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


def construct(N, G, label, group):
    G0 = [set() for _ in range(label)]
    GP = [[] for _ in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
GR = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    GR[b].append(a)

label, group = scc(n, G, GR)
G0, GP = construct(n, G, label, group)

print(label)
for gp in GP:
    print(len(gp), *gp[::-1])
