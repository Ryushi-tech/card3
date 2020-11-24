from math import gcd
n = int(input())

if n == 1:
    print(1)
    exit(0)

N = 2 * n


def list_divs(x):
    divs = []
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            divs.append(y)
            if y != x // y:
                divs.append(x // y)
    divs.sort()
    return divs


def chineserem(r1, m1, r2, m2):
    c0, c1 = m1, m2
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while c1:
        a0, a1 = a1, a0 - c0 // c1 * a1
        b0, b1 = b1, b0 - c0 // c1 * b1
        c0, c1 = c1, c0 % c1
    return (r1 * m2 * b0 + r2 * m1 * a0) % (m1 * m2)


divs = list_divs(N)

ans = float("inf")
for a in divs:
    b = N // a
    if gcd(a, b) == 1:
        tmp = chineserem(0, a, -1, b)
        ans = min(ans, tmp)
print(ans)
