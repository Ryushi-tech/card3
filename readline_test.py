import bisect
import sys
readline = sys.stdin.buffer.readline

n,m = map(int, readline().split())
val = [list(map(int, readline().split())) for _ in range(m)]
a,b,c = val

print(n,m,a,b,c)