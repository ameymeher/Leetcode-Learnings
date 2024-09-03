from collections import defaultdict

def union_find(s,pairs):
    graph = defaultdict(list)

    # Create the graph
    for u,v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Find the connected components
    parent = [i for i in range(len(s))]

    # Find with path compression
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    # Union
    def union(x,y):
        parent_x = find(x)
        parent_y = find(y)

        if parent_x != parent_y:
            parent[parent_y] = parent_x

    for u,v in pairs:
        union(u,v)

    groups = defaultdict(list)
    
    for i in range(len(s)):
        component = find(i)
        groups[component].append(i)