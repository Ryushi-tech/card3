n = int(input())
letters = [input() for _ in range(n)]

common = []

for item in letters[0]:
    i = 0
    while i < n:
        if item in letters[i]:
            i += 1
        else:
            break
    if i == n:
        common.append(item)

if common == []:
    print()
else:
    b = sorted(common)
    ans = ""
    for i in range(len(common)):
        ans = ans + b[i]
    print(ans)