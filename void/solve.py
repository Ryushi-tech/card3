from bisect import bisect


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        # self.data = [i & -i for i in range(n + 1)]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i


n, d, a = map(int, input().split())
XH = []
for _ in range(n):
    x, h = map(int, input().split())
    XH.append((x, (h + a - 1) // a))

XH.sort(key=lambda x: x[0])
X = [y[0] for y in XH]
H = [y[1] for y in XH]

D = 2 * d
b = BIT(n)

ans = 0
for i in range(n):
    cur = b.sum(i + 1) + H[i]
    if cur > 0:
        ans += cur
        index = bisect(X, X[i] + D)
        b.add(i + 1, -cur)
        b.add(index + 1, cur)
print(ans)
