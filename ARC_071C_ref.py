n = int(input())
S = [input() for _ in range(n)]
m = [1000] * 26
al = 'abcdefghijklmnopqrstuvwxyz'
for s in S:
    k = [s.count(l) for l in al]
    m = [min(k[i], m[i]) for i in range(26)]

print(m)

ans = str()
for i in range(26):
    ans += al[i]*m[i]
print(ans)