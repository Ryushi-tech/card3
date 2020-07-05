t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    bnh = -1 if A[-1] > 0 else 1
    A.append(bnh)

    flg = True if A[0] > 0 else False
    inf = 10 ** 10
    tmp = -inf
    res = 0
    for a in A:
        if flg and a > 0:
            tmp = max(tmp, a)
        elif not flg and a < 0:
            tmp = max(tmp, a)
        else:
            res += tmp
            flg = not flg
            tmp = max(-inf, a)
    print(res)
