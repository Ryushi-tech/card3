#  ref https://tomorinao.blogspot.com/2018/09/f-modularpowerequation.html

from math import sqrt


def phi(n):
    res = n
    for x in range(2, int(sqrt(n)) + 2):
        if n % x == 0:
            res = res // x * (x - 1)
            while n % x == 0:
                n //= x
    if n != 1:
        res = res // n * (n - 1)
    return res


def extgcd(a, b):
    x, y, nx, ny = 0, 1, 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, y, nx, ny = nx - q * x, ny - q * y, x, y
    return nx, ny


def modpow(a, b, mod=10 ** 9 + 7):
    r = 1
    a %= mod
    while b:
        if b & 1:
            r = r * a % mod
        a = a * a % mod
        b >>= 1
    return r


def solve(a, m, f=35):
    if m == 1:
        return f
    phiM = phi(m)
    x = solve(a, phiM)
    l = phiM * m
    r = modpow(a, x, l)
    while r < f:
        r += l
    return r


q = int(input())
for i in range(q):
    a, m = map(int, input().split())
    ans = solve(a, m)
    print(ans)
    # print(ans % m == a ** ans % m)
