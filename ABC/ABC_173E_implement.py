from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    import sys
    input = sys.stdin.readline

    mod = 10 ** 9 + 7
    n, k = map(int, input().split())
    pos, neg = [], []
    for x in map(int, input().split()):
        if x < 0:
            neg.append(x)
        else:
            pos.append(x)

    ans = 1
    neg.sort()
    pos.sort(reverse=True)
    neg_r = neg[::-1]
    lp, ln = len(pos), len(neg)

    if not pos and k & 1:
        for i in range(k):
            ans *= neg_r[i]
            ans %= mod
        print(ans)
        exit()

    x, y = 0, 0
    for i in range(k):
        if y >= ln:
            ans *= pos[x]
            ans %= mod
            x += 1
        elif x >= lp:
            ans *= neg[y]
            ans %= mod
            y += 1
        elif pos[x] >= -neg[y]:
            ans *= pos[x]
            ans %= mod
            x += 1
        else:
            ans *= neg[y]
            ans %= mod
            y += 1

    if n == k:
        print(ans)
        exit()

    if y & 1:
        ans_r = 1
        tmp1, tmp2 = -1, -1
        if y < ln and x != 0:
            tmp1 = neg[y] * neg[y - 1]
        if x < lp and y != 0:
            tmp2 = pos[x] * pos[x - 1]
        if tmp1 > tmp2:
            for i in range(x - 1):
                ans_r *= pos[i]
                ans_r %= mod
            for i in range(y + 1):
                ans_r *= neg[i]
                ans_r %= mod
        elif tmp1 <= tmp2:
            for i in range(x + 1):
                ans_r *= pos[i]
                ans_r %= mod
            for i in range(y - 1):
                ans_r *= neg[i]
                ans_r %= mod
        print(ans_r)
    else:
        print(ans % mod)


solve()
