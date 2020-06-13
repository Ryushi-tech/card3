# ref. https://atcoder.jp/contests/abc023/submissions/7901104

import sys
import numpy as np
input = sys.stdin.readline

n = int(input())
h = [0] * n
s = [0] * n

for i in range(n):
    h[i], s[i] = map(int, input().split())

h = np.array(h, np.int64)
s = np.array(s, np.int64)

right = 10 ** 14
left = 0


def check(x):
    t = (x-h)//s
    t.sort()
    return (t >= np.arange(n)).all()


while left + 1 < right:
    mid = (left + right)//2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
