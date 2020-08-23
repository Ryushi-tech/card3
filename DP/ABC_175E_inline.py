import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
v = [[0 for _ in range(c)] for _ in range(r)]

for i in range(k):
    rr, cc, vv = map(int, input().split())
    rr, cc = rr - 1, cc - 1
    v[rr][cc] = vv

dp = [[0 for _ in range(c + 1)] for _ in range(4)]
for y in range(r):
    tmp = [[0 for _ in range(c + 1)] for _ in range(4)]
    for x in range(c):
        for i in range(2, -1, -1):
            dp[i + 1][x] = max(dp[i + 1][x], dp[i][x] + v[y][x])
        for i in range(4):
            tmp[0][x] = max(tmp[0][x], dp[i][x])
            dp[i][x + 1] = max(dp[i][x + 1], dp[i][x])
            print(*dp, sep="\n")
            print("")
    dp = tmp
    print("turn end")
print(dp[0][c - 1])

"""
2 5 5
1 1 3
2 4 20
1 2 1
1 3 4
1 4 2
"""