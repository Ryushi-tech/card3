from collections import defaultdict

n = int(input())
lis = list(map(int, input().split()))

rem = defaultdict(int)
ans = 0

for i, x in enumerate(lis):
    ans += rem[i - x]
    rem[i + x] += 1
print(ans)
