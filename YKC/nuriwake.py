h, w = map(int, input().split())
S = []
for i in range(h):
    S.append(input())

cnt = 0
D = set()
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            D.add(i * 1000 + j)

l = len(D)
if l & 1 or not D:
    print("NO")
    exit()
E = sorted(list(D))

for x in range(h):
    for y in range(-w, w):
        tmp = set()
        cnt = 0
        for e in E:
            z = e + x * 1000 + y
            c, d = divmod(z, 1000)
            if e in tmp:
                continue
            elif c < 0 or c > h or d < 0 or d > w:
                break
            elif z in D:
                cnt += 1
                tmp.add(z)
        if l // 2 == cnt:
            print("YES")
            exit()
print("NO")
