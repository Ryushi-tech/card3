import sys
input = sys.stdin.buffer.readline


def get_diameter(tree):
    u, _, _ = _dfs(0, tree)
    v, diam, dist = _dfs(u, tree)
    path = [v]
    while v != u:
        for nxt_v, cost in tree[v]:
            if cost + dist[nxt_v] == dist[v]:
                path.append(nxt_v)
                v = nxt_v
                break
    return diam, path


def _dfs(start, tree):
    n = len(tree)
    dist = [-1] * n
    dist[start] = 0
    stack = [start]
    while stack:
        v = stack.pop()
        for nxt_v, cost in tree[v]:
            if dist[nxt_v] != -1:
                continue
            dist[nxt_v] = dist[v] + cost
            stack.append(nxt_v)
    max_d = max(dist)
    return dist.index(max_d), max_d, dist


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]


tree = [[] for i in range(n)]
for a, b, cost in edges:
    tree[a].append((b, cost))
    tree[b].append((a, cost))

diam, path = get_diameter(tree)
print(diam, len(path))
print(*path)
