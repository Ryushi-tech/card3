import networkx as nx

n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

G = nx.DiGraph()

source = 2 * n
sink = source + 1

G.add_node(source, demand=n * -k)
G.add_node(sink, demand=n * k)

for r in range(n):
    G.add_edge(source, r, capacity=k, weight=0)
    G.add_edge(r + n, sink, capacity=k, weight=0)
    for c in range(n):
        G.add_edge(r, c + n, capacity=1, weight=-A[r][c])

G.add_edge(source, sink, capacity=n * k, weight=0)  # slack

flowDict = nx.min_cost_flow(G)
flowCost = nx.cost_of_flow(G, flowDict)

grid = [["." for c in range(n)] for r in range(n)]
for r in range(n):
    for c in range(n):
        if flowDict[r][c + n]:
            grid[r][c] = "X"

print(-flowCost)
for row in grid:
    print("".join(row))
