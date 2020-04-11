import itertools
import bisect

def main():
    k, n = map(int, input().split())
    dp = [0] * (k+1)
    dq = [0] * (k+1)
    pen = 0
    for i in range(n):
        p,q = input().split()
        p = int(p)
        if dp[p] == 0:
            if q == 'WA':
                dq[p] += 1
            elif q == 'AC':
                dp[p] = 1
                pen += dq[p]
    print(sum(dp), pen)

if __name__ == '__main__':
    main()