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
    return fct[a] * inv_f[b] * inv_f[a - b] % mod


def nPk(a, b):
    return fct[a] * inv_f[a - b] % mod