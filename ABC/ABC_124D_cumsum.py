n, k = map(int, input().split())
s = input()
res = []

if s[0] == "0":
    res.append(0)
res.append(1)
for i in range(1, n):
    if s[i] == s[i - 1]:
        res[-1] += 1
    else:
        res.append(1)
if s[-1] == "0":
    res.append(0)

l = len(res)
su = [0] * (l + 1)
for i in range(l):
    su[i + 1] = su[i] + res[i]

mil = min(l, 2 * k + 1)

ans = 1
for i in range(0, l - mil + 1, 2):
    ans = max(ans, su[mil + i] - su[i])
print(ans)

