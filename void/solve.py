import sys
input = sys.stdin.read
n, *s = map(int, input().split())
res = [0]

for i in range(n):
    res.append(res[-1] + s[i])
for i in range(n - 1):
    res.append(res[-1] - s[i])

print("\n".join(map(str, res)))