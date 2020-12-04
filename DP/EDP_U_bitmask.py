n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
dp = [0] * (1 << n)
cost = [0] * (1 << n)

for s in range(1 << n):
    for i in range(n):
        if ~s >> i & 1:
            continue
        for j in range(i + 1, n):
            if ~s >> j & 1:
                continue
            cost[s] += a[i][j]

for s in range(1, 1 << n):
    t = s
    while t:
        dp[s] = max(dp[s], dp[s - t] + cost[t])
        t = (t - 1) & s
print(dp[-1])
