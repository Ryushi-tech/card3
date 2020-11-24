# 1-indexed
import sys

input = sys.stdin.readline
mod = 10 ** 9 + 7

n = int(input())
n = int(input())
E = [[] for _ in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)

order = []
que = [(1, 0, -1)]
par = [-1] * (n + 1)
depth = [-1] * (n + 1)
size = [1] * (n + 1)

while que:
    x, d, px = que.pop()
    order.append(x)
    depth[x] = d
    for v in E[x]:
        if v == px:
            continue
        que.append((v, d + 1, x))
        par[v] = x

order.reverse()
for x in order:
    px = par[x]
    if px == -1:
        continue
    size[px] += size[x]

print(par)
print(depth)
print(size)
