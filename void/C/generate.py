#!/usr/bin/env python3

import random
n = random.randint(1, 18)
ans = ""
for i in range(n):
    x = random.randint(1, 9)
    ans = ans + str(x)
print(ans)
