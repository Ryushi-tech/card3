import sys
import networkx as nx

sread = lambda: sys.stdin.read()

n, m = map(int, input().split())
A = sread().split()

G = nx.DiGraph()
supply = sum([x.count("o") for x in A])

sink = n * m + 1

G.add_node(sink, demand=supply)
G.add_nodes_from(range(sink))

for i in range(n):
    for j in range(m):
        if A[i][j] == '#':
            continue
        if A[i][j] == 'o':
            G.add_node(i * m + j, demand=-1)
            G.add_edge(i * m + j, sink, capacity=1)
        if A[i][j] == '.':
            G.add_node(i * m + j)
            G.add_edge(i * m + j, sink, capacity=1)
        if i + 1 < n and A[i + 1][j] != '#':
            G.add_edge(i * m + j, (i + 1) * m + j, weight=-1)
        if j + 1 < m and A[i][j + 1] != '#':
            G.add_edge(i * m + j, i * m + j + 1, weight=-1)

flowDict = nx.min_cost_flow(G)
flowCost = nx.cost_of_flow(G, flowDict)

print(-flowCost)
