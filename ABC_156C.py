import itertools
import bisect

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = round(sum(p)/n)
    ans = 0
    for i in p:
        ans += (i-q)**2
    print(ans)

if __name__ == '__main__':
    main()