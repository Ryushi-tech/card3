import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, mod = map(int, input().split())
E = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

dp = [0] * n
ans = [1] * n


def dfs1(v, p=-1):
    dp[v] = 1
    for to in E[v]:
        if to == p:
            continue
        dfs1(to, v)
        dp[v] *= dp[to] + 1
        dp[v] %= mod


def dfs2(v, p=-1):
    ans[v] = 1
    for to in E[v]:
        ans[v] *= dp[to] + 1
        ans[v] %= mod
    n = len(E[v])
    lft, rft = [0] * n, [0] * n
    for i in range(n):
        lft[i] = dp[E[v][i]] + 1
        rft[i] = dp[E[v][i]] + 1
    for i in range(1, n):
        lft[i] *= lft[i - 1]
        lft[i] %= mod
    for i in range(n - 2, -1, -1):
        rft[i] *= rft[i + 1]
        rft[i] %= mod
    for i in range(n):
        if E[v][i] != p:
            dp[v] = 1
            if i:
                dp[v] *= lft[i - 1]
                dp[v] %= mod
            if i + 1 < n:
                dp[v] *= rft[i + 1]
                dp[v] %= mod
            dfs2(E[v][i], v)


dfs1(0)
dfs2(0)
for i in range(n):
    print(ans[i])
