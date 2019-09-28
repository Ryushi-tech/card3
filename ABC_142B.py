n,k = map(int, input().split())
lis = list(map(int,input().split()))

a = 0
for i in range(n):
    if lis[i]>=k:
        a+=1

print(a)
