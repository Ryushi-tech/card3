import sys
input = lambda: sys.stdin.readline()
sys.setrecursionlimit(10 ** 8)
from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
S = [0] + list(accumulate(A))

dp = [[None] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0


def dfs(i, j):
    if j - i == 1:
        dp[i][j] = A[i] + A[j]
        return dp[i][j]
    if dp[i][j] is not None:
        return dp[i][j]
    res = float("inf")
    for x in range(i, j):
        res = min(res, dfs(i, x) + dfs(x + 1, j) + S[j + 1] - S[i])
    dp[i][j] = res
    return res


print(dfs(0, n - 1))
