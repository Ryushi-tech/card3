import itertools
import bisect

def main():
    n,r = map(int,input().split())
    if n <= 10:
        print((10-n)*100+r)
    else:
        print(r)


if __name__ == '__main__':
    main()