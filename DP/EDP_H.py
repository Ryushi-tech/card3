mod = 10 ** 9 + 7

h, w = map(int, input().split())
g = [[0] * (w + 1)]
for _ in range(h):
    g.append([0] + [int(x == ".") for x in input()])
dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
dp[1][1] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if g[i][j]:
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= mod
print(dp[h][w])
