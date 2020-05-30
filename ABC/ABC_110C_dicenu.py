s = input()
t = input()

d = dict()

for i, ch in enumerate(s):
    if ch not in d:
        if t[i] in d.values():
            print("No")
            exit()
        else:
            d[ch] = t[i]
    elif d[ch] != t[i]:
        print("No")
        exit()

print("Yes")
