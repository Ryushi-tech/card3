import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    INF = 10 ** 6
    cost = [[INF] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = 0

    for i in range(m):
        a, b, t = map(int, input().split())
        a, b = a - 1, b - 1
        cost[a][b] = t
        cost[b][a] = t

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    res = INF
    for x in cost:
        res = min(res, max(x))
    print(res)
if __name__ == '__main__':
    main()
