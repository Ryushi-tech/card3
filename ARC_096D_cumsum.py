import numpy as np
import sys
input2 = sys.stdin.read

# A: Anti-clockwise, B: Clockwise, V: Values
n, c = map(int, input().split())
AV = np.array(list(map(int, input2().rsplit())), dtype=np.int64)
A, V = AV[::2], AV[1::2]
B = (c - A)[::-1]

XA = np.cumsum(V) - A
XB = np.cumsum(V[::-1]) - B
RXA, RXB = XA - A, XB - B    # Cumulative Values returning to Start

MA = np.zeros(n + 1, dtype=np.int64)
MB = np.zeros(n + 1, dtype=np.int64)
MRA = np.zeros(n + 1, dtype=np.int64)
MRB = np.zeros(n + 1, dtype=np.int64)


def max_mem(lis, mlis):
    for i in range(n):
        mlis[i + 1] = max(mlis[i], lis[i])


max_mem(XA, MA)
max_mem(XB, MB)
max_mem(RXA, MRA)
max_mem(RXB, MRB)

if n == 1:
    print(MA[1])
    exit()

res1, res2 = 0, 0
for i in range(n + 1):
    res1 = max(res1, MA[i] + MRB[n - i])
    res2 = max(res2, MB[i] + MRA[n - i])

print(max(res1, res2))
