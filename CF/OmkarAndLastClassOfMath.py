from card3.void.stop_watch import stop_watch


def list_divs(x):
    divs = []
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            divs.append(y)
            if y != x // y:
                divs.append(x // y)
    #divs.sort()
    return divs


@stop_watch
def solve():
    from math import gcd
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnd = list_divs(n)
        ans = [10 ** 10, 0, 0]
        for i in cnd:
            a, b = i, n - i
            if b == 0:
                continue
            lcm = a * b // gcd(a, b)
            if lcm < ans[0]:
                ans = lcm, a, b
        print(*ans[1:])


solve()
