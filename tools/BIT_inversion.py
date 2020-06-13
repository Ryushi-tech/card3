# Index starts at 1
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

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i


N = int(input())
S = list(map(int, input().split()))
b = BIT(N)

res = 0
for j, y in enumerate(S, 1):
    b.add(j, y)
    if j == 1:
        continue
    if b.sum(j - 1) * b.sum(j) >= 0:
        c = -1 if b.sum(j) > 0 else 1
        x = c - b.sum(j)
        b.add(j, x)
        res += abs(x)
print(res)
