import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))

su1 = sum(lis)
su2 = sum(lis[1::2])

ans = [0] * n
ans[0] = su1 - 2 * su2

for i in range(1, n):
    ans[i] = 2 * lis[i - 1] - ans[i - 1]

print(*ans)
