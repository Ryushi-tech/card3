h, w = map(int, input().split())
lis = [] * h
for i in range(h):
    lis.append(tuple(map(int, input().split())))
flg = False
res = []
ans = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if not flg and lis[i][j] % 2 == 1:
                res.append(i+1)
                res.append(j+1)
                flg = not flg
            elif flg and lis[i][j] % 2 == 0:
                ans.append([res[0], res[1], i+1, j+1])
                res = []
                res.append(i+1)
                res.append(j+1)
            elif flg and lis[i][j] % 2 == 1:
                ans.append([res[0], res[1], i+1, j+1])
                res = []
                flg = not flg
    else:
        for j in range(w - 1, -1, -1):
            if not flg and lis[i][j] % 2 == 1:
                res.append(i + 1)
                res.append(j + 1)
                flg = not flg
            elif flg and lis[i][j] % 2 == 0:
                ans.append([res[0], res[1], i+1, j+1])
                res = []
                res.append(i + 1)
                res.append(j + 1)
            elif flg and lis[i][j] % 2 == 1:
                ans.append([res[0], res[1], i+1, j+1])
                res = []
                flg = not flg
print(len(ans))
for a in ans:
    print(*a)