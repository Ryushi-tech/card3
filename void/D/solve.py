x, y, z = map(int, input().split())

dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for c1 in range(100, -1, -1):
    for c2 in range(100, -1, -1):
        for c3 in range(100, -1, -1):
            if c1 == 100 or c2 == 100 or c3 == 100:
                continue
            sm = c1 + c2 + c3
            if not sm:
                continue
            tmp = 0
            tmp += (dp[c1 + 1][c2][c3] + 1) * c1 / sm
            tmp += (dp[c1][c2 + 1][c3] + 1) * c2 / sm
            tmp += (dp[c1][c2][c3 + 1] + 1) * c3 / sm
            dp[c1][c2][c3] += tmp
print("{:.9f}".format(dp[x][y][z]))
