# verified in ABC180E

n = int(input())
nodes = []

for _ in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z))

INF = float("inf")
costs = [[INF] * n for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1, z1 = nodes[i]
        x2, y2, z2 = nodes[j]
        costs[i][j] = abs(x2 - x1) + abs(y2 - y1) + max(0, z2 - z1)
        costs[j][i] = abs(x2 - x1) + abs(y2 - y1) + max(0, z1 - z2)

dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][1] = 0

I = [1 << x for x in range(n)]

for S in range(1, 1 << n, 2):
    for i in range(n):
        if S >> i & 1 == 0:
            continue
        for j in range(n):
            print(bin(S), bin(i), bin(j))
            if S >> j & 1 == 0:
                dp[j][S ^ I[j]] = min(dp[j][S ^ I[j]], dp[i][S] + costs[i][j])

ans = INF
for i in range(n):
    ans = min(ans, dp[i][-1] + costs[i][0])
print(ans)
