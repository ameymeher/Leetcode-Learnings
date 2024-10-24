class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        
        def backtrack(curr,candidate):
            nonlocal ans

            if candidate == "":
                ans.append(curr.copy())
                return

            for i in range(1,len(candidate)+1): #1 to 3
                if candidate[:i] == candidate[:i][::-1]:
                    curr.append(candidate[:i])
                    backtrack(curr,candidate[i:])
                    curr.pop()

        backtrack([],s)

        return ans

"""
s = "aab"
"""