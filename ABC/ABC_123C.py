import sys
input = sys.stdin.readline

def main():
    n = int(input())
    bn = 10**16
    for i in range(5):
        bn = min(bn, int(input()))
    print(-(-n // bn) + 4)

if __name__ == '__main__':
    main()
