h, w = map(int, input().split())
n = 10
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

res = 0
for i in range(h):
    for j in map(int, input().split()):
        if j == -1:
            continue
        else:
            res += cost[j][1]
print(res)
