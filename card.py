import numpy as np
N = np.array([True]*100)

for i in range(1,len(N)):
    for j in range(i,len(N),i+1):
        N[j] = not N[j]
print(np.count_nonzero(N == True))