n = int(input())
m = int(n / 1.08)

if int(m * 1.08) == n:
    print(m)
elif int((m + 1) * 1.08) == n:
    print(m + 1)
else:
    print(":(")