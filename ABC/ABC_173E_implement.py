from card3.void.stop_watch import stop_watch
@stop_watch
def main():
    mod = 10 ** 9 + 7
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    S = sorted(A, key=lambda x: abs(x), reverse=True)
    R = sorted(A, reverse=True)
    F = sorted(A)

    print(R)
    res1 = 1
    res2 = 1
    res3 = 1
    for i in range(k):
        res1 *= S[i]
        res2 *= R[i]
        res3 *= F[i]
        res1 %= mod
        res2 %= mod
        res3 %= mod
    print(res1, res2, res3)

if __name__ == '__main__':
    main()
