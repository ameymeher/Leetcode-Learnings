class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        offset = [(-1,0),(1,0),(0,-1),(0,1)]

        @cache
        def dfs(i,j):
            nonlocal m,n

            max_value = 1

            for x,y in offset:
                new_i, new_j = i+x, j+y

                if (0 <= new_i < m and 0 <= new_j < n and 
                matrix[new_i][new_j] > matrix[i][j]):
                    max_value = max(max_value,dfs(new_i,new_j) + 1)

            return max_value

        ans = 1

        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
            
        return ans