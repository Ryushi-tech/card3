import sys
input = lambda: sys.stdin.readline()

from bisect import bisect
INF = float("inf")


class PPUF:
    def __init__(self, N):
        self.par = [-1] * (N + 1)
        self.time = [INF] * (N + 1)
        self.upd_t = [[0] for _ in range(N + 1)]
        self.upd_s = [[1] for _ in range(N + 1)]

    def find(self, x, t):
        while self.time[x] <= t:
            x = self.par[x]
        return x

    def unite(self, x, y, t):
        px = self.find(x, t)
        py = self.find(y, t)
        if px == py:
            return 0
        if self.par[px] > self.par[py]:
            px, py = py, px
        self.par[px] += self.par[py]
        self.par[py] = px
        self.time[py] = t
        self.upd_t[px].append(t)
        self.upd_s[px].append(-self.par[px])
        return 1

    def size(self, x, t=INF):
        px = self.find(x, t)
        idx = bisect(self.upd_t[px], t) - 1
        return self.upd_s[px][idx]

    def same(self, x, y, t=INF):
        return self.find(x, t) == self.find(y, t)


n, m = map(int, input().split())
uf = PPUF(n)

for i in range(m):
    a, b = map(int, input().split())
    uf.unite(a, b, i + 1)

q = int(input())
ans = []


def is_ok(k, u, v):
    cnt = uf.size(u, k)
    if not uf.same(u, v, k):
        cnt += uf.size(v, k)
    return cnt


for i in range(q):
    x, y, z = map(int, input().split())
    ng, ok = 0, m
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, x, y) >= z:
            ok = mid
        else:
            ng = mid
    ans.append(ok)
print("\n".join(map(str, ans)))
