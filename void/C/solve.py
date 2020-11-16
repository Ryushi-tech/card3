from itertools import permutations
from collections import Counter

n, k = map(int, input().split())
G = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(n):
        if i == j:
            continue
        else:
            G[i][j] = s[j]

ran = [a for a in range(1, n)]
c = permutations(ran, n - 1)

ans = []
for cc in c:
    res = 0
    tmp = 0
    for ccc in cc:
        res += G[tmp][ccc]
        tmp = ccc
    res += G[cc[-1]][0]
    ans.append(res)

goal = Counter(ans)
print(goal[k])