def main():
    n,m = map(int, input().split())
    if n == 1 or m == 1:
        print(1)
    else:
        print(n*m//2 if n*m%2==0 else 1 + n*m//2)

if __name__ == '__main__':
    main()