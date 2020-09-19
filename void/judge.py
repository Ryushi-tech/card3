#!/usr/bin/env python3
import sys
ans = [1, 3, 4, 2, 5]
n = len(ans)
print('[*] n =', n, file=sys.stderr)
print(n)
sys.stdout.flush()
for _ in range(2 * n + 1):
    s = input()
    if s.startswith('!'):
        lis = list(map(int, res))
        assert lis == ans
        exit()
    else:
        i = int(s.split()[1])
        j = int(s.split()[2])
        y = ans[i] % ans[j]
        print(y)
        sys.stdout.flush()
assert False
