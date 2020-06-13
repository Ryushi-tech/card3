# ref: https://atcoder.jp/contests/abc136/submissions/6696160
# ref: https://atcoder.jp/contests/abc136/submissions/6708692
import sys
input = sys.stdin.readline

n = int(input())
XY = sorted(list(map(int, input().split())) for _ in range(n))
X, Y = zip(*XY)
Y_rank = {z: i for i, z in enumerate(sorted(Y), 1)}

mod = 998244353


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, j):
        while i <= self.n:
            self.data[i] += j
            i += i & -i


po2 = [1]
for i in range(200200):
    po2.append(po2[-1] * 2 % mod)

b = BIT(n)

res = 0
for L, (x, y) in enumerate(XY):
    y = Y_rank[y]
    A = b.sum(y)
    B = L - A
    D = y - 1 - A
    C = n - 1 - A - B - D
    res += po2[n] - (po2[A+B] + po2[B+C] + po2[C+D] + po2[D+A]) + (po2[A] + po2[B] + po2[C] + po2[D]) - 1
    res %= mod
    b.add(y, 1)
print(res)
