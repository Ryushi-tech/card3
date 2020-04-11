import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lis = list(map(int, input().split()))
    val = [0] * n

    for i in range(n, 0, -1):
        if n // i == 1:
            val[i - 1] = lis[i - 1]
        else:
            a = sum(val[i - 1::i])
            if a % 2 != lis[i - 1]:
                val[i - 1] ^= 1

    print(sum(val))
    print(*[i + 1 for i in range(n) if val[i] == 1], sep=" ")
if __name__ == '__main__':
    main()