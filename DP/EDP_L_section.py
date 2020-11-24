n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for i in range(n + 1)]

for w in range(1, n + 1):
    for l in range(n - w + 1):
        r = l + w
        dpl = a[l] - dp[l + 1][r]
        dpr = a[r - 1] - dp[l][r - 1]
        dp[l][r] = max(dpl, dpr)

print(dp[0][n])
