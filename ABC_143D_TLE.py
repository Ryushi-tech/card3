import itertools

n = int(input())
lis = list(map(int,input().split()))

a = tuple(itertools.combinations(lis,3))
b = 0

for i in a:
    if i[0] < i[1] + i[2] and i[1] < i[2] + i[0] and i[2] < i[0] + i[1]:
        b += 1
print(b)
