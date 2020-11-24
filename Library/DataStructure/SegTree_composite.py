import sys
input = lambda: sys.stdin.readline()

def seg_f(a, b):
    return a[0] * b[0], b[0] * a[1] + b[1]

ide_ele = (1, 0)

def init(N):
    global num, seg
    num = 2 ** (N - 1).bit_length()
    seg = [ide_ele] * 2 * num

def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = seg_f(seg[2 * k + 1], seg[2 * k + 2])


n, m = map(int, input().split())
PAB = []
for _ in range(m):
    p, a, b = input().split()
    PAB.append((int(p), float(a), float(b)))

sp = sorted({p for p, a, b in PAB})
compress = {pi: i for i, pi in enumerate(sp)}

init(m)
ma = 1
mi = 1

for p, a, b in PAB:
    update(compress[p], (a, b))
    va, vb = seg[0]
    mi = min(mi, va + vb)
    ma = max(ma, va + vb)
print(mi, ma, sep="\n")
