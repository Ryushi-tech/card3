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
                    if order[v] != -1:
                        continue
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
                            if w == v:
                                break
                        gp_num += 1

    for i in range(n):
        gp[i] = gp_num - gp[i] - 1

    return gp


class twosat():
    def __init__(self, n):
        self.n = n
        self.E = [[] for _ in range(n * 2)]

    def clause(self, x, f, y, g):
        self.E[x * 2 + (f ^ 1)].append(y * 2 + g)
        self.E[y * 2 + (g ^ 1)].append(x * 2 + f)

    def satisfiable(self):
        group = SCC_Tarjan(self.E)
        re = [0] * self.n
        for i in range(self.n):
            if group[2 * i] == group[2 * i + 1]:
                return (0, [])
            if group[2 * i] < group[2 * i + 1]:
                re[i] = 1
        return (1, re)


n, d = map(int, input().split())
ts = twosat(n)
G = []
for _ in range(n):
    a, b = map(int, input().split())
    G.append((a, b))

for i, (x1, y1) in enumerate(G):
    for j, (x2, y2) in enumerate(G[:i]):
        if abs(x1 - x2) < d:
            ts.clause(i, 1, j, 1)
        if abs(x1 - y2) < d:
            ts.clause(i, 1, j, 0)
        if abs(y1 - x2) < d:
            ts.clause(i, 0, j, 1)
        if abs(y1 - y2) < d:
            ts.clause(i, 0, j, 0)

flg, re = ts.satisfiable()
if not flg:
    print("No")
else:
    print("Yes")
    ans = []
    for x, r in zip(G, re):
        ans.append(x[r])
    print("\n".join(map(str, ans)))
