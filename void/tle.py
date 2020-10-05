n, s = input().split()
n = int(n)

cnt = 0
for i in range(n - 1):
    for j in range(i + 2, n + 1):
        tmp = s[i:j]
        pt = tmp.count("A")
        pa = tmp.count("T")
        pc = tmp.count("G")
        pg = tmp.count("C")
        # print(tmp, pa, pt, pc, pg)
        if pt == pa and pc == pg:
            cnt += 1
print(cnt)
