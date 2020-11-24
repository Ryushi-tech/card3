from numba import njit, i8


@njit((i8, i8, i8, i8), cache=True)
def floor_sum(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans


N = int(input())
for _ in range(N):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
