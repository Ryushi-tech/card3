n, q = map(int, input().split())
b = list(range(n + 1))
a = [-1] * (n + 1)

def calc(f, t, x):
    bf, ax, bt = b[f], a[x], b[t]
    b[t], b[f], a[x] = bf, ax, bt
    return

for i in range(q):
    f, t, x = map(int, input().split())
    calc(f, t, x)

    ans = [0] * (n + 1)
    for i, k in enumerate(b):
        if i == 0:
            continue
        while k != -1:
            ans[k] = i
            k = a[k]
    print("\n".join(map(str, ans[1:])))


"""
10 20
3 6 3
6 5 6
10 8 10
5 7 3
1 3 1
4 10 4
5 4 6
10 7 4
7 9 3
9 8 4
8 1 4
3 7 1
2 3 2
9 8 3
8 1 10
8 2 8
9 10 9
2 1 8
4 9 6
1 7 4
"""