import itertools as it
n = int(input())
l = len(str(n))

res = []
for i in range(3, l + 1):
    for gen in it.product("357", repeat=i):
        gen_s = "".join(gen)
        if int(gen_s) <= n:
            res.append(gen_s)

cnt = 0
for r in res:
    if all(r.count(c) for c in "357"):
        cnt += 1
print(cnt)
