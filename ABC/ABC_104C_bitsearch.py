import math

n, k = map(int, input().split())
pn = []
bp = []

for i in range(n):
    p, b = map(int, input().split())
    pn.append(p)
    bp.append(b)

res = 10**9

for i in range(1 << n):
    pnt = 0
    num = 0
    x = i ^ (2 ** n - 1)
    for j in range(n):
        if (i >> j) & 1 == 1:
            pnt += (j+1) * 100 * pn[j] + bp[j]
            num += pn[j]
    if pnt >= k:
        res = min(res, num)
    else:
        for l in range(n - 1, -1, -1):
            if (x >> l) & 1 == 1:
                d = min(pn[l], math.ceil((k - pnt)//100/(l + 1)))
                #print(num, pnt, d, d*100*(l+1), num+d, pnt+d*100*(l+1))
                pnt += (l+1) * 100 * d
                num += d
                break
        if pnt >= k:
            res = min(res, num)
print(res)
