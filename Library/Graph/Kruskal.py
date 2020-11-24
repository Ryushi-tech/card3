# ARC-108 C

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        xcopy = x
        while -1 < self.par[x]:
            x = self.par[x]
        while xcopy != x:
            self.par[xcopy], xcopy = x, self.par[xcopy]
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


from collections import defaultdict
n, m = map(int, input().split())
uf = UnionFind(n + 1)
g = [[] for _ in range(n + 1)]
dic = defaultdict(int)

for _ in range(m):
    x, y, c = map(int, input().split())
    if not uf.same(x, y):
        uf.unite(x, y)
        g[x].append(y)
        g[y].append(x)
        dic[(x, y)] = c

que = [(1, -1)]
par = [-1] * (n + 1)
num = [0] * (n + 1)
num[1] = 1

while que:
    x, px = que.pop()
    for v in g[x]:
        if v == px:
            continue
        edge = dic[(x, v)] if dic[(x, v)] else dic[v, x]
        if num[x] == edge:
            num[v] = edge + 1 if edge != n else 1
        else:
            num[v] = edge
        que.append((v, x))
        par[v] = x

for i in range(1, n + 1):
    print(num[i])
