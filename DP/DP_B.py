def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    inf = 10 ** 8
    dp = [inf] * n
    dp[0] = 0

    for j in range(1, n):
        buf = [dp[i] + abs(s[j]-s[i]) for i in range(max(0, j - k), j)]
        dp[j] = min(buf)
    print(dp[-1])

if __name__ == "__main__":
    main()
