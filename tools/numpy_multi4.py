from card3.void.stop_watch import stop_watch


@stop_watch
def solve():
    import sys
    input = sys.stdin.readline
    import numpy as np

    mod = 10 ** 9 + 7
    n, k = map(int, input().split())
    A = np.array(input().split(), np.int64)

    I = (np.abs(A)).argsort()
    A = A[I][::-1]

    pos = A[A >= 0]
    neg = A[A < 0]

    nums = [1]
    if k & 1:
        nums = [pos[0]]
        pos = pos[1:]
        k -= 1

    if len(pos) & 1:
        pos = pos[:-1]
    if len(neg) & 1:
        neg = neg[:-1]

    pos = pos[::2] * pos[1::2]
    neg = neg[::2] * neg[1::2]

    A = np.concatenate([pos, neg])
    A.sort()
    A = A[::-1]
    print(np.concatenate([nums, A[:k // 2]]))


solve()

# for _ in range(3):
# solve()
