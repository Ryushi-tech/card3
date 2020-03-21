mod = 10**9+7
K = input()
D = int(input())
dp = [0] * D
s = 0
for i in range(len(K)):
    ndp = [0] * D
    for j in range(D):
        for d in range(10):
            ndp[(j+d) % D] = (ndp[(j+d) % D] + dp[j]) % mod
    for d in range(int(K[i])):
        ndp[(s+d) % D] += 1
    dp = ndp
    s = (s + int(K[i])) % D
print((dp[0] - 1 + (s == 0)) % mod)
