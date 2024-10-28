class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        m,n = len(matrix), len(matrix[0])

        def get_elements(val):
            elements = 0
            i,j = m-1,0

            while i>=0 and j<n:
                if matrix[i][j] > val:
                    i-=1
                else:
                    elements+=i+1
                    j+=1
            return elements

        l = matrix[0][0]
        r = matrix[-1][-1]

        while l<r:
            mid = (l+r) // 2
            
            elements = get_elements(mid)
            
            if elements < k:
                l = mid + 1
            elif elements >= k:
                r = mid

        return l