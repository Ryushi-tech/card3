import bisect
n = int(input())
lis = list(map(int, input().split()))
lis = sorted(lis)

a = bisect.bisect(lis, 0)
su = 0
mi = 10**10

for b in lis:
    su += abs(b)
    mi = min(mi, abs(b))

if a % 2 == 0:
    print(su)
else:
    print(su - 2 * mi)