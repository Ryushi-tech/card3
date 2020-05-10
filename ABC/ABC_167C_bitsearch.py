n, m, x = map(int, input().split())
C = []
M = []

for _ in range(n):
    c, *mi = map(int, input().split())
    C.append(c)
    M.append(mi)

res = 10**10

for i in range(1 << n):
    tmp = 0
    cnt = [0] * m
    for j in range(n):
        if (i >> j) & 1 == 1:
            tmp += C[j]
            for k in range(m):
                cnt[k] += M[j][k]
    if min(cnt) >= x:
        res = min(res, tmp)

if res == 10**10:
    print(-1)
else:
    print(res)
