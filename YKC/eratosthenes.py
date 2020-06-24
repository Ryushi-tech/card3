n, p = input().split()
n = int(n)
p = float(p)

cnt = [0] * (n + 1)

for i in range(2, n + 1):
    cnt[i] += 1
    for j in range(i * 2, n + 1, i):
        cnt[j] += 1
#print(cnt)

res = cnt.count(1)
for c in cnt:
    if c > 1:
        res += (1 - p) ** (c - 1)
print(res)
