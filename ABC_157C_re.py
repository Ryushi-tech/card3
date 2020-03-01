import itertools
import bisect

def main():
    n,m = map(int, input().split())
    lim = 10 ** n
    val = [list(map(int, input().split())) for _ in range(m)]
    for i in range(10**(n-1) if n >= 2 else 0, lim):
        for j, k in val:
            j = j - 1
            l = str(i)
            if l[j] != str(k):
                break
        else:
             print(i)
             exit()
    print(-1)

if __name__ == '__main__':
    main()