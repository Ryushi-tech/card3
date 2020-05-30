import bisect
import sys
readline = sys.stdin.buffer.readline


def main():
    A, B, Q = map(int, readline().split())
    inf = 10 ** 18
    s = [-inf] + [int(readline()) for _ in range(A)] + [inf]
    t = [-inf] + [int(readline()) for _ in range(B)] + [inf]
    for q in range(Q):
        x = int(readline())
        b, d = bisect.bisect_right(s, x), bisect.bisect_left(t, x)
        res = inf
        for S in [s[b - 1], s[b]]:
            for T in [t[d - 1], t[d]]:
                d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
                res = min(res, d1, d2)
        print(res)

if __name__ == '__main__':
    main()