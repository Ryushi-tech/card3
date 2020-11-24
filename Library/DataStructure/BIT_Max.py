# query: return max value from index 1 to i
# update: x should be greater than data[i]

class BIT:
    def __init__(self, n):
        self.n = n
        self.inf = - 10 ** 11
        self.data = [self.inf] * (n + 1)
        # self.data = [i & -i for i in range(n + 1)]

    def query(self, i):
        s = self.inf
        while i > 0:
            s = max(s, self.data[i])
            i -= i & -i
        return s

    def update(self, i, x):
        while i <= self.n:
            self.data[i] = max(x, self.data[i])
            i += i & -i


n = int(input())
S = list(map(int, input().split()))
bit = BIT(n)

cnt = 0
for i, y in enumerate(S):
    bit.update(i + 1, y)
    z = bit.query(i + 1)
    cnt += 1 if y >= z else 0
print(cnt)
