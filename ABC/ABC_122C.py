n, m = map(int, input().split())
graph = list(input())
ans = [0] * n
sans = [0] * n
for i in range(n-1):
    if graph[i] == "A" and graph[i+1] == "C":
        ans[i] += 1
for j in range(n-1):
    sans[j+1] = sans[j] + ans[j]

for _ in range(m):
    j, k = map(int, input().split())
    print(sans[k-1] - sans[j-1])