def bin_bfs(mod):
    from collections import deque
    que = deque([(1, 1)])
    seen = set()
    while que:
        c, x = que.popleft()
        if not x:
            return c
        if x in seen:
            continue
        seen.add(x)
        que.appendleft((c, x * 10 % mod))
        que.append((c + 1, (x + 1) % mod))


k = int(input())
print(bin_bfs(k))
