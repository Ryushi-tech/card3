n, m = map(int, input().split())
lis = list(map(lambda z: int(z) - 1, map(int, input().split())))

s = {0}
print(type(s))
res = [0]

while lis[res[-1]] not in s:
    res.append(lis[res[-1]])
    s.add(res[-1])

x, y = res.index(lis[res[-1]]), len(res)

if m < y:
    print(res[m] + 1)
else:
    mm = (m - x) % (y - x)
    print(res[mm + x] + 1)
