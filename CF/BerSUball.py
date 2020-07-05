n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = sorted(list(map(int, input().split())))

i, j, cnt = 0, 0, 0
while i < n and j < m:
    if abs(B[j] - A[i]) < 2:
        cnt += 1
        i += 1
        j += 1
    elif B[j] > A[i]:
        i += 1
    else:
        j += 1
print(cnt)

