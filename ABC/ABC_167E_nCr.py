lim = 200001
n, m, k = map(int, input().split())
p = 998244353

fa = [1] * (lim + 1)
fa_inv = [1] * (lim + 1)

for i in range(lim):
    fa[i+1] = fa[i] * (i+1) % p

fa_inv[-1] = pow(fa[-1], p - 2, p)
for i in range(lim - 1, 0, -1):
    fa_inv[i] = fa_inv[i+1] * (i+1) % p


def ncr(a, b):
    if a < b:
        return 0
    else:
        return fa[a] * fa_inv[b] % p * fa_inv[a - b] % p


prt = [1] * (n + 1)
for i in range(n):
    prt[i+1] = prt[i] * (m - 1) % p

res = 0
for i in range(k + 1):
    res += m * prt[n - i - 1] * ncr(n - 1, i) % p
    res %= p
print(res)
