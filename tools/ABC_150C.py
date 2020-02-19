import itertools
import bisect

def main():
    n = int(input())
    p = tuple(map(int,input().split()))
    q = tuple(map(int,input().split()))
    a = list(itertools.permutations(range(1,n+1)))
    print(abs(bisect.bisect_right(a,p)-bisect.bisect_right(a,q)))

if __name__ == '__main__':
    main()