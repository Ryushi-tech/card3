from stop_watch import stop_watch

@stop_watch
def solve():
    class FastModuloTransform():
        def __init__(self, n, mod=998244353, root=3):
        #def __init__(self, n, mod=1541406721, root=17):
            self.h = (n - 1).bit_length()
            self.n = 2**self.h
            self.mod = mod
            self.omega = pow(root, (mod - 1) // self.n, mod)
            self.rev = pow(self.omega, mod - 2, mod)

        def _bit_reverse_(self, A):
            n = self.n
            m = self.n // 2
            i = 0
            for j in range(0, m, 2):
                if j < i:
                    A[i], A[j] = A[j], A[i]
                    A[i + m + 1], A[j + m + 1] = A[j + m + 1], A[i + m + 1]
                A[i + 1], A[j + m] = A[j + m], A[i + 1]
                k = m // 2
                i ^= k
                while k > i:
                    k //= 2
                    i ^= k
            return A

        def _fmt_(self, A, base):
            halfpow = pow(base, self.n // 2, self.mod)
            n = self.n
            m = 1
            while n > 1:
                n //= 2
                w = pow(base, n, self.mod)
                k = 1
                for j in range(m):
                    for i in range(j, self.n, 2 * m):
                        u = A[i]
                        v = (A[i + m] * k) % self.mod
                        A[i] = (u + v) % self.mod
                        A[i + m] = (u + v * halfpow) % self.mod
                    k = (k * w) % self.mod
                m *= 2
            return A

        def fmt(self, f):
            A = f + [0] * (self.n - len(f))
            self._bit_reverse_(A)
            F = self._fmt_(A, self.omega)
            return F

        def ifmt(self, F):
            A = F + [0] * (self.n - len(F))
            self._bit_reverse_(A)
            nrev = pow(self.n, self.mod - 2, self.mod)
            f = [(e * nrev) % self.mod for e in self._fmt_(A, self.rev)]
            return f

        def convolute(self, f, g):
            F = self.fmt(f)
            G = self.fmt(g)
            H = [(s * t) % self.mod for s, t in zip(F, G)]
            h = self.ifmt(H)
            return h

    import sys
    input = sys.stdin.readline

    N = int(input())
    A = [0]
    B = [0]

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    fmt = FastModuloTransform(2 * N + 1)
    C = fmt.convolute(A, B)

    print('\n'.join(map(str, C[1: 2 * N + 1])))


solve()