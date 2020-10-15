import sys
import random
import copy
from time import time
input = sys.stdin.readline

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
start_t = time()


def calScore(T: list):
    scores = [0] * 26
    lasts = [0] * 26
    for i, tt in enumerate(T):
        scores[tt] += s[i][tt]
        dif = i - lasts[tt]
        scores[tt] -= c[tt] * dif * (dif + 1) // 2
        lasts[tt] = i + 1
    for i in range(26):
        dif = len(T) - lasts[i]
        scores[i] -= c[i] * dif * (dif + 1) // 2
    return sum(scores)


t = []
for i in range(D):
    res = - 10 ** 9
    t_cdd = 0
    for j in range(26):
        tmp = copy.deepcopy(t)
        tmp.append(j)
        tmp_score = calScore(tmp)
        if tmp_score > res:
            res = tmp_score
            t_cdd = j
    t.append(t_cdd)

ini_score = calScore(t)
print(ini_score)

while time() - start_t < 0.05:
# while time() - start_t < 1.75:
    tmp_t = copy.deepcopy(t)
    v = random.randint(0, D - 1)
    q = random.randint(0, 25)
    tmp_t[v] = q
    if calScore(tmp_t) > ini_score:
        t = tmp_t
ans = [x + 1 for x in t]
# print("\n".join(map(str, ans)))
