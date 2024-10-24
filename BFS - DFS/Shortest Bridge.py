class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        """
        1. Length calculation was a bit off in the second part
        2. In the second part, I was not adding the second island to the queue.
        3. If there are problems, check the terminating condition and validity check
        4. Always add a visited set
        """

        m,n = len(grid), len(grid[0])
        found = False
        offset = [(-1,0),(1,0),(0,-1),(0,1)]
        island_nodes = None

        def bfs(queue):
            nonlocal offset, grid, m ,n

            visited = set(queue)

            for i,j in queue:

                #Mark this node
                grid[i][j] = 2

                #Explore valid nodes
                for dx,dy in offset:
                    new_x, new_y = i+dx, j+dy
                    if (0 <= new_x < m and 0 <= new_y < n and 
                        grid[new_x][new_y] == 1 and (new_x,new_y) not in visited):
                        visited.add((new_x,new_y))
                        queue.append((new_x,new_y))

            return visited

        def get_shortest_bridge(island_nodes):

            nonlocal grid,m,n, offset

            queue = []
            visited = set()

            for i,j in island_nodes:
                queue.append((i,j,0))

            for i,j,length in queue:

                # Found the other island
                if grid[i][j] == 1:
                    return length-1

                # Explore
                for dx,dy in offset:
                    new_x, new_y = i+dx, j+dy

                    if (0 <= new_x < m and 0 <= new_y < n and 
                        grid[new_x][new_y] != 2 and (new_x,new_y) not in visited):
                        visited.add((new_x,new_y))
                        queue.append((new_x,new_y,length+1))

        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    island_nodes = bfs([(i,j)])
                    found = True
                    break

        print(island_nodes)
        return get_shortest_bridge(island_nodes)

        """
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
        """