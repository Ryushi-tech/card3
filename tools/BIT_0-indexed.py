class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * n

    def query(self, i):
        s = 0
        while i > 0:
            s += self.data[i - 1]
            i &= i - 1
        return s

    def update(self, i, x):
        while i < self.n:
            self.data[i] += x
            i |= i + 1
        return

    def lower_bound(self, k):
        lb = -1
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if self.query(mid) >= k:
                r = mid - 1
                lb = mid
            else:
                l = mid + 1
        return lb - 1


n, q = map(int, input().split())
c = list(map(int, input().split()))
odr_r = [[] for _ in range(n + 1)]
for i in range(q):
    l, r = map(int, input().split())
    odr_r[r].append((l - 1, i))

b = BIT(n)
diff = 0
ans = [-1] * q
last = [-1] * (n + 1)

for i, v in enumerate(c):
    if last[v] != -1:
        b.update(last[v], -1)
    else:
        diff += 1

    b.update(i, 1)
    last[v] = i

    for l, j in odr_r[i + 1]:
        ans[j] = diff - b.query(l)
print("\n".join(map(str, ans)))
