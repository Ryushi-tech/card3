import sys

input = sys.stdin.readline

MOD = 998244353

# ----- seg tree設定 ----- #

e = 0
id_x = -1


def op(a, b):
    a1, a2 = a >> 32, a % (1 << 32)
    b1, b2 = b >> 32, b % (1 << 32)
    c1 = (a1 + b1) % MOD
    c2 = (a2 + b2) % MOD
    return (c1 << 32) + c2


def mapping(x, a):
    if x == -1:
        return a
    a1, a2 = a >> 32, a % (1 << 32)
    c1 = (x * a2) % MOD
    c2 = a2
    return (c1 << 32) + c2


def composition(x, y):
    if x == -1:
        return y
    return x


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
    lz[k] = id_x


def build(arr):
    assert len(arr) == n
    for j in range(n):
        d[size + j] = arr[j]
    for j in range(1, size)[::-1]:
        update(j)


def set(p, x):
    assert 0 <= p < n
    p += size
    for i in range(1, log + 1)[::-1]:
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
    for i in range(1, log + 1)[::-1]:
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
    for i in range(1, log + 1)[::-1]:
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
    for i in range(1, log + 1)[::-1]:
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
    for i in range(1, log + 1)[::-1]:
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
    for i in range(1, log + 1)[::-1]:
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


n, q = map(int, input().split())
log = (n - 1).bit_length()  # n - 1: array size - 1
size = 1 << log
d = [e] * (2 * size)
lz = [id_x] * size

A = [0] * n
tmp = 1
for i in range(n - 1, -1, -1):
    A[i] = (tmp << 32) + tmp
    tmp *= 10
    tmp %= MOD

build(A)

ans = [0] * q
for i in range(q):
    x, y, rep = map(int, input().split())
    range_apply(x - 1, y, rep)
    ans[i] = all_prod() >> 32

print('\n'.join(map(str, ans)))
