l = int(input())
n = int(input())
W = sorted(list(map(int, input().split())))

dp = [-1] * (l + 1)
dp[0] = 0

for w in W:
    for i in range(l, -1, -1):
        if i + w > l:
            continue
        elif dp[i] >= 0:
            dp[i + w] = max(dp[i] + 1, dp[i + w])

print(max(dp[:l + 1]))
