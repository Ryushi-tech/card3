from functools import reduce

def main():
    n, a, b = map(int,input().split())
    mod = 10 ** 9 + 7
    def f(k):
        num = reduce(lambda x,y: x * y % mod, range(n, n-k, -1))
        den = reduce(lambda x,y: x * y % mod, range(1, k+1))
        return num * pow(den, mod-2, mod) % mod
    ans = pow(2,n,mod) - f(a) - f(b) - 1
    ans %= mod
    print(ans)

if __name__ == '__main__':
    main()