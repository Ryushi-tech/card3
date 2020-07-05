from heapq import heappop, heapify, heappush
n, x, y, z = map(int, input().split())
A = list(int(-a) for a in map(int, input().split()))
heapify(A)

if n > x + y + z or -sum(A) >= x * 1000 + y * 5000 + z * 10000:
    print("No")
    exit()

while A:
    if not z:
        break
    a = -heappop(A)
    if a >= 10000:
        t = min(a // 10000, z)
        z -= t
        a -= 10000 * t
        heappush(A, -a)
    else:
        z -= 1

while A:
    if not y:
        break
    a = -heappop(A)
    if a >= 5000:
        t = min(a // 5000, y)
        y -= t
        a -= 5000 * t
        heappush(A, -a)
    else:
        y -= 1

while A:
    if not x:
        break
    a = -heappop(A)
    t = min((a + 1000) // 1000, x)
    x -= t
    a -= t * 1000
    if a >= 0:
        heappush(A, -a)

print("No" if A else "Yes")
