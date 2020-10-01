N, *XY = map(int, open(0).read().split())
X, Y = XY[::2], XY[1::2]
XtoY = [0] * (N+1)
for x, y in zip(X,Y):
  XtoY[x] = y

ans = [0] * (N+1)
l = 1
min_y = N + 1
for x in range(1, N+1):
  min_y = min(min_y, XtoY[x])
  if x + min_y == N+1:
    for i in range(l, x+1):
      ans[i] = x - l + 1
    l, min_y = x+1, N+1

for x in X:
  print(ans[x])
