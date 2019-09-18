n,k,q = map(int, input().split())
num = [int(input()) for _ in range(q)]

point = [k-q for _ in range(n)]

for i in range(q):
    point[num[i]-1] += 1

for j in point:
    if j >= 1:
        print("Yes")
    else:
        print("No")