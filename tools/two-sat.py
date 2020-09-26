import sys

sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline()


def scc(G):
    N = len(G)
    RG = [[] for _ in range(N)]

    for i, e in enumerate(G):
        for v in e:
            RG[v].append(i)

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
    return group, GP


class twosat():
    def __init__(self, n):
        self.n = n
        self.E = [[] for _ in range(n * 2)]

    def sat(self):
        group, GP = scc(self.E)
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
            ts.E[i * 2 + (1 ^ 1)].append(j * 2 + 1)
            ts.E[j * 2 + (1 ^ 1)].append(i * 2 + 1)
        if abs(x1 - y2) < d:
            ts.E[i * 2 + (1 ^ 1)].append(j * 2 + 0)
            ts.E[j * 2 + (0 ^ 1)].append(i * 2 + 1)
        if abs(y1 - x2) < d:
            ts.E[i * 2 + (0 ^ 1)].append(j * 2 + 1)
            ts.E[j * 2 + (1 ^ 1)].append(i * 2 + 0)
        if abs(y1 - y2) < d:
            ts.E[i * 2 + (0 ^ 1)].append(j * 2 + 0)
            ts.E[j * 2 + (0 ^ 1)].append(i * 2 + 0)

flg, re = ts.sat()
if not flg:
    print("No")
else:
    print("Yes")
    ans = []
    for x, r in zip(G, re):
        ans.append(x[r])
    print("\n".join(map(str, ans)))
