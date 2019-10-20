n = int(input())
lis = list(map(int,input().split()))
li = lis[:]

squ = [i**2 for i in lis]
sq = sum(squ)

a = []
for i in lis:
    for j in li:
        a.append(i*j)

print((sum(a)-sq)//2)