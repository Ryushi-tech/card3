s = input()
mod = 13
p = 10 ** 9 + 7
dp = [0] * mod
dp[0] = 1

for i, ss in enumerate(s):
    tmp = [0] * mod
    if ss == "?":
        for j in range(10):
            for k in range(mod):
                d = (10 * k + j) % mod
                tmp[d] += dp[k]
                tmp[d] %= p
    else:
        for k in range(mod):
            d = (10 * k + int(ss)) % mod
            tmp[d] += dp[k]
    dp = tmp
print(dp[5])
