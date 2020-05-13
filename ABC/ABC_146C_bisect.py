a, b, x = map(int, input().split())
l = x // a
inf = 10**9


def val(y):
    return a * y + b * len(str(y))


if x >= val(inf):
    print(inf)
    exit()

z = 0

while z + 1 < l:
    m = (l + z) // 2
    if val(m) > x:
        l = m
    else:
        z = m

print(max(0, int(z)))
