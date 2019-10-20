import bisect

n = int(input())
lis = list(map(int,input().split()))

a = sorted(lis, reverse=True)
c = sorted(lis)
d = 0

for i in range(n):
    for j in range(i + 1, n):
        e = c[:-j-1]
        b = bisect.bisect_right(e, int(a[i]-a[j]))
        d += max(0, len(e) - b)
print(d)


