def nCr(s, t, mod=10 ** 9 + 7):
    assert s >= t >= 0

    def ex_euclid(x, y):
        a, b = 1, 0
        while y != 0:
            a, b = b, (a - x // y * b)
            x, y = y, x % y
        return a

    p = q = 1
    for i in range(s - t + 1, s + 1):
        p *= i
        p %= mod
    for i in range(2, t + 1):
        q *= i
        q %= mod
    p *= ex_euclid(q, mod)
    p %= mod
    return p

print(nCr(3, 2))