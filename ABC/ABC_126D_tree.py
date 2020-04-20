from collections import deque
n = int(input())
g = [[] for _ in range(n)]
ln = []

for _ in range(n - 1):
    a, b, l = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
    ln.append((a, b, l))

q = deque([0])
par = [0] * n
order = []

while q:
    x = q.pop()
    order.append(x)
    for y in g[x]:
        if y == par[x]:
            continue
        par[y] = x
        q.append(y)

chr_l = [0] * n
for a, b, l in ln:
    if par[a] == b:
        chr_l[a] = l
    else:
        chr_l[b] = l

#print(ln, g, order)
#print(chr_l)

color = [-1] * n
color[0] = 0
org = [0, 1]

for x in order:
    for y in g[x]:
        if y == par[x]:
            continue
        if chr_l[y] % 2 == 0:
            color[y] = color[x]
        else:
            color[y] = color[x] ^ 1
print("\n".join(map(str, color)))
