class BITM:
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (n + 1)

    def query(self, index):
        ans = 0
        while index > 0:
            ans = max(ans, self.BIT[index])
            index -= index & (-index)
        return ans

    def update(self, index, value):
        while index <= self.n:
            self.BIT[index] = max(self.BIT[index], value)
            index += index & (-index)


n = int(input())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

b = BITM(n)

for i, h in enumerate(H):
    x = b.query(h - 1)
    b.update(h, x + B[i])
    print(b.BIT)
print(b.query(n))
