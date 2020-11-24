import sys
n = int(input())
res = [0] * n
mx = 0


def ask(x, y):
    print("?", x + 1, y + 1)
    sys.stdout.flush()
    r = int(input())
    return r


for i in range(1, n):
    a = ask(mx, i)
    b = ask(i, mx)
    if a > b:
        res[mx] = a
        mx = i
    else:
        res[i] = b

res[mx] = n
print("!", *res)
