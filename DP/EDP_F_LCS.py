a = input()
b = input()
n, m = len(a), len(b)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

c, d = n, m
ans = ""
while c > 0 and d > 0:
    if dp[c - 1][d] == dp[c][d]:
        c -= 1
    elif dp[c][d - 1] == dp[c][d]:
        d -= 1
    else:
        ans = a[c - 1] + ans
        c -= 1
        d -= 1
print(ans)
