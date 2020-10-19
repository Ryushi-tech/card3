q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    dp = [0] * (n + 1)
    bricks = list(reversed(arr))
    tmp = [0] * (n + 1)
    for i in range(1, len(arr) + 1):
        print(bricks)
        print(dp)
        print(tmp)
        tmp[i] = tmp[i - 1] + bricks[i - 1]
        if i <= 3:
            dp[i] = sum(bricks[:i])
        else:
            a = bricks[i - 1] - dp[i - 1] + tmp[i - 1]
            b = sum(bricks[i - 2:i]) - dp[i - 2] + tmp[i - 2]
            c = sum(bricks[i - 3:i]) - dp[i - 3] + tmp[i - 3]
            dp[i] = max(a, b, c)
            print(a, b, c)
    print(dp[n])
