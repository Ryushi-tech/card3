import sys
input = lambda: sys.stdin.readline()

def init(init_arr):
    global num, seg_f, ide_ele, seg
    seg_f = lambda x, y: max(x, y)
    ide_ele = 0
    num = 2 ** (n - 1).bit_length()
    seg = [ide_ele] * 2 * num
    for i in range(n):
        seg[i + num - 1] = init_arr[i]
    for i in range(num - 2, -1, -1):
        seg[i] = seg_f(seg[2 * i + 1], seg[2 * i + 2])

def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = seg_f(seg[k * 2 + 1], seg[k * 2 + 2])

def prod(l, r):
    if r <= l:
        return ide_ele
    l += num - 1
    r += num - 2
    res = ide_ele
    while r - l > 1:
        if l & 1 == 0:
            res = seg_f(res, seg[l])
        if r & 1:
            res = seg_f(res, seg[r])
            r -= 1
        l = l // 2
        r = (r - 1) // 2
    if l == r:
        res = seg_f(res, seg[l])
    else:
        res = seg_f(seg_f(res, seg[l]), seg[r])
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
a = list(map(int, input().split()))

init(a)
res = []

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        update(a - 1, b)
    elif t == 2:
        res.append(prod(a - 1, b))
    elif t == 3:
        res.append(max_right(a - 1, b))
print("\n".join(map(str, res)))
