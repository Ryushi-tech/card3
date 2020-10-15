import sys
input = sys.stdin.readline
from collections import deque
from operator import itemgetter
key = itemgetter(0)

N, D, A = map(int, input().split())
X = []
for _ in range(N):
    x, h = map(int, input().split())
    X.append((x, h))
X = sorted(X)[::-1]
Q = deque([])

ans = 0
k = 0
while X:
    if len(Q) == 0 or X[-1][0] <= Q[0][0]:
        x, h = X.pop()
        h = max(h - k * A, 0)
        a = (h + A - 1) // A
        ans += a
        k += a
        deque.append(Q, (x + 2 * D, a))
    else:
        x, a = deque.popleft(Q)
        k -= a

print(ans)