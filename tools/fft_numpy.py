from card3.void.stop_watch import stop_watch

@stop_watch
def solve():
    import sys
    from numpy import fft

    n, *ab = map(int, sys.stdin.read().split())
    l = 1 << ((n - 1).bit_length() + 1)
    fa = fft.rfft(ab[0::2], l)
    fb = fft.rfft(ab[1::2], l)
    C = (fft.irfft(fa * fb)[:2 * n - 1] + 0.1).astype(int)
    print(0)
    print("\n".join(map(str, C)))


solve()
