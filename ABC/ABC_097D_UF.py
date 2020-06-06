class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unit(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
            return
        elif self.rank[y] < self.rank[x]:
            self.par[y] = x
        else:
            self.par[y] = x
            self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
s = list(map(int, input().split()))
u = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    u.unit(a, b)

ans = 0
for i, p in enumerate(s):
    if u.same(i, p - 1):
        ans += 1
print(ans)
