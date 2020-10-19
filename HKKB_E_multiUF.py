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


mod = 10 ** 9 + 7
h, w = map(int, input().split())
g = [[x for x in input()] for _ in range(h)]

k = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == ".":
            g[i][j] = 1
            k += 1
        else:
            g[i][j] = 0

ufh = [[] for _ in range(h)]
for i in range(h):
    ufh[i] = UnionFind(w)

ufw = [[] for _ in range(w)]
for i in range(w):
    ufw[i] = UnionFind(h)

p = [1] + [0] * k
for i in range(1, k + 1):
    p[i] = p[i - 1] * 2 % mod

for i in range(h):
    for j in range(w):
        if not g[i][j]:
            continue
        if i < h - 1 and g[i + 1][j]:
            ufw[j].unite(i, i + 1)
        if j < w - 1 and g[i][j + 1]:
            ufh[i].unite(j, j + 1)


t = k * p[k] % mod
for i in range(h):
    for j in range(w):
        if g[i][j]:
            t -= p[k - ufh[i].size(j) - ufw[j].size(i) + 1]
            t %= mod

print(t)
