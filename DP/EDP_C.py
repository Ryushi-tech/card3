import sys
readline = sys.stdin.buffer.readline

def main():
    n = int(readline())
    a = [list(map(int, readline().split())) for _ in range(n)]

    dp = [[0] * 3 for _ in range(n)]
    dp[0] = a[0]

    for i in range(n - 1):
        dp[i + 1][0] = a[i + 1][0] + max(dp[i][1], dp[i][2])
        dp[i + 1][1] = a[i + 1][1] + max(dp[i][2], dp[i][0])
        dp[i + 1][2] = a[i + 1][2] + max(dp[i][0], dp[i][1])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()