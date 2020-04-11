import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lis = list(map(int, input().split()))

    n, m = map(int, input().split())
    lis = [int(input()) for _ in range(n)]

    n, m = map(int, input().split())
    h = [0] * n
    s = [0] * n
    for i in range(n):
        h[i], s[i] = map(int, input().split())

if __name__ == '__main__':
    main()
