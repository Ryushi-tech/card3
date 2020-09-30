from numpy import fft
import sys
input = lambda: sys.stdin.readline()

n = int(input())
A = list(map(int, input().split()))
a = [x for x in A if x != 0]

mod = 200003
pr = 2

g = [0] * mod
log = [0] * mod
exp_pr = 1
for i in range(mod - 1):
    g[i] = exp_pr
    log[exp_pr] = i
    exp_pr = exp_pr * pr % mod

D = [0] * mod
ans = 0
for x in a:
    D[log[x]] += 1
    ans -= x * x % mod

l = 1 << ((mod - 1).bit_length() + 1)
fa = fft.rfft(D, l)
E = (fft.irfft(fa * fa)[:2 * mod - 2] + 0.1).astype(int)

for k in range(mod - 1):
    ans += g[k] * (E[k] + E[mod - 1 + k])

print(ans // 2)
