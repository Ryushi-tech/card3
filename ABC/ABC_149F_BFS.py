# ref https://qiita.com/ZhangChaoran/items/71fab0e4b8647a93d3a0
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

mod = 10**9 + 7
par = [0] * (n + 1)
order = []
stk = deque()
stk.append(1)

while stk:
    v = stk.pop()
    order.append(v)
    for x in g[v]:
        if x == par[v]:
            continue
        par[x] = v
        stk.append(x)

rev = pow(2, mod - 2, mod)
po2_inv = [1] * (n + 1)
size = [1] * (n + 1)
for i, y in enumerate(order[::-1], 1):
    p = par[y]
    size[p] += size[y]
    po2_inv[i] = po2_inv[i - 1] * rev % mod

ans = 1
for i in size[2:]:
    ans += (1 - po2_inv[i] - po2_inv[n - i] + po2_inv[n]) % mod #(1-1/2^i)(1-1/2^n-i)
ans -= po2_inv[n] + n * po2_inv[1] # -「すべての辺が含まれない、つまり空グラフの場合の誤加算」-N/2
ans %= mod
print(ans)
