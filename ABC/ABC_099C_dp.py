n = int(input())
inf = 10**9
dp = [inf] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    mlp6 = 6
    while i - mlp6 >= 0:
        dp[i] = min(dp[i], dp[i - mlp6] + 1)
        mlp6 *= 6
    mlp9 = 9
    while i - mlp9 >= 0:
        dp[i] = min(dp[i], dp[i - mlp9] + 1)
        mlp9 *= 9
print(dp[-1])
