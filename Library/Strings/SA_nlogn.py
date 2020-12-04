def SuffixArray(S):
    S = S + "$"
    n = len(S)
    log = n.bit_length()

    P = [] # permutation and class
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
    C0 = C

    # counting sort cyclic shifts
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

    # LCP
    rank = {i: x for x, i in enumerate(P)}
    LCP = [0] * (n - 1)
    k = 0
    for i in range(n - 1):
        z = rank[i] - 1
        j = P[z]
        while i + k < n and j + k < n and C0[i + k] == C0[j + k]:
            k += 1
        LCP[z] = k
        if k:
            k -= 1
    return P, LCP


s = input()
P, LCP = SuffixArray(s)
n = len(s)
print(n * (n + 1) // 2 - sum(LCP))