k = 20000
l = 20000
m = 20000
for i in range(10):
    k -= 1
    k >>= 1
    l >>= 1
    m >>= 1
    m -= 1
    print(m, k, l)
