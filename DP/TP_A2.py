def main():
    n = int(input())
    s = list(map(int, input().split()))
    maxi = 10001
    dp = [[0] * maxi for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(maxi):
            if dp[i][j]:
                dp[i + 1][j] = 1
                dp[i + 1][j + s[i]] = 1
    print(sum(dp[-1]))


if __name__ == "__main__":
    main()
