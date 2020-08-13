import sys
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')

    @cc.export('solve', '(i8[:],i8[:],i8)')
    def solve(A, F, K):
        lo = 0
        hi = 10 ** 12
        while lo < hi:
            mid = (lo + hi) // 2
            total_train = 0
            for i in range(A.shape[0]):
                need = A[i] - mid // F[i]
                total_train += need if need > 0 else 0
            if total_train <= K:
                hi = mid
            else:
                lo = mid + 1
        return lo

    cc.compile()
    exit(0)

from my_module import solve
stdin = np.fromstring(open(0).read(), dtype=np.int64, sep=' ')
N, K = stdin[:2]
A = stdin[2: 2 + N]
F = stdin[2 + N:]
print(solve(np.sort(A)[::-1], np.sort(F), K))
