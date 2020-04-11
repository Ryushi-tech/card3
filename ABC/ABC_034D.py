n, k = map(int, input().split())
w = [0] * n
p = [0] * n
for i in range(n):
    w[i], p[i] = map(int, input().split())


def check(x):
    s = [0] * n
    for i in range(n):
        s[i] = w[i] * (p[i] - x)
    s.sort()
    return sum(s[-k:]) >= 0


r = float(100)
l = 0

while l + 1e-10 < r:
    m = (l + r) / 2
    if check(m):
        l = m
    else:
        r = m
print('{:.9f}'.format(l))
