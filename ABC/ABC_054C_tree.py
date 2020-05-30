from itertools import permutations

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

lis = list(c for c in permutations(range(n), n) if c[0] == 0)

res = 0
for li in lis:
    flg = True
    for i in range(1, n):
        if li[i-1] in g[li[i]]:
            continue
        else:
            flg = False
            break
    if flg:
        res += 1
print(res)
