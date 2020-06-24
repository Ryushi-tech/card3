N = int(input())
S = list(map(int, input().split()))

res = 0
tmp = N
for j, y in enumerate(S[::-1]):
    if y == tmp:
        res += 1
        tmp -= 1
print(N - res)
