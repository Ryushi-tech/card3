from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    from collections import deque
    import sys

    def bfs(s, g, o):
        move = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([[0, s]])
        visited = {s}
        while queue:
            d, p = queue.popleft()
            if p == g:
                return d
            x, y = p
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                q = (nx, ny)
                if not -202 < nx < 202 or not -202 < ny < 202:
                    continue
                if q in o or q in visited:
                    continue
                visited.add(q)
                queue.append([d + 1, q])
        return -1

    st = (0, 0)
    n, gx, gy, *xy = map(int, sys.stdin.read().split())
    g = (gx, gy)
    obst = set(zip(xy[0::2], xy[1::2]))

    res = bfs(st, g, obst)
    print(res)


solve()
