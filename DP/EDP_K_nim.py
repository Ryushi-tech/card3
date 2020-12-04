n, k = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * 100010

for i in range(1, k + 1):
    for j, a in enumerate(A):
        if i - a >= 0:
            dp[i] |= 1 ^ dp[i - a]

print("First" if dp[k] else "Second")
