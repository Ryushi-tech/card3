mod = (10 ** 9) + 7
lim = 1100000

fct = [0] * lim
inv_f = [0] * lim

fct[0] = 1
for i in range(1, lim):
    fct[i] = fct[i - 1] * i % mod

inv_f[lim - 1] = pow(fct[lim - 1], mod - 2, mod)

for i in range(lim - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % mod


def nCk(a, b):
    if a < b:
        return 0
    else:
        return fct[a] * inv_f[b] * inv_f[a - b] % mod


n, k = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

s_max = 0
s_min = 0

for i in range(k - 1, n):
    s_max = s_max + s[i] * nCk(i, k - 1)
    s_max %= mod

for i in range(n - k + 1):
    s_min = s_min + s[i] * nCk(n - i - 1, k - 1)
    s_min %= mod

print((s_max-s_min) % mod)
# print(s_max, s_min)
