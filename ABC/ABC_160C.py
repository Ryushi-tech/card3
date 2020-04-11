import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    lis = list(map(int, input().split()))
    su = []
    for i in range(m - 1):
        su.append(lis[i + 1] - lis[i])
    ou = lis[0] - lis[-1] + n
    print(sum(su) + ou - max(ou, max(su)))

if __name__ == '__main__':
    main()
