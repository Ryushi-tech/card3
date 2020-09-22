import sys
import networkx as nx

sread = lambda: sys.stdin.read()

n, m = map(int, input().split())
A = sread().split()

G = nx.DiGraph()
supply = sum([x.count("o") for x in A])

sink = n * m + 1

G.add_node(sink, demand=supply)  # sink node definition with supply (=total demand)
G.add_nodes_from(range(sink))

for i in range(n):
    for j in range(m):
        if A[i][j] == '#':
            continue
        if A[i][j] == 'o':
            G.add_node(i * m + j, demand=-1)  # source nodes definition with a demand
            G.add_edge(i * m + j, sink, capacity=1)  # edge definition with zero cost and capacity to start
        if A[i][j] == '.':
            G.add_node(i * m + j)  # path nodes definition without demands
            G.add_edge(i * m + j, sink, capacity=1)  # edge definition with default cost and capacity to finish
        if i + 1 < n and A[i + 1][j] != '#':  # vertical adj edge definition with lower cost and inf capacity
            G.add_edge(i * m + j, (i + 1) * m + j, weight=-1)
        if j + 1 < m and A[i][j + 1] != '#':  # horizontal adj edge definition with lower cost and inf capacity
            G.add_edge(i * m + j, i * m + j + 1, weight=-1)

flowDict = nx.min_cost_flow(G)
flowCost = nx.cost_of_flow(G, flowDict)

print(-flowCost)
