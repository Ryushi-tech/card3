n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

MA = A[n//2] if n&1 else (A[n//2] + A[n//2-1])
MB = B[n//2] if n&1 else (B[n//2] + B[n//2-1])
print(MB - MA + 1)
