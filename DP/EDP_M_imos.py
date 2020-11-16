def acc(arr):
    res = [0]
    for ar in arr:
        res.append((res[-1] + ar) % mod)
    return res[1:]


n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
mod = 10 ** 9 + 7
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n + 1):
    tmp = [0] * (k + 1)
    for j in range(k + 1):
        tmp[j] += dp[j]
        tmp[j] %= mod
        if j + s[i] + 1 <= k:
            tmp[j + s[i] + 1] -= dp[j]
            tmp[j + s[i] + 1] %= mod
    tmp = acc(tmp)
    dp = tmp
print(dp[k])
