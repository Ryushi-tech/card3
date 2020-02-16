q = int(input())
a = [input() for _ in range(q)]
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
keys = [k for k, v in dic.items() if v == max(dic.values())]
keys_s = sorted(keys)
for i in keys_s:
    print(i)