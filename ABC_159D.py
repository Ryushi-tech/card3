from collections import Counter
import sys
input = sys.stdin.buffer.readline

def main():
    n = int(input())
    lis = list(map(int,input().split()))
    d = Counter(lis)
    su = 0
    for e in d:
        su += (d[e] - 1) * d[e] // 2

    for e in lis:
        if d[e] <= 1:
            print(su)
        else:
            k = d[e]
            res = su - k*(k-1)//2 + (k-1)*(k-2)//2
            print(res)

if __name__ == '__main__':
    main()
