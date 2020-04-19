mod = 10 ** 9 + 7


def main():
    n, k = map(int, input().split())
    res = 0
    for i in range(k, n + 2):
        mis = i * (i - 1)//2
        mas = n * (n + 1)//2 - (n - i) * (n - i + 1)//2
        res += mas - mis + 1
        res %= mod
    print(res)


if __name__ == '__main__':
    main()
