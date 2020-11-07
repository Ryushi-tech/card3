import sys
input = lambda: sys.stdin.readline()

from bisect import bisect
INF = float("inf")


class PPUF:
    def __init__(self, N):
        self.par = [i for i in range(N + 1)]
        self.sz = [1] * (N + 1)
        self.height = [1] * (N + 1)
        self.time = [INF] * (N + 1)
        self.update = [[(0, 1)] for _ in range(N + 1)]  # timing, size

    def find(self, x, t):
        while self.time[x] <= t:
            x = self.par[x]
        return x

    def unite(self, x, y, t):
        px = self.find(x, t)
        py = self.find(y, t)
        if px == py:
            return
        if self.height[py] < self.height[px]:
            self.par[py] = px
            self.time[py] = t
            self.sz[px] += self.sz[py]
            self.update[px] += [(t, self.sz[px])]
        else:
            self.par[px] = py
            self.time[px] = t
            self.sz[py] += self.sz[px]
            self.update[py] += [(t, self.sz[py])]
            self.height[py] = max(self.height[py], self.height[px] + 1)

    def size(self, x, t=INF):
        px = self.find(x, t)
        idx = bisect(self.update[px], (t, INF)) - 1
        return self.update[px][idx][1]

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
