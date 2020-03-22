from collections import defaultdict
d = defaultdict(int)

n = int(input())
for i in range(n):
    d[input()] += 1

m = int(input())
for i in range(m):
    d[input()] -= 1

ans = max(d.values())
print(max(0, ans))
