class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        1. Don't forget the visited set in the BFS, it does matter when you don't think it matters
        2. Add all the gates to the queue and do the BFS just once. A cleaner way to do it.
        """

        m = len(rooms)
        n = len(rooms[0])
        queue = []
        visited = set()
        
        def bfs():
            nonlocal rooms,m,n,queue,visited

            #print("Starting bfs ",i,j)
            offset = [(-1,0),(1,0),(0,-1),(0,1)]

            for x,y,val in queue:
                rooms[x][y] = val

                for dx,dy in offset:
                    new_x, new_y = x+dx,y+dy
                    if (0 <= new_x < m and 0 <= new_y < n 
                        and rooms[new_x][new_y] != -1 
                        and (new_x,new_y) not in visited):
                        visited.add((new_x,new_y))
                        queue.append((new_x,new_y,val+1))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j,0))

        bfs()

        return
"""
INF, -1 , 0 , INF
INF, INF, 1, -1
INF, -1, INF, -1
0,   -1, INF, INF

queue = [(0,3,1),()]

"""
                