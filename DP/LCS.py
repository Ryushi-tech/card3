n, m = map(int,input().split())
a = input()
b = input()

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
print(dp)
