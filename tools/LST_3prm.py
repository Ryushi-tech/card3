import sys
sread = lambda: sys.stdin.read()
inp = list(map(int, sread().split()))
from operator import xor

def bit_length(x):
    ret = 0
    while x:
        x >>= 1
        ret += 1
    return ret

def op(a, b):
    c0a, c1a, za = a
    c0b, c1b, zb = b
    return c0a + c0b, c1a + c1b, za + zb + c1a * c0b

def mapping(x, a):
    if x:
        c0, c1, z = a
        return c1, c0, c1 * c0 - z
    else:
        return a

composition = xor

e = (0, 0, 0)
_id = 0

n = inp[0]
q = inp[1]
a = inp[2:n + 2]
T = inp[n + 2::3]
L = inp[n + 3::3]
R = inp[n + 4::3]
log = bit_length(n - 1)  # n - 1: array size - 1
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

A = []
for aa in a:
    if aa:
        A.append((0, 1, 0))
    else:
        A.append((1, 0, 0))

build(A)

ans = []
for i in range(q):
    t, l, r = T[i], L[i], R[i]
    if t == 1:
        range_apply(l - 1, r, 1)
    else:
        v, w, z = prod(l - 1, r)
        ans.append(z)
print('\n'.join(map(str, ans)))
