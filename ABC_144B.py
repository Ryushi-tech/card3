m = int(input())
a = {}
for i in range(1, int(m**0.5)+1):
    if m % i == 0:
        n = m // i
        a[i] = n
b = min(a.values())

if b < 10:
    print("Yes")
else:
    print("No")
