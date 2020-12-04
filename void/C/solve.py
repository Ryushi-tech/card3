n, k = map(int, input().split())
s = [x for x in input()]

t = pow(2, k, n)


def jank(a, b="Z"):
    if b == "Z":
        return a
    if a == b:
        return a
    if a < b:
        a, b = b, a
    if a == "R" and b == "P":
        return "P"
    if a == "S" and b == "P":
        return "S"
    if a == "S" and b == "R":
        return "R"


if n >= pow(2, k):
    m = pow(2, k)
    s = s[:m]
    while len(s) > 1:
        tmp = []
        for i in range(0, len(s), 2):
            if i + 1 < len(s):
                tmp.append(jank(s[i], s[i + 1]))
            else:
                tmp.append(jank(s[i]))
        s = tmp
    print(*s)
else:
    u = s + s[:t]
    m = len(u)
    while len(u) > 1:
        tmp = []
        for i in range(0, len(u), 2):
            if i + 1 < len(u):
                tmp.append(jank(u[i], u[i + 1]))
            else:
                tmp.append(jank(u[i]))
        u = tmp
    while len(s) > 1:
        tmp = []
        for i in range(0, len(s), 2):
            if i + 1 < len(s):
                tmp.append(jank(s[i], s[i + 1]))
            else:
                tmp.append(jank(s[i]))
        s = tmp
    if t + n & 1:
        print(jank(*u, *s))
    else:
        print(*u)
