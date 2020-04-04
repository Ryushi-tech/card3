n, m = map(int, input().split())
lis = list(map(int, input().split()))
mot = sum(lis)
liss = sorted(lis, reverse=True)

flag = True
for a in range(m):
    if liss[a] * 4 * m < mot:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
