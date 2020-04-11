h, w = map(int, input().split())
area = [[0] * w for _ in range(h)]
s = [input() for _ in range(h)]

for i, row in enumerate(s):
    cnt = 0
    for j, x in enumerate(row):
        if x == "#":
            for k in range(j - cnt, j): area[i][k] = cnt
            cnt = 0
        else:
            cnt += 1
    for k in range(w - cnt, w): area[i][k] = cnt

for i in range(w):
    cnt = 0
    for j in range(h):
        x = s[j][i]
        if x == "#":
            for k in range(j - cnt, j): area[k][i] += cnt - 1
            cnt = 0
        else:
            cnt += 1
    for k in range(h - cnt, h): area[k][i] += cnt - 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, area[i][j])

print(ans)
