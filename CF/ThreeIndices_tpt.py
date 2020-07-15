from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        ans = []
        for i in range(0, n - 2):
            j, k = i + 1, i + 2
            if s[i] > s[j]:
                j += 1
                k += 1
            elif s[i] < s[j] < s[k]:
                k += 1
            elif s[i] < s[j] and s[j] > s[k]:
                ans.append([i+1, j+1, k+1])
                break
        if not ans:
            print("NO")
        else:
            print("YES")
            print(*ans[0])


solve()
