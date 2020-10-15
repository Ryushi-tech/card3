from bisect import bisect_left


def LIS(arr: list):
    INF = float("inf")
    L = [INF] * len(arr)
    for ar in arr:
        x = bisect_left(L, ar)
        L[x] = ar
    return bisect_left(L, INF)

