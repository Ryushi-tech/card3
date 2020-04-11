n = int(input())
lis = list(map(int, input().split()))
a = [0]*n

for i, item in enumerate(lis):
    a[item - 1] = i + 1

print(*a)
