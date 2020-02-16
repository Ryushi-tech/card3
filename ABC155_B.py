n = int(input())
lis = list(map(int,input().split()))
ans = [0]

for i in lis:
    if i % 2 == 0:
        if i%3 != 0 and i%5 != 0:
            ans[0]=1
            break
if ans[0] == 0:
    print("APPROVED")
else:
    print("DENIED")
