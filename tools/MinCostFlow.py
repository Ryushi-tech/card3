import networkx as nx

n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

G = nx.DiGraph()

source = "source"
sink = "sink"
offset = 50
supply = n * k

G.add_node(source, demand=-supply)
G.add_node(sink, demand=supply)
G.add_edge(source, sink, capacity=supply, weight=0)

X = [i for i in range(n)]
Y = [i + offset for i in range(n)]

for x in X:
    G.add_edge(source, x, capacity=k, weight=0)
for y in Y:
    G.add_edge(y, sink, capacity=k, weight=0)
for x in X:
    for y in Y:
        G.add_edge(x, y, capacity=1, weight=-A[x][y - offset])

flow_dict = nx.min_cost_flow(G)
flow_cost = nx.cost_of_flow(G, flow_dict)

grid = [["." for _ in range(n)] for _ in range(n)]
for x in X:
    for y in Y:
        if flow_dict[x][y]:
            grid[x][y - offset] = "X"

print(-flow_cost)
for row in grid:
    print("".join(row))
