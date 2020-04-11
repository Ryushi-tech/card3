import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
x, y = x-1, y-1
cnt = [0] * (n - 1)

for i in range(n):
    for j in range(i+1, n):
        a = abs(j-i)
        b = abs(x-i) + abs(y-j) + 1
        c = abs(y-i) + abs(x-j) + 1
        cnt[min(a,b,c) - 1] += 1

print(*cnt, sep="\n")
