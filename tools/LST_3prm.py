import sys
input = lambda: sys.stdin.readline()

po18 = pow(2, 18)
po36 = pow(2, 36)


def bit_length(x):
    ret = 0
    while x:
        x >>= 1
        ret += 1
    return ret

def encode(a, b, c):
    return a * po18 + b + c * po36

def decode(codec):
    return (codec // po18) % po18, codec % po18, codec // po36

def op(a, b):
    c0a, c1a, za = decode(a)
    c0b, c1b, zb = decode(b)
    return encode(c0a + c0b, c1a + c1b, za + zb + c1a * c0b)

def mapping(x, a):
    if x == 1:
        c0, c1, z = decode(a)
        return encode(c1, c0, c1 * c0 - z)
    else:
        return a

def composition(x, y):
    return x ^ y

e = 0
_id = 0

n, q = map(int, input().split())
a = list(map(int, input().split()))
log = bit_length(n - 1)
size = 1 << log
d = [e] * (2 * size)
lz = [_id] * size

# ----- end of setting ----- #

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
    # assert len(arr) == n
    for j in range(n):
        d[size + j] = arr[j]
    for j in range(size - 1, 0, -1):
        update(j)

def set(p, x):
    # assert 0 <= p < n
    p += size
    for i in range(log, 0, -1):
        push(p >> i)
    d[p] = x
    for i in range(1, log + 1):
        update(p >> i)

def get(p):
    # assert 0 <= p < n
    p += size
    for i in range(1, log + 1):
        push(p >> i)
    return d[p]

def prod(l, r):
    # assert 0 <= l <= r <= n
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
    # assert 0 <= p < n
    p += size
    for i in range(log, 0, -1):
        push(p >> i)
    d[p] = mapping(f, d[p])
    for i in range(1, log + 1):
        update(p >> i)

def range_apply(l, r, f):
    # assert 0 <= l <= r <= n
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
    # assert 0 <= l <= n
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
    # assert 0 <= r <= n
    # assert g(e)
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

A = [0] * n
for i, aa in enumerate(a):
    if aa:
        A[i] = encode(0, 1, 0)
    else:
        A[i] = encode(1, 0, 0)

build(A)

ans = []
for i in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        range_apply(l - 1, r, True)
    else:
        v, w, z = decode(prod(l - 1, r))
        ans.append(z)
print('\n'.join(map(str, ans)))
