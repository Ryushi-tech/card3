import sys
from collections import Counter
input = sys.stdin.readline

def main():
    a = input().strip()
    n = int(input())
    l = len(a)
    b = Counter(a)
    if len(b) == 1:
        c = (n * l) // 2
        print(c)
        exit()
    su = 0
    ans = []
    for i in range(1, l):
        if a[i] == a[i - 1]:
            su += 1
        else:
            ans.append(su + 1)
            su = 0
    ans.append(su + 1)
    rev = 0
    for j in ans:
        rev += j // 2
    if a[0] == a[-1]:
        dif = ans[0]//2 + ans[-1]//2 - (ans[0]+ans[-1])//2
        print(rev*n - dif*(n - 1))
    else:
        print(rev*n)

if __name__ == '__main__':
    main()
