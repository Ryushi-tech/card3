x = int(input())


def is_prime(n):
    for i in range(2, int(x ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while not is_prime(x):
    x += 1
print(x)
