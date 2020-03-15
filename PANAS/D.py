n = int(input())

tank = []
res = ["a"]

for le in range(1,n):
    tank = res
    res = []
    for i in range(len(tank)):
        tmp = "a"
        for j in range(le):
            res.append(tank[i] + tank[i][j])
            if tank[i][j] > tmp:
                tmp = tank[i][j]
        res.append(tank[i] + chr(ord(tmp)+1))
    res = list(set(res))
res.sort()

for e in res:
    print(e)
