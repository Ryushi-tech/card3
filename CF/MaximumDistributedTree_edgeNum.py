import io
import os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
MOD = 10 ** 9 + 7

res = []
q = int(input())
for _ in range(q):
    n = int(input())
    adj_lis = [[] for i in range(n)]
    adj_cnt = [0] * n
    adj_cnt[0] = 1
    par = [-1] * n
    des_cnt = [1] * n
    leaf_q = []
    edgeNum = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj_lis[u - 1].append(v - 1)
        adj_lis[v - 1].append(u - 1)
        adj_cnt[u - 1] += 1
        adj_cnt[v - 1] += 1

    tree_q = [(0, -1)]
    while tree_q:
        v, par_v = tree_q.pop()
        par[v] = par_v
        for x in adj_lis[v]:
            if x != par_v:
                tree_q.append((x, v))
        if adj_cnt[v] == 1:
            leaf_q.append(v)

    while leaf_q:
        x = leaf_q.pop()
        if x == 0:
            continue
        edgeNum.append(des_cnt[x] * (n - des_cnt[x]))
        des_cnt[par[x]] += des_cnt[x]
        adj_cnt[par[x]] -= 1
        if adj_cnt[par[x]] == 1:
            leaf_q.append(par[x])
    edgeNum.sort()
    m = int(input())
    edgeWeight = []
    primeList = list(map(int, input().split()))
    primeList.sort()

    if n - 1 < m:
        for i in range(n - 1):
            edgeWeight.append(primeList[i])
        for i in range(n - 1, m):
            edgeWeight[n - 2] *= primeList[i]
            edgeWeight[n - 2] %= MOD
    else:
        for i in range(n - 1 - m):
            edgeWeight.append(1)
        for i in range(m):
            edgeWeight.append(primeList[i])

    ans = 0
    for i in range(n - 1):
        ans += edgeNum[i] * edgeWeight[i]
        ans %= MOD
    res.append(ans)
print("\n".join(map(str, res)))
