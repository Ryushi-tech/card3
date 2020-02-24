n = int(input())
s = input()

dp1 = [[0 for i in range(10)] for _ in range(n + 1)]
dp2 = [[0 for i in range(100)] for _ in range(n + 1)]
dp3 = [[0 for i in range(1000)] for _ in range(n + 1)]

for i in range(n):
    dp1[i + 1][int(s[i])] = 1
    for j in range(10):
        if dp1[i][j]:
            dp2[i + 1][j * 10 + int(s[i])] = 1
            dp1[i + 1][j] = 1
    for j in range(100):
        if dp2[i][j]:
            dp3[i + 1][j * 10 + int(s[i])] = 1
            dp2[i + 1][j] = 1
    for j in range(1000):
        if dp3[i][j]:
            dp3[i + 1][j] = 1

print(sum(dp3[n]))
#print(*dp1, sep="\n")
