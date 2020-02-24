def digit_dp(n):
    # dp[i][j][k] -> i: 現在見ている桁数
    #                j: n以下が保証されているかどうか
    #                k: 既に4か9を含んでいるかどうか
    n = list(map(int, list(str(n))))
    n_len = len(n)
    dp_table = [[[0 for k in range(2)] for j in range(2)] for i in range(n_len + 1)]
    dp_table[0][0][0] = 1

    for i in range(n_len):
        for j in range(2):
            for k in range(2):
                for d in range(0, 10 if j else n[i] + 1):
                    dp_table[i + 1][j or (d < n[i])][k or d == 4 or d == 9] += dp_table[i][j][k]

    return dp_table[-1][0][1] + dp_table[-1][1][1]


a, b = map(int, input().split())
print(digit_dp(b) - digit_dp(a - 1))
