from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    s = [int(x) for x in input()]
    n = len(s)
    m = int(input())
    dp = [[[0] * 5 for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(n):
        for k in range(m + 1):
            dp[i + 1][1][k + 1] += dp[i][1][k] * 9  # add 1-9
            dp[i + 1][1][k] += dp[i][1][k]  # add 0
            if s[i] > 0:
                dp[i + 1][1][k + 1] += dp[i][0][k] * (s[i] - 1)  # add lower s[i]
                dp[i + 1][1][k] += dp[i][0][k]  # add 0
                dp[i + 1][0][k + 1] += dp[i][0][k]  # add s[i]
            else:
                dp[i + 1][0][k] += dp[i][0][k]  # add s[i] = 0
        print(dp)
    print(dp[n][0][m] + dp[n][1][m])


solve()
