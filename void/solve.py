from collections import deque

n, k = map(int, input().split())
org = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
kod = set(map(int, input().split()))
ele = list(org ^ kod)
que = deque(ele)

if n < 10:
    for i in ele:
        if i >= n:
            print(i)
            exit()

while que:
    x = que.popleft()
    for i in ele:
        y = 10 * x + i
        if y >= n:
            print(y)
            exit()
        else:
            que.append(y)