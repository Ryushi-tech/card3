def main():
    n = int(input())
    s = list(map(int, input().split()))
    maxi = 10001
    dp = [False] * maxi
    dp[0] = True

    for a in s:
        for j in range(maxi - a, -1, -1):
            if dp[j]:
                dp[j + a] = True
    print(sum(dp))


if __name__ == "__main__":
    main()
