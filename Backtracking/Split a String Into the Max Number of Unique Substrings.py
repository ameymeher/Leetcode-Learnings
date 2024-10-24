class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        

        """
        Test case which was good: ababab
        1. When the constraints are low, it can be a hint to try all the possible combinations
        2. When dealing with strings in the backtrack, take care of the loop. It will go to till the 1 to len(s)+1
        3. To optimize backtracking implementations, try to find out a good pruning strategy

        """

        used = set()
        ans = 1

        def backtrack(curr,candidate):
            nonlocal used,s,ans

            # Prune step which optimized the solution
            if len(used) + len(candidate) <= ans:
                return
            
            if curr == len(s):
                ans = max(ans,len(used))
                return

            for i in range(1,len(candidate)+1):
                if candidate[:i] not in used:
                    used.add(candidate[:i])
                    backtrack(curr+i,candidate[i:])
                    used.remove(candidate[:i])

        backtrack(0,s)
        
        return ans

"""

ww 
w
z
fv
ed
wf
vh
sw
"""