import networkx as nx
from collections import defaultdict

while True:
    n, m, s, t = map(int, input().split())
    if (n, m, s, t) == (0, 0, 0, 0):
        break
    G = nx.DiGraph()
    edges = []
    capacities = defaultdict(int)
    for _ in range(m):
        a, b = map(int, input().split())
        if (a, b) in capacities:
            capacities[(a, b)] += 1
        else:
            capacities[(a, b)] = 1
        x = capacities[(a, b)]
        G.add_edge(a, b, capacity=x)
        edges.append((a, b))
    res, flow_dict = nx.maximum_flow(G, s, t)

    Gdash = nx.DiGraph()
    for a, b in edges:
        if flow_dict[a][b]:
            Gdash.add_edge(b, a, capacity=1)
            flow_dict[a][b] -= 1
        else:
            Gdash.add_edge(a, b, capacity=1)
    S = nx.descendants(Gdash, s)
    S.add(s)
    T = nx.ancestors(Gdash, t)
    T.add(t)
    cnt = 0
    for edge in edges:
        a, b = edge
        if b in S and a in T:
            cnt += 1
    if not cnt:
        print(res, cnt)
    else:
        print(res + 1, cnt)
