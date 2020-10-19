class SegmentTree:
    def __init__(self, init_arr, segfunc, ide_ele):
        n = len(init_arr)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.range = [(-1, n)] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_arr[i]
            self.range[self.num + i] = (i, i)
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
            self.range[i] = (self.range[2 * i][0], self.range[2 * i + 1][1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def binsearch(self, l, r, x):
        l += self.num
        r += self.num
        Lmin = -1
        Rmin = -1
        while l < r:
            if l & 1:
                if self.tree[l] >= x and Lmin == -1:
                    Lmin = l
                l += 1
            if r & 1:
                if self.tree[r - 1] >= x:
                    Rmin = r - 1
            l >>= 1
            r >>= 1

        if Lmin != -1:
            pos = Lmin
            while pos < self.num:
                if self.tree[2 * pos] >= x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos + 1
            return pos - self.num
        elif Rmin != -1:
            pos = Rmin
            while pos < self.num:
                if self.tree[2 * pos] >= x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos + 1
            return pos - self.num
        else:
            return -1


import sys
input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))

seg_f = lambda x, y: max(x, y)
ide_ele = 0

Seg = SegmentTree(A, seg_f, ide_ele)
ans = []

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        Seg.update(a - 1, b)
    elif t == 2:
        ans.append(Seg.query(a - 1, b))
    elif t == 3:
        k = Seg.binsearch(a - 1, n, b)
        ans.append(n + 1 if k == -1 else k + 1)
print("\n".join(map(str, ans)))
