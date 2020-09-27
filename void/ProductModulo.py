force = 1+10857*3*pow(2, 33)
print(force)
class FMT:
    def __init__(self, n1, mod=force, pr=15):
        # def __init__(self, n1, mod=998244353, pr=3):
        # def __init__(self, n1, mod=1541406721, pr=17):
        self.n0 = n1 - 1
        self.k = self.n0.bit_length()
        self.N = 1 << self.k
        self.mod = mod
        self.pr = pr
        self.inv_pr = pow(self.pr, self.mod - 2, self.mod)
        self.omega = [pow(self.pr, (self.mod - 1) >> i, self.mod) for i in range(24)]
        self.inv_omega = [pow(self.inv_pr, (self.mod - 1) >> i, self.mod) for i in range(24)]

    def fft(self, f):
        for l in range(self.k, 0, -1):
            d = 1 << l - 1
            U = [1]
            for i in range(d):
                U.append(U[-1] * self.omega[l] % self.mod)

            for i in range(1 << self.k - l):
                for j in range(d):
                    s = i * 2 * d + j
                    t = s + d
                    f[s], f[t] = (f[s] + f[t]) % self.mod, U[j] * (f[s] - f[t]) % self.mod

    def ifft(self, f):
        for l in range(1, self.k + 1):
            d = 1 << l - 1
            U = [1]
            for i in range(d):
                U.append(U[-1] * self.inv_omega[l] % self.mod)

            for i in range(1 << self.k - l):
                for j in range(d):
                    s = i * 2 * d + j
                    t = s + d
                    f[s], f[t] = (f[s] + f[t] * U[j]) % self.mod, (f[s] - f[t] * U[j]) % self.mod

    def convolve(self, a, b):
        a = a + [0] * (self.N - len(a))
        b = b + [0] * (self.N - len(b))
        self.fft(a), self.fft(b)
        for i in range(self.N):
            a[i] = a[i] * b[i] % self.mod
        self.ifft(a)
        inv_n = pow(self.N, self.mod - 2, self.mod)
        for i in range(self.n0):
            a[i] = a[i] * inv_n % self.mod
        del a[self.n0:]
        return a


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


fmt = FMT(2 * mod)
E = fmt.convolve(D, D)

for k in range(mod - 1):
    ans += g[k] * (E[k] + E[mod - 1 + k])

print(ans // 2)
