N,K,Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

test = {}
for i in A:
  if i in test:
    test[i]+=1
  else:
    test[i]=1

for j in range(1,N+1):
    if j in test:
        if test[j]+K-Q >= 1:
            print("Yes")
        else:
            print("No")
    else:
        if K-Q >= 1:
            print("Yes")
        else:
            print("No")