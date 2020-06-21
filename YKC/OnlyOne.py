from math import gcd, ceil
import itertools as it
n, l, h = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for _ in range(n + 1)]


def divc(x, y):
    return ceil(x // y)


if n == 1:
    print(divc(h, A[0]) - divc(l - 1, A[0]))
    exit()

for g in it.product([0, 1], repeat=n):
    gc = g.count(1)
    if gc == 0 or gc == 1:
        continue
    tmp = []
    for i, gg in enumerate(g):
        if gg:
            tmp.append(A[i])
    res = tmp[0]
    for j in range(1, gc):
        res = res * tmp[j] // gcd(res, tmp[j])
    G[gc].append(res)


def solve(z):
    ans = [[0] for _ in range(n + 1)]
    su = 0
    for a in A:
        su += divc(z,a)
    for i in range(1, n + 1):
        for gx in G[i]:
            ans[i][0] += divc(z, gx)
    for j, x in enumerate(ans):
        if any(j == c for c in [0, 1]):
            continue
        sign = j & 1
        su -= (-1)**sign * j * x[0]
    return su


print(solve(h) - solve(l - 1))
