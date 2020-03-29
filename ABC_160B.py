n = int(input())
a, b = divmod(n, 500)
c, d = divmod(b, 5)
print(1000 * a + 5 * c)
