def zeta_inv(L0): # 上から累積和
    L = L0[:]
    n = len(L) - 1
    xx = [1] * (n + 1)
    xx[0] = xx[1] = 0
    for i in range(n):
        if not xx[i]: continue
        for j in range(1, n//i + 1)[::-1]:
            xx[i*j] = 0
            L[j] += L[i*j]
    return L


def mobius_inv(L0): # zeta_inv の逆変換
    L = L0[:]
    n = len(L) - 1
    xx = [1] * (n + 1)
    xx[0] = xx[1] = 0
    for i in range(n):
        if not xx[i]: continue
        for j in range(1, n//i + 1):
            xx[i*j] = 0
            L[j] -= L[i*j]
    return L


P = 998244353
N = int(input())
A = [int(a) for a in input().split()]
X = [0] * 1000001
for a in A:
    X[a] += a
X = mobius_inv([a * a for a in zeta_inv(X)])
ans = sum(A) ** 2 - sum(A)
for g, x in enumerate(X):
    if x: ans -= (1 - pow(g, P - 2, P)) * x
print(ans * (P + 1 >> 1) % P)
