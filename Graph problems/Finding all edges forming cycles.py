# Problem: Find all edges forming cycles in a graph
# Can find through Tarjan's Algorithm also
# But covered the DFS solution here

nodes = 6
edges = [[1,2],[1,3],[2,3],[2,7],[7,4],[4,5],[5,6],[6,4]]


def get_cycle_edges_of_graph(nodes,edges):

    from collections import defaultdict

    # Create the graph
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    rank = {}
    cycle_edge = set()

    def dfs(node,curr_rank):
        rank[node] = curr_rank
        min_rank = curr_rank+1

        for nbr in graph[node]:
            # Parent Node skip
            if nbr in rank and rank[nbr] == curr_rank-1:
                continue
            elif nbr in rank:
                if rank[nbr] <= curr_rank:
                    cycle_edge.add((min(nbr,node),max(nbr,node)))
                    min_rank = min(min_rank,rank[nbr])
            else:
                recursive_rank = dfs(nbr,curr_rank+1)
                
                if recursive_rank <= curr_rank:
                    cycle_edge.add((min(nbr,node),max(nbr,node)))
                    min_rank = min(recursive_rank,min_rank)

        return min_rank
    
    for node in graph:
        if node not in rank:
            dfs(node,1)

    print(f"Cycle edges are: {cycle_edge}")

get_cycle_edges_of_graph(nodes,edges)