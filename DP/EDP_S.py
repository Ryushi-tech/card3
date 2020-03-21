import sys
readline = sys.stdin.buffer.readline


def main():
    n = int(readline())
    m = int(readline())
    mod = 10**9 + 7
    n = str(n)
    n_len = len(n)
    dp = [[[0 for _ in range(m)] for _ in range(2)] for _ in range(n_len + 1)]
    dp[0][0][0] = 1

    for i in range(n_len):
        n_n = int(n[i])
        for j in range(2):
            for k in range(m):
                for d in range(10):
                    if j == 1 or (j == 0 and d < n_n):
                        j_n = 1
                    elif d == n_n:
                        j_n = 0
                    else:
                        continue
                    k_n = (k + d % m) % m
                    dp[i + 1][j_n][k_n] += dp[i][j][k] % mod
    print((dp[-1][0][0] + dp[-1][1][0] - 1) % mod)


if __name__ == "__main__":
    main()
