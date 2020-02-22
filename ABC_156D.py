
def main():
    m, a, b = map(int,input().split())
    base = pow(2, m, 10**9+7)
    print(base)
    mod = 10 ** 9 + 7

    fact = [1]
    fact_inv = [0] * (m + 4)
    for i in range(m + 3):
        fact.append(fact[-1] * (i + 1) % mod)

    fact_inv[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(m + 2, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % mod

    def mod_comb_k(n, k, mod):
        return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod
    print(mod_comb_k(m,a,mod))

if __name__ == '__main__':
    main()