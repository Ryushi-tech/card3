import sys
sys.setrecursionlimit(10 ** 7)

from stop_watch import stop_watch
@stop_watch
def solve():
    def I():
        return int(sys.stdin.readline().rstrip())

    def MI():
        return map(int, sys.stdin.readline().rstrip().split())

    n = I()
    A, B = [], []
    for i in range(n):
        a, b = MI()
        A.append(a)
        B.append(b)

    from cmath import pi, exp

    def dfs(f, start, step, N, inverse=False):
        if N == 2:
            a, b = f[start], f[start + step]
            return [a + b, a - b]
        if inverse is False:
            f0 = dfs(f, start, 2 * step, N // 2, inverse=False)
            f1 = dfs(f, start + step, 2 * step, N // 2, inverse=False)
            z = exp(2j * pi / N)
        else:
            f0 = dfs(f, start, 2 * step, N // 2, inverse=True)
            f1 = dfs(f, start + step, 2 * step, N // 2, inverse=True)
            z = exp(-2j * pi / N)
        z0 = 1.0
        for i in range(N // 2):
            a, b = f0[i], f1[i] * z0
            f0[i], f1[i] = a + b, a - b
            z0 *= z
        return f0 + f1

    def DFT(f, N):  # fを離散フーリエ変換
        if N == 1:
            return f
        return dfs(f, 0, 1, N)

    def iDFT(F, N):  # Fを離散フーリエ逆変換
        if N == 1:
            return F
        f = dfs(F, 0, 1, N, inverse=True)
        for i in range(N):
            f[i] /= N
        return f

    # deg(f)+deg(g)<Nとなる2冪Nを選び、f,gの長さがNになるように0を埋めておく

    def product(f, g, N):  # 多項式f,gの積
        F = DFT(f, N)
        G = DFT(g, N)
        FG = [F[i] * G[i] for i in range(N)]
        fg = iDFT(FG, N)
        for i in range(N):
            fg[i] = int(fg[i].real + 0.5)
        return fg

    N = 2 ** ((2 * n - 1).bit_length())
    A += [0] * (N - n)
    B += [0] * (N - n)
    ANS = product(A, B, N)
    print(0)
    for i in range(2 * n - 1):
        print(ANS[i])


solve()
