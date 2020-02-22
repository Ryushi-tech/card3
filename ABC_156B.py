import itertools
import bisect

def main():
    n,k = map(int,input().split())
    bi = ''
    while n != 0:
        bi += str(n % abs(k))
        if k < 0:
            n = -(-n // k)
        else:
            n = n // k
    bilast = bi[::-1]
    print(len(bilast))

if __name__ == '__main__':
    main()