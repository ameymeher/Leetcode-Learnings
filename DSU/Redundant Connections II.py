"""
The same DSU can be implemented as for an undirected graph.
Only case where it fails is when the component is not fully formed and a node has 2 parents.
In this case, since the component is not fully formed, it will consider 2 different parents.
Therefore, the redundant edge would be processed properly.
To avoid this, process the edges which have a common target node at the end, after doing union of all the edge nodes.
"""

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        target_map = {}
        same_target = []

        for i,(_,target) in enumerate(edges):
            if target in target_map:
                same_target.append(target_map[target])
                same_target.append(i)
                break
            target_map[target] = i

        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            p_x = find(x)
            p_y = find(y)

            if p_x != p_y:
                parent[p_y] = p_x
                return True
            
            return False

        # Union all the connections which does not have a same target
        for i,(u,v) in enumerate(edges):
            if i not in same_target:
                if not union(u,v):
                    return [u,v]
                
        # Do Union of the edges having the same target nodes
        for i in same_target:
            u,v = edges[i]
            if not union(u,v):
                return edges[i]