from functools import reduce

m, n = map(int, input().split())
mod = 10 ** 9 + 7


def ncr(p, k):
    if k == 0:
        return 1
    elif k < 0:
        return 0
    else:
        num = reduce(lambda x, y: x * y % mod, range(p, p - k, -1))
        den = reduce(lambda x, y: x * y % mod, range(1, k + 1))
        return num * pow(den, mod - 2, mod) % mod


if (m + n) % 3 != 0:
    print(0)
else:
    p = (m + n) // 3
    k = m - p
    print(ncr(p, k))
