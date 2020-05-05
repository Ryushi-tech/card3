n = int(input())
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

lis = list(map(int, input().split()))
res = n * (n + 1) // 2
for i, j in enumerate(lis):
    bit_add(j, 1)
    res -= bit_sum(j)
print(res)
