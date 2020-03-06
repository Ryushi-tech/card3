import bisect
import sys
readline = sys.stdin.buffer.readline


def main():
    n = int(readline())
    a = list(map(int,readline().rsplit()))
    b = list(map(int,readline().rsplit()))
    c = list(map(int,readline().rsplit()))
    a.sort()
    c.sort()
    ans = 0
    for i in b:
        d = bisect.bisect_left(a, i)
        e = n - bisect.bisect_right(c, i)
        ans += d * e
    print(ans)

if __name__ == '__main__':
    main()
