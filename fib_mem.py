# coding: utf-8
def fib(n, mem={}):
    if n <= 1:
        return n
    elif n in mem:
        return mem[n]
    else:
        mem[n]= fib(n-1)+fib(n-2)
        return mem[n]

def _fib(n):
    if n <= 1:
        return n
    else:
        n = _fib(n-1) + _fib(n-2)
        return n

from functools import lru_cache
@lru_cache(maxsize=1000)
def _fib_(n):
    if n <= 1:
        return n
    else:
        n = _fib_(n-1) + _fib_(n-2)
        return n

