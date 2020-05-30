from collections import Counter
n = int(input())
lis = list(map(int, input().split()))

a = Counter(lis[::2])
b = Counter(lis[1::2])

aa = sorted(a.items(), key=lambda x:x[1], reverse=True)
bb = sorted(b.items(), key=lambda x:x[1], reverse=True)

aa.append((0, 0))
bb.append((0, 0))

if aa[0][0] == bb[0][0]:
    res = n - max(aa[0][1]+bb[1][1], aa[1][1]+bb[0][1])
else:
    res = n - aa[0][1] - bb[0][1]
print(res)
