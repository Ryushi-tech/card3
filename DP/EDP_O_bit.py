n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
mod = 10 ** 9 + 7

dp = [[0] * (1 << n) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for s in range(1 << n):
        if dp[i][s] == 0:
            continue
        for j in range(n):
            if s & 1 << j == 0 and A[i][j]:
                dp[i + 1][s | (1 << j)] += dp[i][s]
                dp[i + 1][s | (1 << j)] %= mod
print(dp[-1][-1])
