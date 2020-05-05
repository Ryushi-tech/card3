import sys

sys.setrecursionlimit(10 ** 7)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
mod = 10 ** 9 + 7

dp = [-1] * (1 << n)
dp[0] = 1


def dfs(bit, i):
    if dp[bit] != -1:
        return dp[bit]
    else:
        tmp = 0
        for j in range(n):
            if bit & (1 << j) and a[i][j]:
                tmp += dfs(bit ^ (1 << j), i + 1)
    dp[bit] = tmp % mod
    return dp[bit]


print(dfs(2 ** n - 1, 0))
