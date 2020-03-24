from collections import Counter
import sys
input = sys.stdin.buffer.readline
ans = {}

def main():
    n = int(input())
    for i in range(n):
        dic = {}
        for a in input().strip():
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        dic2 = tuple(sorted(dic.items()))
        #print(dic2)
        tmp = ""
        for k, v in dic2:
            tmp += str(k) + str(v)
        if tmp in ans:
            ans[tmp] += 1
        else:
            ans[tmp] = 1
    su = 0
    for vv in ans.values():
        su += vv * (vv - 1) // 2
    print(su)

if __name__ == '__main__':
    main()
