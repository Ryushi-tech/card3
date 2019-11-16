n = int(input())
d = input()
if n % 2 == 1:
    print("No")
elif d[:n//2] == d[n//2:]:
    print("Yes")
else:
    print("No")