n = int(input())
lis = []
for i in range(n):
    a, b = map(int, input().split())
    lis.append((a-b, a+b))

lis.sort(key=lambda x: x[1])
cnt = 0
INF = 10**9
prev_r = -INF

for l, r in lis:
    if l < prev_r:
        continue
    cnt += 1
    prev_r = r
print(cnt)
