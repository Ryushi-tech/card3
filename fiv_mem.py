m = 20

def fib(n):
    mem = [0]*(n+1)
    if n <= 1:
        return n
    else:
        if mem[n] != 0:
            return mem[n]
    mem[n] = fib(n-1) + fib(n-2)
    return mem[n]

print(fib(m))