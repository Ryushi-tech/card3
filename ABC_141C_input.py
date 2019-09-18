# Input
temp = []

for line in open("inp_t"):
    num = [int(item) for item in line.split()]
    temp.append(num)

# Body
n,k,q = temp[0]
num = [temp[i][0] for i in range(1,q+1)]

point = [k-q for _ in range(n)]

for i in range(q):
    point[num[i]-1] += 1

for j in point:
    if j >= 1:
        print("Yes")
    else:
        print("No")