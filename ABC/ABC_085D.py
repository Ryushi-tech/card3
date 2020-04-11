import bisect
import math

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

ma = max(a)
b = sorted(b)
mab = bisect.bisect_left(b, ma)
sb = sum(b[mab:])


def cut_throw(ma, sb):
    res = math.ceil((m - sb) / ma)
    return res

cnt = 0
if sb <= m:
    print(cut_throw(ma, sb) + n - mab)
else:
    for x in range(n - 1, -1, -1):
        m = m - b[x]
        cnt += 1
        if m <= 0:
            print(cnt)
            exit()
