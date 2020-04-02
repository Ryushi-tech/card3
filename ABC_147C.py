import itertools as it

n = int(input())
lis = [[] for _ in range(n)]
val = list(it.product([0, 1], repeat=n))

for i in range(n):
    for j in range(int(input())):
        x, y = map(int, input().split())
        x = x - 1
        lis[i].append((x, y))


def honesty(k, lis, n):
    for i in range(n):
        if k[i] == 1:
            for l, m in lis[i]:
                if k[l] != m:
                    return False
    return True


res = 0
for k in val:
    if honesty(k, lis, n):
        res = max(res, sum(k))
print(res)
