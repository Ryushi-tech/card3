class LIS:
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (n + 1)

    def coordinateCompression(self, arr):
        sar = sorted(arr)
        mp = {z: i for i, z in enumerate(sar, 1)}
        res = [mp[x] for x in arr]
        return res

    def query(self, index):
        ans = 0
        while index > 0:
            ans = max(ans, self.BIT[index])
            index -= index & (-index)
        return ans

    def update(self, index):
        x = self.query(index - 1)
        value = x + 1
        while index <= self.n:
            self.BIT[index] = max(self.BIT[index], value)
            index += index & (-index)

    def findLISLength(self, arr):
        n = len(arr)
        for i in range(n):
            self.update(arr[i])
        ans = self.query(n)
        return ans


n = 7
B = [1, 30, 70, 2, 60, 40, 50]

lis = LIS(n)
D = lis.coordinateCompression(B)
print(lis.findLISLength(D))
