n = int(input())
lis = list(map(int, input().split()))
dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in range(1, n + 1):
    print(dic.get(i, 0))
