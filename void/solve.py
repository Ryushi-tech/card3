# ref http://tkori.hateblo.jp/entry/2015/12/16/180521

import numpy as np
import sys
input = sys.stdin.read

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


def alloc(x, y):
    if x < 0 or y < 0 or x * y < D + L:
        return 0
    else:
        return nCr(x * y, D) * nCr(x * y - D, L)


R, C, X, Y, D, L = map(int, input().split())

wa = (R - X + 1) * (C - Y + 1)

dla = alloc(X, Y)
dla -= alloc(X - 1, Y) * 2 + alloc(X, Y - 1) * 2
dla += alloc(X - 1, Y - 1) * 4 + alloc(X, Y - 2) + alloc(X - 2, Y)
dla -= alloc(X - 1, Y - 2) * 2 + alloc(X - 2, Y - 1) * 2
dla += alloc(X - 2, Y - 2)
dla %= mod

print(wa * dla % mod)
