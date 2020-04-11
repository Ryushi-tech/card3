import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lis = []
for i in range(m):
    a, b = map(int, input().split())
    lis.append([a, b])

liss = sorted(lis)
dic = {}
cnt = [0] * n

for i in range(m):
    x, y = liss[i]
    cnt[x - 1] += 1
    xx, yy, cc = str(x), str(y), str(cnt[x - 1])
    id = "0" * (6-len(xx)) + xx + "0" * (6-len(cc)) + cc
    dic[xx + "_" + yy] = id

for x, y in lis:
    xx, yy = str(x), str(y)
    print(dic[xx + "_" + yy])