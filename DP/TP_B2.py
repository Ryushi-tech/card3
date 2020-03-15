A,B = map(int,input().split())

C = list(map(int,input().split()))
C1 = [0 for _ in range(A)]
C1[0] = sum(C)
for i in range(1,A):
    C1[i] = C1[i-1]-C[i-1]

D = list(map(int,input().split()))
D1 = [0 for _ in range(B)]
D1[0] = sum(D)
for j in range(1,B):
    D1[j] = D1[j-1]-D[j-1]
print(C1,D1, sep="\n")

dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
for i in range(A):
    dp[i][B] = sum(C[i::2])
for j in range(B):
    dp[A][j] = sum(D[j::2])
print(*dp,"",
      sep="\n")

for i in range(A-1,-1,-1):
    for j in range(B-1,-1,-1):
        dp[i][j] = C1[i]+D1[j]-min(dp[i+1][j],dp[i][j+1])
        print(*dp,"", sep="\n")
print(dp[0][0])
