import sys
readline = sys.stdin.buffer.readline

def main():
    n, m = map(int, readline().split())
    inf = 10**11
    dp = [inf] * (1000 * n + 1)
    dp[0] = 0

    for i in range(n):
        w, v = map(int, input().split())
        for j in range(1000 * n - v, -1, -1):
            if dp[j] != inf:
                dp[j + v] = min(dp[j + v], dp[j] + w)
    ans = 0
    for a, b in enumerate(dp):
        if b <= m:
            ans = max(ans, a)
    print(ans)

if __name__ == "__main__":
    main()