class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1] * (len(s) + 1)
        l = len(s)
        self.h = h = [0] * (l + 1)
        v = 0
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r - l] % self.mod) % self.mod


import sys
input = lambda: sys.stdin.readline()
from random import randint

def same(l1, r1, l2, r2):
    return rh.get(l1, r1) == rh.get(l2, r2)


def diff(l1, r1, l2, r2):
    n = r1 - l1
    ok = 0
    ng = n + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if same(l1, l1 + mid, l2, l2 + mid):
            ok = mid
        else:
            ng = mid
    return ok < n and same(l1 + ok + 1, r1, l2 + ok + 1, r2)


s, base, mod = input(), randint(3, 998244351), 10 ** 9 + 7
rh = RollingHash(s, base, mod)
q = int(input())
L, R, T = [], [], []
for _ in range(q):
    l, r, t = map(int, input().split())
    L.append(l - 1)
    R.append(r - 1)
    T.append(t)

res = []
for i in range(q):
    l, r, step = L[i], R[i], T[i]
    length = r - l + 1
    n, rem = divmod(length, step)
    ans = False
    z = l + step * n
    for u in range(min(n, 2)):
        cnt = 0
        x = l + step * u
        for t in range(n):
            y = l + step * t
            if cnt > 1:
                continue
            if same(x, x + step, y, y + step):
                cnt += 0
            elif diff(x, x + step, y, y + step):
                cnt += 1
            else:
                cnt += 2
        if same(x, x + rem, z, r + 1):
            cnt += 0
        elif diff(x, x + rem, z, r + 1):
            cnt += 1
        else:
            cnt += 2
        if cnt <= 1:
            ans = True
    x = "Yes" if ans else "No"
    res.append(x)
print("\n".join(map(str, res)))
