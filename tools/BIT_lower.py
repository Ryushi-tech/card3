n = 200000
data = [0] * (n + 1)

def bit_add(k, x):
    while k <= n:
        data[k] += x
        k += k & -k

def bit_sum(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

def lower_bound(x):
    w, res = 0, 0
    k = 1 << (n - 1).bit_length()         # n 以下で最大の 2^n
    while k:
        if res + k <= n and w + data[res + k] <= x:
            w += data[res + k]
            res += k
        k >>= 1
    return res + 1

q = int(input())

for _ in range(q):
    x, y = map(int, input().split())
    if x == 1:
        bit_add(y, 1)
    else:
        z = lower_bound(y - 1)
        print(z)
        bit_add(z, -1)
