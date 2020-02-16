import collections
import sys
input = sys.stdin.readline

q = int(input())
a = [input().rstrip() for _ in range(q)]

dic = collections.Counter(a)

keys = [k for k, v in dic.items() if v == max(dic.values())]
keys_s = sorted(keys)
for i in keys_s:
    print(i)