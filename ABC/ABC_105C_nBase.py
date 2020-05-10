n = int(input())
s = ""
while n != 0:
    a = n % -2
    s += str(-a)
    n = -(n//2)

if s == "":
    print(0)
else:
    print("".join(s[::-1]))
