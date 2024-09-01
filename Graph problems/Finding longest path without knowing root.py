# Learning from this code
# 1. BFS can be used to find the longest path in a tree from leaf to leaf in the case when we are not given the root of the tree.
# 2. For this case, we have to do BFS twice, once from an arbitrary node to find the farthest node.
# 3. Then we have to do BFS from the farthest node to find the longest path.

# An example case
nodes = 7
edges = [(2,1),(3,1),(7,1),(6,3),(5,2),(4,2)]

# Function to find the longest path in a tree from leaf to leaf
def find_longest_path(total_nodes, edges):
    
    from collections import defaultdict

    # Create graph
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Start BFS from an arbitrary node, say 1    
    queue = [(1,0)]
    visited = set()
    farthest_nodes = []
    longest_length = 0

    for node,rank in queue:
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if rank+1 > longest_length:
                    farthest_nodes = [nbr]
                    longest_length = rank+1
                elif rank+1 == longest_length:
                    farthest_nodes.append(nbr)
                queue.append((nbr,rank+1))

    print(f"Farthest nodes: {farthest_nodes}")

    # Start BFS to get the longest paths from leaf to leaf
    for node in farthest_nodes:
        queue = [(node,[node],1)]
        visited = set()
        longest_length = 0
        longest_path = []
        
        longest_path_nodes = set()

        for bfs_node,path,rank in queue:
            visited.add(bfs_node)
            for nbr in graph[bfs_node]:
                if nbr not in visited:
                    if rank+1 > longest_length:
                        longest_length = rank+1
                        longest_path =[path+[nbr]]
                    elif rank+1 == longest_length:
                        longest_path.append(path+[nbr])
                    queue.append((nbr,path+[nbr],rank+1))

        print(f"Longest path for BFS {node}: {longest_path}")
        for path in longest_path:
            longest_path_nodes.update(path)
        
    # All the nodes which are part of the longest path
    print(f"Longest path nodes: {longest_path_nodes}")
    print(f"Answer for Tiktok question specifically:")
    total_sum = total_nodes*(total_nodes+1)//2
    print(f"{ total_sum - sum(longest_path_nodes)}")


find_longest_path(nodes, edges)