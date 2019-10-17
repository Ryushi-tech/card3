import math
m, n = map(int, input().split())
lis = [input() for _ in range(m)]

a = [lis[0][i] for i in range(m)]
print(a)

b = [lis[j][0] for j in range(n)]
print(b)

c=[]
for i in range(m):
    for j in range(n):
        if lis[j][i] == "#":
            c.append([i, j])

d = range(len(c))
e = []
for i in d:
    for j in d:
        if i==j:
            break
        else:
            e.append(((c[i][0] - c[j][0])**2+(c[i][1] - c[j][1])**2)**0.5)
f = math.ceil(min(e))
print(f)