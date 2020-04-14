n = int(input())
res = 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            l = gcd(i,j)
            res += gcd(k, l)
print(res)