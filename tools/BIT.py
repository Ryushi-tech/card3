# n: クエリ処理する列のサイズ
n = 10
data = [0] * (n + 1)


def add(k, x):
    while k <= n:
        data[k] += x
        k += k & -k


def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s


# 二分探索
n0 = 2 ** (n - 1).bit_length()


def lower_bound(x):
    w = i = 0
    k = n0
    while k:
        if i + k <= n and w + data[i + k] <= x:
            w += data[i + k]
            i += k
        k >>= 1
    return i + 1

res=[]
for i in range(n):
    res.append(get(i))
print(res)