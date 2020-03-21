# ref https://atcoder.jp/contests/abc023/submissions/6635676
import sys
input = sys.stdin.readline

n = int(input())
h = [0] * n
s = [0] * n

for i in range(n):
    h[i], s[i] = map(int, input().split())

right = 10 ** 2
left = 0

while left + 1 < right:
    mid = (left + right) // 2
    sim = [0] * n
    judge = True
    for i in range(n):
        if mid < h[i]:
            judge = False
            break
        elif (mid - h[i]) // s[i] >= n:
            continue
        sim[(mid - h[i]) // s[i]] += 1
    p = 0
    if not judge:
        left = mid
        continue
    for i in range(n):
        p += sim[i]
        if p > i + 1:
            judge = False
            break
    if judge:
        right = mid
    else:
        left = mid

print(right)
