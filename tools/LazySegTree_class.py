import sys
input = lambda: sys.stdin.readline()
from operator import xor


class LazySegmentTree:
    def __init__(self, arr, op, e, map_f, cmp_f, _id):
        self.op = op
        self.e = e
        self.map_f = map_f
        self.cmp_f = cmp_f
        self._id = _id
        self.log = len(arr).bit_length()
        self.N = 1 << self.log
        self.d = [e for _ in range(2 * self.N)]
        self.lz = [_id for _ in range(self.N)]
        for i, a in enumerate(arr):
            self.d[i + self.N] = a
        for i in range(self.N - 1, 0, -1):
            self.__update(i)

    def set(self, p, x):
        p += self.N
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.__update(p >> i)

    def __getitem__(self, p):
        p += self.N
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        if l == r:
            return self.e
        l += self.N
        r += self.N
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)
        sml = self.e
        smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def apply(self, l, r, f):
        if l == r:
            return
        l += self.N
        r += self.N
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self.__all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r - 1) >> i)

    def __update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __all_apply(self, k, f):
        self.d[k] = self.map_f(f, self.d[k])
        if k < self.N:
            self.lz[k] = self.cmp_f(f, self.lz[k])

    def __push(self, k):
        self.__all_apply(2 * k, self.lz[k])
        self.__all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self._id


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

n, q = map(int, input().split())
a = list(map(int, input().split()))

A = []
for aa in a:
    if aa:
        A.append((0, 1, 0))
    else:
        A.append((1, 0, 0))

lst = LazySegmentTree(A, op, e, mapping, composition, _id)

ans = []
for i in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        lst.apply(l - 1, r, 1)
    else:
        v, w, z = lst.prod(l - 1, r)
        ans.append(z)
print('\n'.join(map(str, ans)))
