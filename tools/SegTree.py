import sys
input = lambda: sys.stdin.readline()


def solve():
    def init(init_arr):
        global num, segfunc, ide_ele, seg
        segfunc = lambda x, y: max(x, y)
        ide_ele = 0
        num = 2 ** (n - 1).bit_length()
        seg = [ide_ele] * 2 * num
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

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    init(a)
    res = []

    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            update(a - 1, b)
        elif t == 2:
            res.append(query(a - 1, b))
        elif t == 3:
            ng = a - 1
            ok = n + 1
            while ok > ng + 1:
                mid = (ok + ng) // 2
                if query(ng, mid) >= b:
                    ok = mid
                else:
                    ng = mid
            res.append(ok)
    print("\n".join(map(str, res)))


solve()
