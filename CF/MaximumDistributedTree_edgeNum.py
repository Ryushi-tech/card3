import io
import os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
mod = 10 ** 9 + 7

q = int(input())
res = []

for _ in range(q):
    n = int(input())
    E = [[] for _ in range(n + 1)]

    for i in range(n - 1):
        x, y = map(int, input().split())
        E[x].append(y)
        E[y].append(x)

    m = int(input())
    V = sorted(map(int, input().split()))

    if m < n - 1:
        V = [1] * (n - 1 - m) + V
    else:
        X = 1
        for j in range(m - n + 1):
            X = X * V[-j - 1] % mod
        V[n - 2] = V[n - 2] * X % mod

    order = []
    que = [(1, -1)]
    par = [-1] * (n + 1)
    size = [1] * (n + 1)

    while que:
        x, px = que.pop()
        order.append(x)

        for v in E[x]:
            if v == px:
                continue
            que.append((v, x))
            par[v] = x

    products = []
    order.reverse()
    for x in order:
        px = par[x]
        if px == -1:
            continue
        products.append(size[x] * (n - size[x]))
        size[px] += size[x]

    products.sort()

    ans = 0
    for i in range(n - 1):
        ans = (ans + products[i] * V[i]) % mod
    res.append(ans)
print("\n".join(map(str, res)))
