from collections import defaultdict

n = int(input())
rem = defaultdict(int)

def prime_f(m):
    pf = {}
    for i in range(2, int(m**0.5) + 1):
        while not m % i:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        pf[m] = 1
    return pf


cnt = 0
for i in range(3, 100000, 2):
    a = tuple(prime_f(i).values())
    if len(a) == 1 and a[0] == 1:
        b = tuple(prime_f((i+1)//2).values())
        if len(b) == 1 and b[0] == 1:
            cnt += 1
            rem[i] = cnt
        else:
            rem[i] = cnt
    else:
        rem[i] = cnt

for i in range(n):
    a, b = map(int, input().split())
    print(rem[b] - rem[a - 2])
