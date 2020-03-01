import itertools
import bisect

def main():
    n,m = map(int, input().split())
    ans = [0] * n
    chg = [0] * n
    flg = 0
    for i in range(m):
        j,k = map(int, input().split())
        if chg[j-1] == 1 and ans[j-1] != k:
            flg = -1
        elif ans[j-1] == 0:
            ans[j-1] = k
            chg[j-1] = 1
    if flg == -1:
        print(flg)
    elif len(ans) >= 2 and ans[0] == 0:
        if chg[0] == 0:
            ans[0] = 1
            if n == 3:
                print(ans[0], ans[1], ans[2], sep="")
            elif n == 2:
                print(ans[0], ans[1], sep="")
        else:
            print(-1)
    else:
        if n == 3:
            print(ans[0],ans[1],ans[2],sep="")
        elif n == 2:
            print(ans[0],ans[1],sep="")
        else:
            print(ans[0])


if __name__ == '__main__':
    main()