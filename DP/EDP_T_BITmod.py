class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            s %= mod
            i -= i & -i
        return s

    def update(self, i, x):
        while i <= self.n:
            self.data[i] += x
            self.data[i] %= mod
            i += i & -i


mod = 10 ** 9 + 7
n = int(input())
s = [x for x in input()]
dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(n - 1)]

for i in range(n - 1):
    bit = BIT(n)
    for j in range(1, n + 1):
        bit.update(j, dp[i][j])
    for j in range(1, n - i):
        if s[i] == "<":
            dp[i + 1][j] = bit.query(j)
        else:
            dp[i + 1][j] = bit.query(n) - bit.query(j)
            dp[i + 1][j] %= mod
print(dp[n - 1][1])
