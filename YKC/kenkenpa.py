n = int(input())
mod = 10 ** 9 + 7
dp = [[0] * (n + 1) for _ in range(3)]
dp[1][0] = 1

for i in range(1, n + 1):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1]) % mod
    dp[1][i] = dp[0][i-1] % mod
    dp[2][i] = dp[1][i-1] % mod

print((dp[0][n-1] + dp[1][n-1] + dp[2][n-1]) % mod)
