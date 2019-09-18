import heapq

n,m=[10,1]
a=[100,100,100,100,100,100,100,100,100,100]
b=[-int(i) for i in a]

heapq.heapify(b)

for i in range(m):
    x=heapq.heappop(b)//2
    heapq.heappush(b,x)

print(-sum(b))