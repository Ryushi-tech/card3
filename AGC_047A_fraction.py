from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    from collections import defaultdict
    from fractions import Fraction
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        x = Fraction(input())
        x *= 10 ** 9
        cnt2, cnt5 = 0, 0
        while x % 5 == 0:
            x //= 5
            cnt5 += 1
        while x % 2 == 0:
            x //= 2
            cnt2 += 1
        d[(cnt2, cnt5)] += 1
    lis = list(d)
    ans_0 = 0
    ans_f = 0
    for i, (a, b) in enumerate(lis):
        k = d[(a, b)]
        if a >= 9 and b >= 9:
            ans_0 += k * (k - 1) // 2
        for x, y in lis[i + 1:]:
            l = d[(x, y)]
            if a + x >= 18 and b + y >= 18:
                ans_f += k * l
    print(ans_0 + ans_f)
    return


solve()

#for _ in range(3):
    #solve()
