n, x, m = map(int, input().split())
g = x * 1
ans = x
arr = []
res = set([])
roop = (0, 0)
k = 0
for i in range(m + 1):
	tmp = x ** 2 % m
	if tmp in res:
		roop = (i, tmp)
		break
	res.add(tmp)
	arr.append(tmp)
	ans += tmp
	x = tmp

for i, y in enumerate(arr):
	if y == roop[1]:
		k = i
		break

ini = sum(arr[:k])
mul = ans - ini - g
t, v = divmod(n - k - 1, roop[0] - k)
print(g + ini + mul * t + sum(arr[k:k + v]))
