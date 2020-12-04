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


def sa_is(s, upper):
    n = len(s)
    if n == 0:
        return []

    ls = [0] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if s[i] == s[i + 1] else s[i] < s[i + 1]
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if ls[i]:
            sum_l[s[i] + 1] += 1
        else:
            sum_s[s[i]] += 1
    for i in range(upper):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]

    lms_map = [-1] * (n + 1)
    lms = []
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            lms.append(i)
            m += 1

    sa = [-1] * n
    buf = sum_s.copy()
    for d in lms:
        if d == n:
            continue
        sa[buf[s[d]]] = d
        buf[s[d]] += 1
    buf = sum_l.copy()
    sa[buf[s[n - 1]]] = n - 1
    buf[s[n - 1]] += 1
    for i in range(n):
        v = sa[i]
        if v >= 1 and not ls[v - 1]:
            sa[buf[s[v - 1]]] = v - 1
            buf[s[v - 1]] += 1
    buf = sum_l.copy()
    for i in range(n)[::-1]:
        v = sa[i]
        if v >= 1 and ls[v - 1]:
            buf[s[v - 1] + 1] -= 1
            sa[buf[s[v - 1] + 1]] = v - 1
    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l = sorted_lms[i - 1]
            r = sorted_lms[i]
            end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
            end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r += 1
                if l == n or s[l] != s[r]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s, rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]

        sa = [-1] * n
        buf = sum_s.copy()
        for d in sorted_lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l.copy()
        sa[buf[s[n - 1]]] = n - 1
        buf[s[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[s[v - 1]]] = v - 1
                buf[s[v - 1]] += 1
        buf = sum_l.copy()
        for i in range(n)[::-1]:
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[s[v - 1] + 1] -= 1
                sa[buf[s[v - 1] + 1]] = v - 1
    return sa


def suffix_array(s, upper=255):
    if type(s) is str:
        s = s + "$"
        s = [ord(c) for c in s]
    return sa_is(s, upper)


def upper_bound(sa, s, t):
    l = 0
    r = len(sa)
    n = len(t)
    while r - l > 1:
        m = (l + r) // 2
        if s[sa[m]:sa[m] + n] > t:
            r = m
        else:
            l = m
    return l if s[sa[l]:sa[l] + n] == t else -1


def lower_bound(sa, s, t):
    l = 0
    r = len(sa)
    n = len(t)
    while r - l > 1:
        m = (l + r) // 2
        if s[sa[m]:sa[m] + n] < t:
            l = m
        else:
            r = m
    return r if r < len(sa) and s[sa[r]:sa[r] + n] == t else -1


import sys
input = lambda: sys.stdin.readline()

s = input().rstrip()
n = len(s)
INF = float("inf")
sa = suffix_array(s, 128)
sg0, sg1 = SegmentTree(sa, min, INF), SegmentTree(sa, max, -INF)
q = int(input())
ans = [0] * q
for i in range(q):
    x, y = input().split()
    i0, i1 = lower_bound(sa, s, x), upper_bound(sa, s, x)
    j0, j1 = lower_bound(sa, s, y), upper_bound(sa, s, y)
    if i0 == -1 or j0 == -1:
        continue
    tmp = len(y) + sg1.query(j0, j1 + 1) - sg0.query(i0, i1 + 1)
    if tmp < max(len(x), len(y)):
        continue
    else:
        ans[i] = tmp
print("\n".join(map(str, ans)))
