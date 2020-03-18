n, m = map(int, input().split())
inf = 10**8
dp = [-inf] * (m + 1)
dp[0] = 0

for i in range(n):
    w, v = map(int, input().split())
    for j in range(m - w, -1, -1):
        if dp[j] != -inf:
            dp[j + w] = max(dp[j + w], dp[j] + v)
print(max(dp))
