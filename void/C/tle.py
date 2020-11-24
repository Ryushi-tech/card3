from collections import defaultdict
s = [int(x) for x in input()]
S = sum(s) % 3
c = defaultdict(int)
for ss in s:
    c[ss % 3] += 1
diff = abs(c[1] - c[2]) % 3

if len(s) == 1 and c[0] == 0:
    print(-1)
elif len(s) == 2 and c[1] == 2:
    print(-1)
elif len(s) == 2 and c[2] == 2:
    print(-1)
elif S == 0:
    print(0)
elif S == 2:
    if c[2] > 0:
        print(1)
    else:
        print(2)
else:
    if c[1] > 0:
        print(1)
    else:
        print(2)
