import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lunlun = [[] for i in range(11)]
    lunlun[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 9
    if n < 10:
        print(n)
        exit()
    for j in range(0, 10):
        for a in lunlun[j]:
            for b in range(10):
                if abs((a % 10) - b) < 2:
                    lunlun[j + 1].append(10 * a + b)
                    cnt += 1
                    if cnt == n:
                        print(lunlun[j + 1][-1])
                        print(*lunlun[:j+1], sep="\n")
                        exit()
if __name__ == '__main__':
    main()
