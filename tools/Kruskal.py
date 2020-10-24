class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    E = [list(map(int, input().split())) for _ in range(m)]
    E.sort(key=lambda x: x[2])
    uf = UnionFind(n + 1)
    C = []
    for s, t, c in E:
        if not uf.same(s, t):
            uf.unite(s, t)
            C.append(c)
    med = (n - 1) // 2
    print(C[med])
