import sys

input = lambda: sys.stdin.readline()

seg_f = lambda x, y: min(x, y)
ide_ele = float("inf")


def init(n):
    global num, seg
    num = 1 << (n - 1).bit_length()
    seg = [ide_ele] * 2 * num


def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = seg_f(seg[2 * k + 1], seg[2 * k + 2])


def prod(l, r):
    L = l + num
    R = r + num
    res = ide_ele
    while L < R:
        if L & 1:
            res = seg_f(res, seg[L - 1])
            L += 1
        if R & 1:
            R -= 1
            res = seg_f(seg[R - 1], res)
        L >>= 1
        R >>= 1
    return res


n, k = map(int, input().split())
s = input()

init(n + 1)
update(n, 0)
dp = [ide_ele] * (n + 1)
dp[n] = 0

for i in range(n - 1, -1, -1):
    if s[i] == "1":
        continue
    else:
        dp[i] = prod(i, min(n, i + k) + 1) + 1
        update(i, dp[i])

if dp[0] == ide_ele:
    print(-1)
    exit()

ans = []
tmp = (0, dp[0])

for i in range(n + 1):
    x, y = tmp
    if dp[i] == y - 1:
        ans.append(i - x)
        tmp = (i, dp[i])
print(" ".join(map(str, ans)))
