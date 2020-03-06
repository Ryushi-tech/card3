# from collections import Counter
# from collections import deque
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from functools import reduce
# import bisect
# import heapq
# import math
import sys
sys.setrecursionlimit(10 ** 7)
readline = sys.stdin.buffer.readline


def main():
    n,m = map(int, readline().split())
    val = [list(map(int, readline().split())) for _ in range(m)]
    print(n,m,val)

if __name__ == '__main__':
    main()