a, b, x, y = map(int, input().split())

if a > b:
    u = ((a - b) * 2 - 1) * x
    t = (a - b - 1) * y + x
else:
    u = ((b - a) * 2 + 1) * x
    t = (b - a) * y + x
print(min(u, t))
