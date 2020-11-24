import sys
input = lambda: sys.stdin.readline()


def SCC_Tarjan(g):
    n = len(g)
    order = [-1] * n  # 負なら未処理、[0,n) ならpre-order, n ならvisited
    low = [0] * n
    ord_now = 0
    parent = [-1] * n
    gp = [0] * n
    gp_num = 0
    S = []
    q = []
    for i in range(n):
        if order[i] == -1:
            q.append(i)
            while q:
                v = q.pop()
                if v >= 0:
                    if order[v] != -1: continue
                    order[v] = low[v] = ord_now
                    ord_now += 1
                    S.append(v)
                    q.append(~v)
                    for c in g[v]:
                        if order[c] == -1:
                            q.append(c)
                            parent[c] = v
                        else:
                            low[v] = min(low[v], order[c])
                else:
                    v = ~v
                    if parent[v] != -1:
                        low[parent[v]] = min(low[parent[v]], low[v])
                    if low[v] == order[v]:
                        while True:
                            w = S.pop()
                            order[w] = n
                            gp[w] = gp_num
                            if w == v: break
                        gp_num += 1

    rec = [[] for _ in range(gp_num)]
    for i in range(n):
        gp[i] = gp_num - gp[i] - 1
        rec[gp[i]].append(i)

    return gp_num, rec


n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

label, GP = SCC_Tarjan(G)

print(label)
for gp in GP:
    print(len(gp), *gp[::-1])
