n = int(input())
a = n // 100
b = n % 100

if b > a * 5:
    print(0)
else:
    print(1)