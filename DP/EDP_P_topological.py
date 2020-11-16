import sys
input = sys.stdin.readline

mod = 10 ** 9 + 7

n = int(input())
E = [[] for _ in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)

order = []
que = [(1, -1)]
par = [-1] * (n + 1)

while que:
    x, px = que.pop()
    order.append(x)
    for v in E[x]:
        if v == px:
            continue
        que.append((v, x))
        par[v] = x

dp = [1] * (n + 1)
dq = [1] * (n + 1)
z = order[0]

while order:
    x = order.pop()
    px = par[x]
    if px == -1:
        continue
    dp[px] *= dp[x] + dq[x]
    dp[px] %= mod
    dq[px] *= dp[x]
    dq[px] %= mod

print((dp[z] + dq[z]) % mod)
