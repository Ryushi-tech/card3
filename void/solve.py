n = 55555
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    if i not in primes:
        i += 1
    else:
        ran = range(i*2, n+1,i)
        primes.difference_update(ran)
primes = list(primes)

N = int(input())
res = []
for i in primes:
    if len(res) >= N:
        print(*res)
        exit()
    if i % 5 == 2:
        res.append(i)
