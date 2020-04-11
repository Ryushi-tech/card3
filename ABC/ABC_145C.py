import itertools

n = int(input())
x = []
y = []
for i in range(n):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

ans = list(itertools.permutations(range(n),n))

def sqrt(a,b,c,d):
    return(((c-a)**2+(d-b)**2)**0.5)

tot = 0
for aa in ans:
    for i in range(n-1):
        tot += sqrt(x[aa[i]],y[aa[i]],x[aa[i+1]],y[aa[i+1]])
print(tot/len(ans))