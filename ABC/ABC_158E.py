from collections import Counter

N, P = map(int, input().split())
S = list(map(int, input()))

def solve_2(S):
    ind = (i for i, x in enumerate(S, 1) if x % 2 == 0)
    return sum(ind)

def solve_5(S):
    ind = (i for i, x in enumerate(S, 1) if x % 5 == 0)
    return sum(ind)

def solve(S,P):
    if P == 2:
        return solve_2(S)
    if P == 5:
        return solve_5(S)
    S = S[::-1]
    T = [0] * len(S)
    T[0] = S[0] % P
    power = 1
    for i in range(1, len(S)):
        power *= 10
        power %= P
        T[i] = T[i-1] + power * S[i]
        T[i] %= P
    counter = Counter(T)
    return sum(x * (x - 1) // 2 for x in counter.values()) + counter[0]


print(solve(S,P))
