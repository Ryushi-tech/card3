m = int(input())
a = {}
for i in range(1, int(m**0.5)+1):
    if m % i == 0:
        n = m // i
        a[i] = n
ans =[]
for i,j in a.items():
    b = i + j
    ans.append(b)

print(min(ans)-2)
