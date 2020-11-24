from collections import deque

k = int(input())
que = deque([(1, 1)])
seen = set()


def bin_bfs():
    while que:
        c, x = que.popleft()
        if not x:
            return c
        if x in seen:
            continue
        seen.add(x)
        que.appendleft((c, x * 10 % k))
        que.append((c + 1, (x + 1) % k))


print(bin_bfs())
