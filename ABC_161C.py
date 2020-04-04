import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    res = n % k
    ser = abs(res - k)
    print(min(res,ser))

if __name__ == '__main__':
    main()
