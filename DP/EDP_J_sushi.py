n = int(input())
s = list(map(int, input().split()))
C = [0] * 4
for x in s:
    C[x] += 1

n3, n2, n1 = C[3], C[3] + C[2], C[3] + C[2] + C[1]
dp = [[[0.0 for _ in range(n3 + 1)] for _ in range(n2 + 2)] for _ in range(n1 + 2)]

for c3 in range(n3 + 1):
    for c2 in range(n2 + 1):
        for c1 in range(n1 + 1):
            sm = c1 + c2 + c3
            if sm > n:
                continue
            if not sm:
                continue
            dp[c1][c2][c3] = 1.0 * n / sm
            if c1:
                dp[c1][c2][c3] += dp[c1 - 1][c2][c3] * c1 / sm
            if c2:
                dp[c1][c2][c3] += dp[c1 + 1][c2 - 1][c3] * c2 / sm
            if c3:
                dp[c1][c2][c3] += dp[c1][c2 + 1][c3 - 1] * c3 / sm

print(dp[C[1]][C[2]][C[3]])
