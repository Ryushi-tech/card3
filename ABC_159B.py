n = input()
l = len(n)
n_r = n[::-1]
n_1 = n[:(l-1)//2]
n_2 = n[(l+3)//2 - 1:]

if n == n_r and n_1 == n_1[::-1] and n_2 == n_2[::-1]:
    print("Yes")
else:
    print("No")
