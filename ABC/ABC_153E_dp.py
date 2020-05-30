n, m = map(int, input().split())
dmg = []
cost = []

for i in range(m):
    a, b = map(int, input().split())
    dmg.append(a)
    cost.append(b)

inf = 10**9
dp = [inf] * 30000
dp[0] = 0

for i in range(m):
    for j in range(n):
        if dp[j] != inf:
            dp[j + dmg[i]] = min(dp[j + dmg[i]], dp[j] + cost[i])
print(min(dp[n:]))
