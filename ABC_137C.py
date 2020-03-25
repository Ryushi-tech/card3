import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        a = ''.join(sorted(input().rstrip()))
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    su = 0
    for v in dic.values():
        su += v * (v - 1) // 2
    print(su)

if __name__ == '__main__':
    main()
