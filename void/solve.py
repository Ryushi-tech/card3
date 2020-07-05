from card3.void.stop_watch import stop_watch

@stop_watch
def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        ref = a * b
        s = int(ref ** 0.5)
        ans = 2 * s - 1
        if s * (s + 1) >= ref:
            ans -= 1
        if s * s == a * b and a != b:
            ans -= 1
        print(ans)
if __name__ == '__main__':
    main()