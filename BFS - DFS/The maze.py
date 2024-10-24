"""
1. Read the question properly
2. The direction can only change at the wall
3. Also, the ball needs to stop at the destination, that means it should be a wall
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        m,n = len(maze), len(maze[0])
        ans = False

        visited = set()
        dir_map = {
            'u': (lambda x,y: (x-1,y)),
            'd': (lambda x,y: (x+1,y)),
            'l': (lambda x,y: (x,y-1)),
            'r': (lambda x,y: (x,y+1))
        }

        def roll(i,j,direction):
            nonlocal m,n,dir_map,ans

            if ans:
                return

            if (i,j) == tuple(destination):
                ans = True
                return

            prev_x,prev_y = i,j
            x,y = i,j

            # I had checked if it had reached the destination even though it was rolling, which was not proper
            while x>=0 and y>=0 and x<m and y<n and maze[x][y] == 0:
                prev_x,prev_y = x,y
                x,y = dir_map[direction](x,y)

            # Can change direction here
            for direct in list(dir_map.keys()):
                if (prev_x,prev_y,direct) not in visited:
                    visited.add((prev_x,prev_y,direct))
                    roll(prev_x,prev_y,direct)

        for d in list(dir_map.keys()):
            if (start[0],start[1],d) not in visited:
                visited.add((start[0],start[1],d))
                roll(start[0],start[1],d)

        return ans