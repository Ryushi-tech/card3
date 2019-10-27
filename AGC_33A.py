h, w = map(int, input().split())
A = [input() for _ in range(h)]

Q = []
V = [[0] * w for _ in range(h)]
D = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if A[i][j] == "#":
            Q.append([i, j, 0])
            V[i][j] = 1
            D[i][j] = 0

st = 0
while st < len(Q):
    for i in [[-1,0], [1,0], [0,-1], [0,1]]:
        x = Q[st][0] + i[0]
        y = Q[st][1] + i[1]
        print(x,y)
        if 0 <= x < h and 0 <= y < w and V[x][y] == 0:
            V[x][y] = 1
            Q.append([x,y,Q[st][2]+1])
            D[x][y] = Q[st][2] + 1
    st += 1

print(max([max(i) for i in D]))