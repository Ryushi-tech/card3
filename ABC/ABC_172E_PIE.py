import numpy as np

N = 10 ** 6
Nsq = 10 ** 3
mod = 10 ** 9 + 7

fac = np.arange(N, dtype=np.int64).reshape(Nsq, Nsq)
fac[0, 0] = 1
for i in range(1, Nsq):
    fac[:, i] *= fac[:, i - 1]
    fac[:, i] %= mod
for i in range(1, Nsq):
    fac[i] *= fac[i - 1, -1]
    fac[i] %= mod
fac = fac.ravel()

finv = np.arange(1, N + 1, dtype=np.int64)[::-1].reshape(Nsq, Nsq)
finv[0, 0] = pow(int(fac[N - 1]), mod - 2, mod)
for i in range(1, Nsq):
    finv[:, i] *= finv[:, i - 1]
    finv[:, i] %= mod
for i in range(1, Nsq):
    finv[i] *= finv[i - 1, -1]
    finv[i] %= mod
finv = finv.ravel()[::-1]


def nCr(a, b):
    comb = fac[a] * finv[b] % mod * finv[a - b] % mod
    return comb


def nPr(a, b):
    comb = fac[a] * finv[a - b] % mod
    return comb


n, m = map(int, input().split())

res = 0
for i in range(n + 1):
    res += nCr(n, i) * (-1) ** i * nPr(m - i, n - i)
    res %= mod
print(res * nPr(m, n) % mod)
