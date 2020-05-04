ans = int(input())
res = 200

for i in range(-res, res+1):
    for j in range(-res, res+1):
        if i**5 - j**5 == ans:
            print(i,j)
            exit()
