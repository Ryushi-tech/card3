import sys
input = sys.stdin.readline

def main():
    a, b, n = map(int, input().split())
    x = min(n, b - 1)
    X = (a * x) // b
    Y = a * (x // b)
    print(X - Y)
if __name__ == '__main__':
    main()
