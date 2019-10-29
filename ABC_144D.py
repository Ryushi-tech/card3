import math
a, b, x = map(int, input().split())
h = x/a**2

elif h >= b/2:
    tanth = a / (b - h) / 2
else:
    tanth = 2 * a * h / b**2

theta = math.degrees(math.atan(tanth))
print(90 - theta)
