n, x = map(int, input().split())
s = input()

for ss in s:
    if ss == "o":
        x += 1
    else:
        x -= 1
        x = max(0, x)
print(x)
