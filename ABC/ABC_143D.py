import bisect

n = int(input())
lis = list(map(int,input().split()))
lis.sort()

d = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        b = bisect.bisect_left(lis, int(lis[i] + lis[j]))
        d += b - j - 1
print(d)
