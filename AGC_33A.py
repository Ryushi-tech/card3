m, n = map(int, input().split())
lis = [input() for _ in range(m)]

a = [lis[0][i] for i in range(n)]
print(a)

b = [lis[j][0] for j in range(m)]
print(b)
