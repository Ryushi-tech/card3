A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (B + 1) for i in range(A + 1)]

for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B:
            continue
        elif (i + j) % 2 == 0:
            if i == A:
                dp[i][j] = b[j] + dp[i][j + 1]
                #print("me1",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")
            elif j == B:
                dp[i][j] = a[i] + dp[i + 1][j]
                #print("me2",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")
            else:
                dp[i][j] = max(a[i] + dp[i + 1][j], b[j] + dp[i][j + 1])
                #print("me3",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")

        else:
            if i == A:
                dp[i][j] = dp[i][j + 1]
                #print("enemy1",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")
            elif j == B:
                dp[i][j] = dp[i + 1][j]
                #print("enemy2",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
                #print("enemy3",i,j,dp[0],dp[1],dp[2],dp[3],dp[4],dp[5], sep="\n")

print(dp[0][0])
