import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lis = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        for j in range(i, n):
            if lis[i] + lis[j] == j - i:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
