n = 300
primes = set(range(2, n + 1))
for i in range(2, int(n ** 0.5 + 1)):
    if i not in primes:
        i += 1
    else:
        remove = range(i * 2, n + 1, i)
        primes.difference_update(remove)
primes = list(primes)
print(primes)
