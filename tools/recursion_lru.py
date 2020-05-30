from functools import lru_cache
n = 34
lis = [j for j in range(n)]
k = 562


@lru_cache(maxsize=None)
def subs(i, s):
    if i == n:
        return s == k
    rep0 = subs(i+1, s)
    rep1 = subs(i+1, s+lis[i])
    return rep0 or rep1


print(subs(0, 0))
