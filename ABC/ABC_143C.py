n = int(input())
lis = input()

a = 1

for i in range(n-1):
    if lis[i] != lis[i+1]:
        a += 1
print(a)