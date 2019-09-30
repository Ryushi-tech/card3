import cProfile
m = 300

def fib(n):
    mem = [0]*(n+1)
    def _fib(n):
        if n <= 1:
            return n
        if mem[n] != 0:
            return mem[n]
        mem[n] = _fib(n-1) + _fib(n-2)
        return mem[n]
    return _fib(n)

def _fib_(n):
    if n <= 1:
        return n
    return _fib_(n-1) + _fib_(n-2)

print(fib(m))
#print(fib(m), _fib_(m))
cProfile.run("fib(m)")
#cProfile.run("_fib_(m)")
