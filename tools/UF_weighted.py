import sys
input = lambda: sys.stdin.readline()


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.weight = [0] * (n + 1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def unite(self, x, y, w):
        px = self.find(x)
        py = self.find(y)
        w += self.weight[x] - self.weight[y]
        if px == py:
            return 0
        if self.par[px] >= self.par[py]:
            px, py = py, px
            w = -w
        self.par[px] += self.par[py]
        self.par[py] = px
        self.weight[py] = w

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[y] - self.weight[x]


n, m = map(int, input().split())
wuf = WeightedUnionFind(n)
for _ in range(m):
    l, r, d = map(int, input().split())
    if wuf.same(l, r) and wuf.diff(l, r) != d:
        print('No')
        exit()
    wuf.unite(l, r, d)
print('Yes')
