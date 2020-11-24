a, b = 36, 240


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print("GCD Answer: " + str(gcd(a, b)))


def lcm(a, b):
    return a * b // gcd(a, b)


print("LCM Answer: " + str(lcm(a, b)))
