
mod = 10 ** 9 + 7


def nCr(a, b):
    p = q = 1
    for i in range(a - b + 1, a + 1):
        p *= i
        p %= mod
    for i in range(2, b + 1):
        q *= i
        q %= mod
    return p * pow(q, mod - 2, mod) % mod


n, x, y = 2, 3, 4

ans = pow(2, n, mod) - nCr(n, x) - nCr(n, y) - 1
ans %= mod
print(ans)
