def SuffixArray(S):
    S = S + "$"
    n = len(S)
    log = n.bit_length()

    P = []
    C = [0] * n
    bucket = [[] for _ in range(90)]

    for i, s in enumerate(S):
        x = ord(s) - 36
        bucket[x].append(i)
    uniq = 0
    for char in bucket:
        for i in char:
            P.append(i)
            C[i] = uniq
        if char:
            uniq += 1

    for h in range(log):
        r = 1 << h
        Pn, Cn, cnt = [0] * n, [0] * n, [0] * (uniq + 1)

        for i, p in enumerate(P):
            pn = (p - r) % n
            Pn[i] = pn
            x = C[pn]
            cnt[x] += 1

        for i in range(1, uniq + 1):
            cnt[i] += cnt[i - 1]

        for pn in reversed(Pn):
            x = C[pn]
            cnt[x] -= 1
            P[cnt[x]] = pn

        uniq, prev = -1, -1
        for p in P:
            pr = (p + r) % n
            cur = (C[p] << 24) + C[pr]
            if cur != prev:
                uniq += 1
                prev = cur
            Cn[p] = uniq
        C = Cn
    return P


def bl(sa, s, t):
    n = len(t)
    l = 0
    r = len(sa) - 1
    if s[sa[0]:sa[0] + n] == t:
        return 0
    elif s[sa[r]:sa[r] + n] == t:
        while l < r - 1:
            m = (l + r) // 2
            if s[sa[m]:sa[m] + n] == t:
                r = m
            else:
                l = m
        return r
    while l < r - 1:
        m = (l + r) // 2
        mi = sa[m]
        if s[mi:(mi + n)] < t:
            l = m
        elif s[mi:(mi + n)] > t:
            r = m
        else:
            r = m
            while l < r - 1:
                m = (l + r) // 2
                if s[sa[m]:sa[m] + n] == t:
                    r = m
                else:
                    l = m
            return r
    return -1


def br(sa, s, t):
    n = len(t)
    l = 0
    r = len(sa) - 1
    if s[sa[r]:sa[r] + n] == t:
        return r
    elif s[sa[0]:sa[0] + n] == t:
        while l < r - 1:
            m = (l + r) // 2
            if s[sa[m]:sa[m] + n] == t:
                l = m
            else:
                r = m
        return l
    while l < r - 1:
        m = (l + r) // 2
        mi = sa[m]
        if s[mi:(mi + n)] < t:
            l = m
        elif s[mi:(mi + n)] > t:
            r = m
        else:
            l = m
            while l < r - 1:
                m = (l + r) // 2
                if s[sa[m]:sa[m] + n] == t:
                    l = m
                else:
                    r = m
            return l
    return -1


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


s = input()
n = len(s)
sa = SuffixArray(s)
print(sa)

def check(x):
    i0 = bl(sa, s, x)
    i1 = br(sa, s, x)
    i2 = lower_bound(sa, s, x)
    i3 = upper_bound(sa, s, x)
    return i0, i2, i1, i3, i0 == i2, i1 == i3

n = int(input())
for i in range(n):
    x, y = input().split()
    print(check(x))
    print(check(y))

