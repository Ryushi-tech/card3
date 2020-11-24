import sys
input = lambda: sys.stdin.readline()

seg_f = lambda x, y: max(x, y)
ide_ele = 0

def init(N):
    global num, seg
    num = 2 ** (N - 1).bit_length()
    seg = [ide_ele] * 2 * num

def build(init_arr):
    for i in range(n):
        seg[i + num - 1] = init_arr[i]
    for i in range(num - 2, -1, -1):
        seg[i] = seg_f(seg[2 * i + 1], seg[2 * i + 2])

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

def max_right(l, x):
    ng = l
    ok = n + 1
    while ok > ng + 1:
        mid = (ok + ng) // 2
        if prod(ng, mid) >= x:
            ok = mid
        else:
            ng = mid
    return ok

n, q = map(int, input().split())
arr = list(map(int, input().split()))

init(n)
build(arr)
ans = []

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        update(a - 1, b)  # 0-indexed
    elif t == 2:
        ans.append(prod(a - 1, b))  # 0-indexed, 半開区間
    elif t == 3:
        ans.append(max_right(a - 1, b))
print("\n".join(map(str, ans)))
