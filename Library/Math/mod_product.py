n = 5
k = 5
mod = 998244353

# A = list(map(int, input().split()))
A = [1, 2, 3, 4, 5]
S = [n] + [0] * k
acc = [1] * n

for i in range(1, k + 1):
    cur = [1] * n
    for j in range(n):
        cur[j] = acc[j] * A[j] % mod
        S[i] += cur[j]
        S[i] %= mod
    print(S, acc, cur)
    acc = cur
