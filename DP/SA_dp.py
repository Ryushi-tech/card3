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
        # s = s + "$"
        s = [ord(c) for c in s]
    return sa_is(s, upper)


def solve():
    k = int(input())
    s = input()
    n = len(s)
    l = (n + k) // (k + 1)
    sa = suffix_array(s, 128)
    pos = {i: x for x, i in enumerate(sa)}
    low = 0
    high = n - 1
    while high - low > 0:
        mid = (high + low) // 2
        dp = [k + 2] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if i + l <= n and pos[i] <= mid:
                dp[i + l] = min(dp[i + l], dp[i] + 1)
            if i + l - 1 <= n:
                dp[i + l - 1] = min(dp[i + l - 1], dp[i] + 1)
        if dp[n] <= k + 1:
            high = mid
        else:
            low = mid + 1
    return s[sa[low]:sa[low] + l]


print(solve())
