def solve():
    n, k = map(int, input().split())
    s = set(map(int, input().split()))
    t1, t2, t3 = map(int, input().split())
    act1, act2, act3 = t1, t1 + t2, t1 + 3 * t2
    inf = float("inf")
    dp = [inf] * (k + 5)
    dp[0] = 0
    for i in range(1, k + 1):
        dp[i] = min(dp[i], dp[i - 1] + act1)
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + act2)
        if i > 3:
            dp[i] = min(dp[i], dp[i - 4] + act3)
        if i in s:
            dp[i] += t3
    jump1 = (t1 + t2) // 2
    jump2 = jump1 + t2
    jump3 = jump2 + t2
    tmp1 = dp[k - 1] + jump1
    tmp2 = dp[k - 2] + jump2
    tmp3 = dp[k - 3] + jump3 if k > 2 else inf
    print(min(tmp1, tmp2, tmp3, dp[k]))

solve()
