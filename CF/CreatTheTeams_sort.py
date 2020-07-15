from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        S = [int(y) for y in input().split()]
        S.sort(reverse=True)
        team, cnt = 0, 0
        for s in S:
            cnt += 1
            if s * cnt >= x:
                team += 1
                cnt = 0
        print(team)

solve()
