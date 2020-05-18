from collections import deque


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append(b)
        g[b].append(a)

    q = deque([0])
    chk = [False] * n
    res = [0] * n

    while q:
        x = q.popleft()
        for y in g[x]:
            if chk[y]:
                continue
            chk[y] = True
            res[y] = x
            q.append(y)
    print("Yes")
    for i in res[1:]:
        print(i + 1)


if __name__ == '__main__':
    main()
