from functools import reduce

n, k = map(int, input().split())
mod = 10**9 + 7


def ncrf(i, j):
    num = reduce(lambda x, y: x * y % mod, range(i, i - j, -1))
    den = reduce(lambda x, y: x * y % mod, range(1, j + 1))
    return num * pow(den, mod - 2, mod) % mod


for d in range(1, k + 1):
    if d == 1:
        print(ncrf(n - k + 1, d))
    elif d > n - k + 1:
        print(0)
    else:
        print(ncrf(n - k + 1, d) * ncrf(k - 1, d - 1) % mod)
