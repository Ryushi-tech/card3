import sys

input = sys.stdin.readline

n, mod = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

par = [-1] * n
que = [0]
order = []
while que:
    i = que.pop()
    order.append(i)
    for a in G[i]:
        if a != par[i]:
            par[a] = i
            que.append(a)

acu = [1] * n
ans = [0] * n
ltor = [1] * n
for i in order[1:][::-1]:
    ans[i] = acu[i] + 1
    p = par[i]
    acu[p] *= ans[i]
    acu[p] %= mod
ans[order[0]] = acu[order[0]]

for i in order:
    tmp = ltor[i]
    for j in G[i]:
        if j == par[i]:
            continue
        ltor[j] = tmp
        tmp *= ans[j]
        tmp %= mod
    tmp = 1
    for j in G[i][::-1]:
        if j == par[i]:
            continue
        ltor[j] = ltor[j] * tmp % mod + 1
        tmp = tmp * ans[j] % mod
        ans[j] = acu[j] * ltor[j] % mod

print("\n".join(map(str, ans)))
