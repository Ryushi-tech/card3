from collections import deque

n = int(input())
l = n.bit_length()
g = [[] for _ in range(n + 1 + l)]

if n == 1:
    print(1)
    exit()

for i in range(n + 1):
    x = bin(i).count("1")
    g[i].append(i + x)
    g[i].append(i - x)

par = [0] * (n + 1 + l)
chk = [False] * (n + 1 + l)
chk[0] = True
stk = deque()
stk.append(1)

while stk:
    v = stk.popleft()
    for y in g[v]:
        if chk[y]:
            continue
        if y == par[v]:
            continue
        chk[y] = True
        par[y] = v
        stk.append(y)

if not chk[n]:
    print(-1)
    exit()

cnt = 1
while n > 1:
    n = par[n]
    cnt += 1
print(cnt)

