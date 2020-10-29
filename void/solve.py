n = int(input())
T, A = map(int, input().split())
X = [abs(T - 0.006 * x - A) for x in map(int, input().split())]

res = min(X)
for i, xx in enumerate(X, 1):
    if xx == res:
        print(i)
