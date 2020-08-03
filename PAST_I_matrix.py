from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    n = int(input())
    row = list(range(n))
    col = list(range(n))
    flg = True
    q = int(input())
    for _ in range(q):
        s, *ab = list(map(int, input().split()))
        if s == 3:
            row, col = col, row
            flg = not flg
            continue
        a, b = ab
        a, b = a - 1, b - 1
        if s == 1:
            row[a], row[b] = row[b], row[a]
        elif s == 2:
            col[a], col[b] = col[b], col[a]
        elif s == 4:
            print(row[a] + col[b] * n if not flg else row[a] * n + col[b])


solve()
