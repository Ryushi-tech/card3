def main():
    n,a,b = map(int, input().split())
    if a == 0:
        print(0)
        exit()
    elif b == 0:
        print(n)
        exit()
    c = a + b
    d,e = divmod(n,c)
    f,g = divmod(e,a)
    if f == 0:
        print(a * d + g)
    else:
        print(a * d + a)

if __name__ == '__main__':
    main()