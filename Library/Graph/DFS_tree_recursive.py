import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
mod = 10 ** 9 + 7

q = int(input())
n = int(input())
E = [[] for _ in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)

par = [-1] * (n + 1)
depth = [-1] * (n + 1)
size = [1] * (n + 1)


def dfs(E: list, v, p=-1, d=0):
    depth[v] = d
    par[v] = p
    for c in E[v]:
        if c == p:
            continue
        dfs(E, c, v, d + 1)
    # for c in E[v]:
    #     if c == p:
    #         continue
        size[v] += size[c]


dfs(E, 1)

print(par)
print(depth)
print(size)
