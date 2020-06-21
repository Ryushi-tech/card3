n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(min(k, 50)):
    b = [0] * (n + 1)
    for j in range(n):
        l = max(0, j - a[j])
        r = min(n - 1, j + a[j])
        b[l] += 1
        b[r + 1] -= 1
    for m in range(n):
        b[m + 1] += b[m]
    a = b[:-1]
print(*a)
