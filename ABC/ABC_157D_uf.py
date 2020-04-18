n, m, k = map(int, input().split())
par = [i for i in range(n)]
rank = [1] * n
fr = [[] for i in range(n)]
br = [[] for i in range(n)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] < rank[y]:
        rank[y] += rank[x]
        par[x] = y
    else:
        rank[x] += rank[y]
        par[y] = x

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    unite(a, b)
    fr[a].append(b)
    fr[b].append(a)

for i in range(k):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    br[a].append(b)
    br[b].append(a)

res = []
for i in range(n):
    cnt = 0
    if br[i]:
        for b in br[i]:
            if same(i, find(b)):
                cnt += 1
        res.append(rank[find(i)] - len(fr[i]) - cnt - 1)
    else:
        res.append(rank[find(i)] - len(fr[i]) - 1)
print(*res, sep=" ")