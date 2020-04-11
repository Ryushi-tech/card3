import sys

readline = sys.stdin.buffer.readline

n, m = map(int, readline().split())

es = []
for _ in range(m):
    a, b = map(int, readline().split())
    es.append((a, b))


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
    if x == y:
        return 0
    par[x] = y


ans = 0
for i in range(m):
    par = [_ for _ in range(n + 1)]
    for j, k in enumerate(es):
        if i == j:
            continue
        a, b = k
        unite(a, b)
    a, b = es[i]
    if not same(a, b):
        ans += 1
print(ans)
