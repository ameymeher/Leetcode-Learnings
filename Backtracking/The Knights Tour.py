"""
1. An optimization is possible by following a heuristic that always moves to the square from which the knight will have the fewest onward moves.
2. For copying the 2D array, use deepcopy from copy module
"""

class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        
        from copy import deepcopy

        curr_ans = [[-1 for j in range(n)] for i in range(m)]
        ans = None

        def backtrack(curr,r,c):
            nonlocal m,n,ans,curr_ans

            if ans:
                return 

            curr_ans[r][c] = curr

            if curr+1 == m*n:
                ans = deepcopy(curr_ans)
                return

            for i in [-2,-1,1,2]:
                for j in [-2,-1,1,2]:
                    if min(abs(i),abs(j)) == 1 and max(abs(i),abs(j)) == 2 and 0 <= r+i < m and 0 <= c+j < n and curr_ans[r+i][c+j] == -1:
                        backtrack(curr+1,r+i,c+j)

            curr_ans[r][c] = -1

        curr_ans[r][c] = 0
        backtrack(0,r,c)

        return ans