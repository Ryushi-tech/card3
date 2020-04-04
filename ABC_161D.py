import sys
input = sys.stdin.readline
import itertools

lunlun = [[] for i in range(11)]

def main():
    n = int(input())
    for i in range(100):
        flag = True
        l = len(str(i))
        if l == 1:
            lunlun[l - 1].append(i)
        else:
            for a in range(1, len(str(i))):
                if abs(int(str(i)[a - 1]) - int(str(i)[a])) >= 2:
                    flag = False
                    break
            if flag:
                lunlun[l - 1].append(i)
            else:
                continue
    for j in range(1, 9):
        for a in lunlun[j]:
            for b in range(10):
                if abs(int(str(a)[-1]) - b) < 2:
                    lunlun[j+1].append(int(str(a)+str(b)))
    lunlun2 = list(itertools.chain.from_iterable(lunlun))
    print(lunlun2[n])

if __name__ == '__main__':
    main()
