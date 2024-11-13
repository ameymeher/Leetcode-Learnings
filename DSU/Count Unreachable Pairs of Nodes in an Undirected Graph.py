class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            p_x = find(x)
            p_y = find(y)

            if p_x != p_y:
                parent[p_y] = p_x

        for u,v in edges:
            union(u,v)

        from collections import Counter

        counts = Counter(find(i) for i in range(n)) 

        ans = 0
        total_nodes = n

        # This part was tricky
        # I initially did this with O(n^2)
        # Trick was to reduce the total number of nodes since those pairs have already been considered earlier
        for val in counts.values():
            ans+=val*(total_nodes-val)
            total_nodes-=val

        return ans