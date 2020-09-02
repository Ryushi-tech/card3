n, k = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

def is_ok(x):
    tmp = 0
    for a, f in zip(A, F):
        y = a * f
        if y > x:
            tmp += a - x // f
    return tmp <= k

ok = 10 ** 16
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
