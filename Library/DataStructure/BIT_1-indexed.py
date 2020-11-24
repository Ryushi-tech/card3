from bisect import bisect_left


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        # self.data = [i & -i for i in range(n + 1)]

    def query(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def update(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def binary_lift_search(self, k):
        su, pos = 0, 0
        N = 1 << (self.n - 1).bit_length()
        while N:
            if pos + N <= self.n and su + self.data[pos + N] <= k:
                su += self.data[pos + N]
                pos += N
            N >>= 1
        return pos + 1


def LIS(arr: list):
    INF = float("inf")
    L = [INF] * len(arr)
    for ar in arr:
        x = bisect_left(L, ar)
        L[x] = ar
    return bisect_left(L, INF)


n = int(input())
A = list(map(int, input().split()))
bit = BIT(n)

B = [None] * n
for i in range(n - 1, -1, -1):
    x = bit.binary_lift_search(i - A[i])
    B[x - 1] = i + 1
    bit.update(x, -1)

print(LIS(B))
