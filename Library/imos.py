from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))


def calc_imos(arr):
    imos = [0] * (N + 1)
    for i, a in enumerate(arr):
        l = max(0, i - a)
        r = min(N - 1, i + a)
        imos[l] += 1
        imos[r + 1] -= 1
    imos = list(accumulate(imos))
    return imos[:-1]


for k in range(min(50, K)):
    A = calc_imos(A)
print(*A, sep=' ')
