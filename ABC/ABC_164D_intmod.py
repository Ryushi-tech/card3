from collections import Counter
S = list(map(int, input()))
P = 2019

def solve(S,P):
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

print(solve(S,P)