"""
1. Ensure that the visited and the queue are refreshed for each BFS
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_set = set()
        atlantic_set = set()
        rows, cols = len(heights), len(heights[0])
        queue = []

        def bfs(visited):
            nonlocal queue,rows, cols

            offset = [(-1,0),(1,0),(0,-1),(0,1)]

            for i,j in queue:
                # Explore
                for dx, dy in offset:
                    new_x,new_y = i+dx,j+dy

                    if (0 <= new_x < rows and 0 <= new_y < cols and
                        (new_x,new_y) not in visited and
                        heights[new_x][new_y] >= heights[i][j]):
                        visited.add((new_x,new_y))
                        queue.append((new_x,new_y))

        #Explore pacific
        for j in range(cols):
            queue.append((0,j))
            pacific_set.add((0,j))
        
        for i in range(rows):
            queue.append((i,0))
            pacific_set.add((i,0))

        bfs(pacific_set)

        #Explore atlantic
        queue = []

        for j in range(cols):
            queue.append((rows-1,j))
            atlantic_set.add((rows-1,j))
        
        for i in range(rows):
            queue.append((i,cols-1))
            atlantic_set.add((i,cols-1))

        bfs(atlantic_set)

        return list(map(list,pacific_set & atlantic_set))