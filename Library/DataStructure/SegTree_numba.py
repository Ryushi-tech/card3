import sys
import numpy as np


def solve(inp):
    def bit_length(x):
        ret = 0
        while x:
            x >>= 1
            ret += 1
        return ret

    n = 300001
    ide_ele = 0
    num = 1 << bit_length(n)
    seg = [ide_ele] * 2 * num

    def segfunc(x, y):
        return max(x, y)

    def init(init_arr):
        for i in range(n):
            seg[i + num - 1] = init_arr[i]
        for i in range(num - 2, -1, -1):
            seg[i] = segfunc(seg[2 * i + 1], seg[2 * i + 2])

    def update(k, x):
        k += num - 1
        seg[k] = x
        while k:
            k = (k - 1) // 2
            seg[k] = segfunc(seg[k * 2 + 1], seg[k * 2 + 2])

    def query(p, q):
        if q <= p:
            return ide_ele
        p += num - 1
        q += num - 2
        res = ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = segfunc(res, seg[p])
            if q & 1 == 1:
                res = segfunc(res, seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = segfunc(res, seg[p])
        else:
            res = segfunc(segfunc(res, seg[p]), seg[q])
        return res

    N = inp[0]
    d = inp[1]
    A = inp[2:]
    arr = np.zeros(n, dtype=np.int64)
    init(arr)

    for a in A:
        l = max(0, a - d)
        r = min(a + d + 1, n)
        v = query(l, r)
        update(a, v + 1)
    return query(0, n)


if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

from my_module import solve

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print(ans)
