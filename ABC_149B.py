import sys
readline = sys.stdin.buffer.readline


def main():
    a, b, k = map(int, readline().split())
    if k >= a + b:
        print(0, 0)
    elif k >= a:
        print(0, a + b - k)
    else:
        print(a - k, b)

if __name__ == '__main__':
    main()