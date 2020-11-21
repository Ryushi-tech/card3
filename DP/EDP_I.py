n = int(input())
s = list(map(float, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j]:
            dp[i + 1][j] += dp[i][j] * (1 - s[i])
            dp[i + 1][j + 1] += dp[i][j] * s[i]

print(sum([dp[n][k] for k in range(n + 1) if k >= (n + 1) // 2]))
