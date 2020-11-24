mod = 10 ** 9 + 7
n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]


def mod_prod(x, y):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += x[i][k] * y[k][j]
                ret[i][j] %= mod
    return ret


def bin_mod_pow(a, m):
    eye = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                eye[i][j] = 1
    while m:
        if m & 1:
            eye = mod_prod(eye, a)
        m >>= 1
        a = mod_prod(a, a)
    return eye


res = bin_mod_pow(A, k)
ans = 0
for i in range(n):
    for j in range(n):
        ans += res[i][j]
        ans %= mod
print(ans)
