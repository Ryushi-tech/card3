class SegmentTree:
    def __init__(self, arr, op, e):
        n = len(arr)
        self.op = op
        self.e = e
        self.N = 1 << (n - 1).bit_length()
        self.d = [e] * 2 * self.N
        for i, a in enumerate(arr):
            self.d[self.N + i] = a
        for i in range(self.N - 1, 0, -1):
            self.__update(i)

    def __update(self, k):
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 ^ 1])

    def update(self, k, x):
        k += self.N
        self.d[k] = x
        while k:
            k >>= 1
            self.__update(k)

    def query(self, l, r):
        sml, smr = self.e, self.e
        l += self.N
        r += self.N
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(smr, self.d[r])
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def __search(self, k, x):
        pos = k
        while pos < self.N:
            if self.d[pos << 1] >= x:
                pos = pos << 1
            else:
                pos = pos << 1 ^ 1
        return pos - self.N

    def bs_search(self, l, r, x):
        sml, smr = -1, -1
        l += self.N
        r += self.N
        while l < r:
            if l & 1:
                if self.d[l] >= x and sml == -1:
                    sml = l
                l += 1
            if r & 1:
                r -= 1
                if self.d[r] >= x:
                    smr = r
            l >>= 1
            r >>= 1
        if sml != -1:
            return self.__search(sml, x)
        elif smr != -1:
            return self.__search(smr, x)
        else:
            return -1


import io
import os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, q = map(int, input().split())
A = list(map(int, input().split()))

st = SegmentTree(A, max, 0)
ans = []

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        st.update(a - 1, b)
    elif t == 2:
        ans.append(st.query(a - 1, b))
    elif t == 3:
        k = st.bs_search(a - 1, n, b)
        ans.append(k + 1 if k != -1 else n + 1)
print("\n".join(map(str, ans)))
