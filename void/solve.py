import numpy as np
from scipy.sparse.csgraph import bellman_ford as bf
def f(ACM):
    C = np.zeros((27, 27), 'i8')
    for S, T in zip(ACM, ACM[1:]):
        if S == T: continue
        if len(S) > len(T) and S[:len(T)] == T: return False
        for s, t in zip(S, T):
            if s != t: C[s][t] = -1; break
    try: bf(C); return True
    except: return False
while True:
    n = int(input())
    if not n: exit()
    ACM = [[ord(x) - ord("a") for x in input()] for _ in range(n)]
    print("yes" if f(ACM) else "no")
