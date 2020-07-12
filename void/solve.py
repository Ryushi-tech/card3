from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        chk = [0] * n
        for i, x in enumerate(s):
            if i + 1 == x:
                chk[i] = 1
        cnt = 0
        chk.append(1)
        for i in range(n):
            if chk[i] == 0 and chk[i + 1] == 1:
                cnt += 1
        print(min(cnt, 2))

solve()

