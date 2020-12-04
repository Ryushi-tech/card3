def is_ok(i):
    return i * (i + 1) <= 2 * (n + 1)


def solve():
    ok = -1
    ng = 10 ** 10
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return n - ok + 1


n = int(input())
print(solve())
