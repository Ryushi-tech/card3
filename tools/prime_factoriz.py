pf = {}
m = 673
for i in range(2, int(m**0.5) + 1):
    while not m % i:
        pf[i] = pf.get(i, 0) + 1
        m //= i
if m > 1:
    pf[m] = 1
print(pf)
