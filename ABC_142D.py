n, m = map(int, input().split())

while m:
    n, m = m, n % m

pf = {}
for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        pf[i] = pf.get(i, 0)+1
        n //= i
if n > 1:
    pf[n] = 1

if pf == {}:
    print(1)
else:
    print(sum(pf.values()))
