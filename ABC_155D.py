import itertools

n,k = map(int, input().split())
lis = list(map(int,input().split()))

l_p = list(itertools.product(lis, lis))

for i in l_p:
    print(i[0]*i[1])