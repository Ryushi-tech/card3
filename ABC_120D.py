import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
par = [i for i in range(n + 1)]
rank = [0] * (n + 1)
size = [1] * (n + 1)

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1


ans = [0] * m
ans[m - 1] = n * (n-1) // 2

b = [list(map(int, input().split())) for _ in range(m)]

for i in range(m - 1, 0, -1):
    j, k = b[i]
    if same(j, k):
        ans[i - 1] = ans[i]
    else:
        ans[i - 1] = ans[i] - (size[find(j)] * size[find(k)])
    unite(j, k)

for an in ans:
    print(an)