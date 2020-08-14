k = 18
n = 2 ** k
p = 1541406721

for i in range(2, 10000):
    x = pow(i, n, p)
    if x == 1:
        print(i)
