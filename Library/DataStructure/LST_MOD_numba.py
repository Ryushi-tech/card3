import sys
import numpy as np


def solve(inp):
    def bit_length(x):
        ret = 0
        while x:
            x >>= 1
            ret += 1
        return ret

    MOD = 998244353
    SHIFT = 32
    MASK = (1 << SHIFT) - 1

    def encode(hi, lo):
        return ((hi % MOD) << SHIFT) + (lo % MOD)

    def decode(code):
        return code >> SHIFT, code & MASK

    def op(a, b):
        a1, a2 = decode(a)
        b1, b2 = decode(b)
        return encode(a1 + b1, a2 + b2)

    def mapping(x, a):
        x1, x2 = decode(x)
        a1, a2 = decode(a)
        return encode(a1 * x1 + a2 * x2, a2)

    def composition(x, y):
        x1, x2 = decode(x)
        y1, y2 = decode(y)
        return encode(x1 * y1, x1 * y2 + x2)

    e = encode(0, 0)
    _id = encode(1, 0)

    n = inp[0]
    q = inp[1]
    a = inp[2:n + 2]
    REQ0 = inp[n + 2:]
    log = bit_length(n - 1)  # n - 1: array size - 1
    size = 1 << log
    d = [e] * (2 * size)
    lz = [_id] * size

    # ----- seg tree設定 ここまで ----- #

    def update(k):
        d[k] = op(d[2 * k], d[2 * k + 1])

    def all_apply(k, f):
        d[k] = mapping(f, d[k])
        if k < size:
            lz[k] = composition(f, lz[k])

    def push(k):
        all_apply(2 * k, lz[k])
        all_apply(2 * k + 1, lz[k])
        lz[k] = _id

    def build(arr):
        assert len(arr) == n
        for j in range(n):
            d[size + j] = arr[j]
        for j in range(size - 1, 0, -1):
            update(j)

    def set(p, x):
        assert 0 <= p < n
        p += size
        for i in range(log, 0, -1):
            push(p >> i)
        d[p] = x
        for i in range(1, log + 1):
            update(p >> i)

    def get(p):
        assert 0 <= p < n
        p += size
        for i in range(1, log + 1):
            push(p >> i)
        return d[p]

    def prod(l, r):
        assert 0 <= l <= r <= n
        if l == r:
            return e
        l += size
        r += size
        for i in range(log, 0, -1):
            if ((l >> i) << i) != l:
                push(l >> i)
            if ((r >> i) << i) != r:
                push(r >> i)
        sml = smr = e
        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = op(d[r], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)

    def all_prod():
        return d[1]

    def apply(p, f):
        assert 0 <= p < n
        p += size
        for i in range(log, 0, -1):
            push(p >> i)
        d[p] = mapping(f, d[p])
        for i in range(1, log + 1):
            update(p >> i)

    def range_apply(l, r, f):
        assert 0 <= l <= r <= n
        if l == r:
            return
        l += size
        r += size
        for i in range(log, 0, -1):
            if ((l >> i) << i) != l:
                push(l >> i)
            if ((r >> i) << i) != r:
                push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, log + 1):
            if ((l >> i) << i) != l:
                update(l >> i)
            if ((r >> i) << i) != r:
                update((r - 1) >> i)

    def max_right(l, g):
        assert 0 <= l <= n
        # assert g(e)
        if l == n:
            return n
        l += size
        for i in range(log, 0, -1):
            push(l >> i)
        sm = e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(op(sm, d[l])):
                while l < size:
                    push(l)
                    l = 2 * l
                    if g(op(sm, d[l])):
                        sm = op(sm, d[l])
                        l += 1
                return l - size
            sm = op(sm, d[l])
            l += 1
            if (l & -l) == l:
                return n

    def min_left(r, g):
        assert 0 <= r <= n
        assert g(e)
        if r == 0:
            return 0
        r += size
        for i in range(log, 0, -1):
            push((r - 1) >> i)
        sm = e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(op(d[r], sm)):
                while r < size:
                    push(r)
                    r = 2 * r + 1
                    if g(op(d[r], sm)):
                        sm = op(d[r], sm)
                        r -= 1
                return r + 1 - size
            sm = op(d[r], sm)
            if (r & -r) == r:
                return 0

    A = np.zeros(n, dtype=np.int64)
    for i, tmp in enumerate(a):
        A[i] = (tmp << SHIFT) + 1

    build(A)
    REQ = list(REQ0)
    REQ.reverse()
    ans = []
    for i in range(q):
        t = REQ.pop()
        if not t:
            l = REQ.pop()
            r = REQ.pop()
            b = REQ.pop()
            c = REQ.pop()
            range_apply(l, r, encode(b, c))
        else:
            l = REQ.pop()
            r = REQ.pop()
            ans.append(prod(l, r) >> SHIFT)

    return ans


if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

from my_module import solve

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print('\n'.join(map(str, ans)))
