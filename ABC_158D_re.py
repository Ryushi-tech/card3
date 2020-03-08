from collections import deque
import sys
readline = sys.stdin.readline


def main():
    a = input()
    d = deque(a)
    n = int(input())
    flagr = True
    for i in range(n):
        j = list(readline().split())
        if len(j) == 1:
            flagr = not flagr
        elif int(j[1] == "1") ^ flagr:
            d.append(j[2])
        else:
            d.appendleft(j[2])
    if not flagr:
        d.reverse()
    print("".join(d))


if __name__ == '__main__':
    main()