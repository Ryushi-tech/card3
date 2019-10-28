n = 7
pt = [[1, 2, 3], [0], [5, 0], [6, 0], [6], [2], [3, 4]]

def bfs(v):
    d = [-1] * n
    d[v] = 0
    q = [v]
    c = 1
    while q:
        q1 = []
        for i in q:
            for j in pt[i]:
                if d[j] == -1:
                    d[j] = c
                    q1.append(j)
        q = q1
        c += 1
        print(d, q)
    return d

print(bfs(0))
