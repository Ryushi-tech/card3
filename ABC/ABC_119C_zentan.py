import itertools
n, a, b, c = map(int, input().split())
lis = []
for i in range(n):
    lis.append(int(input()))

res = 10**9

for g in itertools.product([0, 1, 2, 3], repeat=n):
    s = [[], [], [], []]
    for i, gg in enumerate(g):
        s[gg].append(lis[i])
    if not s[0] or not s[1] or not s[2]:
        continue
    else:
        x, y, z = sorted([sum(s[0]), sum(s[1]), sum(s[2])])
        l, m, n = len(s[0]), len(s[1]), len(s[2])
        pnt = abs(x-c) + abs(y-b) + abs(z-a) + 10*(l+m+n-3)
        res = min(pnt, res)
print(res)
