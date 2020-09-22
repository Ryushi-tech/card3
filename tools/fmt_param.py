k = 25
n = 2 ** k
p = 998244353
root = 3

for i in range(2, 10000):
    x = pow(i, n, p)
    if x == 1:
        print(i)
print("for loop finished")

y = pow(root, (p - 1) // n, p)
print(y, pow(y, n, p))

"""
    #def __init__(self, n, mod=998244353, root=3): #2^23
    #def __init__(self, n, mod=1541406721, root=17): #2^21
    #def __init__(self, n, mod= 2130706433, root=3): #2^24
    #def __init__(self, n, mod= 754974721, root=11): #2^24
    self.h = (n - 1).bit_length()
    self.n = 2 ** self.h
    self.mod = mod
    self.omega = pow(root, (mod - 1) // self.n, mod)
    self.rev = pow(self.omega, mod - 2, mod)
"""