n = int(input())
pf = {}
mod = 10**9 + 7

for m in range(1, n + 1):
    for i in range(2, int(m**0.5) + 1):
        while not m % i:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        if m in pf:
            pf[m] += 1
        else:
            pf[m] = 1

res = 1
for i, j in pf.items():
    res *= j + 1
print(res % mod)