import networkx as nx

n, m = map(int, input().split())
A = [[s for s in input()] for _ in range(n)]

G = nx.DiGraph()

source = "source"
sink = "sink"

for i in range(n):
    for j in range(m):
        if A[i][j] == '#':
            continue
        if A[i][j] == '.':
            if (i + j) & 1:
                G.add_edge(source, (i, j), capacity=1)
                if i + 1 < n and A[i + 1][j] != '#':
                    G.add_edge((i, j), (i + 1, j), capacity=1)
                if j + 1 < m and A[i][j + 1] != '#':
                    G.add_edge((i, j), (i, j + 1), capacity=1)
                if -1 < i - 1 and A[i - 1][j] != '#':
                    G.add_edge((i, j), (i - 1, j), capacity=1)
                if -1 < j - 1 and A[i][j - 1] != '#':
                    G.add_edge((i, j), (i, j - 1), capacity=1)
            else:
                G.add_edge((i, j), sink, capacity=1)

grid = A

try:
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)

    for sub_dict in flow_dict["source"]:
        y_source, x_source = sub_dict
        for (y_sink, x_sink), val in flow_dict[sub_dict].items():
            if val and y_source != y_sink:
                grid[y_source][x_source], = "v" if y_sink > y_source else "^"
                grid[y_sink][x_sink] = "^" if y_sink > y_source else "v"
            if val and x_source != x_sink:
                grid[y_source][x_source], = ">" if x_sink > x_source else "<"
                grid[y_sink][x_sink] = "<" if x_sink > x_source else ">"

    print(flow_value)
    for gr in grid:
        print("".join(gr))

except nx.NetworkXError:
    print(0)
    for gr in grid:
        print("".join(gr))
