a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = a + b, a - b
z, w = c + d, c - d
mx, my = abs(a - c), abs(b - d)

if a == c and b == d:
    print(0)
elif mx + my <= 3:
    print(1)
elif x == z or y == w:
    print(1)
elif mx + my <= 6:
    print(2)
elif x & 1 == z & 1:
    print(2)
elif abs(x - z) <= 3 or abs(y - w) <= 3:
    print(2)
else:
    print(3)
