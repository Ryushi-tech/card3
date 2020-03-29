import sys
input = sys.stdin.readline

x, y, a, b, c = map(int, input().split())
red = list(map(int, input().split()))
gre = list(map(int, input().split()))
tra = list(map(int, input().split()))

red = sorted(red)[-x:]
gre = sorted(gre)[-y:]
uni = tra + red + gre

ans = sum(sorted(uni)[-(x+y):])
print(ans)
